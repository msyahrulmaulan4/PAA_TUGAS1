class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_all_words(node, prefix)

    def _get_all_words(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            results.extend(self._get_all_words(child_node, prefix + char))
        return results

# Contoh penggunaan Trie untuk sistem pengelolaan rute pengiriman barang
city_trie = Trie()

city_trie.insert("Jakarta")
city_trie.insert("Surabaya")
city_trie.insert("Bandung")
city_trie.insert("Yogyakarta")

# Pencarian cepat berdasarkan awalan
results = city_trie.search("J")
print("Kota-kota dengan awalan 'J':", results)  # Output: ['Jakarta']

results = city_trie.search("S")
print("Kota-kota dengan awalan 'S':", results)  # Output: ['Surabaya']

results = city_trie.search("B")
print("Kota-kota dengan awalan 'B':", results)  # Output: ['Bandung']

results = city_trie.search("Y")
print("Kota-kota dengan awalan 'Y':", results)  # Output: ['Yogyakarta']

# Pencarian cepat berdasarkan kesamaan string
results = city_trie.search("Sur")
print("Kota-kota dengan kesamaan string 'Sur':", results)  # Output: ['Surabaya']

results = city_trie.search("Ban")
print("Kota-kota dengan kesamaan string 'Ban':", results)  # Output: ['Bandung']
