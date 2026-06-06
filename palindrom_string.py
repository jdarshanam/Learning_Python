class palindrom_string:

    inputStr = ""
    def __init__(self, inputStr: str):
        self.inputStr = inputStr
        print(f"raw input string is - {self.inputStr}")
        self.inputStr = "".join(e.lower() for e in inputStr if e.isalnum())
        print(f"cleaned input string is - {self.inputStr}")
    
    #Solution-I, using indexes
    def using_indexes(self) -> bool:
        print(self.inputStr)
        #left, right = 0, len(self.inputStr) - 1
        #above line and below two lines are one and the same in terms of assignment
        left = 0
        right = len(self.inputStr) - 1

        while left < right:
            if self.inputStr[left] != self.inputStr[right]:
                return False
            left += 1 # left = left + 1
            right -= 1 # right = right - 1
        return True
    
    #Solution-II, using reverse funtion from collect
    def using_reverse_function(self) -> bool:
        print(f"cleaned input str - {self.inputStr}")
        revInputStr = "".join(reversed(self.inputStr))
        print(f"reversed input str - {revInputStr}")

        if self.inputStr == revInputStr:
            return True
        else:
            return False
        
    #Solution-III, using list reverse.
    def using_list_reverse(self) -> bool:
        strList = list(self.inputStr)
        strList.reverse()
        reversedStr = "".join(strList)
        print(f"reversedStr - {reversedStr}")
        if self.inputStr == reversedStr:
            return True
        else:
            return False



def main():
    inputStr = "who>><HW"
    c = palindrom_string(inputStr)
    print(c.using_indexes())
    print(c.using_reverse_function())
    print(c.using_list_reverse())

if __name__ == "__main__":
    main()