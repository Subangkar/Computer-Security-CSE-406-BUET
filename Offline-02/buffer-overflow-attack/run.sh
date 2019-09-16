#!/usr/bin/env bash
directory="/tmp/bfoattack/"
if [ -d $directory ]; then
  rm -r "$directory"
fi
mkdir "$directory"
cp compile.sh demo.c exploit.py "$directory"
cd "$directory"
compile.sh demo.c
exploit.py
whoami
#cd -
#"${directory}demo"
./demo
