from task2.trie import Trie

print("Example of using Trie")
trie = Trie()
trie.put("apple", 1)
trie.put("app", 2)
print(trie.get("apple"))  # Output: 1
print(trie.get("app"))  # Output: 2
