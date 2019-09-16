#include<stdio.h>

int f1(int x, int y) {
	int a[2];
	a[0] = (x + 0x0f);
	a[1] = (0x0a + y);
	return a[0] + a[1];
}

int f2(int y) {
	int t = y + 5;
	int m = 0x0a;
	return m * f1(y, t);
}

int main() {
	int z = f2(0x0f);
	printf("%d", z);
	return 0;
}

