"""You have an empty sequence. You will receive an integer – N. On the next N lines you will receive queries.
Each query is one of these four types:
'1 x' – Push the element x into the stack.
'2' – Delete the element at the top of the stack.
'3' – Print the maximum element in the stack.
'4' – Print the minimum element in the stack.
After you go through all the queries, print the stack from the top to the bottom in the following format:
'{n}, {n1}, {n2} …, {nn}' """

n = int(input())
stack = []
for _ in range(n):
    query = input().split()
    command = query[0]
    if command == "1":
        x = int(query[1])
        stack.append(x)
    else:
        if stack:
            if command == "2":
                stack.pop()
            elif command == "3":
                print(max(stack))
            elif command == "4":
                print(min(stack))
print(*stack[::-1], sep=', ')