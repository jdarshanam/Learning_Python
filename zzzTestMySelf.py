class temp:

    def __init__(self, inputStr: str):
        self.cleaned_str = "".join(e.lower() for e in inputStr if e.isalnum())
        print(f"raw input - {inputStr}     cleaned_str - {self.cleaned_str}")
    
    #sol-I
    def find_palindrom_by_index(self) -> bool:
        left = 0
        right = len(self.cleaned_str) -1

        while left < right:
            if self.cleaned_str[left] != self.cleaned_str[right]:
                return False
            left += 1
            right -= 1
        return True


    def check_with_reversed(self) -> bool:    
        revStr = "".join(reversed(self.cleaned_str))
        if revStr == self.cleaned_str:
            return True
        else:
            return False
        
        
def main():
    #wordsList = ["eat", "tea", "tan", "ate", "nat", "bat"]
    inputStr = "whohW!fg!!!"
    c = temp(inputStr)

    print(c.find_palindrom_by_index())
    print(c.check_with_reversed())
    

if __name__ == "__main__":
    main()