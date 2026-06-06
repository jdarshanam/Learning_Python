#Solution - I
def charCounter(text :str):
    from collections import Counter
    
    frequencies = Counter(text)

    return frequencies

#Solution - II
def charCountDict(text :str):
    result = {}
    #prevCharCount = 0 
    for e in text:
        result[e] = result.get(e,0) + 1
        
    return result    
        
def main():
    inputStr ="AVaAcd Acd"

    freq = charCounter(inputStr)
    print("\n\nSolution - I")
    print(freq)
    
    freqs = charCountDict(inputStr)
    print("\n\nSolution - II")
    print(freqs)


if __name__ == '__main__':
    main()
    