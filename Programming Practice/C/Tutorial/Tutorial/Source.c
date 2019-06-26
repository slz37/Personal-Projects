#include <stdio.h>

//Booleans - must define ourselves
#define BOOL char;
#define False 0;
#define True 1;

int main()
{
	//Starting hello world
	printf("Hello world!\n");

	//Numbers
	int a = 1, b = 2, c = 3, SUM;
	SUM = a + b + c;
	printf("%i\n", SUM);

	//Arrays - name[size], must preallocate size for arrays
	int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	char vowels[2][5] = {
						{'A', 'E', 'I', 'O', 'U'},
						{'a', 'e', 'i', 'o', 'u'}
						};
	printf("2nd digit: %i\n", arr[1]);

	return 0;
}