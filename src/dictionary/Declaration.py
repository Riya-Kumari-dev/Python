# dictionary
# key:value
# duplicate keys are not allowed
# heterogeneous object are allowed for both keys and value 
# It is not mandatory that all kets are of same type
# It is not mandatory that all values are of same type
# Insertion order is not preserved
# Mutable
# Dynamic
# Indexing and slicing concept is not there in case of dict

d = {}
print(type(d)) # <class 'dict'>
d = {1:"Pankaj",2:"Eiya",12:"Aditi"} 
print(d) # # {1: 'Pankaj', 2: 'Eiya', 12: 'Aditi'}
l = [(1,"Riya"),(2,"Aditi"),(23,"Gupta")] # set of pairs in list
d = dict(l)
print(d) # {1: 'Riya', 2: 'Aditi', 23: 'Gupta'}
d = dict.fromkeys([2,3,4]) # providing keys to d => it doesn't have values so by default values are None
print(d) # {2: None, 3: None, 4: None}
d = dict.fromkeys([5,3,2],0) # all values are 0
print(d) # {5: 0, 3: 0, 2: 0}

# if keys are same then the key will be updated with that most recent key value
d = {1:"Riya",2:"aditi",1:"Sinha",3:"Find"}
print(d) # {1: 'Sinha', 2: 'aditi', 3: 'Find'}