#include <iostream>
using namespace std;

void print_array(int[], int);
void reverse_array(int[], int, int);
void recur_rev_array(int[], int, int);

int main()
{
    int a[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Original array:";
    print_array(a, n);
    cout << "Reversed Array:";
    reverse_array(a, 0, n - 1);
    print_array(a, n);
    cout << "Recursively reversed array:";
    recur_rev_array(a, 0, n - 1);
    print_array(a, n);

    return 0;
}

void print_array(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

void reverse_array(int a[], int start, int end)
{
    while (start < end)
    {
        int temp = a[start];
        a[start] = a[end];
        a[end] = temp;
        end--;
        start++;
    }
}

void recur_rev_array(int a[], int start, int end)
{
    if (start >= end)
    {
        return;
    }
    int temp=a[start];
    a[start] = a[end];
    a[end] = temp;
    recur_rev_array(a, start+1, end-1);
}
