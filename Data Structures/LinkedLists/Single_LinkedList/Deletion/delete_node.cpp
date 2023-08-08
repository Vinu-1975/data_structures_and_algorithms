#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int val)
    {
        data = val;
        next = NULL;
    }
};

// insertion

void push_back(Node *&head, int val)
{
    Node *NewNode = new Node(val);
    if (head == NULL)
    {
        head = NewNode;
        return;
    }
    Node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = NewNode;
}

void push_front(Node *&head, int val)
{
    Node *NewNode = new Node(val);
    if (head == NULL)
    {
        head = NewNode;
        return;
    }
    NewNode->next = head;
    head = NewNode;
}

void push_after(Node *&head, int key, int val)
{
    Node *NewNode = new Node(val);
    if (head->data == key)
    {
        NewNode->next = head->next;
        head->next = NewNode;
        return;
    }
    Node *temp = head;
    while (temp->data != key)
    {
        temp = temp->next;
        if (temp == NULL)
        {
            return;
        }
    }
    NewNode->next = temp->next;
    temp->next = NewNode;
}

// deletion

void pop_back(Node *&head)
{
    if (head == NULL)
    {
        cout << "List is empty" << endl;
        return;
    }
    if (head->next == NULL)
    {
        head = NULL;
        return;
    }
    Node *temp = head;
    Node *temp2;
    while (temp->next != NULL)
    {
        temp2 = temp;
        temp = temp->next;
    }
    temp2->next = NULL;
    delete temp;
}

void pop_front(Node *&head)
{
    if (head == NULL)
    {
        cout << "List is empty" << endl;
        return;
    }
    Node *temp = head;
    head = head->next;
    delete temp;
}

void remove_node(Node *&head, int key)
{
    if (head == NULL)
    {
        cout << "List is empty" << endl;
    }
    Node *temp = head;
    while (temp->next->data != key)
    {
        temp = temp->next;
    }
    Node *todelete = temp->next;
    temp->next = temp->next->next;
    delete todelete;
}

void deleteList(Node* &head){
    Node* temp = head;
    Node* temp2 = NULL;
    while(temp->next != NULL){
        temp2 = temp;
        temp = temp->next;
        delete temp2;
    }
    head = NULL;
}

void display_list(Node *&head)
{
    if (head == NULL)
    {
        cout << "list is empty" << endl;
        return;
    }
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << endl;
}



int main()
{
    Node *head = NULL;
    int ch;
    while (ch != 0)
    {
        cout << "1. push_back(head,val)" << endl;
        cout << "2. display_list(head)" << endl;
        cout << "3. push_front(head,val)" << endl;
        cout << "4. push_after(head,key,val)" << endl;
        cout << "5. pop_back(head)" << endl;
        cout << "6. pop_front(head)" << endl;
        cout << "7. remove_node(head, key)" << endl;
        cout << "8. deleteList(head)" << endl;
        cin >> ch;
        if (ch == 1)
        {
            cout << "enter val : ";
            int val;
            cin >> val;
            push_back(head, val);
        }
        else if (ch == 2)
        {
            display_list(head);
        }
        else if (ch == 3)
        {
            cout << "enter val : ";
            int val;
            cin >> val;
            push_front(head, val);
        }
        else if (ch == 4)
        {
            cout << "enter val : ";
            int val;
            cin >> val;
            cout << "enter key : ";
            int key;
            cin >> key;
            push_after(head, key, val);
        }
        else if (ch == 5)
        {
            pop_back(head);
        }
        else if (ch == 6)
        {
            pop_front(head);
        }
        else if (ch == 7)
        {
            int key;
            cout << " enter element to be deleted : ";
            cin >> key;
            remove_node(head, key);
        }
        else if (ch == 8){
            deleteList(head);
        }
    }
}