#include <iostream>

using namespace std;

int main()
{
    int num = 10;
    int *pointer;   // declaration of pointer
    pointer = &num; // initization of pointer
    cout << "num = " << num << endl;
    cout << "pointer = " << pointer << endl;
    cout << "pointer value = " << *pointer << endl; // dereferencing of pointer
    num = num - 1;
    cout << "pointer value after [num-1] = " << *pointer << endl;
    *pointer = *pointer + 1;
    cout << "pointer value = after [*pointer+1] = " << *pointer << endl;
    pointer = pointer - 1;
    cout << "pointer after [pointer-1] = " << pointer << endl;
    cout << "pointer value after [pointer-1] = " << *pointer << endl;
    return 0;
}