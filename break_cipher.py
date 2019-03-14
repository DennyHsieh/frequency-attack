import os
import re

origin_fpath = 'frequency_attack_origin_example.txt'
cipher_fpath = 'frequency_attack_cipher_example.txt'


def read_origin(origin_file=origin_fpath):
    try:
        with open(origin_file, 'r', encoding='big5') as f:
            origin_txt = f.read()
        return origin_txt
    except:
        print('Cannot open origin file.')
        return None


def read_cipher(cipher_file=cipher_fpath):
    cipher_string = ''
    try:
        with open(cipher_file, 'r', encoding='big5') as f:
            for line in f:
                for letter in line:
                    cipher_string += letter
        return cipher_string
    except:
        print('Cannot open cipher file.')
        return None


def get_freq_dict():
    freq_dict = {}
    try:
        for letter in read_cipher():
            if re.search('[a-z]', letter):
                if letter not in freq_dict:
                    freq_dict[letter] = 1
                else:
                    freq_dict[letter] += 1
        freq_dict = sorted(freq_dict.items(), key=lambda d: d[1], reverse=True)
    finally:
        return freq_dict


cipher_context = read_cipher()
a = get_freq_dict()
print(a)
