#include <iostream>

using namespace std;

void initailise(struct Rectangle *r, int l, int b)
{
    r->length = l;
    r->breath = b;
}

struct Rectangle
{
    int length;
    int breath;
};

int rectangle_area(struct Rectangle r)
{
    return r.length * r.breath;
}

int rectangle_perimeter(Rectangle r)
{
    return 2 * (r.length + r.breath);
}

int main()
{
    Rectangle rect = {0, 0};
    int l, b;
    cout << ("Enter Length and Breath:");
    cin >> l >> b;

    initailise(&rect, l, b);
    int area = rectangle_area(rect);
    int perimeter = rectangle_perimeter(rect);

    cout << "Area: " << area << endl;
    cout << "Perimeter: " << perimeter << endl;
    return 0;
}