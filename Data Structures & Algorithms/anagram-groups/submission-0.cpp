class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> keepTrack;
        for(int i =0; i < strs.size(); i++)
        {
            string currWord = strs.at(i);
            sort(currWord.begin(), currWord.end());
            if(keepTrack.find(currWord) != keepTrack.end())
            {
                keepTrack.at(currWord).push_back(strs.at(i));
            }
            else 
            {
                keepTrack[currWord] = {strs.at(i)};
            }
        }

        vector<vector<string>> a;

        for (auto anagramVectors : keepTrack) {
            a.push_back(anagramVectors.second);
        }

        return a;
    }
};
