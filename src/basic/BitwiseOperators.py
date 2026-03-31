# only works with bool and int
# first converted to binary and then compute 

# bitwise and => &
print(True & True) # True
print(3&4) # 011 & 100 => 000
print(3 & True) # True means 1 => 011 & 001 => 001
# print(34.2 & 3) # error

# bitwise or => |

print(True | False) # True
print(5 | 6) # 0101 | 0110 => 0111 => 7

# xor => ^
# if bits are different answer is 1  and if same the answer is 0
print(True ^ True) # 1 ^ 1 => 0 => False
print(4 ^ 7) # 0100 ^ 0111 => 0011 => 3