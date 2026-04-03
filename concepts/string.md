# 🧵String

## 🌟Definition

- String in Python is a sequence of Unicode characters enclosed in quotes.
- Python treats everything inside quotes as texted data.
- Strings are written inside :
  - " " (double quotes)
  - ' ' (single quotes) 
  - ''' ''' or """ """ (multi-line strings)
```
text = """ This is a
multi-line string"""
```

---
## 🗝️Immutability 

- Immutability of strings means that once a string object is created, its value cannot be changed. Any modification results in the creation of a new string object.
- Can be checked using id() (memory address)
- Why Python made strings immutable.
  1. 🔒Safety (Security) : Strings often store passwords and messages. If mutable -> can be changed accidentally.
  2. ⚡Performance Optimization : Python uses string interning.
  ```
  a = "hello"
  b = "hello"
  print(a is b) # True
  ```
  - Same memory used -> faster and saves memory.
  3. 🧠Hasing(used in dictionary) : Strings are used as dictionary keys,set elements.These require fixed values. If string changed -> dictionary breaks.❌

---
## ✂️Slicing 

- ` string[start:end:step]`
  - start included
  - end excluded 
  - step controls jump
- Steps can be positive or negative 
  1. if it is positive => it should be in forward direction
  or left to right within string, ans s[begin : end] will slice from begin till end-1 index.
  2. If it is negative => reverse direction or right to left in string, ans s[begin:end] => will slice from begin till end+1 with specified steps
- In forward direction 
  1. default begin = 0
  2. default end = len(string)
  3. default step = 1
- In backward direction
  1. default begin = -1
  2. default end = -(len(string)+1)