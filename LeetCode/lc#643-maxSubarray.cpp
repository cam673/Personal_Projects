class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        vector<int> vals = nums;
        sort(vals.begin(), vals.end());
        float result = 0;
        
        int i = 0;
        int j = vals.size() - 1;
        int inc = 0;
        bool swap = true;
        
        while(inc < k)
        {
            if(swap == true)
            {
                result += vals[i];
                i++;
                swap = false;
            }
            else
            {
                result += vals[j];
                j--;
                swap = true;
            }
            
            inc += 1;
        }
        
        result = result / k;
        
        return result;
    }
};
