/** 
Runtime: 2 ms, faster than 97.65% of Java online submissions for Container With Most Water.
Memory Usage: 52.8 MB, less than 28.29% of Java online submissions for Container With Most Water.

Problem: https://leetcode.com/problems/container-with-most-water/

The key to this problem is to eliminate the comparisons between pairs of elements as much as possible. 
Therefore, given any two indices i, j, find the upperbound area enclosed in i & j such that all areas between i & j must be smaller.
For any two i & j, iteration in one and only one direction will satisfy the above condition ^. Find that direction
Then, iterate the index on the opposite direction
*/

class ContainerWithMostWaterFaster {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = -1;
        int currentArea = -1;
        
        while (left < right) {
            
            if (height[left] < height[right]) {
                currentArea = (right - left) * height[left];
                left += 1;
            }
            else {
                currentArea = (right - left) * height[right];
                right -= 1;
            }
            
            if (currentArea > maxArea)
                maxArea=currentArea;
        }
        
        return maxArea; 
        
    }
}
