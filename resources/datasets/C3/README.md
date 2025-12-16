# PN Synthetic X-ray Event Distribution (KDE)

**Version:** 1.0.0

## Summary

This dataset contains approximately **249,000 synthetic X-ray photon events** generated using a **Kernel Density Estimation (KDE)** approach. Each row represents a single photon event on the detector, characterized by spatial coordinates (**DETX, DETY**) and energy (**PI**).

The synthetic data was created to simulate the statistical distribution of background or source events for the **XMM-Newton PN instrument** (or similar X-ray detectors), trained on observational event lists.

The primary purpose is to provide high-quality synthetic event lists for **background modeling**, **instrument response simulation**, and **testing of machine learning algorithms** in high-energy astrophysics.

---

## Contents

```text
PN_synthetic_dataset/
├── README.md                           # This file
├── metadata.json                       # Machine-readable metadata
├── pn_generated_distribution_KDE.csv # Main dataset (CSV format)
└── supplementary/
    └── distribution_plots.png          # Spatial and spectral density plots
```

---

## Structure and Formats

### File Formats

* **Primary:** CSV (Comma Separated Values)
* **Encoding:** UTF-8
* **Structure:** Tabular event list

### Data Organization

* **Rows:** 248,963 synthetic X-ray events
* **Columns:** 4 columns (Index + 3 physical properties)
* **Column naming:** `Unnamed: 0` (Index), `DETX`, `DETY`, `PI`
* **Total volume:** ~250k individual events

---

## Coordinate Conventions

* **DETX:** Detector X coordinate (approx. range: -17000 to +17000)
* **DETY:** Detector Y coordinate (approx. range: -17000 to +17000)
* **PI:** Pulse Invariant (energy channel, approx. range: 300 to 12000)

---

## Missing Values

* **Expected:** None (synthetic data is complete by design)
* **Representation:** N/A

---

## Provenance and Methods

### Generation Pipeline Overview

1. **Data Preprocessing** – Cleaning and normalization of real PN observational data.
2. **Model Training** – Kernel Density Estimation (KDE) model fitted to the multidimensional space (spatial + spectral).
3. **Sampling** – Random sampling from the estimated probability density function.
4. **Post-processing** – Denormalization to physical units (DET coordinates and PI channels).

### Key Components

* **Statistical Model:** Kernel Density Estimator (Gaussian kernel)
* **Bandwidth Selection:** Optimized for balance between smoothing and feature preservation
* **Training Data:** Observational X-ray event lists
* **Output:** Continuous distribution resampled into discrete events

---

## Physical Parameters (Feature Space)

The generation process models the joint probability distribution of three primary physical parameters:

* **DETX:** Spatial position on the detector (X-axis)
* **DETY:** Spatial position on the detector (Y-axis)
* **PI:** Energy of the photon (Pulse Invariant channel)

> **Note:** Unlike light curves, this dataset represents an integrated image/spectrum and does not currently include a time-of-arrival (`TIME`) column.

---

## Software and Libraries

* **Data Processing:** pandas, numpy
* **Modeling:** scikit-learn (KDE implementation)
* **Visualization:** matplotlib, seaborn

---

## Quality and Limitations

### Validation and Quality Control

* **Statistical Validation:** Generated distribution matches the underlying probability density of the training set.
* **Range Consistency:** Generated events fall within valid physical detector coordinates and energy channels.
* **Visual Inspection:** Spatial distribution accurately reproduces detector geometry and source/background morphology.

### Dataset Statistics

* **Total Samples:** 248,963 events
* **Spatial Coverage:** Full Field of View (FOV)
* **Spectral Range:** Broad energy coverage (soft to hard X-rays)

### Known Limitations

* **Smoothing:** KDE methods may smooth out extremely sharp features or point sources compared to raw data.
* **Boundary Effects:** Edges of the detector (CCD gaps) may be slightly blurred depending on kernel bandwidth.
* **Temporal Info:** No temporal evolution included (static snapshot of distribution).
* **Instrumental Noise:** Does not simulate read-out noise or pile-up effects, only the distribution of recorded events.

---

## Recommended Usage

Suitable for:

* Background subtraction modeling
* Machine learning clustering and classification tests
* Monte Carlo simulations of detector illumination
* Statistical analysis of spatial/spectral correlations

---

## How to Cite

### Plain Text Citation

> Luca Naso et al. (2025). *PN Synthetic X-ray Event Distribution (KDE)* (Version 1.0.0).
> Generated using Kernel Density Estimation.

### BibTeX Citation

```bibtex
@dataset{luca2025pnkde,
  author       = {Luca Naso et al.},
  title        = {PN Synthetic X-ray Event Distribution (KDE)},
  year         = {2025},
  version      = {1.0.0},
  note         = {Generated using Kernel Density Estimation},
  howpublished = {Available at: [repository URL]}
}
```

---

## License and Contact

### License

* **To be specified** (placeholder for `LICENSE` file)

### Contact Information

* **Dataset Creator:** Luca Naso
* **Institution:** Koexai Srl
* **Email:** [luca@koexai.com](mailto:luca@koexai.com)
* **Role:** Principal Investigator

---

## Acknowledgments

This dataset was generated using machine learning models trained on observational X-ray data. We acknowledge the high-energy astrophysics community for providing the foundational observations.

---

## Support

For questions about the dataset, methodology, or technical issues, please contact the dataset creator.

For bug reports, please provide:

* Clear description of the issue
* Steps to reproduce
* Expected vs. actual behavior
* System information (OS, Python version, etc.)
