//ObjCTut1


#import <Foundation/Foundation.h>

@interface Bank: NSObject
{
    int amount;
}

-(void) print;
-(void) setAmount: (int) a;

@end


@implementation Bank

-(void) print
{
    NSLog(@"Your bank account currently has %i dollars in it." ,amount);
}

-(void) setAmount: (int) a
{
    amount = a;
}

@end


int main(int argc, const char * argv[])
{
    @autoreleasepool
    {
        // insert code here...
        
        int n1 = 20;
        int n2 = 50;
        int sum = n1 + n2;
        
        //Alternitively you could write it the following way:
        //Bank *account = [[Bank alloc]init];
        Bank *account;
        account=[Bank alloc];
        account=[account init];
        [account setAmount: 12];
        
        Bank *account12 = [[Bank alloc]init];
        [account12 setAmount: 25];
        
        NSLog(@"Number: %i \nNumber: %i", n1, n2);
        NSLog(@"\nSum: %i", sum);
        [account print];
        [account12 print];
    }
    return 0;
}
