class Solution {
public:
    int characterReplacement(string s, int k) {
        if (s.size() == 0)
            return 0;
        
        int left = 0, result = 0;
        int dict[26] = {0};
        int most_length = ++dict[s[0] - 'A'];

        for (int right = 1; right < s.size(); ++right) {
            most_length = max(most_length, ++dict[s[right] - 'A']);

            if (most_length + k < right - left + 1) {
                dict[s[left++] - 'A'] -= 1;    
            }

            result = max( result, right - left + 1);
        }
        return result;
    }
};
