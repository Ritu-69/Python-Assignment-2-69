#include <stdio.h>

int main() {
    int a = 10;
    printf("Initial value of a = %d\n\n", a);

    // Addition assignment (+=)
    a += 5;  // Equivalent to: a = a + 5
    printf("After a += 5  : %d\n", a);

    // Subtraction assignment (-=)
    a -= 3;  // Equivalent to: a = a - 3
    printf("After a -= 3  : %d\n", a);

    // Multiplication assignment (*=)
    a *= 2;  // Equivalent to: a = a * 2
    printf("After a *= 2  : %d\n", a);

    // Division assignment (/=)
    a /= 4;  // Equivalent to: a = a / 4
    printf("After a /= 4  : %d\n", a);

    // Modulus assignment (%=)
    a %= 4;  // Equivalent to: a = a % 4
    printf("After a %%= 4 : %d\n", a);

    return 0;
}
