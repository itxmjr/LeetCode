class Solution {
public:
    bool isPalindrome(int x) {
        string v = to_string(x);
        reverse(v.begin(), v.end());
        return v == to_string(x);
    }
};