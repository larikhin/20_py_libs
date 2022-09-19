print('_'*70)
print('start script')
print('_'*70)

some_list = [1,2,3,4,]

new_list = []
new_list = list(map(lambda x: float(x), some_list))
print(some_list,'\n' , new_list)

a = 100
l = lambda x: x + 10
b = l(a)
print(a, ' ', b)

def x_2(x):
    return x**20
print(list(map(x_2,some_list )))

print(list(map(lambda x:x**20,some_list)))
