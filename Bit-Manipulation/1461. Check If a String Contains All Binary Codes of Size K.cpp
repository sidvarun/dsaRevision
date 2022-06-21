// we always have 2^k binary number that can be made with k bits
// so one approach is to add all substrings of s of size k to a set and check if the size of the set == 1 << k or pow(2, k)

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<string> st;
        
        if(k > s.length())
            return false;
        
        for(int i = 0; i < s.length() - k + 1; i++){
            st.insert(s.substr(i, k));
        }
        
        // return st.size() == (int) pow(2, k);
        return st.size() == 1 << k;
    }
};

// Time complexity: O(NK). We need to iterate the string, and use \mathcal{O}(K)O(K) to calculate the hash of each substring.
// Space complexity: (NK). There are at most NN strings with length KK in the set.


// We can also use rolling hash
// we can calculate the hash of the substring on the go.
// maintain an array of size totalNums = pow(2, k) or 1 << k
// this will be a boolean array

// new_hash = ((old_hash << 1) & all_one) | last_digit_of_new_hash

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        
        int totalNums = 1 << k;
        
        int allOnes = 1 << (k);
        allOnes -= 1;
        
        vector<bool> visited(totalNums, false); 
        
        int currNum = 0;
        int total = 0;
        for(int i = 0; i < s.length(); i++){
            
            currNum = ((currNum << 1) & allOnes) | (s[i] - '0');
            
             if(i >= k - 1){
                if(!visited[currNum]){
                    visited[currNum] = true;
                    totalNums -= 1;
                }

                if(totalNums == 0)
                    return true;
             }      
            
        }
        
        return false;
    }
};

// Time complexity: O(N). We need to iterate the string, and use O(1) to calculate the hash of each substring.
// Space complexity:O(2^k). There are 2^k elements in the list.