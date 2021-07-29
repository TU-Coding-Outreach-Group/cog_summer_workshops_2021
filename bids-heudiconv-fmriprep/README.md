# Coding Outreach Group Summer Workshop
# BIDS: HeuDiConv + fMRIPrep
07/29/2021

__**Content creator:**__ Liz Beard

**WARNING: THIS WORKSHOP IS UNDER CONSTRUCTION, CHANGES WILL BE MADE LATER**

## Description
This workshop introduces attendees to the concept of using Brain Imaging Data Structures (BIDS) and two crucial BIDS Apps for neuroimaging researchers: HeuDiConv and fMRIPrep using Docker. BIDS is standardized way to organize neuroimaging data that faciliaties ease of use among a variety of software and analytic tools. HeuDiConv automatically converts non-standard neuroimaging data into BIDS format, and fMRIPrep is an automated preprocessing pipeline that utilizes BIDS formatting. 

## Prerequisites
1. Basic experience with the unix shell or terminal and navigating file structures (using commands like `ls`, `cd`, `pwd`, `mkdir`)
    - This [software carpentry workshop](https://swcarpentry.github.io/shell-novice/) is particularly useful for familiarizing yourself with the unix shell. This workshop requires attendees to be comfortable with lessons 1, 2, and 3.
2. Using logic operatores such as `if`, `and`, `or` in pythin.
    - This [software carpentry workshop](https://swcarpentry.github.io/python-novice-inflammation/) will help you to get started with using logical operators and defining variables in pythin. Ideally attendees will be comfortable with lessons 1 and 7.

## Set Up (do before the workshop)
1. Be able to access your terminal/unix shell (instructions [here](https://swcarpentry.github.io/shell-novice/setup.html))
2. Install Docker Desktop onto your local computer (instructions [here](https://docs.docker.com/get-docker/)).
3. Pull `nipy heudiconv:latest` container image onto your local computer (instructions [here](https://heudiconv.readthedocs.io/en/latest/installation.html)).
    - **note**: Use the following command instead of what is listed on the HeuDiConv site `docker pull nipy/heudiconv:latest` 

## Workshop objectives:
1. Introduce and demonstrate the benefits of BIDS formatting neuroimaging data
2. Introduce Docker and containerized applications
3. Demonstrate the flexibility and functionality of HeuDiConv
4. Introduce fMRIPrep as a preprocessing option.

## Workshop Materials
**forthcoming**

## Outline
| Topic | Description | Time |
| --- | --- | --- |
| Intro | What is BIDS? Why is it important? | 5 min |
| Docker | What is Docker? | 5 min |
| Tutorial 1 | HeuDiConv example | 25 min |
| Tutorial 2 | fMRIPrep walkthrough | 15 min |
| Caveats & Troubleshooting | resources for troubleshooting | 5 min |

## Additional Resources
There are SO MANY amazing resources for learning and troubleshooting BIDS apps. Here are a few that I use often:

### Learning
There are many other tutorials for both HeuDiConv and fMRIPrep. But, since both of these tools are in development, the tutorials may not have the most up-to-date version of the software.

- [HeuDiConv Tutorials](https://heudiconv.readthedocs.io/en/latest/tutorials.html)
- [Stanford Center for Reproducible Science fMRIPrep tutorial](https://reproducibility.stanford.edu/fmriprep-tutorial-running-the-docker-image/)
- [Andy's Brain Book fMRIPrep demo](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_1_Download.html)
- [Gelana Tostaeva's fMRIPrep tutorial](https://medium.com/@gelana/using-fmriprep-for-fmri-data-preprocessing-90ce4a9b85bd)

### Troubleshooting
Possibly the hardest challenge in using HeuDiConv and fMRIPrep is getting started and troubleshooting. The error output in both programs can be challenging to parse. That being said, there are a number of different resources to try and troubleshoot your code:
- THE DOCUMENTATION. I cannot stress enough that directly referring to the documentation will help catch any stray typos or commands.
    + [HeuDiConv Documentation](https://heudiconv.readthedocs.io/en/latest/)
    + [fMRIPrep Documentation](https://fmriprep.org/en/stable/)
- [NeuroStars](https://neurostars.org/) is a forum for neuroscience researchers. Search for the HeuDiConv and fMRIPrep tags to see if others have had the same issues as you.
- GitHub. Both HeuDiConv and fMRIPrep are distributed via GitHub. If you think the issue you are running into from a software issue, be sure to check the issues section.
    + [HeuDiConv GitHub](https://github.com/nipy/heudiconv)
    + [fMRIPrep GitHub](https://github.com/nipreps/fmriprep)
