class FizzBuzz:
    def printFizzBuzz(self, n: int):
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

def main():
    f = FizzBuzz()
    f.printFizzBuzz(10)

if __name__ == "__main__":
    main()