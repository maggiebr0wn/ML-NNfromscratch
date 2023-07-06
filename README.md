# CS 7641 - Spring 21 - HW4: [NN, CNN, RandomForest, SVM](https://mahdi-roozbahani.github.io/CS46417641-spring2021/)

# Setup

1. Install [Miniconda](https://conda.io/miniconda.html) if you do not already have it installed.
2. Create an conda environment from the .yml files provided in envs folder. If you are running windows, use the Conda Prompt, on Mac or Linux you can just use the Terminal. Make sure to modify the command based on your OS (`linux`, `mac`, or `win`): `conda env create -f ml_hw4_env_<OS>.yml`
3. This should create an environment named 'ml_hw4'. Activate it using the Windows command, `activate ml_hw4` or the MacOS / Linux command, `conda activate ml_hw4`
4. Run the notebook using `jupyter notebook HW4.ipynb` or `jupyter lab HW4.ipynb`
5. Generate the zip folder to turn into gradescope by running `bash collect_submission.sh`. This will automatically select the required python scripts to turn in as well as convert your jupyter notebook to a pdf to turn in additonally.
