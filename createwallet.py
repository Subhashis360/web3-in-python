import secrets
from eth_account import Account, Mnemonic

while True:
    mnemonic = Mnemonic.generate()

    print("phrase :", mnemonic)

    # Generate a private key
    privs = secrets.token_hex(32)
    private_key = "0x" + privs
    print("SAVE BUT DO NOT SHARE THIS:", private_key)

    # Create an instance of the account with the generated private key
    acct = Account.from_key(private_key)
    print("Address:", acct.address)

    with open('wallet_info.txt', 'a') as f:
        f.write(f'\n{acct.address}||{private_key}')
        f.close()
