class reverse_string:

    #Solution-I
    def withReversedFunction(self ,inputStr: str) -> str:
        rStr = reversed(inputStr)
        print(type(rStr))
        return "".join(rStr)
    

def main():
    inputStr = "abcd"
    c = reverse_string()
    print(c.withReversedFunction(inputStr))


if __name__ == "__main__" :
    main()