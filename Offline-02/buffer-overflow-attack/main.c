#include <stdio.h>

int f1(int x) {
	return x + 1;
}

int f2(int x) {
	return x * 1;
}

int f3(int x) {
	return f1(x) + f2(x);
}

int main() {

	int y = f1(422) + f2(800);

	printf("%d\n", y + f3(2));

	return 0;
}