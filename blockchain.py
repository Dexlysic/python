# Global-defined reward for mining a new block.
MINING_REWARD = 10

# Defines empty genesis block for the initiation of the chain.
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Nick'
participants = {'Nick'}


def create_new_hash(block):
    """ Creates a hash from a designated block.

        :block: Block which should be hashed.
    """
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    """ Stores transaction amount to tx_sender, for every transaction in the block 
        *IF* tx_sender is a participant. Checks for each block in the blockchain.

        :participant: Blockchain user whose balance is being checked.
    """
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
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
    """ Returns the contents of the last block in the blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]
# "Implicit else case"  If blockchain is empty, None type is returned and fn exits.
# No need to put following return as an 'else' statement due to this functionality.


def verify_transaction(transaction):
    """ Verifies that the sender has enough balance to complete requested transaction(s). 

        :transaction: The transaction which should be verified/checked.
    """
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


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
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    """ Functionality to mine a new block into the blockchain. """
    last_block = blockchain[-1]
    block_hash = create_new_hash(last_block)
    reward_transaction = {
        'sender': 'MINING_REWARD',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': block_hash,
        'index': len(blockchain),
        'transactions': copied_transactions
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
    # Enumerate usage example: uses tuples to extract the blocks of blockchain and assign an index.
    for (index, block) in enumerate(blockchain):
        # If on the genesis block (block 0), fn skips the check.
        if index == 0:
            continue
        # If hash of previous block != hash of newest block, return False.
        # create_new_hash() dynamically determines has of the newest block DURING the boolean check.
        if block['previous_hash'] != create_new_hash(blockchain[index - 1]):
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
        if add_transaction(recipient, amount=amount):
            print('Transaction success!')
        else:
            print('Transaction failed...  Please check your balance.')
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
                'transactions': [{'sender': 'hax0r', 'recipient': 'Max', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid.  Please pick a value from the list!')
    # 'if not' statement continually checks for 'False' being returned on verification.
    # If verification fails, execution is broken automatically exits program.
    if not verify_chain():
        print_blockchain_log()
        print('Invalid changes to blockchain detected.  Security shutdown!')
        break
    print(get_balance('Nick'))
else:
    print('Thank you for using DexCoin!')

print('Done.')
