#include <iostream>
#include <vector>
#include "Num_gen.h"
using namespace std;

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

    
void inorder(Tree* root) {
    if (root) {
    	inorder(root->left);
		cout << root->data << endl;
		inorder(root->right);
    }
}

void postorder(Tree* root) {
    if (root) {
		postorder(root->left);
    	postorder(root->right);
    	cout << root->data << endl;
	}
}

void preorder(Tree* root) {
    if (root) {
    	cout << root->data << endl;
    	preorder(root->left);
		preorder(root->right);
    }
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

int main() {
    long int len = 100; // length of the random list
    Tree* root = new Tree(3);
    vector<long int> random_list;

    random_list = rand_gen(len);

//    print all numbers in random_list
//    for(int num: random_list) {
//        cout << num << " ";
//    }

    for (long int i = 0; i < len; i++) {
        insert(root, random_list[i]);
    }
    
    inorder(root);
    del(root);
    return 0;
}