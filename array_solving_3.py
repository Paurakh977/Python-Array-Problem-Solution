nums1 = [1, 3, 5, 7, 9]
m = 5

nums2 = [2, 4, 6, 8, 10]
n = 5
for nums in nums2 :
    nums1.append(nums)

print(nums1)

for i in range(len(nums1)):
    for j in range(i+1,len(nums1)):
        if nums1[i]>nums1[j]:
            x=nums1[i]
            nums1[i]=nums1[j]
            nums1[j]=x 

print(nums1)



