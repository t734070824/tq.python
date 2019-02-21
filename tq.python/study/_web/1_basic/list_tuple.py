### list

list = [1,2,3,4,4,55,5,31]
print(list)

list.append(123)
print(list)

print(len(list))

list.clear()
print(list)

list = [1,2,3,4,4,55,5,31]
print(list[-3])

print(list[0])
print(list[1])
print(list[-0])
print(list[-1])

list.append("123")
print(list)

list.remove(2)
print(list)

list.remove(4)
print(list)

list.insert(2, 123)
print(list)

print(list.pop())
print(list)
print(list.index(3))

print(list.pop(1))
print(list)

print(list.pop(-1))
print(list)

print(list.pop())
print(list)

list[1]="aaa";
print(list)

list[2]=[123,312,312,31,23,123,23]
print(list)
print(len(list))

### Tuple
### 不可改变
### tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，
# 指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
tuple=(1,12,31,231,23,231);
print(tuple)



