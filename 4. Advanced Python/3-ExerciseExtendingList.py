# Exercise Extending List

'''
By creating this "super list" class, we are able to extend the capability of the list method.
By adding list as the parameter, we're allowing list to become the parent class of SuperList, 
giving SuperList access to all of list's functionalities
'''
class SuperList(list): #dunde method list is now parent class
    def __len__(self):
        return 1000
    

super_list1 = SuperList()

print(len(super_list1)) #prints out the length of super_list1, after it's method modification
super_list1.append(5) #add 5 to the superlist
print(super_list1[0]) #prints out the new value, which is 5
print(issubclass(SuperList, list)) #checks if SuperList is a subclass of list