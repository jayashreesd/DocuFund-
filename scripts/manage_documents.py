from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

TENDERLY_URL = os.getenv('TENDERLY_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')

w3 = Web3(Web3.HTTPProvider(TENDERLY_URL))
account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)

def store_document(ipfs_hash):
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=json.loads(os.getenv('CONTRACT_ABI')))
    
    tx = contract.functions.storeDocument(ipfs_hash).buildTransaction({
        'from': account.address,
        'gas': 500000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address),
    })

    signed_tx = w3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Document stored with transaction hash: {tx_hash.hex()}")

if __name__ == "__main__":
    ipfs_hash = 'QmSomeHashValue'
    store_document(ipfs_hash)
