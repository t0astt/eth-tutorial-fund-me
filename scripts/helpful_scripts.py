from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3


FORKED_LOCAL_BLOCKCHAINS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAINS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    """
    Easy way for determining which account to test, local, testnet, prod, etc
    :return:
    """
    if network.show_active in LOCAL_BLOCKCHAINS or network.show_active() in FORKED_LOCAL_BLOCKCHAINS:
        print("Deploying to development")
        return accounts[0]
    else:
        private_key = config["wallets"]["from_key"]
        print("Deploying to network")
        print(f"Got private key {private_key}")
        return accounts.add(private_key)


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:  # Contracts are arrays holding their addresses, so we can check this to simplify
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
