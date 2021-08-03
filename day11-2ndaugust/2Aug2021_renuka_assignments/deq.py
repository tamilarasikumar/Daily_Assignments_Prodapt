#deque-Double Ended Queue
import collections #in normal list we can add items only to one side but in deque we can add items to both sides
x=collections.deque([1,2,3,4,5])
x.appendleft(0)
print(x)
x.append(6)
print(x)
x.pop()
print(x)
x.popleft()
print(x)