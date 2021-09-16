# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # if the list is empty
        if len(strs) == 0:
            return ""
        # if there is only one element that is the longest common prefix
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        prefixlength = len(prefix)

        for s in strs[1:]:
            while prefix != s[0:prefixlength]:
                prefix = prefix[0:(prefixlength - 1)]
                prefixlength -= 1

                if prefixlength == 0:
                    return ""

        return prefix 
