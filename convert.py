from web3 import Web3


bytes_content=0x48656c6c6f
string_content = Web3.toText(bytes_content)
print(string_content)


print(Web3.toBytes("Hello"))
