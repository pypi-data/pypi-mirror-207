#imports
import numpy as np
import random       
from PIL import Image
from numba import jit, njit, prange
import sys
import scipy
import logging

def FCM(image_path="", save_to_path="", numClust=3, m=2, maxIter=50, clusterMethod="Euclidean", centroid_init="None",  error=0.001, hard="True", popSize=50, maxGen=50, bboAlpha=0.25, E=1, I=1, mutationRate=0.25, mutationStrength=1, initError=0.001, fAlpha=0.05, fBeta=1, fGamma=1.5):
    
    logging.basicConfig(
        level= logging.INFO,
        format= '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
    )
 
    #Select clustering method
    if(clusterMethod=="Euclidean"):
        FCM_Euclidean(image_path, save_to_path, numClust, m, maxIter, centroid_init, error, hard, popSize, maxGen, bboAlpha, E, I, mutationRate, mutationStrength, initError, fAlpha, fBeta, fGamma)
    elif(clusterMethod=="Mahalanobis"):
        FCM_Mahalanobis(image_path, save_to_path, numClust, m, maxIter, centroid_init, error, hard, popSize, maxGen, bboAlpha, E, I, mutationRate, mutationStrength, initError, fAlpha, fBeta, fGamma)
    return

# Calculate membership for FCM Euclidian
@njit(parallel=True)
def Euclidian_membership(numpydata, C, m, centroids):
    width = numpydata.shape[1]
    height = numpydata.shape[0]
    membership = np.empty((height, width, C),dtype=np.float64)
    power = (2/(m-1))
    for c in prange(C):
        for row in prange(height):
            for col in prange(width):
                x = numpydata[row, col, :]
                y = centroids[c]
                d1 = np.power(((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2), 0.5)
                d1 = np.power(d1, power)
                d2 = np.zeros((1,C))
                for d in prange(C):
                    x = numpydata[row, col, :]
                    y = centroids[d]
                    dist = np.power(((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2), 0.5)
                    d2[0,d] = dist
                d3 = np.sum(np.power(d2, -power))
                denom  = d1 * d3
                membership[row, col, c] = 1/denom
    return membership

# Calculate centroids for FCM Euclidian
@njit(parallel=True)
def Euclidian_centroids(numpydata, C, m, centroids, membership):
    width = numpydata.shape[1]
    height = numpydata.shape[0]
    for c in prange(C):
        top = np.array([0.,0.,0.], dtype=np.float64)
        bot = 0
        for row in prange(height):
            for col in prange(width):
                b = np.power(membership[row, col, c], m)
                exp = b * numpydata[row,col,:]
                if(False == np.isnan(b)):
                    bot += b
                    top += exp
        centroids[c] = top / bot
    return centroids

# Euclidean distance
@njit()
def Euclidian_distance(x,y):
   return np.power(((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2), 0.5)

# Initialization objective function
@njit(parallel=True)
def objective(x,c):
    """ The initialization objective function for FCM is defined as the sum of squared distances between clusters and pixel values
    Parameters:
        x - pixel data
        c - centroids list"""
    total = 0
    for row in prange(x.shape[0]):
        for col in prange(x.shape[1]):
            for i in prange(len(c)): # This is number of clusters
               total +=  Euclidian_distance(x[row,col,:],c[i])
    return total

# Firefly alogirthm
def firefly(x,alpha = 0.05,beta0 = 1, n = 20,gamma = 1.5,MaxGeneration = 5,numClusts=3, error=0.001):
    """ Initalize cluster centroids using the firefly algorithm.
    Parameters:
        x - image data
        alpha - step size
        beta0 - inital attractiveness
        n - population size
        gamma - light aborption coefficent
        MaxGeneration - max iterations
        numClusts - how many centroids per firefly
    """
    logging.info("Firefly algorithm: ")
    t = 0
    pop = np.empty((n,numClusts,3))
    for i in range(n):
        for j in range(numClusts):
            pop[i,j] = np.floor(np.random.rand(3)*255)
    old_obj = cur_obj = 0
    while(t < MaxGeneration):
        logging.info("Iteration: {}".format(t))
        for i in range(n): # for every ith firefly
            for j in range(n): # for every jth firefly
                Ii = objective(x,pop[i])
                Ij = objective(x,pop[j])
                if(Ii < Ij):
                    r = Euclidian_distance(pop[i],pop[j])
                    pop[i] = pop[i] + beta0 * np.exp(-gamma * (r**2)) * (pop[j]-pop[i]) + alpha * np.random.rand()
        t = t+1
        g_star = [objective(x,firefly) for firefly in pop]
        min_idx = g_star.index(min(g_star))
        old_obj = cur_obj
        cur_obj = objective(x,pop[min_idx])
        logging.info("Difference: {}".format(np.abs(cur_obj - old_obj)))
        if(np.abs(cur_obj - old_obj) <= error):
            break
    logging.info("Algorithm Complete: Max Iteration Reached")
    return pop[min_idx]

# Sorting Algorithm for BBO
@njit()
def sort(list1):  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1): 
            if(list1[j,0]>list1[j+1,0]):  
                temp0 = list1[j,0]
                temp1 = list1[j,1]
                list1[j,0] = list1[j+1,0]  
                list1[j,1] = list1[j+1,1]
                list1[j+1,0] = temp0
                list1[j+1,1] = temp1
    return list1

# Migration algorithm for BBO
@njit()
def migration(H, I, E):
    """
    H - matrix of all Habitats size is (n, numClusts, 3). Habitats need to be sorted in ascending order of HSI
    n - number of solutions
    numClusts - number of centroids in FCM 
    I - maximum immigration rate
    E - maximum emmigration rate
    """
    #initialize values
    n = H.shape[0]
    numClust = H.shape[1]
    immigration = np.empty((n))
    emmigration = np.empty((n))

    #calculate immigration rate and emmigration rate for all habitats
    for i in range(n):
        immigration[i] = (I*(1-(i/n)))
        emmigration[i] = ((E*i)/n)

    #for all solutions
    for i in range(n):
        #if H_i is selected
        if(immigration[i] > np.random.rand()):
            #for all solutions
            for j in range(n):
                #if H_j is selected
                #randomly select clusters to switch
                for k in range(numClust):
                    if(emmigration[j] > np.random.rand()):
                        #replace the SIV of H_i with SIV from H_j
                        H[i,k] = H[j,k]
    return H

# Factorial calculation for BBO
@njit(parallel=True)
def factorial(n):
    fact=1
    if int(n) >= 1:
        for i in prange(1,int(n)+1):
            fact = fact * i
        return fact
    else:
        return 1
    
# Mutation for algorithm BBO
@njit()
def mutation(H, alpha):
    """
    H - matrix of all Habitats size is (n, numClusts, 3). Habitats need to be sorted in ascending order of HSI
    n - number of solutions
    numClusts - number of centroids in FCM
    alpha - user defined parameter for tuning migration rate
    """
    #initialize values
    n = H.shape[0]
    numClust = H.shape[1]
    v = np.empty((n))
    p = np.empty((n))
    m = np.empty((n))
    
    #calculate vi for each solution
    i_prime = np.ceil((n+1)/2)
    n_fact = factorial(n)
    for i in range(1,(n+1)):
        if(i <= i_prime):
            v[i-1] = (n_fact)/((factorial(n-1-i))*(factorial(i-1)))
        else:
            v[i-1] = v[n-i]

    #calculate probability for each solution
    v_sum = np.sum(v)
    for i in range(n):
        p[i] = v[i]/v_sum

    #calculate mutation rate for each solution
    p_max = np.amax(p)
    for i in range(n):
        m[i] = alpha*(1-((p[i])/(p_max)))
   
    #for all solutions
    for i in range(n):
        #randomly select cluster to mutate
        for k in range(numClust):
            #if clsuter is selected
            if(m[i] > np.random.rand()):
                #randomly change values
                H[i,k] = np.floor(np.random.rand(3)*255)
    return H

# BBO algorithm
def BBO(x, n=50, numClust=3, maxIter=20, alpha=0.5, E=1, I=1, error=0.001):
    """ Initalize cluster centroids using the BBO algorithm.
    Parameters:
        x - image data
        n - number of solutions in population
        numClusts - how many centroids per solution
        maxIter - max number of iterations
        alpha - maximum mutation rate
        E - maximum emmigration rate
        I - maximumm immigration rate
        error - error cutoff
    """
    logging.info("BBO algorithm: ")
    #randomly create a population H of n solutions
    H = np.empty((n,numClust,3))
    for i in range(n):
        for k in range(numClust):
            H[i,k] = np.floor(np.random.rand(3)*255)

    #initialize variables
    new_best_obj = 0
    best_obj = 0

    for t in range(maxIter):
        logging.info("Iteration: ", t)
        #evaluate HSI of each solution (using reciprocal of objective function)
        new_best_obj = 0
        obj = np.empty((n,2))
        for i in range(n):
            obj[i,0] = 1/objective(x, H[i])
            obj[i,1] = i
        
        #sort each solution by HSI
        obj = sort(obj)
        tempH = H.copy()
        for i in range(n):
            idx = int(obj[i,1])
            H[i] = tempH[idx]
        new_best_obj = obj[n-1,0].copy()
        
        #calculate objective function difference
        if t != 0:
            difference = (1/best_obj) - (1/new_best_obj)
            logging.info("Difference: ", difference)
            if(abs(difference) < error):
                logging.info("Algorithm Complete: Difference < Error")
                logging.info(new_best_obj)
                return H[n-1]
        else:
            logging.info("Difference: NA")

        #reset best_obj score
        best_obj = new_best_obj.copy()

        #call migration algorithm
        H = migration(H, E, I)

        #call mutation algorithm
        H = mutation(H, alpha)
        
    #return the best solution found so far
    #evaluate HSI of each solution (using reciprocal of objective function)
    obj = np.empty((n,2))
    for i in range(n):
        obj[i,0] = 1/objective(x, H[i])
        obj[i,1] = i

    #sort each solution by HSI
    obj = sort(obj)
    tempH = H.copy()
    for i in range(n):
        idx = int(obj[i,1])
        H[i] = tempH[idx]

    #return best solution
    logging.info("Algorithm Complete: Max Iteration Reached")
    logging.info(obj[n-1,0])
    return H[n-1]

# Genetic Algorithm
def GA(x, n, numClust, maxIter, mutation_rate, mutation_strength=1, error=0.001):
    """ Initalize cluster centroids using the GA algorithm.
    Parameters:
        x - image data
        n - number of solutions in population
        numClusts - how many centroids per solution
        maxIter - maximum number of iterations 
        mutation_rate - how frequently mutation occurs
        mutation_strength - how large mutations are
        error - error cutoff
    """
    logging.info("BBO algorithm: ")
    #randomly create a population P of n solutions
    P = np.empty((n,numClust,3))
    for i in range(n):
        for k in range(numClust):
            P[i,k] = np.floor(np.random.rand(3)*255)
    
    #create initially empty p_prime population
    P_prime = np.empty((n,numClust,3))
    
    #initialize variables
    obj = np.empty((n))
    new_best_obj = 0
    best_obj = 0

    for iter in range(maxIter):
        #print current iteration 
        logging.info("Iteration: ", iter)

        #evaluate objective function of each solution
        new_best_obj = 0
        for i in range(n):
            obj[i] = 1/objective(x, P[i])
            if obj[i] > new_best_obj:
                new_best_obj = obj[i].copy()
                best_child = P[i].copy()

        #calculate objective function difference
        if iter != 0:
            difference = (1/best_obj) - (1/new_best_obj)
            logging.info("Difference: ", difference)
            if(abs(difference) < error):
                logging.info("Algorithm Complete: Difference < Error")
                logging.info(new_best_obj)
                logging.info(best_child)
                return best_child
        else:
            logging.info("Difference: NA")
    

        #create ratio of objective function vector
        obj_ratio = np.empty((n))
        obj_sum = np.sum(obj)
        for i in range(n):
            obj_ratio[i] = obj[i]/obj_sum

        #reset population count and best_obj score
        counter = 0
        best_obj = new_best_obj.copy()

        for t in range(n):
            #select parents 
            p_idx = np.arange(n)
            idx_1 = np.random.choice(p_idx, 1, p=obj_ratio)
            idx_2 = np.random.choice(p_idx, 1, p=obj_ratio)
            parent_1 = P[idx_1]
            parent_2 = P[idx_2]

            crossover_point = np.random.randint(0,numClust+1)

            child_1 = np.empty((numClust, 3))
            child_2 = np.empty((numClust, 3))

            for i in range(crossover_point):
                child_1[i] = parent_1[0,i]
                child_2[i] = parent_2[0,i]

            for i in range(crossover_point, numClust):
                child_1[i] = parent_2[0,i]
                child_2[i] = parent_1[0,i]

            for i in range(numClust):
                for k in range(3):
                    if mutation_rate >= np.random.rand():
                        mutation = np.random.normal(0,1) * mutation_strength
                        child_1[i,k] = child_1[i,k] + mutation

            for i in range(numClust):
                for k in range(3):
                    if mutation_rate >= np.random.rand():
                        mutation = np.random.normal(0,1) * mutation_strength
                        child_2[i,k] = child_2[i,k] + mutation

            if counter >= n:
                break

            P_prime[counter] = child_1

            counter = counter+1

            if counter >= n:
                break

            P_prime[counter] = child_2

        #Children become parents of next generation
        P = P_prime.copy()
    
    #evaluate objective function of each solution
    for i in range(n):
        obj[i] = 1/objective(x, P[i])
        if obj[i] > new_best_obj:
            new_best_obj = obj[i].copy()
            best_child = P[i].copy()

    logging.info("Algorithm Complete: Max Iteration Reached")
    return best_child

# Maximum membership index for Euclidian
@njit()
def max_mem_index_fcm(membership,c,row,col):
    maxMem = 0
    maxIdx = 0 # index of max cluster
    for i in range(c):
        if membership[row,col,i] > maxMem:
            maxIdx = i
            maxMem = membership[row,col,i]
    return maxIdx

# FCM with Euclidian Distance
def FCM_Euclidean(image_path, save_to_path, C, m, maxIter, centroid_init, error, hard, popSize, maxGen, bboAlpha, E, I, mutationRate, mutationStrength, initError, fAlpha, fBeta, fGamma):
    image = Image.open(fp=image_path)
    numpydata = np.asarray(image,dtype=np.float64)
    width, height = image.size
    centroids = np.empty((C,3), dtype=np.float64) # TODO: This will cause problems won't be 3x3 every time

    if(centroid_init == "firefly"):
        centroids = firefly(numpydata, fAlpha, fBeta, popSize, fGamma, maxGen, C, initError)
    elif(centroid_init == "BBO"):
        centroids = BBO(numpydata, popSize, C, maxGen, bboAlpha, E, I, initError)
    elif(centroid_init == "GA"):
        #def GA(x, n, numClust, maxIter, mutation_rate, mutation_strength=1, error=0.001)
        centroids = GA(numpydata, popSize, C, maxGen, mutationRate, mutationStrength, initError)
    else:
        # Randomly choose centroids
        for i in range(C):
            row = random.choice(range(height))
            col = random.choice(range(width))
            while(np.all(numpydata[row,col,:] == 0)):
                row = random.choice(range(height))
                col = random.choice(range(width))
            centroids[i,:] = numpydata[row,col,:]

    logging.info("FCM Euclidean algorithm: ")
    for t in range(maxIter):
        logging.info("Iteration: ", t)
        #copy over old centroids
        centroids_old = centroids.copy()

        #calculate membership matrix
        mem = Euclidian_membership(numpydata, C, m, centroids)

        #calculate new centroids
        centroids = Euclidian_centroids(numpydata, C, m, centroids, mem)

        #Calculate Ck - CK+1
        difference = np.linalg.norm(centroids_old - centroids)
        logging.info("Difference: ", difference)
        if(difference < error):
            logging.info("Algorithm complete")
            break

    logging.info("Saving Output")

    membership = mem
    copies = [numpydata.copy() for i in range(C+1)]
    pxl_idx = 0
    for row in range(height):
        for col in range(width):
            max_idx_clust = max_mem_index_fcm(membership,C,row,col)
            idx_for_black = [x for x in range(0,C) if x != max_idx_clust]
            for i in idx_for_black:
                copies[i][row,col,:] = np.array([0.,0.,0.])
            pxl_idx += 1

    colors = [np.random.randint(0, 256, size=(3,)) for _ in range(C)]

    if(hard == "True"):
        logging.info(colors)
        pxl_idx = 0
        for row in range(height):
            for col in range(width):
                max_idx_clust = max_mem_index_fcm(membership,C,row,col)
                copies[C][row,col,:] = copies[C][row,col,:] + colors[max_idx_clust]
                pxl_idx += 1
    else:
        logging.info(colors)
        pxl_idx = 0
        for row in range(height):
            for col in range(width):
                max_idx_clust = max_mem_index_fcm(membership,C,row,col)
                copies[C][row,col,:] = copies[C][row,col,:] + (colors[max_idx_clust] * membership[row,col,max_idx_clust])
                pxl_idx += 1

    images = [Image.fromarray(group.astype(np.uint8),mode="RGB") for group in copies]

    group_num = 0
    for image in images:
        image.save(save_to_path + "/group"+str(group_num)+"_FCM.jpeg")
        group_num += 1

# Mahalanobis Distance
@njit()
def mahalanobis_distance(xj, ai,sigma):
    inverse = np.linalg.inv(sigma + (0.001 * np.identity(3)))
    correction = np.log(np.linalg.det(inverse))
    return np.float64(((xj - ai) @ inverse @ (xj-ai).T) - correction)

# Calculate centroids for FCM Mahalanobis
@njit(parallel=True)
def mahalanobis_centroids(c, m, x, U, a):
    # Update Centroids
    width = x.shape[1]
    height = x.shape[0]
    for i in prange(c):
        ## Compute numerator
        numerator = np.zeros((1,3)) #TODO: this could be a potential problem
        j = -1
        for row in prange(height):
            for col in prange(width):
                j += 1
                numerator = numerator + ((np.power(U[i,j],m)) * x[row,col,:])
        # Compute denominator
        denominator = np.sum(np.power(U[i,:],m))    
        # Compute Centroid
        a[i] = numerator/denominator
    return a

# Calculate covariance for FCM Mahalanobis
@njit(parallel = True)
def mahalanobis_covariance(c, m, x, U, a, sigma):
    # Calculate Covariance Matrix
    width = x.shape[1]
    height = x.shape[0]

    for i in prange(c):
        # Compute numerator
        numerator = np.zeros((3,3)) # TODO: likely going to be a problem
        j = -1
        for row in prange(height):
            for col in prange(width):
                j += 1
                #reshaping matrix
                a123 = np.zeros((1,3)) # TODO: Could be a problem
                a234 = (x[row,col,:] - a[i])
                for z in prange(c):
                    a123[0,z] = a234[z]
                #final numerator computation
                numerator = numerator + ((np.power(U[i,j],m)) * ((a123).T * (a123)))
        # Computer denominator
        denominator = np.sum(np.power(U[i,:],m))
        # Compute Covariance Matrix
        sigma[i] = numerator / denominator
    return sigma

# Calculate membership for FCM Mahalanobis
@njit(parallel=True)
def mahalanobis_membership(c, m, x, U, a, sigma):
    # Update Membership Matrix
    width = x.shape[1]
    height = x.shape[0]
    for i in prange(c):
        j = -1
        # Compute denominator
        for row in prange(height):
            for col in prange(width):
                j += 1
                botnumer = 1/np.power((mahalanobis_distance(x[row,col,:],a[i],sigma[i])),(1/(m-1))) 
                botdenom = 0
                for l in prange(c):
                    botdenom = botdenom + 1/np.power((mahalanobis_distance(x[row,col,:],a[l],sigma[l])),(1/(m-1)))
                # Update Membership
                U[i,j] = botnumer/botdenom         
    return U

# Maximum membership index for FCM Mahalanobis
@njit()
def max_mem_index_fcm_m(U,c,pixel_idx):
    maxMem = 0
    maxIdx = 0 # index of max cluster
    for i in range(c):
        if U[i,pixel_idx] > maxMem:
            maxIdx = i
            maxMem = U[i,pixel_idx]
    return maxIdx

# FCM with Mahalanobis distance
def FCM_Mahalanobis(image_path, save_to_path, c, m, maxIter, centroid_init, error, hard, popSize, maxGen, bboAlpha, E, I, mutationRate, mutationStrength, initError, fAlpha, fBeta, fGamma):
    # Read in image     YOU MUST USE AN RGB IMAGE
    image = Image.open(image_path)
    x = np.asarray(image,dtype=np.float64)

    # Initalize values
    a = np.empty((c,3), dtype=np.float64) # create matrix for centroids
    sigma = np.zeros((c,3,3), dtype=np.float64) # list for covariance matrices
    height = image.height
    width = image.width
    n = height * width # number of pixels
    U = np.empty((c,n),dtype=np.float64) # Empty membership matrix

    if(centroid_init == "firefly"):
        a = firefly(x, fAlpha, fBeta, popSize, fGamma, maxGen, c, initError)
    elif(centroid_init == "BBO"):
        a = BBO(x, popSize, c, maxGen, bboAlpha, E, I, initError)
    elif(centroid_init == "GA"):
        a = GA(x, popSize, c, maxGen, mutationRate, mutationStrength, initError)
    else:
        # Initalize Centroids
        for i in range(c):
            row = random.choice(range(height))
            col = random.choice(range(width))
            a[i,:] = x[row,col,:]

    logging.info("FCM Mahalanobis algorithm: ")
    # Randomize membership matrix values (must sum to 1)
    pxl_count = 0
    for row in range(height):
        for col in range(width):
            for i in range(c):
                U[i,pxl_count] = random.random()
            U[:,pxl_count] = U[:,pxl_count]/sum(U[:,pxl_count])
            pxl_count += 1

        
    for t in range(maxIter):
        logging.info("Iteration: {}".format(t))

        oldU = U.copy()
        
        a = mahalanobis_centroids(c, m, x, U, a)

        sigma = mahalanobis_covariance(c, m, x, U, a, sigma) 

        U = mahalanobis_membership(c, m, x, U, a, sigma)

        #Calculate Ck - CK+1
        difference = np.linalg.norm(oldU - U)
        logging.info("Difference: ", difference)
        if(difference < error):
            logging.info("Algorithm complete")
            break
    
    logging.info("Saving output")

    copies = [x.copy() for i in range(c+1)]
    pxl_idx = 0
    for row in range(height):
        for col in range(width):
            max_idx_clust = max_mem_index_fcm_m(U,c,pxl_idx)
            idx_for_black = [x for x in range(0,c) if x != max_idx_clust]
            for i in idx_for_black:
                copies[i][row,col,:] = np.array([0.,0.,0.])
            pxl_idx += 1

    
    if(hard == "True"):
        colors = [np.random.randint(0, 256, size=(3,)) for _ in range(c)]
        logging.info(colors)
        pxl_idx = 0
        for row in range(height):
            for col in range(width):
                max_idx_clust = max_mem_index_fcm_m(U,c,pxl_idx)
                copies[c][row,col,:] = copies[c][row,col,:] + colors[max_idx_clust]
                pxl_idx += 1
    else:
        colors = [np.random.randint(0, 256, size=(3,)) for _ in range(c)]
        logging.info(colors)
        pxl_idx = 0
        for row in range(height):
            for col in range(width):
                max_idx_clust = max_mem_index_fcm_m(U,c,pxl_idx)
                copies[c][row,col,:] = copies[c][row,col,:] + (colors[max_idx_clust] * U[max_idx_clust,pxl_idx])
                pxl_idx += 1


    images = [Image.fromarray(group.astype(np.uint8),mode="RGB") for group in copies]

    group_num = 0
    for image in images:
        image.save(save_to_path + "/group"+str(group_num)+"_FCM_M.jpeg")
        group_num += 1

