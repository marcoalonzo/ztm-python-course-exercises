# Ternary Operator

#condition_if_true if condition else condition_if_else
'''
if the condition is true, then we're going to run the "if true condition"
on the left. If the condition is not true, then we are going to run the "if else condition"
on the right
'''
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)