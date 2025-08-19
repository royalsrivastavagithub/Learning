/*
reference is only availab in c++ !

reference is giving alias to a variable
*/

#include <iostream>

using namespace std;

int main()
{
    int number = 10;
    int &reference = number;//must be initialized

    cout<<"number value = "<<number<<endl;
    cout<<"reference value = "<<reference<<endl;
    cout<<"number address :"<<&number<<endl;
    cout<<"reference address:"<<&reference<<endl;
}