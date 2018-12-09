const SHA256 = require('crypto-js/sha256');

class Block {
    constructor(index, timestmap, data, previousHash='') {
        this.index = index;
        this.timestmap = timestmap;
        this.data = data;
        this.previousHash = previousHash;

        this.hash = this.calculateHash();
        this.nonce = 0;
    }

    calculateHash() {
        return SHA256(this.index + this.previousHash + this.timestmap 
            + JSON.stringify(this.data) + this.nonce).toString();
    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGenesisBlock()];
    }

    createGenesisBlock() {
        return new Block(0, '09/12/2018', 'Genesis Block', '0');
    }

    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock(newBlock) {
        newBlock.previousHash = this.getLatestBlock().hash;
        newBlock.hash = newBlock.calculateHash();
        this.chain.push(newBlock);
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
let block1 = new Block(1, '01/01/2018', {amount: 4});
ourCrypto.addBlock(block1);
ourCrypto.addBlock(new Block(2, '01/03/2018', {amount: 10}));
console.log(JSON.stringify(ourCrypto, null, 4));
console.log("Is chain vailid? " + ourCrypto.isChainValid());

block1.data = {amount: 1000};
block1.hash = block1.calculateHash();
console.log("Is chain vailid? " + ourCrypto.isChainValid());
