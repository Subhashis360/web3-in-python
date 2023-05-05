import web3
from web3 import Web3

# connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/998b882531b24adba6f30c717b2d5c88'))

# specify your account's private key (without the '0x' prefix)
private_key = '0123456789abcdef0123456789abcdef0123456xxxxxxxxxxxxxxxxxxxx'

# get the account object from the private key
account = w3.eth.account.from_key(f'0x{private_key}')

# get the address of the account
addrsesss = "0x000ED96F3C5636BBB1A4fa59B96C2CCD042e5000"

# get the balance of the account
balance_wei = w3.eth.get_balance(addrsesss)

# convert the balance from Wei to Ether
balance_eth = balance_wei / 10**18

print(f"The balance of {addrsesss} is {balance_wei} WEI")

print(f"The balance of {addrsesss} is {balance_eth} ETH")
