#include <iostream>
#include <vector>
using namespace std;

struct node {
    int data;
    node *left = nullptr;
    node *right = nullptr;
};

int n, Counter = 0, e;
vector<node> tree(100001);
bool visited[100001];
int parents[100001];

void chk_end(node *current_node) {
    if (current_node == nullptr) return;
    chk_end(current_node->left);
    e = current_node->data;
    chk_end(current_node->right);
}

void inorder(node *currentnode) {
    while (true) {
        if (currentnode->left && !visited[currentnode->left->data]) 
        {
            currentnode = currentnode->left;
        }
        else if (currentnode->right && !visited[currentnode->right->data]) 
        {
            currentnode = currentnode->right;
        }
        else if (currentnode->data == e) 
        {
            break;
        }
        else 
        {
            currentnode = &tree[parents[currentnode->data]];
        }
        visited[currentnode->data] = true;
        Counter++;
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int rootnode, leftnode, rightnode;
        cin >> rootnode >> leftnode >> rightnode;
        tree[rootnode].data = rootnode;
        if (leftnode != -1) {
            tree[rootnode].left = &tree[leftnode];
            parents[leftnode] = rootnode;
        }
        if (rightnode != -1) {
            tree[rootnode].right = &tree[rightnode];
            parents[rightnode] = rootnode;
        }
    }
    parents[1] = 1;

    chk_end(&tree[1]);
    inorder(&tree[1]);

    cout << Counter;
}
