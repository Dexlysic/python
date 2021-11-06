# Initialize the blockchain list.
blockchain = []


def get_last_block():
    """ Returns the contents of the last block in the blockchain """
    return blockchain[-1]

#


def add_value(transaction_amount, last_transaction=[1]):
    """Writes the new transaction amount and last block onto the existing blockchain

    Arguments:
        transaction_amount: the amount that should be added.
        last_transaction: the last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns user's desired transaction amount as a floating number """
    return float(input("Please enter transaction amount: "))


tx_amount = get_user_input()
# User input (transaction) amount stored as variable 'tx_amount'
add_value(tx_amount)
# add_value() is called to store the new transaction into the blockchain.

tx_amount = get_user_input()
add_value(tx_amount, get_last_block())

tx_amount = get_user_input()
# Below is redundant use of keyword arguments (kwargs), simply for showing example of use.
add_value(last_transaction=get_last_block(), transaction_amount=tx_amount)

print(blockchain)
