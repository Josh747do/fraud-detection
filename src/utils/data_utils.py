import pandas as pd
import logging

# basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_csv(path):
    """
    Load a CSV file with basic error handling.
    """
    try:
        logging.info(f"Loading data from {path}")
        df = pd.read_csv(path)
        logging.info(f"Loaded data shape: {df.shape}")
        return df
    except FileNotFoundError:
        logging.error(f"File not found: {path}")
        raise
    except Exception as e:
        logging.error(f"Error loading {path}: {e}")
        raise


def preprocess_fraud_data(df):
    """
    Basic preprocessing for Fraud_Data dataset.
    """
    try:
        logging.info("Preprocessing fraud data")

        df["signup_time"] = pd.to_datetime(df["signup_time"])
        df["purchase_time"] = pd.to_datetime(df["purchase_time"])

        df["time_since_signup"] = (
            df["purchase_time"] - df["signup_time"]
        ).dt.total_seconds() / 3600

        df["hour_of_day"] = df["purchase_time"].dt.hour
        df["day_of_week"] = df["purchase_time"].dt.dayofweek

        logging.info("Fraud data preprocessing completed")
        return df

    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")
        raise
