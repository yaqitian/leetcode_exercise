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
