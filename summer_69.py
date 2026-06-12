def summer_69(nums: list) -> int:
    total = 0
    add = True
    for num in nums:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                break
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1,2,3,4,5,6,7,8,9,10]))