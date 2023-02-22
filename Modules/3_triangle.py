# the code will be imported in the module triangle_from_numbers

# n = int(input())
#
#
# def print_up_part(n):
#     for row_num in range(1, n+1):
#         for num in range(1, row_num + 1):
#             print(num, end="")
#         # once finished go to the next row
#         print()
#         # n= 3
#         # 1
#         # 12
#         # 123
#
# def print_bottom(n):
#     for row_number in range(n-1, 0, -1):
#         for number in range(1, row_number + 1):
#             print(number, end="")
#         print()
#         # 12
#         # 1
#
#
# def print_triangle(n):
#     print_up_part(n)
#     print_bottom(n)
#
#
# print_triangle(n)

from triangle_from_numbers.triangle import print_triangle

n = int(input())
print_triangle(n)