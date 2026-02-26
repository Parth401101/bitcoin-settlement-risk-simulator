import uuid

class Transaction:
    def __init__(self, sender, receiver, amount, fee):
        # unique transaction ID
        self.tx_id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        # starts with 0 confirmations
        self.confirmations = 0

    def __repr__(self):
        return (f"Transaction(tx_id={self.tx_id}, sender={self.sender}, "
                f"receiver={self.receiver}, amount={self.amount}, "
                f"fee={self.fee}, confirmations={self.confirmations})")