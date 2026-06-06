class ReverseStringSolutions:
    
    #Solution-I using reverse function
    def reverseWithFunction(self,inputStr: str) -> str:
        return "".join(reversed(inputStr))
    
    #Solution-II using indexes
    def reverseUsingIndexes(self, inputStr: str) -> str:
        return inputStr[::-1]
    
    #Solution-III using reverse function of list
    def reverseUsingList(self, inputStr: str) -> str:
        listStr = list(inputStr)
        listStr.reverse() #inplace reverse
        return "".join(listStr)

def main():
    c = ReverseStringSolutions()
    inputStr = "abcdef"
    #print(c.reverseWithFunction(inputStr))
    #print(c.reverseUsingIndexes(inputStr))
    print(c.reverseUsingList(inputStr))

if __name__ == "__main__":
    main()


