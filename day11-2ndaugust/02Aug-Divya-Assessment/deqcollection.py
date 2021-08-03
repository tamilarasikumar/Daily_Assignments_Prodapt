import collections
x = collections.deque([1,2,3,4,5])
x.append(6)
x.appendleft(0)
x.popleft()
x.pop()
print(x)
