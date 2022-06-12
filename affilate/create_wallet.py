from tronpy import Tron

client = Tron()

# create a Tron wallet and print out the wallet address & private key
def create_wallet():
    wallet = client.generate_address()
    print("Wallet address:  %s" % wallet['base58check_address'])
    print("Private Key:  %s" % wallet['private_key'])
    return wallet['base58check_address'] , wallet['private_key']

def get_blance(user):
    return client.get_asset("usdt")
    pass
