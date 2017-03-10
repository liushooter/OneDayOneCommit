//
// Created by shooter on 3/10/17.
//
#include <iostream>
#include <ctime>
#include <cassert>

using namespace std;

#ifndef SUNDRY_SORETESTHELPER_H_H
#define SUNDRY_SORETESTHELPER_H_H
namespace SortTestHelper{
    // 生成n个随机数组, 每个元素的随机范围为 [rangeL, range]
    int* generateRandomArray(int n, int rangeL, int rangeR){
        assert(rangeL <= rangeR);

        int *arr = new int[n]; // 需要释放
        srand(time(nullptr)); // ctime
        for (int i = 0; i < n; ++i) {
            arr[i] = rand() % (rangeR - rangeL + 1) + rangeL;
        }

        return arr;
    }

    template<typename T>
    void printArray(T arr[], int n){
        for (int i = 0; i < n; ++i) {
            cout << arr[i] << " ";
        }

        cout << endl;

        return;
    }


    template<typename T>
    bool isSorted(T arr[], int n) {

        for (int i = 0; i < n - 1; i++)
            if (arr[i] > arr[i + 1])
                return false;

        return true;
    }

    template<typename T>
    // params 函数名称, 函数指针, 元素, 数量
    void testSort(string sortName, void(*sort)(T[], int), T arr[], int n){
        clock_t  startTime = clock(); // ctime
        sort(arr, n); // sort 是个函数, 通过函数指针的形式传递
        clock_t  endTime = clock();

        assert(isSorted(arr, n));
        cout << sortName << ":" << double(endTime - startTime) / CLOCKS_PER_SEC << "s" << endl;
        return;
    }
}

#endif //SUNDRY_SORETESTHELPER_H_H
