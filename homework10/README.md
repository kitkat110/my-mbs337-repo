# Homework 10

## About
This directory contains all the files for **Homework 10**, which focuses on **MLOps with a linear classifier**. Building on Homework 09, the goal of this homework is to take the linear classifier built for the **UCI Breast Cancer Wisconsin Dataset** and put it into production. This involves fitting and saving two models, a baseline linear classifier and a normalized pipeline, and deploying them via an inference script that accepts sample data and returns predictions from both models.

## Directory Structure
```
my-mbs337-repo/
└── homework10/
    ├── README.md
    ├── training.py
    ├── inference.py
    ├── classifier.pkl
    ├── normalizer_and_data_classifier_pipeline.pkl
    ├── sample_data.csv
    └── requirements.txt
```

## Summary Workflow
1. Clone the repository.
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Train and save both models:
```bash
   python training.py
```
4. Run inference on sample data:
```bash
   python inference.py --sample_data sample_data.csv
```

## Part 1: Model Training (`training.py`)

### Data Preparation
The UCI Breast Cancer Wisconsin Dataset is loaded using `sklearn.datasets.load_breast_cancer`. Input features `X` and target labels `y` are defined, and the data is split into training and test sets using `train_test_split` with stratification to preserve class balance.

### Model 1 — Baseline Linear Classifier
A `SGDClassifier` using the Perceptron algorithm is fit directly to the raw training data with no preprocessing. The fitted model is saved to `classifier.pkl` using the `pickle` module.

### Model 2 — Normalized Pipeline
A `Pipeline` is constructed that first normalizes features using `StandardScaler`, then classifies using `SGDClassifier`. The pipeline is fit to the same training data and saved to `normalizer_and_data_classifier_pipeline.pkl` using the `pickle` module.

### Model Performance
| Model | Training Accuracy | Test Accuracy |
|---|---|---|
| Baseline Classifier | 0.902 | 0.901 |
| Normalized Pipeline | 0.990 | 0.953 |

## Part 2: Inference (`inference.py`)

The inference script loads both saved models using `pickle` and accepts sample data via a command-line argument. The sample data should be a `.csv` file in the same feature format as the original dataset (30 features, no target column). The script outputs predictions from both models for each sample entry.

### Usage
```bash
python inference.py --sample_data sample_data.csv
```

### Example Output
```
Your sample data contains 1 entry:
non-normalized model predicts: [malignant]
normalized model in pipeline predicts: [benign]
```