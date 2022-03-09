#-----Iterators in python----- 
class Car:
    def __init__(self,num,cost):
        self.num = num
        self.cost = cost
    def __iter__(self):
        return self
    def __next__(self):
        if self.num > self.cost:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1

if __name__ == '__main__':
    a, b = 2, 5
    car = Car(a, b)
    obj = iter(car)
    try:
        while True:
            print(next(obj))
    except:
        print('Oh stoppped')
print('\n')
list = [1,2,3,4,5,6]
try:
    iter_list = list.__iter__()
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__()) #StopIteration Error
except:
    print("OH that's to bigger")
print('\n')
#-----Generators in Python-----
#Генератор функция 
def f_gen(number):
    s = 1
    for i in range(1, number):
        yield i**2 + s
        s += 1 
gen_f = f_gen(5)
for i in gen_f:
    print(i)
print('\n')
#Функция yield возвращает значение сохраняя в памяти свое нынешнее значение, 
#стирая свое предыдущее значение.Чтобы перейти к следующему значению используй next()
#Генераторное выражение 
generator = (i for i in range(10) if i % 2 == 0) 
for j in generator:
    print(j)
print('\n')
def gen():
    n = 1
    while True:
        yield n**2
        n += 1 

new_gen_obj = gen()
new_gen_obj2 = gen()

for i in new_gen_obj:
    print(i)
    if i > 10:
        new_gen_obj.close()
for i in new_gen_obj2:
    print(i)
    if i > 20:
        new_gen_obj2.close()
        #new_gen_obj2.throw(Exception('BAD!')) Traceback (most recent call last): ...
 
print('\n')
def send_gen(x):
    while True:
        x = yield x + 1

g = send_gen(5)
print(g.send(None))
print(g.send(10))
print('\n')