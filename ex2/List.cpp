#include <iostream>

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

    void insert(List* list, int data) {
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
};


int main() {
    List list = List();


        list.insert(&list, 3);
        list.insert(&list, 4);
        list.insert(&list, 4);
        list.insert(&list, 4);
        list.insert(&list, 1);
                list.insert(&list, 6);
        list.insert(&list, 9);
        list.insert(&list, 6);
        list.insert(&list, 2);
                list.insert(&list, 10);
                        list.insert(&list, 11);
                                list.insert(&list, 10);
    list.print();
    return 0;
}