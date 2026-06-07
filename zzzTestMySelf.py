class temp:

    #Sol-I
    def sum_in_array_look_back(self, nums: list[int], target: int) -> list[int]:
        look_back = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in look_back:
                return [look_back.get(complement),index]
            else:
                look_back[num] = index
        return []

    #Sol-I
    def sum_in_array_multi_match(self, nums: list[int], target: int) -> list[list[int]]:
        look_back = {}
        result = []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in look_back:
                result.append((look_back.get(complement),index))
            else:
                look_back[num] = index
        return result
        
def main():
    input = [1,2,3,4,5,6,7,8,9]
    target = 7
    c = temp()
    print(c.sum_in_array_look_back(input,target))
    print(c.sum_in_array_multi_match(input,target))
    

if __name__ == "__main__":
    main()