from network.transaction import Transaction

# create 3 sample transactions
tx1 = Transaction("Alice", "Bob", 0.5, 0.0001)
tx2 = Transaction("Charlie", "Dave", 1.2, 0.0002)
tx3 = Transaction("Eve", "Frank", 0.8, 0.00015)

# put them in a list
transactions = [tx1, tx2, tx3]

# print them
for tx in transactions:
    print(tx)


from network.mempool import Mempool

# create mempool
mempool = Mempool()

# add transactions
for tx in transactions:
    mempool.add_tx(tx)

# print mempool
print("Mempool initial state:")
print(mempool)

# print sorted by fee
print("\nMempool sorted by fee (highest first):")
sorted_txs = mempool.get_sorted_by_fee()
for tx in sorted_txs:
    print(tx)

# remove a tx
mempool.remove_tx(tx2)
print("\nMempool after removing tx2:")
print(mempool)



from network.block import Block

# Mine a block manually using top 2 transactions from sorted mempool
top_txs = mempool.get_sorted_by_fee()[:2]
block1 = Block(height=1, transactions=top_txs)

print("\nBlock 1 mined with transactions:")
print(block1)