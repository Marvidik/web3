from solcx import compile_standard
import json

with open("MarviesBet.sol", "r") as solfile:
    output_sol=solfile.read()


compiled_sol=compile_standard(
    {
       "language":"Solidity",
       "sources":{"MarviesBet.sol":{"content":output_sol}},
       "settings":{
           "outputSelection":{
               "*":{
                   "*":["abi","metadata","evm.bytecode","evm.sourceMap"]
               }
           }
       }
    },
    solc_version="0.8.0",
    
)

with open("compiled_sol.json","w") as compiled_sol_json:
    json.dump(compiled_sol,compiled_sol_json)
    

bytecode=compiled_sol["contracts"]["MarviesBet.sol"]["MarviesBet"]["evm"]["bytecode"]
abi=compiled_sol["contracts"]["MarviesBet.sol"]["MarviesBet"]["abi"]
