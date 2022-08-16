def balanced_parenthesis_recursive(s):
    if s == "":
        return True

    cleaned = clean_good_signs(s)

    # if the string cannot be cleaned, it's not a valid string
    if cleaned == s:
        return False

    return balanced_parenthesis_recursive(cleaned)


def clean_good_signs(s):
    s = s.replace("()", "")
    s = s.replace("[]", "")
    s = s.replace("{}", "")
    return s


def balanced_parenthesis_iterative(s):
    stack = []
    for c in s:
        if c in [")", "}", "]"]:
            last = stack.pop()
            if not (
                    (last == "(" and c == ")") or
                    (last == "[" and c == "]") or
                    (last == "{" and c == "}")
            ):
                return False
        else:
            stack.append(c)

    return len(stack) == 0



# Test Program
assert balanced_parenthesis_recursive("()(){(())") is False
assert balanced_parenthesis_recursive("") is True
assert balanced_parenthesis_recursive("([{}])()") is True
assert balanced_parenthesis_recursive("({[}])") is False

assert balanced_parenthesis_iterative("()(){(())") is False
assert balanced_parenthesis_iterative("") is True
assert balanced_parenthesis_iterative("([{}])()") is True
assert balanced_parenthesis_iterative("({[}])") is False