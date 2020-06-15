
def check_magazine(magazine, note):
    """

    :param magazine:
    :param note:
    :return:
    """
    mag = dict()

    for index, value in enumerate(magazine):
        if mag.get(value, None) is None:
            mag.update({value: 1})
        else:
            mag[value] += 1

    for word in note:
        if mag.get(word, 0) != 0:
            mag[word] -= 1
        else:
            return False

    return True


def main():
    # magazine = ["give", "Give", "me", "one", "grand", "today", "night", "today", "or" "the", "girl", "dies"]    # all present
    magazine = ["give", "Give", "me", "one", "grand", "today", "night", "today", "or" "the", "dies"]    # missing word
    note = ["Give", "me", "one", "grand", "today", "or" "the", "girl", "dies", "today"]
    result = check_magazine(magazine, note)
    print(result)


if __name__ == "__main__":
    main()
