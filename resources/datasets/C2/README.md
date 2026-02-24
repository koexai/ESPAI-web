# ESPAI Synthetic EPIC-MOS2 Camera Solar-Flare events (Version 1.0)

## Summary
This dataset contains 420773 synthetic records generated using a Variational Autoencoder (VAE) model. Each event is characterized by spatial coordinates (DETX/DETY) and the energetic parameter PI (Pulse Invariant). 

The primary purpose is generate realistic synthetic solar-flare events for training machine learning models or background modeling.

## Contents
```
synthetic_mos2_flare_events/
├── mos2_generated_distribution_VAE.csv     # Main dataset (CSV format)
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
- **Primary**: CSV format
- **Encoding**: UTF-8

### Data Organization
- **Rows**: 420773
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
- **Computing Infrastructure**: Model training was performed on the Leonardo supercomputer (Cineca). 
- **Training Strategy**: Utilize the Adam optimizer and an Early Stopping policy based on validation set performance.

### Physical Parameters
- **DETX and DETY**: Spatial detector coordinates.
- **PI (Pulse Invariant)**: Energy of reconstructed event.

### Software and Libraries
- **Data Reduction and Analysis**: Science Analysis System (SAS)
- **Deep Learning**: PyTorch 2.0+ (torch)
- **Data Processing**: pandas, numpy, h5py
- **Scientific Computing & Statistics**: scipy, scikit-learn
- **Astronomical Data I/O**: astropy (FITS/Table)
- **Visualization**: matplotlib, seaborn
- **Image Processing**: opencv-python (cv2)
- **Execution Environment (Leonardo Supercomputer - Cineca)**: SLURM (sbatch, srun) + CUDA/GPU 

## Quality and Limitations

### Validation and Quality Control
- **Distribution Comparison**: Qualitative visual analysis through comparison of the spatial and energy distributions of input and output VAE datasets.
- **Statistical Validation**: Kolmogorov-Smirnov (KS) statistics and high p-values verify that the generated data achieves a successful "Match" with the target distributions.

### Dataset Statistics
- **Total Samples**: 420773

### Known Limitations
1. **ELBO Loss Balancing**: The training process requires calibrating the β parameter to balance reconstruction precision with latent space regularity. This balance is essential for maintaining the internal coherence of the generative framework.
2. **Focus on Generalization**: The model is designed to prioritize the reconstruction of the macroscopic architecture of distributions and generalization capabilities. Consequently, it places less emphasis on replicating specific point-wise statistical micro-fluctuations of the data.
3. **Specialized Cost Function**: Due to the stochastic nature of detected photons, the model utilizes a specialized loss function integrating metrics such as Chamfer distance and KS distance. This personalization replaces standard metrics (like MSE or BCE) to better reflect global probability density.

### Recommended Usage
**Suitable for**:
- solar-flare background modeling
- training machine learning algorithms

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
