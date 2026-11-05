# MaNGA rotation curves: project material

Four notebooks, in order, and one module. Work in this folder (open the notebooks in Jupyter Lab or VS Code with the `astr119` kernel); `mangaRotCurves.py` is imported by notebooks 3 and 4, so keep it next to them.

| File | What it is |
|---|---|
| `FinalProject-MaNGA_galaxy_rotation_curves.ipynb` | 1. Overview: what a rotation curve is and why it is evidence for dark matter. Read first. |
| `FinalProject-MaNGARotCurves-2_manga_spectra.ipynb` | 2. The data cube: open your galaxy's `LOGCUBE` file with `astropy.io.fits`, display the reconstructed image, find the H-alpha line, measure velocities. |
| `FinalProject-MaNGARotCurves-3_velocity_fitting.ipynb` | 3. A model of a rotating disk, and fitting it to a made-up velocity field. |
| `FinalProject-MaNGARotCurves-4_fit_real_data.ipynb` | 4. Fit the model to your real velocity field; the rotation curve; what it says. |
| `mangaRotCurves.py` | The velocity-field class and fitting helpers the notebooks import. |
| `example_*.jpg`, `Rotation_curve_annotated.png`, `mangaIFU.jpeg`, `manga_infographic.jpeg`, `rotCurve_coordinate_systems.jpg` | Figures the notebooks show. |

**The data are not in this folder.** Notebook 2 tells you how to get your galaxy's cube from [Marvin](https://dr17.sdss.org/marvin/): type a plate-IFU such as `8138-9101`, download the `LOGCUBE` file (a few hundred megabytes), and put it in this folder. **Do not commit it** (`*.fits` and `*.fits.gz` are ignored by the repository's `.gitignore`). `astropy` is in the course environment.

These notebooks were written for the 2023 and 2024 offerings; if a cell fails on a newer numpy or pandas, that is a legitimate thing to ask Claude about, and worth a line in your AI-use log.
