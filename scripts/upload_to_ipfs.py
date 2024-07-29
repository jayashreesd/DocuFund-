import requests
import os
from dotenv import load_dotenv

load_dotenv()

IPFS_URL = os.getenv('IPFS_URL')

def upload_to_ipfs(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(
            f"{IPFS_URL}/api/v0/add",
            files={"file": f}
        )
        response_data = response.json()
        return response_data['Hash']

if __name__ == "__main__":
    file_path = 'path/to/your/file.txt'
    ipfs_hash = upload_to_ipfs(file_path)
    print(f"File uploaded to IPFS with hash: {ipfs_hash}")
