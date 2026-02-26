from network.transaction import Transaction

class Block:
    def __init__(self, height, transactions, previous_block=None):
        self.height = height
        self.transactions = transactions  # list of Transaction objects
        self.previous_block = previous_block  # link to previous block

    def __repr__(self):
        tx_ids = [tx.tx_id for tx in self.transactions]
        return f"Block(height={self.height}, tx_ids={tx_ids})"