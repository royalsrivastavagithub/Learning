#include <iostream>

using namespace std;

class Rectangle
{
private:
    int length;
    int breath;

public:
    Rectangle()
    {
        length = 0;
        breath = 0;
    }
    Rectangle(int l, int b)
    {
        length = l;
        breath = b;
    }
    int area()
    {
        return length * breath;
    }
    int perimeter()
    {
        return 2 * (length + breath);
    }
    void setLength(int l)
    {
        length = l;
    }
    void setBreath(int b)
    {
        breath = b;
    }
    int getLength()
    {
        return length;
    }
    int getBreath()
    {
        return breath;
    }
    ~Rectangle()
    {
        cout << "Destructor";
    }
};

int main()
{
    Rectangle r(10, 5);
    cout << "Area: " << r.area() << endl;
    cout << "Perimeter: " << r.perimeter() << endl;
    return 0;
}