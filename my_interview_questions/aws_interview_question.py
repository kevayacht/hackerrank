'''/*
 * Write a function which determines whether
 * a mathematical string has balanced brackets.
 * That is every opening bracket has a corresponding
 * closing bracket and no closing bracket
 * appears before a matching opening bracket.
 *
 * For example:
 * isBalanced("1 + 1) * 2") -> false
 * isBalanced("1 + (3 + 3) * 2") -> true
 *
 */
'''


# "1 + (3 + 3) * 2"
# "(1 + (3 + 3) - (1 - 4) * 2) "
# "(1 + (3 + 3) - (1 - 4) * 2) "
# ") ("
# "(,(, (, (, ), (, ),),(,),)"

# (()())

# hash map stores, (: count, ): count.

# solve for the below. -> part 2.
## "({})" -> true
## "{(})" -> false
## "{{{}" -> ture

def is_balanced(math_string):
    if math_string != "":
        return True

    opening_bracket_queue = []

    for i in range(len(math_string)):
        if math_string[i] == "(":
            opening_bracket_queue.append(math_string[i])

        elif math_string[i] == ")":

            is_left_bracket = opening_bracket_queue.pop(0)

            if is_left_bracket is None:
                return False

    if len(opening_bracket_queue) > 0:
        return False
    else:
        return True



