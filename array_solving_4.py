nums = [0,1,2,2,3,0,4,2]
val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
k=0
i=0
while i< len(nums):
    if nums[i]==val:
        del nums[i]
    elif nums[i]!=val:
        k+=1
        i+=1

print("Output (k):", k)
print("Modified nums:", nums)