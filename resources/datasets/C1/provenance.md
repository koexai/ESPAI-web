# Provenance and Methods: ESPAI Synthetic EPIC-MOS1 Camera Flare events (Version 1.0)
## Data Generation Overview
This document provides a comprehensive description of the development and characterization of the optimized generative AI model within the ESPAI project. The methodology utilizes a Variational Autoencoder (VAE) to generate synthetic solar-flare events.

## 1. Acquisition Sources

### Primary Training Data
**Source**: XMM-Newton Space Observatory
* **Target Data**: Observations from the EPIC-MOS1 detector.
* **Content**: Single photon events characterized by high instrumental quality.
* **Key Features**: DETX (spatial), DETY (spatial), and PI (Pulse Invariant/Energy).

**Data Preprocessing**:
* **Filtering**: Application of astronomical filters to isolate instrumental events and solar flares.
* **Pulse Invariant (PI)**: Selection of events exceeding a specific threshold value.
* **Normalization**: Features are rescaled using the Quantile Transformer from scikit-learn to ensure uniformity.

## 2. Processing Pipeline

### Step 1: Variational Autoencoder (VAE) Architecture
The optimized model is implemented in PyTorch and replaces the standard point-mapping of an Autoencoder with a probabilistic approach to the latent space.

**Encoder Structure**:
* **Input Layer**: Dimension of 3 (DETX, DETY, PI).
* **Hidden Layer**: Single hidden layer with a fixed size of 16 units (`hidden_dim = 16`).
* **Output**: Maps input to two vectors: mean (μ) and log-variance (logvar) of a Gaussian distribution.
* **Activation**: ReLU function is used for internal layers.

### Step 2: Latent Space and Reparameterization
To allow backpropagation during training, the model employs the reparameterization trick:
* **Sampling**: z = μ + ε · exp(0.5 · logvar), where ε ~ N(0, I).
* **Purpose**: This creates a continuous and differentiable latent space, enabling the generation of new, physically plausible samples through interpolation.

### Step 3: Decoder and Reconstruction
The Decoder reconstructs the original input features from the sampled latent vector z.
* **Structure**: Mirror architecture to the Encoder using ReLU activations.
* **Output Layer**: Utilizes a linear activation function to remap features back into the original starting space.

### Step 4: Training and Loss Optimization
The model was trained on the **Leonardo supercomputer** (Cineca) using an 80/20 training/validation split.

**Evidence Lower Bound (ELBO) Loss**:
The core optimization lies in a custom ELBO function designed for the stochastic nature of photon detection:

> **L = L_Recon + β · L_KL**

* **L_Recon**: A combination of Chamfer distance and Kolmogorov-Smirnov (KS) distance calculated batch by batch.
* **L_KL**: Standard Kullback-Leibler divergence for latent space regularization.
* **β Parameter**: Controls the balance between reconstruction fidelity and latent space regularity.

## 3. Quality Control and Validation

### Model Validation
| Variable | KS Statistic | P-value | Outcome |
| :--- | :--- | :--- | :--- |
| DETX / DETY / PI | 0.0023 - 0.0028 | 0.28 - 0.51 | ✓ Match |

### Statistical Validation
* **P-values**: Both models produced synthetic samples statistically indistinguishable from real data (p-values > critical threshold).
* **Spatial Fidelity**: Models accurately replicate the multi-modal profile and structural "voids" of the detector.
* **Energy Profile**: The VAE successfully models the PI energy peak around 10^3 eV, demonstrating the effectiveness of the combined Chamfer/KS loss.

## 4. Software and Dependencies

### Computational Resources
* **Hardware**: Leonardo Supercomputer managed by the Cineca consortium.
* **Framework**: PyTorch.
* **Optimization**: Adam optimizer with an Early Stopping policy based on the best validation ELBO.

## 5. Usage Recommendations

### Limitations and Assumptions
* **Data Scope**: The model is currently optimized for the EPIC-MOS1 detector instrumental background.
* **Feature Constraints**: Training is currently limited to three primary features (DETX, DETY, PI) to define the input dimension.
* **ELBO Loss Balancing**: The training process requires calibrating the β parameter to balance reconstruction precision with latent space regularity. This balance is essential for maintaining the internal coherence of the generative framework.
* **Focus on Generalization**: The model is designed to prioritize the reconstruction of the macroscopic architecture of distributions and generalization capabilities. Consequently, it places less emphasis on replicating specific point-wise statistical micro-fluctuations of the data.
* **Specialized Cost Function**: Due to the stochastic nature of detected photons, the model utilizes a specialized loss function integrating metrics such as Chamfer distance and KS distance. This personalization replaces standard metrics (like MSE or BCE) to better reflect global probability density.

### Research Directions
1. **Anomaly Detection**: Utilizing the VAE for advanced anomaly detection in X-ray observations.
2. **Dataset Expansion**: Applying the optimized framework to other XMM-Newton instruments beyond MOS1.
