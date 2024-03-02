// SPDX-License-Identifier: MIT
pragma solidity >=0.6.12 <0.9.0;

contract MarviesBet {

    uint256 answer=345;
    mapping(address => uint256) public addressToAmountStaked;
    address payable public recipient;

    constructor(address payable _recipient) {
        recipient = _recipient;
    }

    function bet() public payable {
        require(msg.value >= 100000000000000000   wei, "Insufficient betting amount the minimum is $50");
        addressToAmountStaked[msg.sender] += msg.value;

        payable(recipient).transfer(100000000000000000 wei);
    
    }

    
    // function prediction(uint256 bettingAmount, uint256 _prediction) public payable  {
    //     require(bettingAmount >= 50, "Betting amount must be at least 50 Wei");
    //     require(_prediction ==answer , "Your prediction is incorrect");
        
    //     payable(msg.sender).transfer(address(this).balance);
    // }

    // function calculateWinings(uint256 amount) public {
        
    // }
    
    

  
}
