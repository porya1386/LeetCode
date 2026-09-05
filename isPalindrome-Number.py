class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s[::-1] == s


    # Python3 Version 
# Palindrome yani khondan ye str ya x ke az do taraf yeki bashe mesl 131
# X ro be STR tabdil kardim va az sliece :: estefade kardim -1 yani ke az akhar shoro kone
# pas return mikonim x (input) == ::-1 (reveresd) shode

# Easy Way

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1] 




# Hard way 
def polyint(x):
    if x < 0:
        return False
    res = 0  # Reveresd i ke adad am ro tosh mizaram
    temp = x  # temepory sanavast ke badan adad ro mizaram tosh
    while temp > 0:  # ta zamani ke temp bozorg tar az 0
        res = res*10 + temp % 10  # reveresed * 10 + temp % 10
        temp //= 10
    return res == x
# idk what this shit do ngl
