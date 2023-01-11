from _collections import  deque

example_q = deque()

example_q.append(1)
example_q.append(2)
example_q.append(3)
example_q.append(4)

while example_q:
    print(example_q.popleft()) 