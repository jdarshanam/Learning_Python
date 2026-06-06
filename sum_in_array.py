class sum_in_array:

    #Solution-I, more efficient, search complexity O(n), means searches array element atmost onces.
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        #num and index already visit for the match
        alreadyVisitNums = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in alreadyVisitNums:
                return [alreadyVisitNums[complement],index]
            
            alreadyVisitNums[num] = index
            print(f"alreadyVisitNums - {alreadyVisitNums}")
        
        #Nothing is found return empty array.
        return []
    
    #Solution-II, find pair of tuples make the target.
    def two_sum_tuples(self, nums: list[int], target: int) -> list[int]:
        #num and index already visit for the match
        alreadyVisitNums = {}
        result = ()

        for index, num in enumerate(nums):
            complement = target - num

            if complement in alreadyVisitNums:
                temp = (alreadyVisitNums[complement],index)
                result = result + (temp,)
            
            alreadyVisitNums[num] = index
            #print(f"alreadyVisitNums - {alreadyVisitNums}")
        
        #Nothing is found return empty array.
        return result
    

def main():
    searchArray = [1,2,3,4,5,6,7]
    target = 9
    c = sum_in_array()
    #solution-I
    #res = c.two_sum(searchArray,target)
    #solution-II
    res = c.two_sum_tuples(searchArray,target)
    #print(res)
    if len(res) == 0:
        print("No match found!!")
    else:
        print(f"indexes  - {res}")

if __name__ == "__main__":
    main()



















