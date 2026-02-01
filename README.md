# phd_research

Repo for old Jupyter notebooks, data analysis and visualizations from physics PhD research. 

### Prerequisites

- Python 3.10
- [Poetry](https://python-poetry.org/) for dependency management

# Project Notebooks

## [NanoparticleSizeDistribution](notebooks/NanoparticleSizeDistribution.ipynb)
<p align="center">
  <img src="imgs/nanoparticles.png" alt="Nanoparticle Size Distribution" width="500">
</p>

- Using thresholding and region analysis on STEM images of nanoparticle films to get statistical properties of synthesis runs.

## [hBNonSiSEMTrajectories](notebooks/hBNonSiSEMTrajectories.ipynb)
<p align="center">
  <img src="imgs/SEMBeam.png" alt="Electron trajectories in SEM beams" width="700">
</p>

- Visualization of SEM electron trajectories inside a typical semiconducting multilayer sample.



## [AverageUnitCellNanotube](notebooks/AverageUnitCellNanotube.ipynb)
<p align="center">
  <img src="imgs/nanotube_cell.png" alt="Averaging nanotube unit cells in TEM images" width="700">
</p>

- Using template matching to extract unit cells of 1D crystallite chains inside of nanotubes in HRSTEM images and creating an average composite super resolution image and figure.

## [HRSTEMAtoms](notebooks/HRSTEMAtoms.ipynb)
<p align="center">
  <img src="imgs/Atom_Fitting_0.png" alt="Atomic Resolution STEM" width="600">
</p>

- Analysis of an atomic resolution HRSTEM image. Identifying all atomic columns and fitting 2D Gaussian curves to each to extract properties of the material.

## [datCasinoToh5](notebooks/datCasinoToh5.ipynb)
- Parsing utility to convert `.dat` files to `.h5`. Data generated using CASINO software simulating electrons in a SEM incident on a multilayer substrate.





