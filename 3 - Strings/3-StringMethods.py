'''
String Methods:
-- isalpha()
-- isdigit()
-- islower()
-- lower()
-- upper()
-- isupper()
-- lstrip()
-- rstrip()
'''

password = "abcd"
print(password.isalpha())

room_no = "3A101"
print(room_no.isdigit())

s = "abcde"
print("isAlpha: ", s.isalpha())
print("isDigit: ", s.isdigit())
print("isLower: ", s.islower())
print("isUpper: ", s.isupper())

print("\n")
print("Lowercase ", s.lower())
print("Uppercase ", s.upper())
print("\n")

s2 = "   spaces  "
print("Remove spaces in the left", s2.lstrip())
print("Remove spaces in the right", s2.rstrip())
print("\n")

print("Strings are immutable")
print(s)
print(s2)
S = "aewergrththy"
ans = ""
maxLen = 0

for j in range(len(S)):

    i = S[j]

    if i not in ans:
        ans += i
        print(ans)

    else:
        ans += i
        indexFirst = ans.index(i)
        print(indexFirst)
        ans = ans[(indexFirst+1):]
        print(ans)

    maxLen = max(maxLen, len(ans))

print(maxLen)





