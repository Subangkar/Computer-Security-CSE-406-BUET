#Disable kernel address virtualization
sudo sysctl -w kernel.randomize_va_space=0

#Executable (from root)
gcc -o demo -z execstack -fno-stack-protector demo.c

#Debug (from seed)
gcc -z execstack -fno-stack-protector -g -o demo_dbg demo.c
gdb demo_dbg
b foo
run
p $ebp
p &buffer
quit

