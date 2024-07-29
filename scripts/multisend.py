from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Set up Web3 connection
# Load environment variables
TENDERLY_URL = os.getenv('TENDERLY_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
CONTRACT_ABI = os.getenv('CONTRACT_ABI')

# Check if environment variables are loaded correctly
if not all([TENDERLY_URL, PRIVATE_KEY, CONTRACT_ADDRESS, CONTRACT_ABI]):
    raise ValueError("One or more environment variables are missing or incorrect.")

w3 = Web3(Web3.HTTPProvider(TENDERLY_URL))
account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)

def multisend(addresses, amounts):
    try:
        # Load the contract ABI
        abi = json.loads(CONTRACT_ABI)
        contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

        # Build the transaction
        tx = {
            'from': account.address,
            'gas': 500000,
            'gasPrice': w3.toWei('20', 'gwei'),
            'nonce': w3.eth.getTransactionCount(account.address),
        }

        # Call the contract method
        tx_data = contract.functions.distribute(addresses, amounts).buildTransaction(tx)

        # Sign and send the transaction
        signed_tx = w3.eth.account.signTransaction(tx_data, private_key=PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction receipt: {tx_receipt}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    addresses = ['0xAddress1', '0xAddress2']
    amounts = [1000, 2000]
    multisend(addresses, amounts)
