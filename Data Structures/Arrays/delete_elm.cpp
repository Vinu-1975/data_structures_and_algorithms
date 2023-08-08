
#include<iostream>
using namespace std;

int findElm(int [],int,int);

int deleteElm(int a[],int n,int elm){
    int pos=findElm(a,n,elm);
    if(pos==-1){
        cout<<"Element not found!"<<endl;
        return n;
    }
    for(int i=pos;i<n-1;i++){
        a[i]=a[i+1];
    }
    return n-1;
}

int findElm(int a[],int n,int elm){
    for(int i=0;i<n;i++){
        if(a[i]==elm){
            return i;
        }
    }
    return -1;
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
    int a[]={1,2,3,4,5,6};
    int n=sizeof(a)/sizeof(a[0]);

    int elm=4;
    n=deleteElm(a,n,elm);
    print_array(a,n);
}