#include <time.h>
#include <stdlib.h>
#include <stdio.h> 

void swap(int arr[], int i, int j)
{
	/*
	Swaps two elements in an array.
	*/

	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

int randomNumber(int low, int high)
{
	/*
	Generates a random integer in the range of low to high.
	*/

	int num = rand() % (high - low + 1) + low;

	return num;
}

int partition(int arr[], int low, int high)
{
	/*
	Determine the partition used for the quicksort
	algorithm.
	*/

	//Random pivot to minimize o(n^2) case
	int index = randomNumber(low, high);
	int pivot = arr[index];
	int i = low;

	//Move pivot to end
	swap(arr, index, high);

	//Loop over all elements
	for (int j = low; j < high; j++)
	{
		printf("Compare %i to %i\n", arr[j], pivot);
		if (arr[j] < pivot)
		{
			swap(arr, i, j);
			i++;
		}
	}

	//Restore pivot
	swap(arr, i, high);

	return i;
}

void quickSort(int arr[], int low, int high)
{
	/*
	Use the quicksort algorithm to sort an array.
	*/

	//Only sort for right inputs
	if (low < high)
	{
		int part = partition(arr, low, high);

		//Now sort each partition separately
		quickSort(arr, low, part - 1);
		quickSort(arr, part + 1, high);
	}
}

int main()
{
	/*
	Initial setup for testing the quicksort algorithm.
	*/
	
	//Seed
	srand(time(NULL));

	//Sample quicksort
	int arr[9] = {36, 2, 27, 30, 5, 6, 10, 33, 25};
	quickSort(arr, 0, sizeof(arr) / sizeof(arr[0]) - 1);

	//Output
	for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) 
	{
		printf("%i", arr[i]);

		//Formatting
		if (i < sizeof(arr) / sizeof(arr[0]) - 1)
		{
			printf(", ");
		}
	}

	return 0;
}