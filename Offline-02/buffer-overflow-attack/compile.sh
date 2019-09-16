#!/usr/bin/env bash
filename="$1"
execname=`echo "$filename" | sed 's/\..*//'`
gcc -o "$execname" -z execstack -fno-stack-protector "$filename"
sudo chown root "$execname"
sudo chmod 4777 "$execname"
#sudo chmod 4755 "$execname"
