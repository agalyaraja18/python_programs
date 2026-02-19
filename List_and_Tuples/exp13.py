nums = list(map(int, input("Enter the list of numbers:").split()))
k = int(input("Enter the k value:"))
n = len(nums)
if n != 0:
    k = k % n
    start = 0
    end = n - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    start = 0
    end = k - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    start = k
    end = n - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
print(nums)
