#include<iostream>
using namespace std;

void rotate(int a[],int d,int n){
    int temp[n];

    int k=0;
    //storing elements from d to n in temp[]
    for(int i=d;i<n;i++){
        temp[k]=a[i];
        k++;
    }

    //storing elements from n to d in temp[]
    for(int i=0;i<d;i++){
        temp[k]=a[i];
        k++;
    }

    //copying temp[] to a[]
    for(int i=0;i<n;i++){
        a[i]=temp[i];
    }
}

void print_array(int a[],int n){
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
}


int main(){
    int a[]={1,2,3,4,5,6,7};
    int n=sizeof(a)/sizeof(a[0]);

    int d=3;

    rotate(a,d,n);
    print_array(a,n);
}