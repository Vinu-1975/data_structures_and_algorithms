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
    }
}