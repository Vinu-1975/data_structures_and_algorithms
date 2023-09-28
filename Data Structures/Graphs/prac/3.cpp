#include<vector>
#include<iostream>
using namespace std;

int main(){
    vector<int> v(5);
    for(int x:v){
        cout<<x<<" ";
    }
    cout<<endl;
    int n=5;
    vector<int> a(5);
    a[0]=2;
    for(int x:a){
        
        cout<<x<<" ";
    }
    vector<vector<int>> adj(6);

    for (int i = 0; i < 5; i++)
    {
        adj[a[i][0]].push_back(1);
    }
}


