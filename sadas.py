def funWithAnagrams(s):
    # Write your code here
    count = 0
    while count <= len(s):
        if sorted(s[count]) == sorted(s[count+1]):
            s.remove(s[count]+1)
    return sorted(s)

funWithAnagrams(["4","code", "aaagmnrs", "doce", "anagrams"])
print(funWithAnagrams(["4","code", "aaagmnrs", "doce", "anagrams"]))