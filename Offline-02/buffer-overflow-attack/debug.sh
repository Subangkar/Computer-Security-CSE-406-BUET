#!/usr/bin/env bash
filename="$1"
execname=`echo "$filename" | sed 's/\..*//'`
gcc -o "dbg_$execname" -z execstack -fno-stack-protector -g "$filename"
exploit.py
gdb "dbg_$execname"
