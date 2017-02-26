cmake_minimum_required(VERSION 3.6)
project(c)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        getline.c
        hi.c
        input.c
        power.c
        scanf.c
        temperature.c)

add_executable(c ${SOURCE_FILES})