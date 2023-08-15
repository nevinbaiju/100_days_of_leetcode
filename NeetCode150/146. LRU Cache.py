class Node:
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        if self.val:
            return str(f'{self.key}: {self.val}')
        else:
            return "None"

class LRUCache:
    
    def __debug(self):
        return
        ptr = self.left
        print("left to right")
        while ptr:
            print(ptr, sep=" ", end=" -> ")
            ptr = ptr.right
        print()
        
        print("right to left")
        
        
        ptr = self.right
        while ptr:
            print(ptr, sep=" ", end=" -> ")
            ptr = ptr.left
        print('\n')

    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.left.right = self.right
        self.right.left = self.left

        self.map = {}
        self.cap = capacity 
        

    def get(self, key: int) -> int:
        node = self.map.get(key, None)
        if node:
            node.left.right = node.right
            node.right.left = node.left

            node.right = self.left.right
            node.left = self.left
            self.left.right.left = node
            self.left.right = node

            self.__debug()
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if not key in self.map and len(self.map.keys()) == self.cap:
            del_node = self.right.left
#             print(del_node)
            self.right.left = del_node.left
            del_node.left.right = self.right
            self.map.pop(del_node.key)
        if key in self.map:
            node = self.map[key]
            node.val = value
            node.left.right = node.right
            node.right.left = node.left
        else:
            node = Node(key, value)
        node.right = self.left.right
        node.right.left = node
        node.left = self.left
        self.left.right = node
        self.map[key] = node
        self.__debug()
