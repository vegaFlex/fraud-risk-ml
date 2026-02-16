import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_PATH = BASE_DIR / "data" / "raw" / "creditcard.csv"
PROCESSED_PATH = BASE_DIR / "data" / "processed" / "creditcard.parquet"

def main():
    print("Reading raw CSV...")
    df = pd.read_csv(RAW_PATH)

    print("Shape:", df.shape)

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("Saving parquet...")
    df.to_parquet(PROCESSED_PATH, index=False)

    print("Done")

if __name__ == "__main__":
    main()
