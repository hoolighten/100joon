import sys

input = sys.stdin.readline
n = int(input())
tree_graph = {}
for i in range(n):
    root, left, right = map(str, input().split())
    tree_graph[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree_graph[root][0])
        preorder(tree_graph[root][1])
    return 0
def inorder(root):
    if root != '.':
        inorder(tree_graph[root][0])
        print(root, end = '')
        inorder(tree_graph[root][1])
    return 0
def postorder(root):
    if root != '.':
        postorder(tree_graph[root][0])
        postorder(tree_graph[root][1])
        print(root, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')
