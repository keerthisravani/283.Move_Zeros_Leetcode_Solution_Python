
def moveZeroes(nums):
    n=len(nums)
    slow=0
    fast=1
    while fast<n:
        if nums[slow]==0:
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
                fast+=1
            else:
                fast+=1
        else:
            slow+=1
            fast+=1
    return nums
nums=[1,0,0,3,4,0]
print(moveZeroes(nums))

        