from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
TENDERLY_URL = os.getenv('TENDERLY_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

w3 = Web3(Web3.HTTPProvider(TENDERLY_URL))
account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)

# Load contract
with open('contracts/DocumentStorage.json') as f:
    contract_data = json.load(f)
    abi = contract_data['abi']
    bytecode = contract_data['bytecode']

DocumentStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

def deploy_contract():
    tx = DocumentStorage.constructor().buildTransaction({
        'chainId': 1,
        'gas': 5000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address),
    })

    signed_tx = w3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    print(f"Contract deployed at address: {tx_receipt.contractAddress}")

if __name__ == "__main__":
    deploy_contract()
