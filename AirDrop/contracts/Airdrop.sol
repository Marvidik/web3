// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Airdrop {
    address payable public recipient;

    constructor(address payable _recipient) {
        recipient = _recipient;
    }

    function displayAmount() public payable returns(uint256){

            return 345;
    }

    function transferEther() public {
        uint256 amountToSend = 50;
        

        payable(recipient).transfer(amountToSend);
    }
}
