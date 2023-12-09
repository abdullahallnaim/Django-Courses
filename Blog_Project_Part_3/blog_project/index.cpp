#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node(int val)
    {
        this->val = val;
        this->next = NULL;
    }
};
void insert_head(Node *&head, int v)
{
    Node *newnode = new Node(v);
    newnode->next = head;
    head = newnode;
}
void print_link(Node *head)
{
    Node *tmp = head;
    while (tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
    cout << endl;
}
void insert_tail(Node *&head, int v)
{
    Node *newnode = new Node(v);
    if (head == NULL)
    {
        head = newnode;
        return;
    }
    Node *tmp = head;
    while (tmp->next != NULL)
    {
        tmp = tmp->next;
    }
    tmp->next = newnode;
}
void insert_pos(Node *head, int pos, int v)
{
    Node *newNode = new Node(v);
    Node *tmp = head;
    for (int i = 1; i <= pos - 1; i++)
    {
        tmp = tmp->next;
    }
    newNode->next = tmp->next;
    tmp->next = newNode;
}
void size_link(Node *head, int pos, int val)
{
    Node *tmp = head;
    int cnt = 0;
    while (tmp != NULL)
    {
        tmp = tmp->next;
        cnt++;
    }
    if (pos == cnt)
    {
        insert_tail(head, val);
        print_link(head);
    }
    else if (pos > cnt)
    {
        cout << "invalid" << endl;
    }
    else if (pos < cnt)
    {
        insert_pos(head, pos, val);
        print_link(head);
    }
    else if (pos == 0)
    {
        insert_head(head, val);
        print_link(head);
    }
}

int main()
{
    Node *head = NULL;
    int val;
    while (true)
    {
        cin >> val;
        if (val == -1)
        {
            break;
        }
        insert_tail(head, val);
    }
    int q;
    cin >> q;

    while (q--)
    {
        int pos, val;
        cin >> pos >> val;
        size_link(head, pos, val);
    }
}
