'''
list []
list()
ordered , mutable , iterable

'''

ch = ['a','b','c','d','e']
# print(type(ch))
# print(ch)

# TODO: indexing
# print(ch[0])
# print(ch[-1])

# TODO: mutable
# print(ch)
# ch[0] = 'z'
# print(ch)

# TODO: iterable
# for i in ch:
#     print(i)

# for index in range(5)
# for index in range(len(ch)):
#     print(ch[index] , index)


# TODO: slicing -
# list_name[start_idx : end_idx + 1 : step]

# print(ch[1:4])
# print(ch[0 : 5 : 2])

# print(ch[: : -1])
# print(ch[::])
# print(ch[2:])
# print(ch[: 3])

# print(ch[-4:-1])

ch.append('f')
# print(ch)

ch.extend(['g','h'])
print(ch)

# ch.pop()
# ch.pop(1)
# print(ch)

# ch.remove('g')
# print(ch)

# print(ch.count('a'))

# print(ch.index('b'))

ch.insert(3,'z')
print(ch)

# ch.sort()
# ch.sort(reverse=True)
# print(ch)

ch.reverse()
print(ch)