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
    Node *newNode = new Node(val);
    if (head == NULL)
    {
        head = newNode;
        return;
    }
    Node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newNode;
}

void display_list(Node *&head)
{
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << endl;
}

bool search(Node *head, int key)
{
    if (head == NULL)
    {
        return false;
    }
    else if (head->data == key)
    {
        return true;
    }
    search(head->next, key);
}

int main()
{
    Node *head = NULL;
    int ch;
    do
    {
        cout << "0. Exit(0)" << endl;
        cout << "1. push_back(head,val)" << endl;
        cout << "2. display_list(head)" << endl;
        cout << "3. search(head,key)" << endl;
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
            cout << "enter key : ";
            int val;
            cin >> val;
            bool ans = search(head, val);
            if (ans)
            {
                cout << "Element found !" << endl;
            }
            else
            {
                cout << "Element not found !" << endl;
            }
        }
    } while (ch != 0);
}