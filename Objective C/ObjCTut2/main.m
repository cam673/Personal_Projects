//  ObjCTut2

#import <Foundation/Foundation.h>

@interface Candy: NSObject
{
    int chocolate;
    int gummi;
    int sour;
}

-(void) print;
-(void) setChocolate: (int) c;
-(void) setGummi: (int) g;
-(void) setSour: (int) s;
-(int) chocolate;
-(int) gummi;
-(int) sour;
@end

@implementation Candy

-(void) print
{
    NSLog(@"You currently have %i chocolate candies, %i gummi candies, and %i sour candies." ,chocolate, gummi, sour);
}

-(void) setChocolate: (int) c
{
    chocolate = c;
}

-(void) setGummi: (int) g
{
    gummi = g;
}

-(void) setSour: (int) s
{
    sour = s;
}

-(int) chocolate
{
    return chocolate;
}

-(int) gummi
{
    return gummi;
}

-(int) sour
{
    return sour;
}

@end

int main(int argc, const char * argv[])
{
    @autoreleasepool
    {
        Candy *billy = [[Candy alloc]init];
        
        [billy setChocolate: 25];
        [billy setGummi: 12];
        [billy setSour: 30];
        
        //%i = integer, %f = float, %e = double, %c = character
        NSLog(@"Billy currently has %i chocolates, %i gummi's, and %i sour candies in his pocket.", [billy chocolate], [billy gummi], [billy sour]);
    }
    return 0;
}
