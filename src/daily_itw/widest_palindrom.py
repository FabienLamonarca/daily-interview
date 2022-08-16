def longest_palindrome(s):
    longest_pal = ""
    for center in range(0, len(s)):

        # expends around ; center can be this char only or center+1
        pal1 = get_pal(s, center, center)
        pal2 = get_pal(s, center, center + 1)

        if len(pal1) > len(longest_pal):
            longest_pal = pal1
        if len(pal2) > len(longest_pal):
            longest_pal = pal2

    return longest_pal


def get_pal(s, left_cursor, right_cursor):
    pal = s[left_cursor:right_cursor]

    while left_cursor > 0 and right_cursor < len(s):
        if s[left_cursor] == s[right_cursor]:
            pal = s[left_cursor:right_cursor + 1]
            left_cursor = left_cursor - 1
            right_cursor = right_cursor + 1
        else:
            return pal

    return pal


if __name__ == '__main__':
    print(longest_palindrome("tracecarskkkkayakkkk"))
