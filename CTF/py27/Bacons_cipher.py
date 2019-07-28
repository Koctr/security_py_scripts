import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

first_cipher = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "aba aa", "abaab", "ababa",
                "ababb", "abbaa", "abbab", "abbba", "abbbb", "baaaa", " baaab", "baaba", "baabb", "babaa", "babab",
                "babba", "babbb", "bbaaa", "bbaab "]

second_cipher = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "aba aa", "abaaa", "abaab",
                 "ababa", "ababb", "abbaa", "abbab", "abbba", "abbbb", " baaaa", "baaab", "baaba", "baabb", "baabb",
                 "babaa", "babab", "babba", "babbb "]


def encode():
    strndexing = raw_input("please input string to encode:\n")
    e_string1 = ""
    e_string2 = ""
    for index in string:
        for i in range(0, 26):
            if index == alphabet[i]:
                e_string1 += first_cipher[i]
                e_string2 += second_cipher[i]
                break
        print "first encode method result is:\n" + e_string1
        print "second encode method result is:\n" + e_string2
        return


def decode():
    e_string = "baabaaabbbabaaabbaaaaaaaaabbabaaaabaaaaaabaaabaabaaaabaabbbaabbbaaba bb"
    e_array = e_string[0:4]
    d_string1 = ""
    d_string2 = ""
    index = 0
    print e_string[index:index + 5]
    while index < len(e_string):
        for i in range(0, 26):
            if e_string[index:index + 5] == first_cipher[i]:
                d_string1 += alphabet[i]
                print e_string[index:index + 5]
            if e_string[index:index + 5] == second_cipher[i]:
                d_string2 += alphabet[i]
                print e_string[index:index + 5]
    index = index + 5
    print "first decode method result is:\n" + d_string1
    print "second decode method result is:\n" + d_string2
    return


if __name__ == '__main__':
    decode()
