#include <iostream>

using namespace std;

void array_print(int arr[], int size)
{
    cout << "array: ";
    for (int i = 0; i < size; i++)
    {
        cout << arr[i];
        if (i == size - 1)
        {
            break;
        }
        cout << ",";
    }
    cout << endl;
}

int main()
{
    int array[5] = {1, 2, 3, 4, 5};
    array_print(array, 5);
}