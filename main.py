# Length of Longest Repeating Substring
# In this problem you are given a string of alphabetic characters. You need to find the length of the longest substring of repeating characters.
# Examples:
# longRepeat("aaa") => 3
# longRepeat("a") => 1
# longRepeat("bdsagbgagggaaatttyyyyau") => 4
# longRepeat("abcdefghijklmnopqrstuvwxyz") => 1
# longRepeat("") => 0

def longRepeat(string):
    string_length = len(string)
    long_list = []
    longest = ""

    for char in range(string_length - 1):
        print(string[char])
        if string[char] == string[char+1]:
            longest = longest + string[char]
            return longest
        elif string[char] != string[char]:
            long_list.append(len(longest))
    return max(long_list)
longRepeat("aaabbbbcccccdddd")


# Incomplete