import collections

d = collections.deque()

d.append(30)
d.append(20)
d.appendleft(10)
d.append(50)
d.append(11)
d.appendleft(5)

d.extend([20, 66, -4, 10])

d.rotate()
d.rotate()
d.rotate()
m = d.copy()

m = d.copy()

m.rotate()
print(d)
print(m)
