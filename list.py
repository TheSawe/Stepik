int_list = [1, 2, 3]
cut_list = int_list[1:]
print(cut_list)
print(int_list[-1])
print(int_list[0])

names1 = ['Максим', 'Лера']
names2 = ['Андрей', 'Аня']
names = names1 + names2
print(names)
print()

names.append('Вася')
print(names)
print()

names.pop(-1)
print(names)
print()

numbers = [1, 2, 3, 4, 5, 1]
print(numbers.count(1))
print()

numbers.sort()
names.sort()
print(numbers)
print(names)

word = ['abc', 'a', 'ab']
word.sort(key=len)
print(word)

numbers = [1, 2, 3, 4, 5, 1]
numbers.reverse()
print(numbers)

numbers = [1, 2, 3, 4, 5, 1]
numbers.sort(reverse=True)
print(numbers)

numbers = [1, 2, 3, 4, 5, 1]
numbers.insert(-1, 22)
print(numbers)
