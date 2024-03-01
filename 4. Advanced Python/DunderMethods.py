#Dunder Methods
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name':'Yoyo',
            'has_pets': False
        }

    def __str__(self): #modified str dunder method
        return f'{self.color}'
    
    def __len__(self): #modified len dunder method
        return 5

    def __del__(self): #modified del dunder method
        print('deleted')

    def __call__(self): #modified call dunder method
        return('yes??')
    
    def __getitem__(self,i): #modified getitem dunder method
        return self.my_dict[i]
    
    def __abs__(self, num):
        return num

    def __hex__(self):
        return 6

    def __set__(self):
        return 'done setting'


action_figure = Toy('red', 0)
print(action_figure.__str__()) #will perform the new defined str method behavior
print(str(action_figure)) #will perform the new defined str method behavior
print(len(action_figure)) #will perform the new defined len method behavior
#del action_figure #will perform the new defined del method behavior
print(action_figure()) #will perform new defined call method behavior
print(action_figure['name']) #will perform new defined getitem method behavior
print(action_figure.__abs__(-50))
print(action_figure.__hex__())
print(action_figure.__set__())