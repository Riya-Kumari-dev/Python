import queue

def display(q) :
    while q.empty() is False : 
        print(q.get(),end=" ") # return and remove the front element
    print()

q = queue.Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(50)
display(q)