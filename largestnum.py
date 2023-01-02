
def largestNumber(nums):
    nums2 = []
    s = ''

    if len(nums) == 2:
        s1 = str(nums[0])+str(nums[1])
        s2 = str(nums[1])+str(nums[0])
        n = max(int(s1), int(s2))
        return str(n)

    for i in nums:
        if i >= 10:
            i /= 10 
        nums2.append(i)

    print(nums2)

    nums2.sort()
    print(nums2)

    for i in range(len(nums2)):
        if type(nums2[i]) == float:
            t = (nums2[i] * 10) % 10
            if t < nums2[i-1] and nums2[i] - nums2[i-1] < 1 and i != 0:
                x = nums2[i]
                nums2[i] = nums2[i-1]
                nums2[i-1] = x
    
    print(nums2)

    for i in range(len(nums2)):
        if type(nums2[i]) == float:
            nums2[i] = int(nums2[i] * 10)
    
    print(nums2)

    for i in range(len(nums2)):
        s += str(nums2.pop())

    return s



l1 = [128,12,320,32]

print(largestNumber(l1))




