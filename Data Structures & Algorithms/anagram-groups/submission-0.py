class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        for s in strs: # sorting
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        
        for s in strs: # hash table
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                res[tuple(count)].append(s)
        return list(res.value()) 