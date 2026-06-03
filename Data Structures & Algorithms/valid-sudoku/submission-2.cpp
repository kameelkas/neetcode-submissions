class Solution {
public:
    void printt(vector<int>& a, char b)
    {
        cout << "The Char is: " << b;
        for (auto ch : a)
        {
            cout <<  ch << ' ';
        }
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        map<char, vector<int>> allInCol;
        map<int, vector<char>> allInBox;
        for(int i = 0; i < 9; i++)
        {
            vector<char> allInRow;
            for(int j = 0; j < 9; j++)
            {
                char num = board[i][j];
                if(num == '.')
                {
                    continue;
                }

                if(find(allInRow.begin(), allInRow.end(), num) != allInRow.end())
                {
                    return false;
                } else {
                    allInRow.push_back(num);
                }

                if(auto find1 = allInCol.find(num); find1 != allInCol.end())
                {
                    vector<int> colsForNum = find1->second;
                    printt(colsForNum, num);
                    if(find(colsForNum.begin(), colsForNum.end(), j) != colsForNum.end())
                    {
                        return false;
                    } else {
                        find1->second.push_back(j);
                    }
                } else {
                    allInCol[num] = {j};
                }

                int box = ((i/3)*3) + (j/3);
                if(auto find2 = allInBox.find(box); find2 != allInBox.end())
                {
                    vector<char> numsInBox = find2->second;
                    if(find(numsInBox.begin(), numsInBox.end(), num) != numsInBox.end())
                    {
                        return false;
                    } else {
                        find2->second.push_back(num);
                    }
                } else {
                    allInBox[box] = {num};
                }
            }
        }
        return true;
    }
};
