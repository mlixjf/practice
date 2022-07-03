from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)
q.appendleft(323)
q.append(4)
print(q)


q1 = deque(maxlen=3)
q1.append(1)
q1.append(2)
q1.append(3)
q1.append(3)
print(q1)