from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for x in strs:
            if x=="":
                r=""
            else:
                y = list(x)
                c = list(sorted(y))
                r = "".join(c)
            if r in seen:
                seen[r].append(x)
            else:
                seen[r] = [x]
        return list(seen.values())
        