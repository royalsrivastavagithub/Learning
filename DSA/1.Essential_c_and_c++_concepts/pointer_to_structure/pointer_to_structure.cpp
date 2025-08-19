#include <iostream>

using namespace std;

struct Rectangle
{
    int length;
    int breath;
};

int main()
{
    struct Rectangle *p;
    p = (struct Rectangle *)malloc(sizeof(struct Rectangle));

    p->length = 15;
    p->breath = 33;
    cout << p->length << endl;
    cout << p->breath << endl;
    return 0;
}