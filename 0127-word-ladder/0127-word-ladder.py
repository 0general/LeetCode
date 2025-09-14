class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        beginSet, endSet = {beginWord}, {endWord}
        L = len(beginWord)
        step = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            nextSet = set()
            for w in beginSet:
                arr = list(w)
                for i in range(L):
                    ch = arr[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == ch:
                            continue
                        arr[i] = c
                        nw = ''.join(arr)
                        if nw in endSet:
                            return step + 1
                        if nw in wordSet:
                            nextSet.add(nw)
                            wordSet.remove(nw)
                    arr[i] = ch
            beginSet = nextSet
            step += 1
        return 0