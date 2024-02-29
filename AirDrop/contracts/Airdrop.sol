// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EtherCollector {
    address payable public recipient;

    constructor(address payable _recipient) {
        recipient = _recipient;
    }

    function collectAndTransfer() public payable {
        require(msg.value >= 100000000000000000   wei, "Please send exactly 0.001 ether");

        // Transfer Ether to the recipient
        payable(recipient).transfer(100000000000000000  wei);
    }

    function getBalance(address _address) public view returns(uint) {
        return _address.balance;
    }
}
