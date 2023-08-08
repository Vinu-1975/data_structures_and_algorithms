def all_construct(target, word_bank):
    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [([word] + way) for way in suffix_ways]
            result.extend(target_ways)

    return result

# Test cases
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))
