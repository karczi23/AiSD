
struct Node {
    Node* next = nullptr;
    int data;

    Node(int data) {
        this.data = data;
    }
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
    }
};


int main() {

    return 0;
}