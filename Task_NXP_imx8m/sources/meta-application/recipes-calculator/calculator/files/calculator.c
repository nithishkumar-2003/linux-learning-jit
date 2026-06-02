#include <stdio.h>
#include <stdlib.h>

void show_menu() {
    printf("\nSimple Calculator:\n");
    printf("1. Addition (+)\n");
    printf("2. Subtraction (-)\n");
    printf("3. Multiplication (*)\n");
    printf("4. Division (/)\n");
    printf("5. Demo Pattern (R)\n");
    printf("6. Exit\n");
    printf("Choose an operation: ");
}

void print_Razeena(void );
void print_R(void );
void print_N(void );
void print_E(void );
void print_Z(void );
void print_A(void );


int main(void) {
    int choice;
    double num1, num2, result;

    while (1) {
        show_menu();
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Exiting.\n");
            break;
        }

        if (choice == 6) {
            printf("Exiting calculator.\n");
            break;
        }

        printf("Enter two numbers: ");
        if (scanf("%lf %lf", &num1, &num2) != 2) {
            printf("Invalid numbers. Try again.\n");
            while (getchar() != '\n'); // Clear input buffer
            continue;
        }

        switch (choice) {
            case 1: 
                result = num1 + num2; printf("Result: %.2f\n", result); 
                break;
            case 2: 
                result = num1 - num2; printf("Result: %.2f\n", result); 
                break;
            case 3: 
                result = num1 * num2; printf("Result: %.2f\n", result); 
                break;
            case 4:
                if (num2 == 0) {
                    printf("Error: Division by zero is undefined.\n");
                } else {
                    result = num1 / num2;
                    printf("Result: %.2f\n", result);
                }
                break;
            case 5:
                print_Razeena();
                break;
            default: printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}

void print_R() {
    printf("*****   \n");
    printf("*    *  \n");
    printf("*   *   \n");
    printf("****    \n");
    printf("*   *   \n");
    printf("*    *  \n");
    printf("*     * \n");
}

void print_A() {
    printf("   *    \n");
    printf("  * *   \n");
    printf(" *   *  \n");
    printf("******* \n");
    printf("*     * \n");
    printf("*     * \n");
    printf("*     * \n");
}

void print_Z() {
    printf("******* \n");
    printf("     *  \n");
    printf("    *   \n");
    printf("   *    \n");
    printf("  *     \n");
    printf(" *      \n");
    printf("******* \n");
}

void print_E() {
    printf("******* \n");
    printf("*       \n");
    printf("******  \n");
    printf("*       \n");
    printf("*       \n");
    printf("******* \n");
}

void print_N() {
    printf("*     * \n");
    printf("**    * \n");
    printf("* *   * \n");
    printf("*  *  * \n");
    printf("*   * * \n");
    printf("*    ** \n");
    printf("*     * \n");
}

void print_Razeena() {
    print_R();
    printf("\n");
    print_A();
    printf("\n");
    print_Z();
    printf("\n");
    print_E();
    printf("\n");
    print_E();
    printf("\n");
    print_N();
    printf("\n");
    print_A();
    printf("\n");
}
