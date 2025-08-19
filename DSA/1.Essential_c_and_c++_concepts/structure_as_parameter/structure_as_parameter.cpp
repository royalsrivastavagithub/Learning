#include <iostream>

using namespace std;

struct Rectangle
{
    int length;
    int breath;
};

int area(struct Rectangle rect) // call by value
{
    return rect.length * rect.breath;
}

void swap(struct Rectangle &rect) // call by reference
{
    int temp;
    temp = rect.breath;
    rect.breath = rect.length;
    rect.length = temp;
}

void changeLength(struct Rectangle *p, int l) // call by address
{
    p->length = l;
}

int main()
{
    struct Rectangle r = {10, 5};
    cout << "Length = " << r.length << endl;
    cout << "Breath = " << r.breath << endl;
    cout << "Area = " << area(r) << endl;
    cout << "Changing Lenth value to 4" << endl;
    changeLength(&r, 4);
    cout << "Length = " << r.length << endl;
    cout << "Breath = " << r.breath << endl;
    cout << "Swaping values" << endl;
    swap(r);
    cout << "Length = " << r.length << endl;
    cout << "Breath = " << r.breath << endl;
}