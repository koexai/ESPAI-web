# ESPAI Synthetic EPIC-pn Camera Flare events (Version 1.0)

## Summary
This dataset contains 1981559 synthetic records generated using a Variational Autoencoder (VAE) model. Each event is characterized by spatial coordinates (DETX/DETY) and the energetic parameter PI (Pulse Invariant). 

The primary purpose is generate realistic synthetic solar-flare events for training machine learning models, background subtraction, or instrument response simulation.

## Contents
```
synthetic_pn_flare_events/
├── pn_generated_distribution_VAE.parquet   # Main dataset (parquet format)
├── metadata.json                           # Machine-readable metadata
├── README.md                               # Project description and usage instructions
├── dictionary.csv                          # Data dictionary
├── provenance.md                           # Detailed generation methodology
├── checksum.txt                            # SHA 256 code for dataset
├── LICENSE_CC_BY_40.md                     # License information (CC BY 4.0)
└── citation.txt                            # citations file 
```
## Structure and Formats

### File Formats
- **Primary**: parquet format
- **Encoding**: UTF-8

### Data Organization
- **Rows**: 1981559
- **Columns**: 4
- **Column naming**: ['Unnamed: 0', 'DETX', 'DETY', 'PI']

### Missing Values
- **Expected**: None (synthetic data is complete by design)

## Provenance and Methods

### Generation Pipeline Overview
1. **Variational Autoencoder (VAE)**: The system utilizes a Variational Autoencoder (VAE) to generate synthetic solar-flare events.
2. **Latent Space** The process transforms raw data from the XMM-Newton observatory into probabilistic samples through a continuous latent space.

### Key Components
- **Encoder-Decoder Architecture**: The model consists of linear layers with 16 hidden units and ReLU activations designed to map the input data into a Gaussian probability distribution.
- **Reparameterization Trick**: This technique allows for differentiable sampling in the latent space through the equation:\[z = \mu + \epsilon \cdot \exp(0.5 \cdot \logvar)\]
where:
\[\epsilon \sim \mathcal{N}(0, I)\]
- **Optimized ELBO Loss**: A specialized cost function that combines Kullback-Leibler (KL) divergence for regularization with Chamfer and Kolmogorov-Smirnov distances to better manage the stochastic nature of detected photons.
- **Computing Infrastructure**: Model training was performed on the Leonardo supercomputer (Cineca) utilizing the Adam optimizer and an Early Stopping policy based on validation set performance.

### Physical Parameters
- **DETX and DETY**: Spatial detector coordinates used to precisely reconstruct the instrument's multi-modal geometry and structural voids.
- **PI (Pulse Invariant)**: An energy parameter filtered by threshold and modeled to replicate instrumental peaks, specifically around 103 eV.
- **Quantile Transformer**: A pre-processing method from scikit-learn used to rescale all features to ensure statistical uniformity before training.

### Software and Libraries
- **Deep Learning**: PyTorch 2.0+
- **Data Reduction and Analysis**: Science Analysis System (SAS)
- **Data Processing**: pandas, numpy. scikit-learn
- **Visualization**: matplotlib

## Quality and Limitations

### Validation and Quality Control
- **Model Validation**: Qualitative visual analysis of marginal distributions confirms the successful replication of multi-modal spatial and energy profiles of the detector.
- **Parameter Consistency**: Operational uniformity is ensured through fixed input/layer dimensions, Quantile Transformer rescaling, and an Early Stopping training policy.
- **Statistical Validation**: Kolmogorov-Smirnov (KS) statistics and high p-values verify that the generated data achieves a successful "Match" with the target distributions.

### Dataset Statistics
- **Total Samples**: 

### Known Limitations
1. **ELBO Loss Balancing**: The training process requires calibrating the β parameter to balance reconstruction precision with latent space regularity. This balance is essential for maintaining the internal coherence of the generative framework.
2. **Focus on Generalization**: The model is designed to prioritize the reconstruction of the macroscopic architecture of distributions and generalization capabilities. Consequently, it places less emphasis on replicating specific point-wise statistical micro-fluctuations of the data.
3. **Specialized Cost Function**: Due to the stochastic nature of detected photons, the model utilizes a specialized loss function integrating metrics such as Chamfer distance and KS distance. This personalization replaces standard metrics (like MSE or BCE) to better reflect global probability density.

### Recommended Usage
**Suitable for**:
- data augmentation 
- controlled experiments on cadence/noise
- benchmarking generalisation

## How to Cite

### Plain Text Citation
```
ESPAI Project (2025). ESPAI Core (v1.0) — Generative models and classification tools.
Source code. URL: https://ESPAI.koexai.com/resources/  Licence: MIT.
```

### BibTeX Citation

```bibtex
@dataset{ESPAI_C_v0_1_2025,
      author  = {Koexai Srl},
      title   = {ESPAI Solar Flare — Synthetic Solar Flare Dataset},
      year    = {2025},
      version = {1.0},
      url     = {https://ESPAI.koexai.com/resources/},
      license = {CC BY 4.0},
      note    = {}
    }
```

## License and Contact

### License
[CC BY 4.0]

### Contact Information
- **Project**: ESPAI (Koexai S.r.l.) [espai.koexai.com]
- **Email**: [info@koexai.com]
- **LinkedIn**:[https://www.linkedin.com/company/koexai/]
