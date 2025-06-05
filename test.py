import sys

datas = sys.stdin.read()
datas = datas.strip().split("\n")
datas = datas[1:]

vowels = ['A','E','I','O','U','a','e','i','o','u']
alphabet_upper = [chr(i) for i in range(65,91)]
alphabet_lower = [chr(i) for i in range(97,123)]
alphabet = alphabet_lower + alphabet_upper

for sentence in datas:
    consonant = 0
    vowel = 0
    for letter in sentence:
        if letter in vowels:
            vowel += 1
        elif letter in alphabet:
            consonant += 1
    print(consonant, vowel)