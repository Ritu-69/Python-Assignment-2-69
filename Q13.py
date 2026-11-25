#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    // Using logical AND (&&) to check both conditions
    if (num >= 10 && num <= 100) {
        printf("%d lies between 10 and 100.\n", num);
    } else {
        printf("%d does not lie between 10 and 100.\n", num);
    }

    return 0;
}
