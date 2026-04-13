import argparse
import pickle
import logging
import pandas as pd

# Set up argument parser
parser = argparse.ArgumentParser(description="Run inference on sample data")
parser.add_argument(
    "--sample_data",
    type=str,
    required=True,
    help="Path to input CSV file containing sample data"
)

LABEL_MAP = {
    0: "malignant",
    1: "benign"
}

args = parser.parse_args()

def load_pickle(file_path):
    """
    Loads in the model and pipeline created using Pickle.

    Args:
        file_path: Path to file that should be pickled.
    """
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def main():
    """
    Loads in sample data, models, and makes predictions on the sample data.
    """
    try:
        data = pd.read_csv(args.sample_data)
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return

    try:
        model = load_pickle("classifier.pkl")
        pipeline = load_pickle("normalizer_and_data_classifier_pipeline.pkl")
    except Exception as e:
        logging.error(f"Error loading pickle files: {e}")
        return

    X = data

    raw_preds = model.predict(X)
    pipeline_preds = pipeline.predict(X)

    # Convert to labels
    raw_labels = [LABEL_MAP[p] for p in raw_preds]
    pipeline_labels = [LABEL_MAP[p] for p in pipeline_preds]

    results = (f"Your sample data contains {len(data)} entry:\n"
               f"non-normalized model predicts: {raw_labels}\n"
               f"normalized model in pipeline predicts: {pipeline_labels}")
    
    print(results)


if __name__ == "__main__":
    main()