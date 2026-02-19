def aggregate(nums, op):
    if not nums:
        return None
    if op == "sum":
        return sum(nums)
    elif op == "avg":
        return sum(nums) / len(nums)
    elif op == "max":
        return max(nums)
    else:
        raise ValueError("Unsupported operation")
nums = list(map(int, input("Enter the list of numbers: ").split()))
op= input("Enter the operation: ")
print(aggregate(nums,op))
