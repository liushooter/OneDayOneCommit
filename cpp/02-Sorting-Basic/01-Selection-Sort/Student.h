//
// Created by shooter on 3/10/17.
//

#ifndef SUNDRY_STUDENT_H
#define SUNDRY_STUDENT_H

#include <iostream>
#include <string>

using namespace std;


struct Student{
    string name;
    int score;

    bool operator<(const Student &otherStudent){
        return score < otherStudent.score;
    }

    friend ostream& operator<<(ostream &os, const Student &student){
        os <<"Student: " << student.name << " " << student.score << endl;
        return os;
    }

};

#endif //SUNDRY_STUDENT_H
