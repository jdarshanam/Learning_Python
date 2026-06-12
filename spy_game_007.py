#solution-I
def spy_game_007(nums: list) -> bool:
    only_zeros_seven = []
    for num in nums:
        if num in [0,7]:
            only_zeros_seven.append(num)
    print(f"only_zeros_seven - {only_zeros_seven}")
    str_only_zeros_seven = "".join(str(n) for n in only_zeros_seven)
    print(f"str_only_zeros_seven - {str_only_zeros_seven}")
    if '007'in str_only_zeros_seven:
        return True
    else:
        return False    


#print(spy_game_007([1, 2, 4, 0, 0, 7, 5,1, 2, 4, 0, 0, 7, 5]))  # Returns True
#print(spy_game_007([1, 0, 2, 4, 0, 5, 7]))  # Returns True
#print(spy_game_007([1, 7, 2, 0, 4, 5, 0]))  # Returns False

#solution-II
def spy_game_007_sol_2(nums: list) -> bool:
    code = [0,0,7]
    for num in nums:
        if num == code[0] :
            code.pop(0)
    
        if not code: # code list is empty, means we noticed pattern
            return True
        
    return False
    
print(spy_game_007_sol_2([1, 2, 4, 0, 0, 7, 5,1, 2, 4, 0, 0, 7, 5]))  # Returns True
print(spy_game_007_sol_2([1, 0, 2, 4, 0, 5, 7]))  # Returns True
print(spy_game_007_sol_2([1, 7, 2, 0, 4, 5, 0]))  # Returns False
