cmake_minimum_required(VERSION 3.10)
project(raw_ping C)

set(CMAKE_C_STANDARD 11)

add_executable(raw_ping icmp_ping.c icmp_ping.h checksum.c raw_socket.c)