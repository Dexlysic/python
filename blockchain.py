# Initialize the blockchain list.
blockchain = []


def get_last_block():
    """ Returns the contents of the last block in the blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]
# "Implicit else case"  If blockchain is empty, None type is returned and function exits.
# No need to put following return as an 'else' statement due to this functionality.


def add_transaction(transaction_amount, last_transaction=['start.hash']):
    """Writes the new transaction amount and last block onto the existing blockchain

    Arguments:
        transaction_amount: the amount that should be added.
        last_transaction: the last blockchain transaction (default string marks beginning of blockchain)
    """
    if last_transaction == None:
        last_transaction = ['start.hash']
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns user's desired transaction amount as a floating number """
    return float(input("Please enter transaction amount: "))


def get_user_choice():
    """ Collects user input from the console interface """
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_log():
    # Output blockchain list data to the console
    for block in blockchain:
        print('Outputting new block...')
        print(block)


def verify_chain():
    """ Verifies the integrity of the blockchain.

        block_index keeps track of the current block being checked, to allow checking of previous block
                    in the list.
    """
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            # If start of blockchain, skip previous hash check by incrementing block_index and continuing
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            # If previous block matches current new block hash, return as valid blockchain transaction.
            is_valid = True
        else:
            # If not, set validity to false and break from the loop.
            is_valid = False
            break
        block_index += 1
    return is_valid
# return is_valid results in the verify_chain() function being assigned a boolean of True or False.


while True:
    print('Please choose:')
    print('1: Add a new transaction.')
    print('2: Output the blockchain log.')
    print('m: Attempt to manipulate the chain.')
    print('q: Quit.')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_block())
    elif user_choice == '2':
        print_blockchain_log()
    elif user_choice == 'm':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        print('Thank you for using DexCoin!')
        break
    else:
        print('Input was invalid.  Please pick a value from the list!')
    # 'if not' statement below checks the previously returned value assigned to verify_chain() function.
    if not verify_chain():
        print('Invalid blockchain.  Security shutdown!')
        break

print('Done.')
