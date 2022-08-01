a = 'hyungil'
b = 'ban'

a_list = ['사과', '배', '감']
a_dict = {
    'name': 'bob',
    'age': 27
}

print(a_list)
print(a_dict)


def sum(a, b):
    print('더하자')
    return a + b


result = sum(3, 2)
print(result)


def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년입니다')


is_adult(15)

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0
for fruit in fruits:
    if fruit == '사과':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] > 20:
        print(person['name'])


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Ban", 30)

print(p1.name, p1.age)
