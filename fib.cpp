#include <iostream>
#include <string>
using namespace std;
int fib1 (int n)
{
    if (n==0)
    {
        return 0;    
    }
    if (n==1)
    {
        return 1;
    }
    int result = fib1(n-1)+fib1(n-2);
    return result;
}

int fib2 (int n)
{
    if (n==0)
    {
        return 0;    
    } 
    int arr[n+1];
    arr[0] = 0;
    arr[1] = 1;
    for (int i=2; i<n+1; i++)
    {
    arr[i]=arr[i-1]+arr[i-2];    
    }
    int result = arr[n];
    return result;
}

int main()
{
cout << fib1(42) << endl;
cout << fib2(42) << endl;
}
