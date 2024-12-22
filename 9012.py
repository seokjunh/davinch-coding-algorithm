# 괄호

n = int(input())


for _ in range(n):
    ps = input()
    stack = []

    for j in ps:
        if not stack:
            if j == ")":
                stack.append(j)
                break
            else:
                stack.append(j)
        else:
            if stack[-1] == "(" and j == ")":
                stack.pop()
            else:
                stack.append(j)
    
    if stack:
        print("NO")
    else:
        print("YES")




