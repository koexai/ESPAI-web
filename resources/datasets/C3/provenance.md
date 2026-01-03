# Provenance and Methods: Synthetic X-ray Telescope Event Dataset (ESPAI)

## Overview

This document provides a comprehensive description of how the synthetic X-ray telescope event dataset was generated within the ESPAI project (Enhancing Signal Purity with Artificial Intelligence in X-band telescopes). While the project explored various architectures, the final dataset described here was produced using a **Kernel Density Estimator (KDE)** model. The goal is to generate a balanced dataset of instrumental background signals and transient phenomena (such as Solar Flares) to support astronomical research.

## Data Sources and Acquisition

### Primary Training Data

**Source**: Observations from **XMM-Newton** (detectors MOS1, MOS2, PN).
- **Content**: Real X-ray events specifically filtered to isolate high-energy instrumental background and solar flares.
- **Structure**: Point clouds where each event represents a single photon defined by spatial coordinates and energy.
- **Features**: 3-dimensional data points: `x = [DETX, DETY, PI]`.
  - **DETX, DETY**: Spatial coordinates on the detector.
  - **PI**: Pulse Invariant (Energy).
- **Temporal sampling**: The methodology treats photons as independent instances (triples of DETX, DETY, PI); the temporal occurrence is considered decoupled from physical properties for this generation task.

**Data Preprocessing**: 
- **Filtering**:
  - Removal of instrumental noise and events outside the Field of View (FOV).
  - **Energy Threshold**: `PI > 300` (approx. 300 eV) to isolate high-energy non-cosmic components typical of flares/background.
  - **Quality Flags**: Usage of `FLAG` and `PATTERN` filters to select events of good instrumental quality.
- **Normalization**: 
  - Features (DETX, DETY, PI) are standardized using **Scikit-Learn's StandardScaler**.
  - This ensures uniformity and compatibility with machine learning input ranges.

## Generation Pipeline

### Model Architecture: Kernel Density Estimator (KDE)

The synthetic dataset was generated using a **Kernel Density Estimator (KDE)** implemented via `scikit-learn`, serving as a robust probabilistic approach.

**Methodology**:
- **Core Concept**: The model estimates the non-parametric probability density function of the real dataset ($X$) by summing kernel functions centered on each data point.
- **Sampling**: New synthetic data points ($\hat{x}$) are sampled from this estimated distribution, reflecting the statistical properties of the original input.

**Key Hyperparameters**:
- **Bandwidth**: Set to **0.001**.
  - **Rationale**: This extremely small value was selected to represent the intrinsic structural error of the sensor.
  - **Effect**: Unlike larger bandwidths that might smooth the distribution, this specific value forces the model to generate a distribution that remains extremely close to the true multi-dimensional data, ensuring the synthetic samples are statistically indistinguishable from the real ones.

## Quality Assurance

### Statistical Validation

The quality of the KDE-generated dataset was validated using the **Kolmogorov-Smirnov (KS)** test, comparing the synthetic distributions against the real data.

**Results (Baseline KDE Model)**:
- **DETX**: KS Stat `0.0010` | P-value `0.9998`
- **DETY**: KS Stat `0.0017` | P-value `0.8861`
- **PI**: KS Stat `0.0017` | P-value `0.8431`

**Interpretation**:
- The exceptionally low KS statistics and high P-values ($>0.05$) confirm that the null hypothesis cannot be rejected.
- This statistically validates that the distributions produced by the KDE model are **indistinguishable** from the reference real data, outperforming other tested architectures like the Autoencoder in terms of pure statistical fidelity.

### Visual and Structural Validation

The validation process included several graphical checks to ensure physical consistency:
- **Correlation Matrices**: Comparison of feature interdependencies (DETX, DETY, PI) between real and synthetic sets.
- **Global Energy Distribution**: Verification of spectral shape (linear and log scales) to ensure the model learned the background energy profile.
- **Spatial Coverage**:
  - **Radial Histograms**: Comparison of radial distribution ($\sqrt{DETX^2 + DETY^2}$).
  - **Spatial Scatter Plots**: 2D overlay of real vs. synthetic events to validate spatial fidelity across the detector surface.

## Processing Environment

### Computing Resources
- **Hardware**: Validated and run on the **Leonardo supercomputer**, managed by the CINECA consortium.

### Software Stack
- **Library**: `scikit-learn` (specifically for `KernelDensity` and `StandardScaler`).

## Limitations and Assumptions

### Methodological Assumptions
1. **Temporal Independence**: The model assumes that single photon events (DETX, DETY, PI) are independent instances in a 3D point cloud. The temporal sequence is not modeled explicitly as a time series (e.g., via RNNs) because the physical properties are considered decoupled from the timestamp for this specific simulation goal.
2. **Bandwidth Sensitivity**: The success of this method relies heavily on the specific bandwidth (0.001). A larger bandwidth would result in an overly smoothed distribution that fails to capture the specific sensor noise characteristics.