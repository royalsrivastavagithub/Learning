#include <iostream>

using namespace std;

struct Rectangle
{
    int length;
    int breadth;
    char x;
};

int main()
{
    struct Rectangle rect1;
    // inputs
    cout << "Enter Length: ";
    cin >> rect1.length;
    cout << "Enter Breath: ";
    cin >> rect1.breadth;
    // calc
    int area = rect1.length * rect1.breadth;
    // output
    cout << "Area of Rectangle: " << area << endl;
    cout << "Struct size in bytes: " << sizeof(rect1) << endl;
    return 0;
}

/*
4 bytes of memory will be allocated for char due to "padding" were its easy
to allocate 4bytes of memery but char will only use 1 byte of it and 3byte will be wasted
unless we define and use array of char of size 4
*/
