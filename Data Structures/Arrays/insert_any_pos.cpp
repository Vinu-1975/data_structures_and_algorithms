#include <iostream>
using namespace std;

void insertAtPos(int a[], int *n, int pos, int elm)
{
    for(int i=*n-1;i>=pos;i--){
        a[i+1]=a[i];
    }
    a[pos]=elm;
    (*n)++;

}
void print_array(int a[], int *n)
{
    for (int i = 0; i < *n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

int main()
{
    int a[20] = {1, 2, 3, 4, 5, 6};
    int n = 6;
    int pos=4;
    int elm = 40;

    print_array(a, &n);
    insertAtPos(a, &n,pos, elm);
    print_array(a, &n);
}