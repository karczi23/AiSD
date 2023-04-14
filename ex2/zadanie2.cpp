#include <iostream>
#include <vector>
#include <chrono>
#include "Num_gen.h"
using namespace std;
vector<long int> temp_list;

struct Tree {
    int data;
    Tree* left;
    Tree* right;

    Tree(int data) {
        this->data = data;
        this->left = this->right = nullptr;
    }
};

Tree* insert(Tree* root, int data) {
    if (!root) {
        root = new Tree(data);
        return root;
    }
    if (root->data > data) {
        root->left = insert(root->left, data);
    } else {
        root->right = insert(root->right, data);
    }
    return root;
}

void del(Tree* root) {
    if (!root)
        return;
    del(root->left);
    del(root->right);
    delete root;
}


vector<long int> inorder(Tree* root) {
    if (root) {
        inorder(root->left);
        temp_list.push_back(root->data);
//        cout << root->data << endl;
        inorder(root->right);
    }
    return temp_list;
}

void postorder(Tree* root) {
    if (root) {
        postorder(root->left);
        postorder(root->right);
        cout << root->data << endl;
    }
}

vector<long int> preorder(Tree* root) {
    if (root) {
        temp_list.push_back(root->data);
//        cout << root->data << endl;
        preorder(root->left);
        preorder(root->right);
    }
    return temp_list;
}

Tree* find(Tree* root, int value) {
    if (root->data == value)
        return root;
    if (root->data > value)
        return find(root->left, value);
    else
        return find(root->right, value);
    return nullptr;
}
int find_height(Tree* root) {
    if (root == nullptr) {
        return -1;
    }

    int lefth = find_height(root->left);
    int righth = find_height(root->right);

    if (lefth > righth) {
        return lefth + 1;
    } else {
        return righth + 1;
    }
}

int main() {
    vector<long int> random_list;
    vector<long int> preorder_list;
    vector<long int> inorder_list;
    int len = 10;
    random_list = rand_gen(len);

    Tree *root = new Tree(random_list[0]);

    for (long int i = 1; i < len; i++) {
        insert(root, random_list[i]);
    }

    preorder_list = preorder(root);
    for (int num: preorder_list) {
        cout << num << endl;
    }
    cout << endl << "Wysokość tego drzewa BST wynosi: " <<find_height(root) << endl << endl;

    temp_list.clear();
    inorder_list = inorder(root);
    for (int num: inorder_list) {
        cout << num << endl;
    }

    cout << "Drzewo AVL" << endl;
    cout << inorder_list.size() / 2 << endl;
    Tree *avl = new Tree(1);
    insert(avl, 2);
    for (int num: inorder(avl)) {
        cout << num << endl;
    }

    return 0;
}