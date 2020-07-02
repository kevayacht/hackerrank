def is_balanced(s):
    stack = []
    value = False

    for i in range(0, len(s)):

        if any([s[i] == "{", s[i] == "(", s[i] == "["]):
            stack.append(s[i])

        elif any([s[i] == "}", s[i] == ")", s[i] == "]"]):
            if len(stack) == 0:
                return False

            else:
                element = stack.pop()

                if s[i] == "}" and element == "{":
                    value = True
                elif s[i] == ")" and element == "(":
                    value = True
                elif s[i] == "]" and element == "[":
                    value = True
                else:
                    return False
        else:
            return False

    # this ensures the stack is empty, else it can't possibly be balanced.
    if len(stack) == 0:
        return value
    else:
        return "NO"


def main():
    # a = "{[()]}"
    # a = "{[(])}"
    # a = "{{[[(())]]}}"
    # a = "[{"
    a = "}([]]][[){}}[[)}[(}(}]{(}[{}][{}](}]}))]{][[}(({(]}[]{[{){{(}}[){[][{[]{[}}[)]}}]{}}(}"
    result = is_balanced(a)

    if result:
        print("YES")

    else:
        print("NO")


if __name__ == "__main__":
    main()
