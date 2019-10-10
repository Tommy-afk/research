import hashlib
import time


class Block:
    #-----ブロックチェーンの生成クラス-----#
    def block_chain(self,block_num):       
        self.block_num=block_num
        print("Block Number:",self.block_num)

        transaction=input("transaction is:")
        self.transaction=transaction
        self.block_hash=hashlib.sha256(self.transaction.encode()).hexdigest()
        return print(str(self.block_hash),"\n")


    #-----実装次第では使わない-----#
    def next_block(self):
        print("Block Number:",self.block_num+1)
        transaction=input("transaction is:")
        self.transaction=transaction
        self.block_hash=hashlib.sha256(self.transaction.encode()).hexdigest()
        return print("This Block hash is:",self.block_hash)
        
    
def main():
    block=Block()
    for i in range(0,3):
        if i==0:
            block.block_chain(i)
        else:
            block.block_chain(i)
     

if __name__=="__main__":
    main()
