#include<iostream>
using namespace std;

void generate_subarray(int a[],int start,int end,int n){
    if(end==n){
        return;
    }
    if(start>end){
        generate_subarray(a,0,end+1,n);
    }
    else{
        cout<<"[";
        for(int i=start;i<end;i++){
            cout<<a[i]<<",";
        }
        cout<<a[end]<<"]"<<endl;
        generate_subarray(a,start+1,end,n);
    }
    return;
}

int main(){
    int a[]={1,2,3};
    int n=sizeof(a)/sizeof(a[0]);

    generate_subarray(a,0,0,n);
}