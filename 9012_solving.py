T = int(input())
result = []

for _ in range(T):
    stack = []
    isVPS = True
    for char in input():
        if char == '(':
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                isVPS = False
                break

    if len(stack) > 0:
        isVPS = False

    result.append(isVPS)

for i in result:
    if i == True:
        print("YES")
    else :
        print("NO")
