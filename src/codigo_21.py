#inserccion sort
nums = [9,8,5,3,7,5,6,8,3,2,1]
for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and key < nums[j]:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
print(nums)