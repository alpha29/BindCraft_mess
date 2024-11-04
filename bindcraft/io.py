import os
import tarfile
from pathlib import Path

import requests

from bindcraft.logger import logger

BINDCRAFT_HOME = os.getenv("BINDCRAFT_HOME", os.getcwd())
DATA_DIR = Path(BINDCRAFT_HOME) / "data"
PARAMS_DIR = Path(BINDCRAFT_HOME) / "params"


def is_empty(_dir: Path) -> bool:
    """
    helper fxn
    """
    return not any(_dir.iterdir())


def download_af_params(params_dir: str | Path = PARAMS_DIR) -> Path:
    """
    Download and extract Alphafold parameters.
    """
    params_dir = Path(params_dir)
    params_dir.mkdir(parents=True, exist_ok=True)
    if is_empty(params_dir):
        url = "https://storage.googleapis.com/alphafold/alphafold_params_2022-12-06.tar"

        logger.info(f"Downloading {url}")
        response = requests.get(url)

        tar_local_filepath = params_dir / "alphafold_params_2022-12-06.tar"
        logger.info(f"Writing to {tar_local_filepath}")
        with open(tar_local_filepath, "wb") as f:
            f.write(response.content)

        # Extract the file
        logger.info(f"Extracting into {params_dir}")
        with tarfile.open(tar_local_filepath, "r") as tar:
            tar.extractall(params_dir)
        logger.info("Done.")
    else:
        logger.info(f"{params_dir} has stuff in it; doing nothing.")
    return params_dir
