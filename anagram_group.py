class anagram_group:

    # Solution-I, using defaultDict from collections, which does not throw if KeyError, if is not present. 
    # Rather, it creates a key with empty value.
    def find_anagrams_in_list(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)

        #Iterate through input list of words
        for word in strs:
            #sorted turns the string into array.
            # we shall be using join to convert array into string
            sortedWord = "".join(sorted(word))
            anagram_map[sortedWord].append(word)
        return list(anagram_map.values())
    
    

def main():
    wordsList = ["eat", "tea", "tan", "ate", "nat", "bat"]
    c = anagram_group()
    result = c.find_anagrams_in_list(wordsList)
    print(f"result - {result}")

if __name__ == "__main__":
    main()