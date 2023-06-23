input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

stack = []

operators = {'+', '-', '/', '*'}

for item in input:
    if item in operators:
        b = stack.pop()
        a = stack.pop()
        ans = str(int(eval(a + item + b)))

        stack.append(ans)
    else:
        stack.append(item)
    print(stack)

print(int(stack[0]))