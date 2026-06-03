#include <map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        // map<int, int> check;
        // for (int i = 0; i < nums.size(); i++)
        // {
        //     check.insert({i, nums.at(i)});
        // }
        for (int i = 0; i < nums.size(); i++)
        {
            for (int k = i+1; k < nums.size(); k++)
            {
                if((nums.at(i) + nums.at(k) == target) && (i != k))
                {
                    ans.push_back(i);
                    ans.push_back(k);
                }
            }
        }
        return ans;
    }
};


