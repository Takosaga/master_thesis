from pathlib import Path

from dotenv import load_dotenv
from loguru import logger
import pickle

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass


# --- Added Functions ---
def save_dataframe_as_pickle(df, filepath):
    """
    Saves a pandas DataFrame to a pickle file.

    Args:
        df: The pandas DataFrame to save.
        filepath: The path to the pickle file (e.g., 'data.pkl').
    """
    try:
        with open(filepath, 'wb') as f:
            pickle.dump(df, f)
        print(f"DataFrame saved to {filepath}")
    except Exception as e:
        print(f"Error saving DataFrame: {e}")

def load_dataframe_from_pickle(filepath):
    """
    Loads a pandas DataFrame from a pickle file.

    Args:
        filepath: The path to the pickle file.

    Returns:
        The loaded pandas DataFrame, or None if an error occurs.
    """
    try:
        with open(filepath, 'rb') as f:
            df = pickle.load(f)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error loading DataFrame: {e}")
        return None