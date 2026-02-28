from network.block import Block
from network.transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []  # list of Block objects

    def add_block(self, block: Block):
        # Link to previous block if exists
        if self.chain:
            block.previous_block = self.chain[-1]
        self.chain.append(block)
        # Update confirmations
        self.update_confirmations()

    def update_confirmations(self):
        # For each transaction in the chain, count how many blocks include it after its block
        for i, block in enumerate(self.chain):
            confirmations = len(self.chain) - i
            for tx in block.transactions:
                tx.confirmations = confirmations

    def get_confirmations(self, tx_id):
        # Return confirmation count of a transaction
        for block in self.chain:
            for tx in block.transactions:
                if tx.tx_id == tx_id:
                    return tx.confirmations
        return 0

    def __repr__(self):
        return f"Blockchain({[block.height for block in self.chain]})"