from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str) or not pattern:
            raise TypeError(
                f"Illegal argument for count_words_with_suffix: pattern = {pattern} must be a non-empty string"
            )
        matching_words = [
            word.lower() for word in self.keys() if word.endswith(pattern.lower())
        ]

        for word in matching_words:
            print(word)

        return len(matching_words)

    def has_prefix(self, prefix) -> bool:
        pass


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat", "app", "cocoapp", "dodge"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс

    print(trie.get("apple"))  # Output: 1
    print(trie.get("app"))  # Output: 2

    print(trie.count_words_with_suffix("app"))  # Output: 3

    # assert trie.count_words_with_suffix("e") == 1  # apple
    # assert trie.count_words_with_suffix("ion") == 1  # application
    # assert trie.count_words_with_suffix("a") == 1  # banana
    # assert trie.count_words_with_suffix("at") == 1  # cat

    # # Перевірка наявності префікса
    # assert trie.has_prefix("app") == True  # apple, application
    # assert trie.has_prefix("bat") == False
    # assert trie.has_prefix("ban") == True  # banana
    # assert trie.has_prefix("ca") == True  # cat
