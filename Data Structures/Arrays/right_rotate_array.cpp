#include <iostream>
using namespace std;

void rotate(int a[], int d, int n)
{
    int p = 0;
    while (p < d)
    {
        int first = a[n-1];
        for (int i = n-1; i >0 ; i--)
        {
            a[i] = a[i - 1];
        }
        a[0] = first;
        p++;
    }
}
void print_array(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(a) / sizeof(a[0]);

    int d = 2;

    rotate(a, d, n);
    print_array(a,n);
}