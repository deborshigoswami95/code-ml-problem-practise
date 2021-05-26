// Problem: https://leetcode.com/problems/generate-parentheses/

class generateParanthesesTree {
    private List<String> sol = new ArrayList<>();
    
    public List<String> generateParenthesis(int n) {
        int i = n;
        int j = 0;
        String s = "";
        this.recursiveParanthesis(i,j,s);
        return sol;
    }
  
    private void recursiveParanthesis(int i, int j, String s) {
        if (i==0 & j==0) {
            this.sol.add(s);
        }
        else if (i>0 & j==0) {
            recursiveParanthesis(i-1,1,s+"(");
        }
        else if (i==0 & j>0) {
            recursiveParanthesis(0,j-1,s+")");
        }
        else if (i>0 & j>0) {
            recursiveParanthesis(i-1, j+1, s+"(");
            recursiveParanthesis(i, j-1, s+")");
        }
    }
}
