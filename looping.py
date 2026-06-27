# for i in range(5):
#     print(i+1)


# l = [1,2,3,5,2,5,2,5,3,5]
# for i in l:
#     print(i)
#  practise questions
'''1'''
# for i in range(1,11):
#     print(i)
'''2'''
# for i in range(1,21):
#     if i%2 == 0:
#         print(i)
'''3'''
# for i in range(1,11):
#     print(f"7 x {i} = {7*i}")
'''4'''
# for i in range(1,101):
#     a=0
#     a += i
#     if i == 100:
#         print(a)
'''5'''
# nums = [10, 20, 30, 40, 50, 60]
# a = 0

# for i in nums:
#     a += 1

# print(a)
'''6'''
# nums = [1, 2, 3, 4, 5]
# for i in reversed(nums):
#     print(i)
'''7'''
# nums = [1, 2, 3, 5, 2, 5, 2, 5, 3, 5]
# a = 0
# for i in nums:
#     if i == 5:
#         a += 1
# print(a)
'''8'''
# nums = [12, 45, 3, 89, 23]
# a = 0
# for i in nums:
#     if i >= a:
#         a = i
# print(a)
'''9'''
nums = [12, 45, 3, 89, 23]
smallest = nums[0]
for i in nums:
    if i < smallest:
        smallest = i

print(smallest)