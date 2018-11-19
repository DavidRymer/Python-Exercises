from AdvancedExercises.Strings import longest_common_substring


def min_deletions_and_insertions(string1, string2):
    lcs_length = len(longest_common_substring(string1, string2))
    print("The minimum number of deletions is:", len(string1) - lcs_length)
    print("The minimum number of insertions is:", len(string2) - lcs_length)

min_deletions_and_insertions("heap", "pea")