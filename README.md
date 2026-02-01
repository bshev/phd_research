# phd_research

Repo for old Jupyter notebooks, data analysis and visualizations from physics PhD research. 

### Prerequisites

- Python 3.10
- [Poetry](https://python-poetry.org/) for dependency management

# Project Notebooks

## hBNonSiSEMTrajectories
<p align="center">
  <img src="imgs/SEMBeam.png" alt="Electron trajectories in SEM beams" width="700">
</p>

- Visualization of SEM electron trajectories inside a typical semiconducting multilayer sample.

## HRSTEMAtoms
<p align="center">
  <img src="imgs/HRSTEMAtoms.png" alt="Atomic Resolution STEM" width="500">
</p>

- Analysis of an atomic resolution HRSTEM image. Identifying all atomic columns and fitting 2D Gaussian curves to each to extract properties of the material.

## NanoparticleSizeDistribution
<p align="center">
  <img src="imgs/nanoparticles.png" alt="Nanoparticle Size Distribution" width="500">
</p>

- Using thresholding and region analysis on STEM images of nanoparticle films to get statistical properties of synthesis runs.

## AverageUnitCellNanotube
<p align="center">
  <img src="imgs/nanotube_cell.png" alt="Averaging nanotube unit cells in TEM images" width="700">
</p>

- Using template matching to extract unit cells of 1D crystallite chains inside of nanotubes in HRSTEM images and creating an average composite super resolution image and figure.

## datCasinoToh5
- Parsing utility to convert `.dat` files to `.h5`. Data generated using CASINO software simulating electrons in a SEM incident on a multilayer substrate.





