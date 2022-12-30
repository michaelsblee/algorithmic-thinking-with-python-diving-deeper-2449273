def ransom_note(magazine, note):
    count_table = {}

    for word in magazine:
        if word not in count_table:
            count_table[word] = 1
        else:
            count_table[word] += 1

    for word in note:
        if word not in count_table or count_table[word] == 0: 
            return False
        else:
            count_table[word] -= 1
    return True

magazine = "give me one grand today night".split()
note = "give one grand today".split()
assert ransom_note(magazine, note) is True

magazine = "two times three is not four".split()
note = "two times two is four".split()
assert ransom_note(magazine, note) is False
