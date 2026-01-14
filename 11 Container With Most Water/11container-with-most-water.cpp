class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0, area = 0;
        int l = 0, r = height.size() - 1;
        int h = 0, w = 0;
        while(l < r) {
            h = min(height[l], height[r]);
            w = r - l;
            area = h * w;
            res = max(area, res);
            height[l] <= height[r] ? l++ : r--;
        }
        return res;
    }
};