//Successful Submission
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        vector<string> results;
        multimap<int, string> temp;
        int min_value = list1.size() + list2.size();
        
        //go through the list and grab all of the restaurants that are in both strings
        //record both the restaurant name and index sum
        for(int i = 0; i < list1.size(); i++)
        {
            for(int j = 0; j < list2.size(); j++)
            {
                if(list1[i] == list2[j])
                {
                    int c = i + j;
                    if(c < min_value)
                    {
                        min_value = c;
                    }
                    temp.insert(pair <int, string> (c, list1[i]));
                }
            }
        }

        //create an iterator to get the lowest value key
        std::pair <std::multimap<int,string>::iterator, std::multimap<int,string>::iterator> ret;
        ret = temp.equal_range(min_value);
        
        //grab all restaurants with the same index sum
        for (std::multimap<int,string>::iterator it=ret.first; it!=ret.second; ++it)
        {
            results.push_back(it->second);
        }
        
        return results;
        
    }
};
