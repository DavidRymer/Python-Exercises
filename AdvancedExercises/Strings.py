def longest_common_substring(string1, string2):
    string1_substrings = find_substrings(string1)
    string2_substrings = find_substrings(string2)
    common_substrings = [value for value in string1_substrings if value in string2_substrings]
    return max(common_substrings, key=len)


def find_substrings(string):
    substrings = []

    for i in range(0, len(string)+1):
        for j in range(0, len(string)+1):
            if j > i:
                substrings.append(string[i:j])
    return substrings

