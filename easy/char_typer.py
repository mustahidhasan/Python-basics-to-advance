# **Problem Statement:** Given a single English letter, print Vowel if it is a vowel, otherwise Consonant.
ch = input()
print("Vowel" if ch in "aeiou" or ch in "AEIOU" else "Consonant")