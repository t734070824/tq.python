# for

names=[1,123,12,31,231,23,12,3]
for name in names:
    print(name)

print("-----------")

# for and pop
names=[1,123,12,31,231,23,12,3]
for name in names:
    print(name)
    names.pop(0)

# range [0, x)
print(range(123))
print(list(range(123)))

print("-----  while -----")

sum =0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

print("------- break -------")
n=1
while n <= 100:
    if n>10:
        break
    print(n)
    n=n+1
print("END")


print("------ continue ------")

n=0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)
    







