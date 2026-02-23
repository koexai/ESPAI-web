# Provenance and Methods: ESPAI Synthetic EPIC-MOS1 Camera Flare events (Version 1.0)

## Overview
This document provides a comprehensive description of the development and characterization of the optimized generative AI model within the ESPAI project. The methodology utilizes a Variational Autoencoder (VAE) to generate synthetic solar-flare datasets.

## Data Sources and Acquisition

### Primary Training Data
**Source**: XMM-Newton Space Observatory
* **Target Data**: Observations from the EPIC-MOS1 detector.
* **Content**: Single photon events characterized by high instrumental quality.
* **Key Features**: DETX (spatial), DETY (spatial), and PI (Pulse Invariant/Energy).

**Data Preprocessing**:
* **Filtering**: Application of astronomical filters to isolate instrumental events and solar flares.
* **Pulse Invariant (PI)**: Selection of events exceeding a specific threshold value.
* **Normalization**: Features are rescaled using the Quantile Transformer from scikit-learn to ensure uniformity.

---

## Generation Pipeline

### Step 1: Variational Autoencoder (VAE) Architecture
The optimized model is implemented in PyTorch and replaces the standard point-mapping of an Autoencoder with a probabilistic approach to the latent space.

**Encoder Structure**:
* **Input Layer**: Dimension of 3 (DETX, DETY, PI).
* **Hidden Layer**: Single hidden layer with a fixed size of 16 units (`hidden_dim = 16`).
* **Output**: Maps input to two vectors: mean ($\mu$) and log-variance ($logvar$) of a Gaussian distribution.
* **Activation**: ReLU function is used for internal layers.

### Step 2: Latent Space and Reparameterization
To allow backpropagation during training, the model employs the reparameterization trick:
* **Sampling**: $z = \mu + \epsilon \cdot \exp(0.5 \cdot logvar)$, where $\epsilon \sim \mathcal{N}(0, I)$.
* **Purpose**: This creates a continuous and differentiable latent space, enabling the generation of new, physically plausible samples through interpolation.

### Step 3: Decoder and Reconstruction
The Decoder reconstructs the original input features from the sampled latent vector $z$.
* **Structure**: Mirror architecture to the Encoder using ReLU activations.
* **Output Layer**: Utilizes a linear activation function to remap features back into the original starting space.

### Step 4: Training and Loss Optimization
The model was trained on the **Leonardo supercomputer** (Cineca) using an 80/20 training/validation split.

**Evidence Lower Bound (ELBO) Loss**:
The core optimization lies in a custom ELBO function designed for the stochastic nature of photon detection:
$$\mathcal{L} = \mathcal{L}_{Recon} + \beta \cdot \mathcal{L}_{KL}$$
* **$\mathcal{L}_{Recon}$**: A combination of Chamfer distance and Kolmogorov-Smirnov (KS) distance calculated batch by batch.
* **$\mathcal{L}_{KL}$**: Standard Kullback-Leibler divergence for latent space regularization.
* **$\beta$ Parameter**: Controls the balance between reconstruction fidelity and latent space regularity.

---

## Quality Assurance

### Model Validation

| Variable | KS Statistic | P-value | Outcome |
| :--- | :--- | :--- | :--- |
| DETX / DETY / PI | 0.0023 - 0.0028 | 0.28 - 0.51 | ✓ Match |


### Statistical Validation
* **P-values**: Both models produced synthetic samples statistically indistinguishable from real data (p-values > critical threshold).
* **Spatial Fidelity**: Models accurately replicate the multi-modal profile and structural "voids" of the detector.
* **Energy Profile**: The VAE successfully models the PI energy peak around $10^3$ eV, demonstrating the effectiveness of the combined Chamfer/KS loss.

---

## Processing Environment

### Computational Resources
* **Hardware**: Leonardo Supercomputer managed by the Cineca consortium.
* **Framework**: PyTorch.
* **Optimization**: Adam optimizer with an Early Stopping policy based on the best validation ELBO.

## Limitations and Assumptions
* **Statistical Fidelity**: .
* **Data Scope**: The model is currently optimized for the EPIC-MOS1 detector instrumental background.
* **Feature Constraints**: Training is currently limited to three primary features (DETX, DETY, PI) to define the input dimension.

## Future Improvements

### Potential Enhancements
1. **Framework Integration**: Further integration of the VAE into the ESPAI generative framework for automated dataset enrichment.
2. **Latent Interpolation**: Leveraging the continuous latent space to generate rare event scenarios not fully captured in training data.

### Research Directions
1. **Anomaly Detection**: Utilizing the VAE for advanced anomaly detection in X-ray observations.
2. **Dataset Expansion**: Applying the optimized framework to other XMM-Newton instruments beyond MOS1.
