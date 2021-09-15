class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        int ind1 = 0;
        int ind2 = 0;
        int ind3 = 0;
        vector<int> reBar = barcodes;
        bool stopLoop = true;
        int swap2 = 0;
        int swap3 = 0;
        
        //get the barcode
        //set the index positions for the starting point
        //check if the next number is different
        //if it is, go to the next number
        //if not, move the second index to the next number
        //keep checking until you find a different number
        //swap the two numbers
        //repeat until at the end of the list
        
        if(reBar.size() < 3)
        {
            return reBar;
        }
        
        while(ind1 < (reBar.size() - 1))
        {
            ind2 = ind1 + 1;
            ind3 = ind1 + 1;
            stopLoop = false;
            
            while(stopLoop == false)
            {
                if(reBar[ind1] == reBar[ind3])
                {
                    ind3 += 1;
                }
                else
                {
                    swap2 = reBar[ind2];
                    swap3 = reBar[ind3];
                    
                    reBar[ind2] = swap3;
                    reBar[ind3] = swap2;
                    
                    ind1 += 1;
                    stopLoop = true;
                }
            }
        }
        
        return reBar;
        
    }
};
