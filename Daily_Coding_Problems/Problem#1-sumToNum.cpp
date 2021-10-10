#include <iostream>
using namespace std;
/*
Daily Coding Problems - #1
Given a list of numbers and a number k, return whether any two
numbers from the list add up to k
*/

bool sumToNum(int numList[], int k)
{
    //iterate through each possible combination
    for(int i = 0; i < sizeof(numList); i++)
    {
        for(int j = 0; j < sizeof(numList); j++)
        {
            //check if the two indexes are not pointing to the same number
            if(i != j)
            {
                //check if the two numbers add up to k
                int result = numList[i] + numList[j];
                if(result == k)
                {
                    return true;
                }
            }
        }
    }
    
    return false;
}

int main()
{
    int numbers[] = {10, 15, 3, 7};
    int number = 17;
    
    bool result = sumToNum(numbers, number);
    
    if(result)
    {
        cout << "Matching Pairs Found." << endl;
    }
    else
    {
        cout << "No Matching Pairs Found." << endl;
    }

    return 0;
}
