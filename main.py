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