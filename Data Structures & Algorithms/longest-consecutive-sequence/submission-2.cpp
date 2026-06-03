class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0)
        {
            return 0;
        } 
        sort(nums.begin(), nums.end());
        int ans = 0;
        int counter = 1;
        for(int i = 0; i < nums.size() - 1; i++)
        {
            if(nums.at(i) == nums.at(i + 1))
            {
                continue;
            }

            if((nums.at(i) + 1) == nums.at(i + 1))
            {
                counter++;
                cout << nums.at(i) << nums.at(i + 1) << endl;
            }
            else 
            {
                if(counter > ans)
                {
                    ans = counter;
                }
                counter = 1;
            }
        }
        if(counter > ans)
        {
            ans = counter;
        }
        return ans;
    }
};
