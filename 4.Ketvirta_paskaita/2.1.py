def equal_halfs(num):
#     digit_count = (len(str(num)))
#     num_list = [int(i) for i in str(num)]
#     sum1 = 0
#     sum2 = 0
#     if digit_count % 2 == 0:
#         half = int(digit_count / 2)
#         for i in range(half):
#             sum1 += num_list[i]
#         for i in range(half, len(num_list)):
#             sum2 += num_list[i]
#     else:
#         half = int(digit_count / 2) + 1
#         for i in range(half):
#             sum1 += num_list[i]
#         for i in range(half-1, len(num_list)):
#             sum2 += num_list[i]
#     if sum1 == sum2:
#         return True
#     else:
#         return False
#
# print(equal_halfs(1221))
# print(equal_halfs(51215))
# print(equal_halfs(1234))
# print(equal_halfs(565656))