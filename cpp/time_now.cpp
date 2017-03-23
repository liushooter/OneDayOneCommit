#include <iostream>
#include <string>
#include <stdio.h> // c head file
#include <time.h> // c head file

// Get current date/time, format is YYYY-MM-DD.HH:mm:ss
const std::string currentLocalDateTime(time_t time_now) {
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&time_now);
    // Visit http://en.cppreference.com/w/cpp/chrono/c/strftime
    // for more information about date/time format
    strftime(buf, sizeof(buf), "%Y-%m-%d.%X", &tstruct);

    return buf;
}

const std::string currentUTCDateTime(time_t time_now) {
    std::tm* now_tm = std::gmtime(&time_now);
    char buf[42];
    std::strftime(buf, 42, "%Y-%m-%d %X", now_tm);
    return buf;
}

int main() {
    std::time_t time_now = std::time(0);

    std::cout << "timestamp = " << time_now << std::endl;
    std::cout << "currentLocalDateTime = " << currentLocalDateTime(time_now) << std::endl;
    std::cout << "currentUTCDateTime = "   << currentUTCDateTime(time_now) << std::endl;
    // getchar();  // wait for keyboard input
    return 0;
}