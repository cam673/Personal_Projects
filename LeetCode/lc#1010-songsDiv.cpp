class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        //count the number of song pairs divisible by 60
        int accum = 0;
        int i = 0;
        int j = 0;
        int combo = 0;
        
        //go though all song pairs in the list
        while(i < (time.size() - 1))
        {
            j = i + 1;
            while(j < time.size())
            {
                combo = time[i] + time[j];
                if((combo % 60) == 0)
                {
                    accum += 1;
                }
                
                j++;
            }
            i++;
        }
        
        //return amount of song pairs
        return accum; 
    }
};
