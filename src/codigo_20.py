#bobble sort
nums = [9,8,5,3,7,5,6,8,3,2,1]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[j] > nums[i]:
            ant = nums[j]
            nums[j] = nums[i]
            nums[i] = ant
print(nums)

    