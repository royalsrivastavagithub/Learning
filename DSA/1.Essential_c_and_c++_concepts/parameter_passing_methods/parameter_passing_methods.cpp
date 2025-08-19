#include <iostream>

using namespace std;

void Swap_Call_by_value(int x, int y)
{
    int temp;
    temp = x;
    x = y;
    y = temp;
}

void Swap_Call_by_address(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
void Swap_Call_by_reference(int &x, int &y)
{
    int temp;
    temp = x;
    x = y;
    y = temp;
}

int main()
{
    int num1 = 3;
    int num2 = 5;
    cout << "Original values :\n"
         << endl;
    cout << "num1 = " << num1 << endl;
    cout << "num2 = " << num2 << endl;
    cout << endl;
    cout << "Call by value:\n"
         << endl;
    Swap_Call_by_value(num1, num2);
    cout << "num1 = " << num1 << endl;
    cout << "num2 = " << num2 << endl;
    cout << "Values are not swapped!\n"
         << endl;
    cout << "Call by address:" << endl;
    Swap_Call_by_address(&num1, &num2);
    cout << "num1 = " << num1 << endl;
    cout << "num2 = " << num2 << endl;
    cout << "Values are swapped!\n"
         << endl;
    cout << "Call by reference:\n"
         << endl;
    Swap_Call_by_reference(num1, num2);
    cout << "num1 = " << num1 << endl;
    cout << "num2 = " << num2 << endl;
    cout << "Values are swapped!\n"
         << endl;
}