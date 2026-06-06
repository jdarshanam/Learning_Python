class missing_numbers_sequence:

    def find_missing_number_sequence(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) / 2
        actual_sum = sum(nums)
        missing_num = expected_sum - actual_sum
        return int(missing_num)
    
    #Finding list of numbers missing in natural numbers
    def find_missing_numbers_list(self, nums: list[int]) -> list[int]:
        min_num = min(nums)
        max_num = max(nums)
        full_num_list = range(min_num,max_num)
        print(f"full_num_list - {full_num_list}")
        missing_nums = sorted(list(set(full_num_list) - set(nums)))
        return missing_nums


def main():
    input_array = [-2,3,1,4,6]
    c = missing_numbers_sequence()
    #print(c.find_missing_number_sequence(input_array))

    print(c.find_missing_numbers_list(input_array))


if __name__ == "__main__":
    main()