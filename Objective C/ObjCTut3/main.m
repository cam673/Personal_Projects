//ObjCTut3
//for loop
//Input/Output
//while loop
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{
    @autoreleasepool
    {
        int x;
        
        for(x = 1; x <= 10; x++)
        {
            if(x % 2 == 0)
            {
                NSLog(@"EVEN");
            }
            else
            {
                NSLog(@"ODD");
            }
        }
        int userNum;
        NSLog(@"Enter a Number:");
        scanf("%i", &userNum);
        NSLog(@"You entered the number %i", userNum);
        
        int num = 1;
        
        while(num <= 10)
        {
            num += 1;
            if(num == 10)
            {
                NSLog(@"The number is 10!!!");
            }
        }
    }
    return 0;
}
