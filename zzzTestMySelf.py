class reverse_string:

    #Solution-I
    def withReversedFunction(self ,inputStr: str) -> str:
        rStr = reversed(inputStr) # It converts to reversed class
        print(type(rStr))
        return "".join(rStr)
    
    #Solution-II
    def withIndexes(self, inputStr: str) -> str:
        return inputStr[::-1]
    
    #Solution-III
    def withList(self, inputstr: str) :
        listStr = list(inputstr)
        listStr.reverse()
        return "".join(listStr)


def main():
    inputStr = "abcd"
    c = reverse_string()
    #print(c.withReversedFunction(inputStr))
    #print(c.withIndexes(inputStr))
    print(c.withList(inputStr))


if __name__ == "__main__" :
    main()