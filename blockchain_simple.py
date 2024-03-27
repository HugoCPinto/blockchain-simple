import datetime as d
import hashlib as h

class Block:
    def __init__(self, id, timestamp, data, prevhash):
        self.id = id
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.hash = self.hashblock()

    def hashblock(self):
        to_encode = str( str(self.id) + str(self.timestamp) + str(self.data) + str(self.prevhash)).encode('utf-8')
        encryption = h.sha256(to_encode)
        return encryption.hexdigest()

    @staticmethod
    def genesisblock():
        return Block(0, d.datetime.now(), "first block transaction", " ")

    def newblock(tailblock):
        id = tailblock.id + 1
        timestamp = d.datetime.now()
        prevHash = tailblock.hash
        data = "Transaction id " + str(id)
        return Block(id, timestamp, data, prevHash)


blockchain = [Block.genesisblock()]
prevblock = blockchain[0]

print ("Block id: " + str(prevblock.id) + "; timestamp: " + str(prevblock.timestamp) + "; data: " + str(prevblock.data) + "; hash: " + str(prevblock.hash) + "; prevhash: " + str(prevblock.prevhash))

for i in range (0,3):
    block = Block.newblock(prevblock)
    blockchain.append(block)
    prevblock = block

    print("Block id: " + str(block.id) + "; timestamp: " + str(block.timestamp) + "; data: " + str(block.data) + "; hash: " + str(block.hash) + "; prevhash: " + str(block.prevhash))