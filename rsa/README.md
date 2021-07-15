# Coding Outreach Group Summer Workshop
# Representational Similarity Analysis
07/15/2021

__**Content creator:**__ Haroon Popal

**WARNING: THIS WORKSHOP IS UNDER CONSTRUCTION, CHANGES WILL BE MADE LATER**

## Description
Representational similarity analysis (RSA) is a newer analytic technique that can be used for both neural and behavioral data and is great for exploring high-dimensional data or comparing data across different modalities.

## Prerequisites
1. Comfort coding in python
2. Familiarity with file path structures
3. Faimilarity with general neuroimaging analysis concepts

## Set Up (do before the workshop)
1. Make sure you've installed the following python packages:
    - [nltools](https://nltools.org/install.html) in a python 3 environment. `pip install nltools`
2. Make sure you have a python 2 and a python 3 environment.
    - Instructions on how to [set up environments with anaconda](https://docs.anaconda.com/anaconda/user-guide/tasks/switch-environment/).
    - [nltools](https://nltools.org/install.html) 
    - We will be using the nltools package to create and visual RDMs, and complete a region of interest RSA.
3. Install [pymvpa](pymvpa.org/installation.html) in a python 2 environment.
    
## Workshop objectives:
1. Introduce the basic framework of representational similarity analysis 
2. Demonstrate how to create representational dissimilarity matrices from models, behavioral data, and neuroimaging data
3. Demonstrate RSA with a region of interest approach

## Workshop Materials
- [Notebook Viewer](https://tu-coding-outreach-group.github.io/cog_summer_workshops_2021/rsa/index.html)
- [Intro Slides](https://github.com/TU-Coding-Outreach-Group/cog_summer_workshops_2021/blob/main/rsa/rsa_intro-COG2021.pdf)

## Outline
| Topic | Time | Description |
| --- | --- | --- |
| Intro | Why use RSA? | 5 min |
| Tutorial 1 | ROI RSA | 30 min |
| Tutorial 2 | Searchlight RSA (coming soon) | 15 min |
| Tutorial 3 | Significance Testing (coming soon) | 10 min |
| Outro | RSA with multi-dimensional data | 5 min |

## Additional Resources
*** UNDER CONSTRUCTION ***

### Literature
- [Kriegeskorte et al., 2008](https://www.frontiersin.org/articles/10.3389/neuro.06.004.2008/full?utm_source=FWEB&utm_medium=NBLOG&utm_campaign=ECO_10YA_top-research)
    - The original paper that introduced RSA
- [Popal et al., 2019](https://academic.oup.com/scan/article/14/11/1243/5693905)
    - An RSA how-to and why-to guide aimed for the social neuroscience community
- [Dimsdale-Zucker & Ranganath, 2018](http://hrz-website.s3.amazonaws.com/papers/dimsdale-zucker_ranganath_2018_published-chapter.pdf)
    - An in-depth RSA guide aimed for memory researchers

### Packages
- [Dartbrains](https://dartbrains.org/content/RSA.html)
    - Excellent tutorial. Much of the code in this workshop was adapted from this resource.
    - Uses the nltools package
- [PyMVPA](http://www.pymvpa.org/examples/rsa_fmri.html)
    - Includes searchlight analysis
- [Brain imaging analysis kit](https://brainiak.org/tutorials/06-rsa/)
- [NeuroRA](https://neurora.github.io/NeuroRA/)

### Other Workshops
- [Mark Thornton's RSA workshop](https://colab.research.google.com/drive/1UEtFr-oJisRzl8BmzbNdMZZ7-Of0gLcH?usp=sharing) for Society for Social Neuroscience 2021
- [MIND 2018 RSA workshop](https://github.com/markallenthornton/mind_2018/tree/master/tutorials/representational_similarity) in R

