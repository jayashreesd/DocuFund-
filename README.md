# OLAS Autonomy

## Overview

OLAS Autonomy is a project for managing and storing documents using IPFS and Ethereum smart contracts. The project includes functionalities for deploying a smart contract, uploading documents to IPFS, storing document references on the Ethereum blockchain, and executing multisend transactions.

## Project Structure

- `contracts/`: Contains Solidity smart contracts.
- `scripts/`: Python scripts for deployment, IPFS upload, multisend, and document management.
- `docker/`: Docker configuration files.
- `.env`: Environment variables.
- `skills.yaml`: List of skills and technologies used.
- `README.md`: Project documentation.

## Setup
1. Clone the repository
   git clone (https://github.com/jayashreesd/DocuFund-.git)
   cd DocuFund
   
2.Create and Configure Environment Variables
Create a .env file in the root of your project with the following contents:

TENDERLY_URL=https://mainnet.gateway.tenderly.co/YOUR_PROJECT_ID
CONTRACT_ADDRESS=0xYourContractAddress
CONTRACT_ABI='[Your Contract ABI]'
PRIVATE_KEY=your_private_key
LOG_FILE_PATH=/app/logs/monitor.log


3. **Install Dependencies**
   Create a virtual environment and install the dependencies specified in requirements.txt:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt


   
