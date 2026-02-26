from network.transaction import Transaction

class Mempool:
    def __init__(self):
        # list to store pending transactions
        self.transactions = []

    def add_tx(self, tx: Transaction):
        self.transactions.append(tx)

    def remove_tx(self, tx: Transaction):
        if tx in self.transactions:
            self.transactions.remove(tx)

    def get_sorted_by_fee(self):
        # return transactions sorted by fee, highest first
        return sorted(self.transactions, key=lambda tx: tx.fee, reverse=True)

    def __repr__(self):
        return f"Mempool({self.transactions})"