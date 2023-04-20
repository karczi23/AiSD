#include <iostream>
#include <vector>
#include <chrono>
#include <math.h>
#include <algorithm>
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

vector<long int> postorder(Tree* root) {
    if (root) {
        postorder(root->left);
        postorder(root->right);
        temp_list.push_back(root->data);
    }
    return temp_list;
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

void find_height(Tree* root, int num, int height = 0) {
    if (root == nullptr) {
        return;
    }
    if (num == root->data) {
        cout << height;
        return;
    } else {
        find_height(root->left, num, height + 1);
        find_height(root->right, num, height + 1);
    }
}
int main() {
    vector<long int> input_list = {43, 11, 23, 322, 13};
    vector<long int> output_list;
    vector<long int> inorder_list;
//    int beg = 2;
//    int iterations = 5;
//    int len = pow(beg, i);
//    input_list = rand_gen(len);
    int len = input_list.size();
    cout << "Lista wejsciowa: ";
    for (int num: input_list) {
        cout << num << " ";
    }
    cout << endl << endl;

    cout << "Drzewo BST:" << endl;
    Tree *root = new Tree(input_list[0]);
    for (long int i = 1; i < len; i++) {
        insert(root, input_list[i]);
    }

    cout << "kolejnosc preorder: ";
    output_list = preorder(root);
    for (int num: output_list) {
        cout << num << " ";
    }
    cout << endl;
    temp_list.clear();
    output_list.clear();

    cout << "kolejnosc postorder: ";
    output_list = postorder(root);
    for (int num: output_list) {
        cout << num << " ";
    }
    cout << endl;
    temp_list.clear();
    output_list.clear();

    cout << "kolejnosc inorder: ";
    output_list = inorder(root);
    for (int num: output_list) {
        cout << num << " ";
    }
    cout << endl;
    temp_list.clear();
    output_list.clear();

    cout << "wysokosc: ";
    cout << find_height(root)<< endl << endl;


    cout << "Drzewo AVL:" << endl;
    inorder_list = inorder(root);
    long int median = inorder_list[inorder_list.size()/2];
    inorder_list.erase(inorder_list.begin() + inorder_list.size()/2);
    Tree *avl = new Tree(median);
    if (inorder_list.size() != 0) {
        generate_avl(avl, inorder_list);
    }

    temp_list.clear();
    cout << "kolejnosc preorder: ";
    output_list = preorder(avl);
    for (int num: output_list) {
        cout << num << " ";
    }
    cout << endl;
    temp_list.clear();
    output_list.clear();

    cout << "kolejnosc postorder: ";
    output_list = postorder(avl);
    for (int num: output_list) {
        cout << num << " ";
    }
    cout << endl;
    temp_list.clear();
    output_list.clear();

    cout << "kolejnosc inorder: ";
    output_list = inorder(avl);
    for (int num: output_list) {
        cout << num << " ";
    }
    cout << endl;
    temp_list.clear();
    output_list.clear();

    cout << "wysokosc: ";
    cout << find_height(avl) << endl << endl;

    // finding on what level element is
    int num = 23;
    cout << "Element " << num << " znajduje sie na wysokosci ";
    find_height(avl, num);
    return 0;
}