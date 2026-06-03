class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int end = nums.size() - 1;
        for (int i = 0; i < end; i++){
            if (nums.at(i) == nums.at(i+1))
                return true;
        }
        return false;
    }
};