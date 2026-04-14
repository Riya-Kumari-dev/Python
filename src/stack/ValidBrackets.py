def valid(str) :
    stack = []
    i = 0 
    while i < len(str) :
        if str[i] in ')}]' :
            if str[i] == ')' :
                if len(stack) == 0 or stack[len(stack)-1] != '(':
                    return False
                else :
                    stack.pop()
            elif str[i] == '}' :
                if len(stack) == 0 or stack[len(stack)-1] != '{':
                    return False
                else :
                    stack.pop()
            else :
                if len(stack) == 0 or stack[len(stack)-1] != '[':
                    return False
                else :
                    stack.pop()
        else :
            stack.append(str[i])
        i+=1
    if len(stack) != 0 :
        return False
    return True

str = input("Enter a string consist of only brackets : ")
print(valid(str))