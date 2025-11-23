class TrieNode:
    __slots__ = ('children', 'is_end')
    def __init__(self):
        # 26개의 자식 또는 딕셔너리 방식
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        # 내부 DFS 함수: position i in word, current trie node
        def dfs(i: int, node: TrieNode) -> bool:
            if node is None:
                return False
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                # 모든 가능한 자식 노드로 시도
                for child in node.children:
                    if child is not None and dfs(i+1, child):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                child = node.children[idx]
                return dfs(i+1, child)
        return dfs(0, self.root)