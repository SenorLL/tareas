#bobble sort
nums = [8,9,5,3,7,5,6,8,3,2,1]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            ant = nums[i]
            nums[i] = nums[j]
            nums[j] = ant
            print(nums[i], nums[j])
            print(nums)
print(nums)

    