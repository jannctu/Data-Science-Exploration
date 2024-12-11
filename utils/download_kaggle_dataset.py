import os
import argparse
from dotenv import load_dotenv
load_dotenv()
from kaggle.api.kaggle_api_extended import KaggleApi



api = KaggleApi()
api.authenticate()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Download dataset from Kaggle.")
    parser.add_argument('dataset_name', type=str, help="The Kaggle dataset identifier (e.g., 'owner/dataset-name').")
    parser.add_argument('download_path', type=str, help="The path where the dataset will be saved.")
    return parser.parse_args()


def download_kaggle_dataset(dataset_name, download_path):
    # Check if the download path exists, create it if not
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Download the dataset
    api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Dataset '{dataset_name}' downloaded to {download_path}")

if __name__ == "__main__":
    # Parse arguments
    args = parse_arguments()

    # Download the dataset
    download_kaggle_dataset(args.dataset_name, args.download_path)
