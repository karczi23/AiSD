#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

#include <chrono>
#include "Num_gen.h"
using namespace std;

vector<long int> rand_gen(long int len) {
    vector<long int> numbers;

    for (long int i = 0; i < len; i ++) {
        numbers.push_back(i);
    }

    mt19937 seed(chrono::system_clock::now().time_since_epoch().count());
    shuffle(numbers.begin(), numbers.end(), seed);

    return numbers;
}

struct Node {
    Node* next = nullptr;
    int data;

    Node(int data) {
        this->data = data;
    };
    
};

struct List {
    Node* head = nullptr;

    void insert(int data) {
        Node* node = new Node(data);
        if (!head) {
            head = node;
            node->next = nullptr;
            return;
        }
        Node* before = find(data);
        if (before == nullptr) {
            node->next = head;
            head = node;
            return;
        }
        node->next = before->next;
        before->next = node;
    }
    
    Node* find(int data) {
        Node* prev = nullptr;
        Node* current = head;
        while(current) {
            if (current->data >= data) {
                return prev;
            }
            prev = current;
            current = current->next;
        }

        return prev;
    }
    
    void print() {
        Node* current = head;
        cout << current->data << endl;
        while(current->next) {
            cout << current->next->data << endl;
            current = current->next;
        }
    }
    
    Node* findByValue(int value) {
        Node* current = head;
        while (current) {
            if (current->data == value)
                return current;
            current = current->next;
        }
        return nullptr;
    }
    
    void removeElements() {
        while (head) {
            delete head;
            head = head->next;
        }
    }
};


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
    List list = List();
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

    long int len = 100; // length of the random list to
    random_list = rand_gen(len);
    for (auto i : random_list) {
        cout << i << endl;
    }
    
    cout << endl;
    
    for (long int i = 0; i < len; i++) {
        list.insert(random_list[i]);
    }
    
    list.print();
    list.removeElements();


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