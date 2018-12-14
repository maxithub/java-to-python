package code4fun;

import org.apache.commons.codec.digest.DigestUtils;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by max on 18-12-14.
 */
public class SImplestBlockchain {
    static class Transaction {
        private String fromAddress;
        private String toAddress;
        private BigDecimal amount;

        public Transaction(String fromAddress, String toAddress, BigDecimal amount) {
            this.fromAddress = fromAddress;
            this.toAddress = toAddress;
            this.amount = amount;
        }

        public String getFromAddress() {
            return fromAddress;
        }

        public void setFromAddress(String fromAddress) {
            this.fromAddress = fromAddress;
        }

        public String getToAddress() {
            return toAddress;
        }

        public void setToAddress(String toAddress) {
            this.toAddress = toAddress;
        }

        public BigDecimal getAmount() {
            return amount;
        }

        public void setAmount(BigDecimal amount) {
            this.amount = amount;
        }

        @Override
        public String toString() {
            return "Transaction{" +
                    "fromAddress='" + fromAddress + '\'' +
                    ", toAddress='" + toAddress + '\'' +
                    ", amount=" + amount +
                    '}';
        }
    }

    static class Block {
        private LocalDateTime timestamp;
        private List<Transaction> transactions;
        private String previousHash;
        private String hash = "";
        private int nonce = 0;

        public Block(LocalDateTime timestamp, List<Transaction> transactions,
                     String previousHash) {
            this.timestamp = timestamp;
            this.transactions = transactions;
            this.previousHash = previousHash;
        }

        public LocalDateTime getTimestamp() {
            return timestamp;
        }

        public void setTimestamp(LocalDateTime timestamp) {
            this.timestamp = timestamp;
        }

        public String getPreviousHash() {
            return previousHash;
        }

        public void setPreviousHash(String previousHash) {
            this.previousHash = previousHash;
        }

        public String getHash() {
            return hash;
        }

        public void setHash(String hash) {
            this.hash = hash;
        }

        public String calculateHash() {
            return DigestUtils.sha256Hex(toString());
        }

        public void mineBlock(int difficulty) {
            String prefix = IntStream.rangeClosed(1, difficulty)
                    .mapToObj(i -> "0").collect(Collectors.joining());
            while(!hash.startsWith(prefix)) {
                nonce ++;
                hash = calculateHash();
            }

            System.out.println("Block mined: " + hash);
        }

        @Override
        public String toString() {
            return "Block{" +
                    "timestamp=" + timestamp +
                    ", transactions=[" + transactions.stream()
                                            .map(Transaction::toString)
                                            .collect(Collectors.joining(", ")) +
                    "], previousHash='" + previousHash + '\'' +
                    ", nonce=" + nonce +
                    '}';
        }
    }

    static class Blockchain {
        private List<Block> chain = new ArrayList<>();
        private int difficulty = 4;
        private List<Transaction> pendingTransactions = new ArrayList<>();
        private BigDecimal miningReward = BigDecimal.valueOf(100);

        public Blockchain() {
            chain.add(createGenesisBlock());
        }

        private Block createGenesisBlock() {
            Block block = new Block(LocalDateTime.now(), Collections.emptyList(), "");
            block.setHash(block.calculateHash());
            return block;
        }

        public Block getLatestBlock() {
            return chain.get(chain.size() - 1);
        }

        public void minePendingTransactions(String miningRewardAddress) {
            Block block = new Block(LocalDateTime.now(), pendingTransactions, getLatestBlock().getHash());
            block.mineBlock(this.difficulty);
            pendingTransactions = new ArrayList<>();
            pendingTransactions.add(new Transaction("", miningRewardAddress, miningReward));
            System.out.println("Block successfully mined");
            chain.add(block);
        }

        public void createTransaction(Transaction transaction) {
            pendingTransactions.add(transaction);
        }

        public BigDecimal getBalanceOfAddress(String address) {
            return chain.stream().flatMap(block -> block.transactions.stream())
                    .map(transaction -> {
                        if (transaction.getFromAddress().equals(address)) {
                            return transaction.getAmount().multiply(BigDecimal.valueOf(-1));
                        }
                        if (transaction.getToAddress().equals(address)) {
                            return transaction.getAmount();
                        }
                        return BigDecimal.valueOf(0);
                    }).reduce(BigDecimal.ZERO, BigDecimal::add);

        }

        public boolean isChainValid() {
            for (int i = 1; i < chain.size(); i ++) {
                Block currentBlock = chain.get(i);
                Block previousBlock = chain.get(i - 1);

                if (!currentBlock.getHash().equals(currentBlock.calculateHash())) {
                    return false;
                }

                if (!currentBlock.getPreviousHash().equals(previousBlock.getHash())) {
                    return false;
                }
            }

            return true;
        }
    }

    public static void main(String[] args) {
        Blockchain blockchain = new Blockchain();
        blockchain.createTransaction(new Transaction("address1", "address2", BigDecimal.valueOf(100)));
        blockchain.createTransaction(new Transaction("address2", "address1", BigDecimal.valueOf(50)));
        System.out.println("Starting the miner..");
        blockchain.minePendingTransactions("miner1");
        System.out.println(String.format("Balance of the miner: %s is %s", "miner1", blockchain.getBalanceOfAddress("miner1").toString()));
        System.out.println(String.format("Balance of the miner: %s is %s", "address1", blockchain.getBalanceOfAddress("address1").toString()));
        System.out.println(String.format("Balance of the miner: %s is %s", "address2", blockchain.getBalanceOfAddress("address2").toString()));
        System.out.println("Starting the miner..");
        blockchain.minePendingTransactions("miner1");
        System.out.println(String.format("Balance of the miner: %s is %s", "miner1", blockchain.getBalanceOfAddress("miner1").toString()));
        System.out.println("Is chain valid: " + blockchain.isChainValid());
    }
}
