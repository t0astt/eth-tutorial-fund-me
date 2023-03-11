from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAINS


def deploy_fund_me():
    account = get_account()
    # pass price feed address to fundme contract
    # anything making a state change needs to pass account
    # sepolia pricefeed address

    # if on a persistent network like sepolia, use assoc address
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print(f"Mocks deployed at {price_feed_address}")

    fund_me = FundMe.deploy(price_feed_address,
                            {"from": account},
                            publish_source=config["networks"][network.show_active()].get("verify", False))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()