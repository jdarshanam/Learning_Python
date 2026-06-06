class chars_in_a_string:
    
    #Solution-I
    def count_chars_using_dict(self, inputStr: str) -> dict:
        result = {}
        for e in inputStr:
            result[e] = result.get(e,0) + 1
        return result
    
    #Solution-II
    def count_chars_using_function(self, inputStr: str) -> dict:
        from collections import Counter
        freq = Counter(inputStr)
        return freq
    
def main():
    inputStr = "abcabAbC"
    c = chars_in_a_string()
    print(c.count_chars_using_dict(inputStr))
    print(c.count_chars_using_function(inputStr))
    cntr  = c.count_chars_using_function(inputStr)
    print(cntr.total())
    print(cntr['A'])
    

if __name__ == "__main__" :
    main()
