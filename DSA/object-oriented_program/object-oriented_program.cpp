#include <iostream>

using namespace std;

class Rectangle
{
    public:
    int length;
    int breath;

    void initialise(int l, int b)
    {
        length = l;
        breath = b;
    }

    int rectangle_area()
    {
        return length * breath;
    }

    int rectangle_perimeter()
    {
        return 2 * (length + breath);
    }
};

int main()
{
    Rectangle rect = {0, 0};
    int l, b;
    cout << ("Enter Length and Breath:");
    cin >> l >> b;

    rect.initialise(l, b);
    int area = rect.rectangle_area();
    int perimeter = rect.rectangle_perimeter();

    cout << "Area: " << area << endl;
    cout << "Perimeter: " << perimeter << endl;
    return 0;
}