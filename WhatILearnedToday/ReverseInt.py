# x = 123
# list1 = ['flower', 'flow', 'flight']
# dict1 = {}
# count = 1
# str1 = 'theat treants beant'
# cond = []

def isValid(s: str) -> bool:
    dict1 = {')':'(',']':'[','}':'{'}
    stack = []
    
    for i in s:
        if i not in dict1.keys():
            stack.append(i)
            if len(stack) >= 2:
                return False
        elif i in dict1.keys():
            if dict1[i] in stack:
                stack.remove(dict1[i])
            else:
                stack.append(i)

    print(stack)

    # if len(stack) == 0:
    #     return True
    # else:
    #     return False

print(isValid("([)]"))#False
print(isValid("{[]}"))#True