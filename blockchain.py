# Initialize the blockchain list.
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Nick'
participants = {'Nick'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def verify_balance(participant):
    # Store tx amount for every tx in the block IF tx sender is a participant.  Runs for every block in the blockchain.
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_last_block():
    """ Returns the contents of the last block in the blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]
# "Implicit else case"  If blockchain is empty, None type is returned and fn exits.
# No need to put following return as an 'else' statement due to this functionality.


def add_transaction(recipient, sender=owner, amount=1.0):
    """Writes the new transaction amount and last block onto the existing blockchain

    Arguments:
        sender: sender of the transaction
        recipient: recipient of the transaction.
        amount: The amount of the designated transaction. (default=1.0)
    """
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount
                   }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    block_hash = hash_block(last_block)
    block = {
        'previous_hash': block_hash,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns user's desired transaction amount as a floating number """
    print('-' * 30)
    tx_recipient = input('Enter the recipient: ')
    tx_amount = float(input("Please enter transaction amount: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    """ Collects user input from the console interface """
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_log():
    # Output blockchain list data to the console
    for block in blockchain:
        print('Outputting next block...')
        print(block)
    else:
        print('-' * 30)


def verify_chain():
    """ Verifies the integrity of the blockchain.  """
    # Enumerate usage, uses tuples to extract the blocks of blockchain and assign an index.
    for (index, block) in enumerate(blockchain):
        # If on the genesis block (block 0), fn skips the check.
        if index == 0:
            continue
        # hash_block fn dynamically checks 'current' previous hash to the new recalculated hash.
        # If the check fails, the fn returns a 'False' boolean to indicate the blockchain is invalid.
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('-' * 30)
    print('Please choose:')
    print('1: Add a new transaction.')
    print('2: Mine a new block.')
    print('3: Output the blockchain log.')
    print('4: View list of blockchain users.')
    print('m: Attempt to manipulate the chain.')
    print('q: Quit.')
    print('-' * 30)
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_log()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'm':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid.  Please pick a value from the list!')
    # 'if not' statement below checks the previously returned value assigned to verify_chain() fn.
    if not verify_chain():
        print_blockchain_log()
        print('Invalid changes to blockchain detected.  Security shutdown!')
        break
    print(verify_balance('Nick'))
else:
    print('Thank you for using DexCoin!')

print('Done.')
