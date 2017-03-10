#include <iostream>
#include <string>
#include <algorithm>

#include "Student.h"
#include "SortTesthelper.h"

using namespace std;

template <typename T> //模板函数  java中的泛型

void selectionSort(T arr[], int n){ // arr[] 不受具体的类型限制

    for(int i = 0 ; i < n ; i ++){
        // 寻找[i, n)区间里的最小值
        int minIndex = i;
        for( int j = i + 1 ; j < n ; j ++ )
            if( arr[j] < arr[minIndex] )
                minIndex = j;

        swap( arr[i] , arr[minIndex] ); // swap 在 algorithm
    }

}

int main() {
    int  n = 10000;
    int *arr = SortTestHelper::generateRandomArray(n, 0, n);
    float b[4] = {23.4, 12.4, 10, 12 };
    string c[4] = {"a", "b", "c", "d"};
    Student d[4] = {{"Z", 34}, {"Q", 67}, {"W", 87}, {"L", 85}};

    ////////////////////////////////
    selectionSort(arr, n);
    SortTestHelper::printArray(arr, n);

    SortTestHelper::testSort("Selection Sort", selectionSort, arr, n);

    delete[] arr;
    cout << endl;


    ////////////////////////////////
    selectionSort(d, 4);
    for (int k = 0; k < 4; ++k) {
        cout << d[k] << " ";
    }


    return 0;
}