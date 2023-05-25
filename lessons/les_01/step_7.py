age = 18

if age >= 18:
    print('access granted')
elif age >= 16:
    print('access granted (partial)')
else:
    print('access denied')


print([1, (1,)])

l1 = [1,2,3]
t1 = tuple([1, l1])
print(id(t1), t1)

l1 = [1,2,3]
t1 = tuple([1, l1])
print(type(t1), id(t1), t1)