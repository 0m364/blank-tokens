contract = web3.eth.contract(address=contract_address, abi=contract_abi)
tx_hash = contract.functions.mint(bot_address, amount).transact({'from': my_address})
