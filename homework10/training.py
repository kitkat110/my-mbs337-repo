import pickle
import logging
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

MODEL_PATH = "classifier.pkl"
PIPELINE_PATH = "normalizer_and_data_classifier_pipeline.pkl"
TEST_SIZE = 0.3
RANDOM_STATE = 1


def load_data() -> tuple:
    """
    Load the breast cancer dataset and return a DataFrame and target names.
    """
    try:
        data = load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df["target"] = data.target
        return df, data.target_names
    except Exception:
        logging.error("Failed to load in dataset")


def split_features_target(df: pd.DataFrame) -> tuple:
    """
    Split DataFrame into feature matrix X and target vector y.

    Args:
        df: Breast cancer dataset as pandas DataFrame.

    Returns:
        tuple: feature matrix A and target vector y.
    """
    try:
        return df.drop(columns=["target"]), df["target"]
    except KeyError as e:
        logging.error(f"Missing 'target' column: {e}")


def split_train_test(X: pd.DataFrame, y: pd.Series) -> tuple:
    """
    Return a stratified train/test split of X and y.

    Args:
        X: Breast cancer features as pandas DataFrame.
        y: Breast cancer target column as pandas Series.

    Returns:
        tuple: train/test split of X and y.
    """
    return train_test_split(X, y, test_size=TEST_SIZE, stratify=y, random_state=RANDOM_STATE)


def train_linear_classifier(X_train: pd.DataFrame, y_train: pd.Series) -> SGDClassifier:
    """
    Fit and return an SGD perceptron classifier.

    Args:
        X_train: Training dataset for X.
        y_train: Training dataset for y.

    Returns:
        SGDClassifier: Results of SGDCClassifier model.
    """
    clf = SGDClassifier(loss="perceptron", alpha=0.1)
    clf.fit(X_train, y_train)
    return clf


def train_pipeline(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    """
    Fit and return a StandardScaler + SGDClassifier pipeline.

    Args:
        X_train: Training dataset for X.
        y_train: Training dataset for y.

    Returns:
        Pipeline: Results of data standardization and SGDCClassifier model.
    """
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", SGDClassifier())
        ])
    pipeline.fit(X_train, y_train)
    return pipeline


def evaluate_model(model, X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series,) -> dict:
    """
    Return train and test accuracy scores for a fitted model.

    Args:
        X_train: Training dataset for X.
        X_test: Test dataset for X.
        y_train: Training dataset for y.
        y_test: Test dataset for y.

    Returns:
        dict: Dictionary of training and test accuracies of model. 
    """
    return {
        "train_accuracy": accuracy_score(y_train, model.predict(X_train)),
        "test_accuracy": accuracy_score(y_test, model.predict(X_test)),
    }

def save_model(model, path: str) -> None:
    """
    Save a fitted model to disk using pickle.

    Args:
        model: Fitted model.
        path: Path to save the model to.

    Returns:
        None: This function does not return a value; it writes output to disk.
    """
    try:
        with open(path, "wb") as f:
            pickle.dump(model, f)
    except (OSError, pickle.PicklingError) as e:
        logging.error(f"Could not save model to '{path}': {e}")


def main() -> None:
    """
    Load data, train and evaluate both models, and save them to disk.
    """
    df, target_names = load_data()
    X, y = split_features_target(df)
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    print(f"Classes: {target_names} | Train: {len(X_train)} | Test: {len(X_test)}\n")

    clf = train_linear_classifier(X_train, y_train)
    clf_scores = evaluate_model(clf, X_train, X_test, y_train, y_test)
    print("Linear Classifier")
    print(f"  Train: {clf_scores['train_accuracy']} | Test: {clf_scores['test_accuracy']}")
    save_model(clf, MODEL_PATH)

    pipeline = train_pipeline(X_train, y_train)
    pipe_scores = evaluate_model(pipeline, X_train, X_test, y_train, y_test)
    print("\nStandardised Pipeline")
    print(f"  Train: {pipe_scores['train_accuracy']} | Test: {pipe_scores['test_accuracy']}")
    save_model(pipeline, PIPELINE_PATH)


if __name__ == "__main__":
    main()