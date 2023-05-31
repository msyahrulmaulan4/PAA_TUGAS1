class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._find_minimum(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)

        return root

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Contoh penggunaan Binary Tree untuk menyimpan informasi tentang kota-kota
city_tree = BinarySearchTree()
city_tree.insert("Jakarta")
city_tree.insert("Surabaya")
city_tree.insert("Bandung")
city_tree.insert("Yogyakarta")

# Pencarian kota dalam Binary Tree
print(city_tree.search("Surabaya"))  # Output: <__main__.Node object at 0x7f2cbea81810>
print(city_tree.search("Bali"))  # Output: None

# Menghapus kota dari Binary Tree
city_tree.delete("Bandung")
print(city_tree.search("Bandung"))  # Output: None

