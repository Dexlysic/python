# Declaring the list with double braces sets the 1 as a standalone nested list.
blockchain = []


def get_last_block():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=["block_start"]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input("Please enter transaction amount: "))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_block())

tx_amount = get_user_input()
# Below is redundant use of keyword arguments (kwargs), simply for showing example of use.
add_value(last_transaction=get_last_block(), transaction_amount=tx_amount)

print(blockchain)
