#include <iostream>
#include <vector>
#include <chrono>
#include <list>
#include <fstream>
#include "Num_gen.h"

using namespace std;

struct Node {
    Node* next = nullptr;
    int data;

    Node(int data) {
        this->data = data;
    };
    
};

struct List {
    Node* head = nullptr;
    Node* tail = nullptr;

    void insert(int data) {
        Node* node = new Node(data);
        if (!head) {
            head = tail = node;
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
        while(current->next) {
            if (current->data >= data) {
                return prev;
            }
            prev = current;
            current = current->next;
        }
        if (current != head) {
            return current;
        
        }
        if (current->data > data) {
            return nullptr;
        }
        return current;
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
            Node *tmp = head->next;
            delete head;
            head = tmp;
        }
    }
};

int main() {
    vector<long int> random_list;
    int step = 2000; // step between current and next length of generated list
    int iterations = 10; // number of iterations
    int begin_len = 1000; // length of first generated list
    vector<vector<int>> results_all; // nested list with all the results
    vector<int> results; // list with results of one iteration

    cout << "len create find delete" << endl;

    for (int j = 0; j < iterations; j++) {
        List list = List();
        long int len = begin_len + step * j; // length of the random list to generate
        random_list = rand_gen(len);
//        cout << j + 1 << "/" << iterations << endl;
        cout << len << " ";

//      creation of list
        auto begin_creation = chrono::high_resolution_clock::now();

        for (long int i = 0; i < len; i++) {
            list.insert(random_list[i]);
        }

        auto end_creation = chrono::high_resolution_clock::now();
        auto elapsed_creation = chrono::duration_cast<chrono::nanoseconds>(end_creation - begin_creation);

        cout << elapsed_creation.count() << " ";


//      finding all elements of list
        auto begin_find = chrono::high_resolution_clock::now();

        for (int num: random_list) {
            list.find(num);
        }

        auto end_find = chrono::high_resolution_clock::now();
        auto elapsed_find = chrono::duration_cast<chrono::nanoseconds>(end_find - begin_find);

        cout << elapsed_find.count() << " ";


//      deletion of list
        auto begin_delete = chrono::high_resolution_clock::now();

        list.removeElements();

        auto end_delete = chrono::high_resolution_clock::now();
        auto elapsed_delete = chrono::duration_cast<chrono::nanoseconds>(end_delete - begin_delete);

        cout << elapsed_delete.count() << endl;
//
        results.push_back(len);
        results.push_back(elapsed_creation.count());
        results.push_back(elapsed_find.count());
        results.push_back(elapsed_delete.count());

        results_all.push_back(results);
        results.clear();
    }
    return 0;
}

