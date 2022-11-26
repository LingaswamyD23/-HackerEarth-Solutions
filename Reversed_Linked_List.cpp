#include<bits/stdc++.h>
using namespace std;
class node{
public:
    int data;
    node* next;
    node(int val)
    {
    data=val;
    next=NULL;
    }
};

void display(node* head)
{
    node* temp=head;
    while(temp!=NULL)
    {
    cout<<temp->data<<" ";
    temp=temp->next;
    }
}

void insertAtTail(node* &head,int val)
{
    node* n =new node(val);
    n->next=NULL;
    node* temp=head;
    if(temp==NULL)
    {
        head=n;
        return;
    }

    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=n;
}

node* reverse(node* &head)
{
    node* prevPtr=NULL;
    node* currentPtr=head;
    node*nextPtr;

    while(currentPtr!=NULL)
    {
        nextPtr=currentPtr->next;
        currentPtr->next=prevPtr;
        prevPtr=currentPtr;
        currentPtr=nextPtr;
    }
    return prevPtr;
}

void insertAtHead(node* &head,int val)
{
    node* n=new node(val);
    n->next=head;
    head=n;
}

void specialFun(node* &head)
{
    node* temp=head;
    while(temp->next!=NULL)
    {
        if( (temp->data)%2==0)
        {
            node* head2=NULL;
            while(( (temp->data)%2==0)&&(temp->next!=NULL) )
            {
                insertAtHead(head2,temp->data);
                temp=temp->next;
            }
            if((temp->data)%2==0)
            {
                insertAtHead(head2,temp->data);
            }
            display(head2);
        }
        else
        {
            cout<<temp->data<<" ";
            temp=temp->next;
        }
    }
    if( (temp->next==NULL)&&((temp->data)%2!=0) )
    {
        cout<<temp->data<<" ";
    }
}



int main()

{
    node* head=NULL;
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        int num;
        cin>>num;
        insertAtTail(head,num);
    }
    specialFun(head);
}