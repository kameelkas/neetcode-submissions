class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        set<int> setNoDup(nums.begin(), nums.end());
        vector<int> vectNoDup(setNoDup.begin(), setNoDup.end());
        sort(vectNoDup.begin(), vectNoDup.end(), [&nums](const auto& a, const auto& b){
            return count(nums.begin(), nums.end(), a) > count(nums.begin(), nums.end(), b);
        });

        vector<int> ans;

        for(int i =0; i < k; i++)
        {
            ans.push_back(vectNoDup.at(i));
        }

        return ans;
    }
};
