#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
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

void search(Node *&head, int key)
{
    vector<int> v;
    Node *temp = head;
    while (temp != NULL)
    {
        v.push_back(temp->data);
        temp = temp->next;
    }
    vector<int>::iterator it;
    it = find(v.begin(), v.end(), key);
    if (it != v.end())
    {
        cout << "Element found at " << (it - v.begin()) + 1 << " node" << endl;
    }
    else
    {
        cout << "Element not found !" << endl;
    }
}

int main()
{
    Node *head = NULL;
    int ch;
    while (ch != 0)
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
            search(head, val);
        }
    }
}