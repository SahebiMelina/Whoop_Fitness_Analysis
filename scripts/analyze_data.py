import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/whoop_fitness_dataset_100k.csv")


def load_data():
    return pd.read_csv(DATA_PATH)


def preview_columns(df):
    print("Available columns:")
    for col in df.columns:
        print("-", col)


if __name__ == "__main__":
    df = load_data()
    print("Shape:", df.shape)
    preview_columns(df)
    print("\nSample rows:")
    print(df.head(5))
