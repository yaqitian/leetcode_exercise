## 12. Integer to Roman
Date:  2022-04-11
https://leetcode.com/problems/integer-to-roman/
### Solution:
```golang
func intToRoman(num int) string {   
    res := ""
    
    for num > 0 {
        switch {
            case num >= 1000:
                res = res + "M"
                num -= 1000
            
            case num >= 900:
                res = res + "CM"
                num -= 900
            case num >= 800:
                res = res + "DCCC"
                num -= 800
            case num >= 700:
                res = res + "DCC"
                num -= 700
            case num >= 600:
                res = res + "DC"
                num -= 600
            case num >= 500:
                res = res + "D"
                num -= 500
            case num >= 400:
                res = res + "CD"
                num -= 400
            case num >= 300:
                res = res + "CCC"
                num -= 300
            case num >= 200:
                res = res + "CC"
                num -= 200
            case num >= 100:
                res = res + "C"
                num -= 100
            
            case num >= 90:
                res = res + "XC"
                num -= 90
            case num >= 80:
                res = res + "LXXX"
                num -= 80
            case num >= 70:
                res = res + "LXX"
                num -= 70
            case num >= 60:
                res = res + "LX"
                num -= 60
            case num >= 50:
                res = res + "L"
                num -= 50
            case num >= 40:
                res = res + "XL"
                num -= 40
            case num >= 30:
                res = res + "XXX"
                num -= 30
            case num >= 20:
                res = res + "XX"
                num -= 20
            case num >= 10:
                res = res + "X"
                num -= 10
            
            case num >= 9:
                res = res + "IX"
                num -= 9
            case num >= 8:
                res = res + "VIII"
                num -= 8
            case num >= 7:
                res = res + "VII"
                num -= 7
            case num >= 6:
                res = res + "VI"
                num -= 6
            case num >= 5:
                res = res + "V"
                num -= 5
            case num >= 4:
                res = res + "IV"
                num -= 4
            case num >= 3:
                res = res + "III"
                num -= 3
            case num >= 2:
                res = res + "II"
                num -= 2
            case num >= 1:
                res = res + "I"
                num -= 1
        }
    }
    
    return res
}
```

## 13. Roman to Integer
Date:  2022-04-11
https://leetcode.com/problems/roman-to-integer/
### Solution:
```golang
func romanToInt(s string) int {
    romanMap := map[string]int{
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    
    // Case 1: only 1 roman number.
    res := 0
    if len(s) == 1 {
        res = romanMap[s]
        return res 
    }
    
    // Case 2: more than 1 romam number.
    numList := make([]int, 20)
    for i := 0; i < len(s); i++ {
        numList = append(numList, romanMap[s[i:i+1]]) 
    }
    
    for i := 0; i < len(numList) - 1; i++ {
        if numList[i] >= numList[i+1] {
            res += numList[i]
        } else {
            res -= numList[i]
        }
    }
    
    res += numList[len(numList)-1]
    return res
}
```

## 14. Longest Common Prefix
Date:  2022-04-11
https://leetcode.com/problems/longest-common-prefix/
### Solution:
```golang
func longestCommonPrefix(strs []string) string {
    res := ""
    
    // Case 1: empty list.
    if len(strs) == 0 {
        return res
    }
    
    // Case 2: only 1 string.
    if len(strs) == 1 {
        return strs[0]
    }
    
    // Case 3: more than 1 string.
    minStr := strs[0]
    minLen := len(minStr)
    for _, str := range strs {
        newLen := len(str)
        if newLen < minLen {
            minLen = len(str)
            minStr = str
        }
    }
    
    for _, ch := range minStr {
        for i := 0; i < len(strs); i++ { // can't use: for _, str := range strs
            if string(strs[i][0]) == string(ch) {
                strs[i] = strs[i][1:]
            } else {
                return res
            }
        }
        res = res + string(ch)
    }
    
    return res
}```
