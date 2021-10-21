
if __name__ == '__main__':

    # a = (1, 2, [1, 4],) # Создали обьект с типом данных кортеж и присвоили ему переменную
    # print(id(a)) # Вывели id обьекта
    # a[2].append(3)
    # print(a)
    # print(id(a))
    # a = (1, 2, [6, 4],)
    # print(a)
    #
    #
    # a = (1, 2, [3, 5],)
    # print(id(a))
    # a[2].append(3)
    # print(a)
    # a = [1, 4, 2, 9, 7, 8, 9, 3, 1]
    # x = a.count(1)
    # print(a)

    d = {}
    d[1] = 1
    print(d)

    d = {'dict': 1, 'dictionary': 2}
    print(d)

    d = dict(short='dict', long='dictionary')
    print(d)
    d = dict.fromkeys(['a', 'b'], 100)

#       dict.clear

    d = {1: "one", 2: "two"}

    d.clear()
    print('d =', d)

#       dict.copy

    original = {1: 'one', 2: 'two'}
    new = original.copy()

    print('оригинал: ', original)
    print('новый: ', new)

#       dict.get

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.get("price", 15000)

    print(x)

#       dict.items

    sales = {'apple': 2, 'orange': 3, 'grapes': 4}

    print(sales.items())

#       dict.keys

    # Python program to show working
    # of keys in Dictionary

    # Dictionary with three keys
    Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

    # Printing keys of dictionary
    print(Dictionary1.keys())

    # Creating empty Dictionary
    empty_Dict1 = {}

    # Printing keys of Empty Dictionary
    print(empty_Dict1.keys())

#       dict.pop

    marks = {'Physics': 67, 'Chemistry': 72, 'Math': 89}

    element = marks.pop('Chemistry')

    print('Popped Marks:', element)

#       dict.popitem

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car.popitem()

    print(car)

#       dict.setdefault

    person = {'name': 'Phill', 'age': 22}

    age = person.setdefault('age')
    print('person = ', person)
    print('Age = ', age)

#       dict.update

    marks = {'Physics': 67, 'Maths': 87}
    internal_marks = {'Practical': 48}

    marks.update(internal_marks)

    print(marks)

#       dict.values

    marks = {'Physics': 67, 'Maths': 87}

    print(marks.values())