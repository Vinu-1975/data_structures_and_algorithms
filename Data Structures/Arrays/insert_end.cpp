#include<iostream>
using namespace std;

int insertAtEnd(int a[],int capacity,int n,int ele){
    if(n>=capacity){
        return n;
    }
    a[n]=ele;
    return n+1;
}
void print_array(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

int main(){
    int a[20]={1,2,3,4,5,6};
    int capacity=sizeof(a)/sizeof(a[0]);
    int n=6;
    int elm=7;

    print_array(a,n);
    n=insertAtEnd(a,capacity,n,elm);
    print_array(a,n);
}