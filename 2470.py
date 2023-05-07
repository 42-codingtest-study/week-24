n = int(input())
num_list = list(map(int, input().split()))
num_list = sorted(num_list)
left = 0
right = n-1
final = []
limit =21000000001

while left < right :     
    res = num_list[left] + num_list[right]
    # sum_list.append(res)
    if abs(res) < limit:
        limit = abs(res)
        final = [num_list[left], num_list[right]]
        
    if res < 0 :
        left += 1
    elif res > 0 :
        right -= 1
    else: 
        break
print(final[0], final[1])
    

# for i in range(n):
#     res = abs(num_list[left] + num_list[right])
#     sum_list.append(res)
#     if res == 0:
#         print(num_list[left], num_list[right])
#     final = [num_list[left], num_list[right]]
#         for j in sum_list:
#             if j <= limit:
#                 limit = j
#         for j in sum_list:
#             if j == limit:
#     left += 1
#     right -= 1