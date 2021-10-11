#include <iostream>
using namespace std;
/*
Daily Coding Problems - #2
Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the 
original array except the one at i.
*/

//multiply the product of all numbers exept at index i and store it at i
void productArray(int *firstList, int *secondList, int size)
{
    //go through each element of the original list
    for(int i = 0; i < size; i++)
    {
        //reset accumulator each iteration
        int accum = 1;
        
        //go through each element of the original list
        for(int j = 0; j < size; j++)
        {
            //you only multiply to the total if the index positions don't match
            if(i != j)
            {
                accum *= firstList[j];
            }
        }
        
        secondList[i] = accum;
    }
}

int main()
{
    int startingList[] = {1, 2, 3, 4, 5};
    int size = 5;
    int newList[size] = {0};
    
    productArray(startingList, newList, size);
    
    cout << "The Original List: ";
    for(int i = 0; i < size; i++)
    {
        cout << startingList[i] << " ";
    }
    
    cout << "\nNew List: ";
    for(int i = 0; i < size; i++)
    {
        cout << newList[i] << " ";
    }
    
    cout << "\n";

    return 0;
}
