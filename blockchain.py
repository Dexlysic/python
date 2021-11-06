# Initialize the blockchain list.
blockchain = []


def get_last_block():
    """ Returns the contents of the last block in the blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=['chain-start']):
    """Writes the new transaction amount and last block onto the existing blockchain

    Arguments:
        transaction_amount: the amount that should be added.
        last_transaction: the last blockchain transaction (default string marks beginning of blockchain)
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns user's desired transaction amount as a floating number """
    return float(input("Please enter transaction amount: "))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_log():
    # Output blockchain list data to the console
    for block in blockchain:
        print('Outputting new block...')
        print(block)


# User input (transaction amount) stored as variable 'tx_amount'
tx_amount = get_transaction_value()
# add_value() is called to store the new transaction into the blockchain.
add_value(tx_amount)

tx_amount = get_transaction_value()
# Below is redundant use of keyword arguments (kwargs), simply for showing example of use.
add_value(last_transaction=get_last_block(), transaction_amount=tx_amount)

while True:
    print('Please choose:')
    print('1: Add a new transaction.')
    print('2: Output the blockchain log.')
    print('3: Exit.')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_block())
    else:
        print_blockchain_log()

print('END OF BLOCKCHAIN RECORD.')
