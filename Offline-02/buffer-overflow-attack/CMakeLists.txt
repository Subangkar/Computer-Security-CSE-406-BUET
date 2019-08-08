cmake_minimum_required(VERSION 3.10)
project(buffer_overflow_attack C)

set(CMAKE_C_STANDARD 11)

set(CMAKE_C_FLAGS "-z execstack -fno-stack-protector")

add_executable(buffer_overflow_attack demo.c)