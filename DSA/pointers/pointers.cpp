#include <iostream>

using namespace std;

int main()
{
    int num = 10;
    int *pointer;
    pointer = &num;//init
    cout << "num = " << num << endl;
    cout << "pointer = " << pointer << endl;
    cout << "pointer value = " << *pointer << endl;//dereferencing with *
    num = num - 1;
    cout << "pointer value after [num-1] = " << *pointer << endl;
    *pointer = *pointer + 1;
    cout << "pointer value = after [*pointer+1] = " << *pointer << endl;
    pointer = pointer-1;
    cout << "pointer after [pointer-1] = " << pointer << endl;
    cout << "pointer value after [pointer-1] = " << *pointer << endl;
}