#include <iostream>

using namespace std;

void fun(int n)//recursive function
{
    if (n > 0)
    {
         fun(n - 1);
        cout << n;
        //fun(n - 1);
    }
}
int main()
{
    int x = 3;
    fun(x);
    return 0;
}