# Homework 09

## About
This directory contains all the files for **Homework 09**, which focuses on **linear classification of breast cancer malignancy**. The goal of this homework is to load and explore the **UCI Breast Cancer Wisconsin Dataset**, preprocess data for machine learning, fit a **linear classifier** using stochastic gradient descent (Perceptron), validate the model using accuracy metrics and a confusion matrix, and discuss model performance with respect to benign and malignant tumors.

## Directory Structure
```
my-mbs337-repo/
└── homework09/
    ├── Notebook.ipynb
    ├── README.md
    └── requirements.txt
```

## Summary Workflow
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Launch Jupyter Notebook:
   ```bash
   jupyter lab
4. Open Notebook.ipynb and execute the cells sequentially.

## Notebook Sections
### 1. Retrieve the Data
Load the dataset using sklearn.datasets `load_breast_cancer`. Explore dataset shape, features, and target.

### 2. Prepare the Data
Define input `X` and output `y` variables. Split data into training and test sets using train_test_split with stratification to preserve class balance.

### 3. Fit a Linear Classifier
Use `SGDClassifier` with the Perceptron algorithm. Fit the classifier to the training data.

### 4. Validation and Assessment
Evaluate model accuracy on training and test sets. Plot a confusion matrix using `ConfusionMatrixDisplay`. Analyze performance for each target label.