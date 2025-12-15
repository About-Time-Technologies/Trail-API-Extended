
from typing import List
import csv
import os
import logging

logger = logging.getLogger(__name__)

def get_asset_ids(input_str: str) -> List[str]:
    if input_str.lower().endswith(".csv"):
        if not os.path.exists(input_str):
            raise FileNotFoundError(f"The specified CSV file '{input_str}' does not exist.")
        
        asset_ids: List[str] = []
        logger.debug(f"Loading asset asset_ids from {input_str}...")
        with open(input_str, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                asset_ids.append(row[0].strip())
        logger.debug(f"Loaded {len(asset_ids)} asset ids.")
        return asset_ids
    else:
        return [input_str]