#include <iostream>

using namespace std;

//adding function
int add(int a, int b)
{
    int c;
    c = a + b;
    return c;
}

int main()
{
    int num1 = 10;
    int num2 = 15;
    int sum;

    sum = add(num1, num2);//calling add function

    cout << num1 << " + " << num2 << " = " << sum << endl;

    return 0;
}
