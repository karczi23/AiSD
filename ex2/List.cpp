#include <iostream>
#include <vector>
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
            delete head;
            head = head->next;
        }
    }
};


int main() {
    List list = List();
    vector<long int> random_list;

    long int len = 100; // length of the random list to
    random_list = rand_gen(len);

//    print all numbers in random_list
//    for(int num: random_list) {
//        cout << num << " ";
//    }

    for (long int i = 0; i < len; i++) {
        list.insert(random_list[i]);
    }

    list.print();
    list.removeElements();
    cout << list.findByValue(10) << list.head << endl;

    return 0;
}