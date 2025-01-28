### Базові речі для всіх поточних завдань, дерево та вставка
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


### Завдання 2: пошук мінімального елемента
def f_min(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val


### тестування
def main():
    b = TreeNode(15)
    b = insert(b, 20)
    b = insert(b, 10)
    b = insert(b, 30)
    b = insert(b, 25)
    b = insert(b, 35)

    print(f"Мінімальне значення у дереві: {f_min(b)}")


if __name__ == "__main__":
    main()
