#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

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


int main() {
    List list = List();
    vector<long int> random_list;

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

    return 0;
}