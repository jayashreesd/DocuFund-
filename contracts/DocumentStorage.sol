// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentStorage {
    mapping(address => string[]) private userDocuments;

    function storeDocument(string memory documentHash) public {
        userDocuments[msg.sender].push(documentHash);
    }

    function getDocuments() public view returns (string[] memory) {
        return userDocuments[msg.sender];
    }
}
