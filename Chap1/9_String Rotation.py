def isSubstring(str1, str2):
    if str2 in str1:
        return True
    return False

s1 = "waterbottle"
s2 = "erbottlewat"

s1s1 = s1 + s1
result = isSubstring(s1, s2)
print(result)
result = isSubstring(s1s1, s2)
print(result)