class Solution {
public:
    bool isPalindrome(string s) {
        string clean;
        for(const auto& ch : s)
        {
            if(isalnum(ch))
            {
                clean.push_back((char)tolower(ch));
            }
        }
        
        string r = clean;
        reverse(r.begin(), r.end());
        cout << s << endl;
        cout << r << endl;
        return clean == r;
    }
};
