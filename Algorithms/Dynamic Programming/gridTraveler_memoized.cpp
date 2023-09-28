#include<iostream>
#include<string>
#include<unordered_map>
using namespace std;


typedef long long ll;

ll gridTraveler(int m,int n,unordered_map<string,ll>& memo){
    string key = to_string(m) + "," + to_string(n);
    if (memo.find(key)!=memo.end()){
        return memo[key];
    }
    if (m==1 && n==1){
        return 1;
    }
    if (m==0 or n==0){
        return 0;
    }
    memo[key] = gridTraveler(m-1,n,memo) + gridTraveler(m,n-1,memo);
    return memo[key];
}

ll gridTraveler(int m,int n){
    unordered_map<string,ll> memo;
    return gridTraveler(m,n,memo);
}

int main() {
    cout << gridTraveler(1,1) << endl;
    cout << gridTraveler(2,3) << endl;
    cout << gridTraveler(3,2) << endl;
    cout << gridTraveler(3,3) << endl;
    cout << gridTraveler(18,18) << endl;
    return 0;
}