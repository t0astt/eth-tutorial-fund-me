deploy-local:
	brownie run scripts/deploy.py

deploy-goerli:
	brownie run scripts/deploy.py --network goerli

deploy-sepolia:
	brownie run scripts/deploy.py --network sepolia

deploy-ganache-local:
	brownie run scripts/deploy.py --network ganache-local

test:
	brownie test -s

networks_list:
	brownie networks list True