from hashlib import sha256
from datetime import datetime

class Transaction:
    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount

    def __str__(self):
        return f"Transaction{{fromAddress='{self.fromAddress}', toAddress='{self.toAddress}', amount={self.amount}}}"


class Block:
    def __init__(self, timestamp=datetime.now(), transactions=[], previousHash=''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.hash = ''
        self.nonce = 0       

    def __str__(self):
        transactionStrs = [t.__str__() for t in self.transactions]
        transactionsStr = ', '.join(transactionStrs)
        return f"Block{{timestamp={self.timestamp}, transactions=[{transactionsStr}], previousHash='{self.previousHash}', nonce={self.nonce}}}"

    def mineBlock(self, difficulty):
        prefex = '0' * difficulty
        while not self.hash.startswith(prefex):
            self.nonce += 1
            self.hash = self.calculateHash()
        print(f'Block mined: {self.hash}')

    def calculateHash(self):
        return sha256(self.__str__().encode('utf-8')).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 4
        self.pendingTransactions = []
        self.miningReward = 100

    def createGenesisBlock(self):
        block = Block()
        block.hash = block.calculateHash()
        return block

    def getLatestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self, miningRewardAddress):
        block = Block(datetime.now(), self.pendingTransactions, self.getLatestBlock().hash)
        block.mineBlock(self.difficulty)
        self.pendingTransactions = [ Transaction('', miningRewardAddress, self.miningReward) ]
        print('Block successfully mined')
        self.chain.append(block)

    def createTransaction(self, transaction):
        self.pendingTransactions.append(transaction)

    def getBalanceOfAddress(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.fromAddress == address:
                    balance -= transaction.amount
                elif transaction.toAddress == address:
                    balance += transaction.amount
        return balance

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]

            if currentBlock.hash != currentBlock.calculateHash():
                return False

            if currentBlock.previousHash != previousBlock.hash:
                return False
        
        return True


blockchain = Blockchain()
blockchain.createTransaction(Transaction('address1', 'address2', 100))
blockchain.createTransaction(Transaction('address2', 'address1', 50))
print('Starting miner...')
blockchain.minePendingTransactions('miner1')
print(f"Balance of the miner: miner1 is {blockchain.getBalanceOfAddress('miner1')}")
print('Starting miner...')
blockchain.minePendingTransactions('miner1')
print(f"Balance of the miner: miner1 is {blockchain.getBalanceOfAddress('miner1')}")
print(f"Is chain valid: {blockchain.isChainValid()}")

block = blockchain.chain[1]
block.transactions = [ Transaction('some-address', 'my-address', 100000) ]
block.hash = block.calculateHash()
print(f"Is chain valid: {blockchain.isChainValid()}")