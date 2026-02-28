from network.block import Block

class Miner:
    def __init__(self, mempool, blockchain, block_size=2):
        self.mempool = mempool
        self.blockchain = blockchain
        self.block_size = block_size  # max tx per block

    def mine_block(self):
        # Get highest fee transactions
        sorted_txs = self.mempool.get_sorted_by_fee()
        selected_txs = sorted_txs[:self.block_size]

        # Remove them from mempool
        for tx in selected_txs:
            self.mempool.remove_tx(tx)

        # Determine block height
        height = len(self.blockchain.chain) + 1

        # Create block
        new_block = Block(height=height, transactions=selected_txs)

        # Add to blockchain
        self.blockchain.add_block(new_block)

        print(f"Block {height} mined with {len(selected_txs)} transactions")
        return new_block