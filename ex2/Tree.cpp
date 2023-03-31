#include <iostream>

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

int main() {
    Tree* root = new Tree(5);
    insert(root, 4);
    insert(root, 7);
    insert(root, 2);
    insert(root, 9);
    insert(root, 5);
    insert(root, 3);
    insert(root, 11);
    insert(root, 1);
    insert(root, 7);
    insert(root, 8);
    
    inorder(root);
    del(root);
    return 0;
}