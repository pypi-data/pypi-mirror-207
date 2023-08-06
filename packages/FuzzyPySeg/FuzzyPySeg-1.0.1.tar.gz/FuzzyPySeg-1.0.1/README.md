# FuzzyPySeg

FuzzyPySeg is a package for segmenting images using Fuzzy C Means clustering with either a Euclidean or Mahalanobis distance. You may also specify a centroid initialization using the firefly algorithm, genetic algorithm, or the Biogeography-based optimization algorithm. It is done throug using the FCM function:


```python

FCM(image_path, save_to_path, numClust=3L, m=2, maxIter=20L, clusterMethod="Euclidean", centroid_init="None",  error=0.001, hard="True", popSize=50L, maxGen=50L, bboAlpha=0.25, E=1, I=1, mutationRate=0.25, mutationStrength=1, initError=0.001, fAlpha=0.05, fBeta=1, fGamma=1.5)

```


- image_path - file pathway indicating where the image to be segmented has been stored.
- save_to_path - file pathway indicating where the output images should be saved..
- numClust- number of clusters produced by the fcm algorithm.
- m - degree of fuzziness to be used by fcm algorithm.
- maxIter - integer indicating the maximum number of iterations the fcm algorithm runs for. This may cause the algorithm to not converge.
- clusterMethod - a description of the distance measurement to be used. Can be "Euclidean" or "Mahalanobis".
- centroid_init - a description of the centroid initialization to be used by fcm. Defualt "none" results in centroids being randomly initialized. Other options supported are "GA", "firefly", and "BBO". "GA" uses the genetic algorithm to initialize the centroids. "firefly" uses the firefly algorithm to initialize the centroids and "BBO" uses the Biogeography-Based Optimization algorithm to initialize the centroids.
- error - minimum difference required between fcm iterations before the algorithm converges.
- hard - string; if 'True' hard clustering is used. If 'False' soft clustering is used. 
- popSize - size of the population for "GA", "firefly", or "BBO" algorithm initializations.
- maxGen - maximum number of iterations for "GA", "firefly", or "BBO" algortihm initializations.
- bboAlpha - alpha parameter of BBO algorithm.
- E - maximum emmigration rate of BBO algorithm.
- I - maximum immigration rate of BBO algorithm.
- mutationRate - mutation rate of GA algorithm.
- mutationStrength - mutation strength of GA algorithm.
- initError - minimum difference required between GA, firefly, or BBO iterations before the algorithm converges.
- fAlpha - alpha parameter of firefly algorithm
- fBeta - beta parameter of firefly algorithm
- fGamma - gamma parameter of firefly algorithm


