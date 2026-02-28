# from network.transaction import Transaction
# from network.mempool import Mempool
# from network.blockchain import Blockchain
# from network.miner import Miner

# # Create transactions
# tx1 = Transaction("Alice", "Bob", 0.5, 0.0001)
# tx2 = Transaction("Charlie", "Dave", 1.2, 0.0002)
# tx3 = Transaction("Eve", "Frank", 0.8, 0.00015)

# transactions = [tx1, tx2, tx3]

# # Create mempool and add transactions
# mempool = Mempool()
# for tx in transactions:
#     mempool.add_tx(tx)

# # Create blockchain
# blockchain = Blockchain()

# # Create miner
# miner = Miner(mempool, blockchain, block_size=2)

# # Mine until mempool empty
# while mempool.transactions:
#     miner.mine_block()

# print("\nFinal Blockchain:", blockchain)

# print("\nTransaction confirmations:")
# for block in blockchain.chain:
#     for tx in block.transactions:
#         print(f"{tx.tx_id} → {tx.confirmations} confirmations")

import random
from network.transaction import Transaction
from network.mempool import Mempool
from network.blockchain import Blockchain
from network.miner import Miner

# ----------------------------
# Initialize Core Components
# ----------------------------

mempool = Mempool()
blockchain = Blockchain()
miner = Miner(mempool, blockchain, block_size=3)


# ----------------------------
# Random Transaction Generator
# ----------------------------

def generate_random_transactions(step):
    # Random number of new transactions per step
    num_txs = random.randint(1, 4)

    for _ in range(num_txs):
        sender = f"User_{random.randint(1, 10)}"
        receiver = f"User_{random.randint(1, 10)}"
        amount = round(random.uniform(0.1, 2.0), 2)
        fee = round(random.uniform(0.00005, 0.0003), 6)

        tx = Transaction(sender, receiver, amount, fee)
        mempool.add_tx(tx)

    print(f"\nStep {step}: Generated {num_txs} transactions")
    print(f"Mempool size: {len(mempool.transactions)}")


# ----------------------------
# Simulation Loop
# ----------------------------

NUM_STEPS = 5

for step in range(1, NUM_STEPS + 1):
    generate_random_transactions(step)
    miner.mine_block()


# ----------------------------
# Final State Output
# ----------------------------

print("\nFinal Blockchain:", blockchain)

print("\nFinal Transaction Confirmations:")
for block in blockchain.chain:
    for tx in block.transactions:
        print(f"{tx.tx_id} → {tx.confirmations} confirmations")