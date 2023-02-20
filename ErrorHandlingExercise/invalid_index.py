# Handling invalid index
a = [int(x) for x in input().split()]

index = int(input())

try:
    print(a[index])
except IndexError:
    print("Invalid index")

