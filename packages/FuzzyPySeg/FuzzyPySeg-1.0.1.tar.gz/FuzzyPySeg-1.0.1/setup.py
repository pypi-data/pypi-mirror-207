from distutils.core import setup
setup(
  name = 'FuzzyPySeg',         
  packages = ['FuzzyPySeg'],   
  version = '1.0.1',      
  license='MIT',        
  description = 'FuzzyPySeg is a package for segmenting images using Fuzzy C Means clustering with either a Euclidean or Mahalanobis distance. You may also specify a centroid initialization using the firefly algorithm, genetic algorithm, or the Biogeography-based optimization algorithm.',   # Give a short description about your library
  author = 'Daniel Krasnov',                   
  author_email = 'dkrasnov@student.ubc.ca',     
  url = 'https://github.com/Danyulll/FuzzyPySeg',   
  download_url = 'https://github.com/Danyulll/FuzzyPySeg/archive/refs/tags/v1.0.1.tar.gz',   
  keywords = ['image segmentation', 'clustering', 'fuzzy c-means', 'firefly algorithm', 'genetic algorithm', 'biogeography-based optimization algorithm'],   
  install_requires=[            
          'numpy',
          'Image',
          'numba',
          'scipy'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)