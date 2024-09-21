# Pusula_HazarKagan_Elbeyli
 In-depth analysis and preprocessing of a drug side effects dataset using Python. Includes exploratory data analysis (EDA), data cleaning, and feature engineering
 
This project involves an in-depth analysis and preprocessing of a drug side effects dataset using Python. The analysis includes the following steps:

Project Overview

    This project is part of the Pusula Academy Data Scientist program, where the goal is to analyze a dataset of drug side effects. The tasks include:

    Exploratory Data Analysis (EDA):
        Understanding the structure and statistics of the data.
        Identifying missing values, outliers, and patterns.
        Visualizing distributions and relationships between variables using Seaborn and Matplotlib.

    Data Preprocessing:
        Handling missing values using imputation methods.
        Converting categorical variables into numerical form.
        Scaling numerical features.
        Parsing and handling date features for further analysis.

    Feature Engineering:
    Creating new features such as age from existing columns.
    Encoding categorical variables using Label Encoding.
    
    Visualization:

        Visualizing the distribution of categorical features like gender and nationality.
        
    Files Structure:
    
        project_folder/
    │
    ├── data/
    │   └── side_effect_data_1.xlsx  # Original dataset used for analysis.
    │
    ├── scripts/
    │   ├── data_loader.py            # Contains code for loading data.
    │   ├── data_exploration.py       # Contains code for EDA and visualizations.
    │   ├── data_preprocessing.py     # Contains data cleaning and preprocessing functions.
    │   └── main.py                   # Main script to run the analysis and processing.
    │
    ├── README.md                     # Project documentation.
    
    
    Usage:

    Clone the repository and run the scripts inside the scripts/ folder to analyze the dataset.
    Ensure the required Python libraries such as pandas, seaborn, and matplotlib are installed.

    Results:
    
        The processed data and visualizations give insights into the drug side effects reported, including correlations between patient characteristics and the observed side effects.
