#include <stdio.h>

int input_number(void);
int valid_number(int number);

int main(void)
{
    int number = input_number();
    int errorcode = valid_number(number);
    if (errorcode == 0)
    {

        for (int i = 1; i <= number; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                printf("fizzbuzz\n");
            }
            else if (i % 3 == 0)
            {
                printf("fizz\n");
            }
            else if (i % 5 == 0)
            {
                printf("buzz\n");
            }
            else
            {
                printf("%d\n", i);
            }
        }
    }
    else
    {
        printf("invalid number\n");
    }
};

int input_number(void)
{
    int number = 0;
    printf("please input a number between 1 and 100\n");
    scanf("%d", &number);
    return number;
};

int valid_number(int number)
{
    if (number > 0 && number < 101)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
