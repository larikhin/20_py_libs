some_list = [1,2,3,4,5,6,78,234,23,43,23,32,43,24,2,4]

new_list = []
new_list = list(map(lambda x: str(x), some_list))

print(some_list,'\n' , new_list)
  
