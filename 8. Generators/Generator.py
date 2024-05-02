#Generator

range(100) #creates one by one, not being held in memory
#list(range(100)) #creates a list of 100 items in memory

def make_list(num):
    result = []
    for i in range(num): #not being held in memory
        result.append(i * 2)
    return result

my_list = make_list(100) #this list now lives in memory
print(list(range(1000000)))

