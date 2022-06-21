// Bitset

// Use a bitset, then flip the bit for each character.
// If a bit is still set, then the character occurred an odd number of times.
// for string to be a potential palindrome, the number of character with odd occurences can be atmost 1

class Solution {
public:
    bool canPermutePalindrome(string s) {
        bitset<128> bitSet;
        
        for(auto c : s){
            int asciiCode = c;
            bitSet[asciiCode] = !bitSet[asciiCode];
        }
        
        return bitSet.count() <= 1;
    }
};

// the count() method resturn  the number of set bit s in the bitset. 