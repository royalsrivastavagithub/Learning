#include <iostream>

using namespace std;

int rectangle_area(int length, int breath)
{
    return length * breath;
}

int rectangle_perimeter(int length, int breath)
{
    return 2 * (length + breath);
}

int main()
{
    int length, breath = 0;
    cout << ("Enter Length and Breath:");
    cin >> length >> breath;

    int area = rectangle_area(length, breath);
    int perimeter = rectangle_perimeter(length, breath);

    cout << "Area: " << area << endl;
    cout << "Perimeter: " << perimeter << endl;
    return 0;
}