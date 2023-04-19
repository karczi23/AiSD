#include <iostream>
#include <vector>
#include <chrono>
#include <math.h>
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
    cout << root->data << endl;
    delete root;

}

void del(Tree* root, int data) {
//    if (root) {
//        cout << "halo " << endl;
//        root->data = data;
//        root->left = nullptr;
//        root->right = nullptr;
//        return;
//    }
    cout << root->data << endl;
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
vector<long int> slicing(vector<long int>& arr, long int X, long int Y) {
    // Starting and Ending iterators
    auto start = arr.begin() + X;
    auto end = arr.begin() + Y + 1;

    // To store the sliced vector
    vector<long int> result(Y - X + 1);

    // Copy vector using copy function()
    copy(start, end, result.begin());

    // Return the final sliced vector
    return result;
}
void generate_avl(Tree* root, vector<long int> list) {
    long int middle = (list.size() - 1) / 2;
    insert(root, list[middle]);
//    cout << middle << " " << list[middle] << endl;
    if (list.size() == 1) {
        return;
    }
    if (middle != 0) {
//        cout << "left " << middle-1 << endl;
        generate_avl(root, slicing(list, 0, middle-1));
    }
//    cout << "right " << middle+1 << " " << list.size() << endl;
    generate_avl(root, slicing(list, middle+1, list.size()-1));
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
    int beg = 2;
    int step = 2;
    int iterations = 5000;
    int repeats = 7;
    cout << "len BST AVL" << endl;
    for (int i = 0; i < iterations; i++) {
        int len = pow(beg, i);
        random_list = rand_gen(len);
        Tree *root = new Tree(random_list[0]);
        cout << len << " ";
        for (long int i = 1; i < len; i++) {
            insert(root, random_list[i]);
        }

//    cout << "kolejność preorder: " << endl;
        preorder_list = preorder(root);
//    for (int num: preorder_list) {
//        cout << num << endl;
//    }
        cout << find_height(root)<< " ";

//    cout << "kolejność inorder: " << endl;
        temp_list.clear();
        inorder_list = inorder(root);
//    for (int num: inorder_list) {
//        cout << num << endl;
//    }


//        cout << "Drzewo AVL" << endl;
        Tree *avl = new Tree(inorder_list[inorder_list.size()/2]);
        temp_list.clear();

        generate_avl(avl, inorder_list);

//    for (int num: inorder(avl)) {
//        cout << num << endl;
//    }
        cout << find_height(avl) << endl;


//        for (int j = 0; j < repeats; j++) {
//
//        }
    }

    return 0;
}