<!-- Create a README.md with these sections:
     1. Project title and one-sentence description
     2. Installation (activate ece105 conda env, conda/mamba install numpy matplotlib)
     3. Usage (python generate_plots.py)
     4. Example output (describe the three plots briefly)
     5. AI tools used and disclosure -->

# ECE105 Lab 3 Sensor Plot Generation
This project generates reproducible synthetic temperature sensor data and saves a combined analysis figure with scatter, histogram, and box plots.

## Installation
Activate the `ece105` conda environment, then install dependencies with either `mamba` or `conda`:

```bash
conda activate ece105
mamba install numpy matplotlib
```

If `mamba` is not available:

```bash
conda install numpy matplotlib
```

## Usage
Run the script from the repository root:

```bash
python generate_plots.py
```

## Example output
The script creates one output image file, `sensor_analysis.png`, containing three subplots:
1. A scatter plot of Sensor A and Sensor B temperatures versus timestamp.
2. Overlaid temperature histograms for both sensors with dashed vertical lines marking each mean.
3. Side-by-side box plots for Sensor A and Sensor B with a dashed horizontal line for the overall mean.

## AI tools used and disclosure
Placeholder: Add your disclosure here describing any AI tools used, what they were used for, and how you reviewed or validated their outputs.
