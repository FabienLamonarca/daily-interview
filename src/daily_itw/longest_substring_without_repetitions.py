class Solution:

    @staticmethod
    def length_of_longest_substring(s):
        max_size = 0
        for i in range(0, len(s), 1):
            for j in range(i + 1, len(s), 1):
                if s[j] == s[j - 1]:
                    if j - i > max_size:
                        max_size = j - i
                    break
        return max_size

    @staticmethod
    def length_of_longest_substring_linear(s):
        max_size = 0
        curr_size = 0
        last_c = ""

        for c in s:

            if c == last_c:
                curr_size = 0

            curr_size = curr_size + 1
            last_c = c

            if curr_size > max_size:
                max_size = curr_size

        return max_size


if __name__ == '__main__':
    # print(Solution.length_of_longest_substring('abrkaabcdefghijjxxx'))
    print(Solution.length_of_longest_substring_linear('abrkaabcdefghijjxxx'))
    print(Solution.length_of_longest_substring_linear('abrkaabcdefghijjxxxabcdefghijk'))
