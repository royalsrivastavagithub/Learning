#include <iostream>

using namespace std;

int main()
{
    int length,breath=0;
    cout<<("Enter Length and Breath:");
    cin>>length>>breath;

    int area = length*breath;
    int perimeter = 2*(length+breath);

    cout<<"Area: "<<area<<endl;
    cout<<"Perimeter: "<<perimeter<<endl;
    return 0;
}