class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        //retrieve jobs list and sort it in ascending order
        vector<int> tasks = jobs;
        sort(tasks.begin(), tasks.end());
        
        //initialize all employee hours to 0
        int employees[k];
        for(int i = 0; i < k; i++)
        {
            employees[i] = 0;
        }
        
        //keep track of maximum working time
        int max = 0;
        
        //used to fill employee hours
        int taskHr = 0;
        int empID = 0;
        int hrMin = 0;

        //assign employee hours
        while(tasks.size() > 0)
        {
            //pick largest available value from vector
            taskHr = tasks[tasks.size() - 1];
            
            //find index of employee with least amount of hours
            for(int i = 0; i < k; i++)
            {
                if(employees[i] < hrMin)
                {
                    empID = i;
                    hrMin = employees[i];
                }
            }
            
            //add in hours to the selected employee
            employees[empID] += taskHr;
            
            //check if current employee has greatest hours
            if(employees[empID] > max)
            {
                max = employees[empID];
            }
            
            //reset hrMin
            hrMin = max;
            
            //remove selected job from vector list
            tasks.pop_back();
        }
        
        //return result
        return max;
    }
};
