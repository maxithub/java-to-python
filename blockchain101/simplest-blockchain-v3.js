const SHA256 = require('crypto-js/sha256');


class Transaction {
    constructor(fromAddress, toAddress, amount) {
        this.fromAddress = fromAddress;
        this.toAddress = toAddress;
        this.amount = amount;
    }
}

class Block {
    constructor(timestamp, transactions, previousHash='') {
        this.timestamp = timestamp;
        this.transactions = transactions;
        this.previousHash = previousHash;

        this.hash = '';
        this.nonce = 0;
    }

    calculateHash() {        
        return SHA256(this.timestamp + this.previousHash
            + JSON.stringify(this.transactions) + this.nonce).toString();
    }

    mineBlock(difficulty) {
        let prefix = Array(difficulty + 1).join('0');
        while(!this.hash.startsWith(prefix)) {
            this.nonce ++;
            this.hash = this.calculateHash();
        }

        console.log('Block mined: ' + this.hash);
    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGenesisBlock()]
        this.difficulty = 4;
        this.pendingTransactions = [];
        this.miningReward = 100;
    }

    createGenesisBlock() {
        let block = new Block(Date.now(), [], '');
        block.hash = block.calculateHash();
        return block;
    }

    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    minePendinTransactions(miningRecordAddress) {
        let block = new Block(Date.now(), this.pendingTransactions, this.getLatestBlock().hash);
        block.mineBlock(this.difficulty);
        this.pendingTransactions = [
            new Transaction(null, miningRecordAddress, this.miningReward)
        ];
        console.log('block successfully mined');
        this.chain.push(block);
    }

    createTransaction(transaction) {
        this.pendingTransactions.push(transaction);
    }

    getBalanceOfAddress(address) {
        let balance = 0;
        for (const block of this.chain) {
            for (const trans of block.transactions) {
                if (trans.fromAddress === address) {
                    balance -= trans.amount;
                }

                if (trans.toAddress === address) {
                    balance += trans.amount;
                }
            }
        }
        return balance;
    }

    isChainValid() {
        for (let i = 1; i < this.chain.length; i ++) {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];

            if (currentBlock.hash !== currentBlock.calculateHash()) {
                return false;
            }

            if (currentBlock.previousHash !== previousBlock.hash) {
                return false;
            }
        }

        return true;
    }
}

let ourCrypto = new Blockchain();
ourCrypto.createTransaction(new Transaction('address1', 'address2', 100));
ourCrypto.createTransaction(new Transaction('address2', 'address1', 50));
console.log('\nStarting the miner...');
ourCrypto.minePendinTransactions('our-address');
console.log('\nBalance of our account is ' + ourCrypto.getBalanceOfAddress('our-address'));
console.log('\nStarting the miner...');
ourCrypto.minePendinTransactions('our-address');
console.log('\nBalance of our account is ' + ourCrypto.getBalanceOfAddress('our-address'));