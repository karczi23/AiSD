#include <iostream>
#include <vector>
#include <chrono>
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
    vector<long int> random_list;
    int step = 2000; // step between current and next length of generated list
    int iterations = 10; // number of iterations
    int begin_len = 1000; // length of first generated list

    cout << "len create find delete" << endl;

    for (int j = 0; j < iterations; j++) {

        long int len = begin_len + step * j; // length of the random list to generate
        random_list = rand_gen(len);
        Tree* root = new Tree(random_list[0]);
//        cout << j + 1 << "/" << iterations << endl;
        cout << len << " ";

//      creation of list
        auto begin_creation = chrono::high_resolution_clock::now();

        for (long int i = 1; i < len; i++) {
            insert(root, random_list[i]);
        }

        auto end_creation = chrono::high_resolution_clock::now();
        auto elapsed_creation = chrono::duration_cast<chrono::nanoseconds>(end_creation - begin_creation);

        cout << elapsed_creation.count() << " ";


//      finding all elements of list
        auto begin_find = chrono::high_resolution_clock::now();

        for (int num: random_list) {
            find(root, num);
        }

        auto end_find = chrono::high_resolution_clock::now();
        auto elapsed_find = chrono::duration_cast<chrono::nanoseconds>(end_find - begin_find);

        cout << elapsed_find.count() << " ";


//      deletion of list
        auto begin_delete = chrono::high_resolution_clock::now();

        del(root);

        auto end_delete = chrono::high_resolution_clock::now();
        auto elapsed_delete = chrono::duration_cast<chrono::nanoseconds>(end_delete - begin_delete);

        cout << elapsed_delete.count() << endl;
    }
    return 0;
}