# Length of Longest Repeating Substring
# In this problem you are given a string of alphabetic characters. You need to find the length of the longest substring of repeating characters.
# Examples:
# longRepeat("aaa") => 3
# longRepeat("a") => 1
# longRepeat("bdsagbgagggaaatttyyyyau") => 4
# longRepeat("abcdefghijklmnopqrstuvwxyz") => 1
# longRepeat("") => 0

import math
def longRepeat(string):
    string_length = len(string)
    long_list = []
    longest = ""

    if string_length > 0:

        for i in range(string_length-1):
        
            if string[i] == string[i + 1]:
                longest = longest + string[i]
            else:
                long_list.append(len(longest) + 1)
                longest = ""
        return max(long_list)
    else:
        return string_length


print(longRepeat("bdsagbgagggaaatttyyyyau"))


