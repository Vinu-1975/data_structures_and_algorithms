/*
Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array. 
The functions should put all 0s first, then all 1s and all 2s in last.

*/

#include<iostream>
#include<algorithm>
using namespace std;

void swap(int &a,int &b){
    int temp=a;
    a=b;
    b=temp;
}

void sort_array(int a[],int n){
    int low=0;
    int mid=0;
    int high=n-1;

    while(mid<=high){
        switch(a[mid]){
            case 0:
                swap(a[low++],a[mid++]);
                break;
            case 1:
                mid+=1;
                break;
            case 2:
                swap(a[mid],a[high--]);
                break;
            default:
            break;
        }
    }
}

void print_array(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
}
int main(){
    int a[]={ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 };
    int n=sizeof(a)/sizeof(a[0]);

    sort_array(a,n);
    print_array(a,n);
}