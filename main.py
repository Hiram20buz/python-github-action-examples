import logging
import logging.handlers
import os
import requests
from datetime import datetime


# Set up logging configuration
log_file = 'solana_price.log'

logger = logging.getLogger('SolanaPrice')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Function to fetch Solana price in MXN
def fetch_solana_price():
    try:
        # Make a GET request to fetch Solana price data from an API (CoinGecko in this case)
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=mxn')
        if response.status_code == 200:
            solana_price = response.json().get('solana', {}).get('mxn')
            if solana_price:
                return solana_price
            else:
                logger.error("Unable to retrieve Solana price in MXN")
        else:
            logger.error(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        logger.exception(f"Request Exception: {e}")
    return None

# Log Solana price in MXN to the file
solana_price = fetch_solana_price()
if solana_price:
    logger.info(f"Solana price in MXN: {solana_price} MXN at {datetime.now()}")

# Example of reading the log file
if os.path.exists(log_file):
    with open(log_file, 'r') as file:
        log_content = file.read()
        print(log_content)
