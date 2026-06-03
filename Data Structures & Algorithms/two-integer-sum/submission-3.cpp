class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numIndex;

        for (int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums.at(i);
            if(numIndex.count(diff) != 0)
            {
                return {numIndex[diff], i};
            }
            numIndex[nums.at(i)] = i;
        }
        return {};
    }
};
