import re
from collections import Counter


# Read origin file. However, I don't use this function in this case.
def read_origin():
    origin_file = 'frequency_attack_origin_example.txt'
    try:
        with open(origin_file, 'r', encoding='big5') as f:
            origin_txt = f.read()
        return origin_txt
    except:
        print('Cannot open origin file:', origin_file)
        return None


# Read encrypted file.
def read_cipher():
    cipher_string = ''
    while True:
        cipher_file = input('Enter file name with extension (or enter "default"):')
        try:
            if cipher_file == 'default':
                cipher_file = 'frequency_attack_cipher_example.txt'

            with open(cipher_file, 'r', encoding='big5') as f:
                for line in f:
                    for letter in line:
                        cipher_string += letter

            print('Success to read %s. Ready to decrypt.' % cipher_file)
            return cipher_string
        except:
            print('Cannot open cipher file: %s. Please enter the file name again.\n' % cipher_file)
            continue


# Get frequency. However, it can be replace by 'counter' module
def get_freq():
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


def get_lower_char(text):
    lower_char = ''
    for letter in text:
        if re.search('[a-z]', letter):
            lower_char += letter
    return lower_char


# print('Decrypting file:', cipher_fpath)
cipher_context = read_cipher()

# Get frequency by 'counter' module
count = Counter(cipher_context)
freq = count.most_common()
# freq = get_freq()
# print(freq)

# most frequent letters in order are ["e", "t", "a", "o", "i"]
# one letter may be ["a", "i"]
test = cipher_context.replace('u', 'A')
test = test.replace('c', 'I')
test = test.replace('y', 'E')

# most frequent 3 letters words is "the"
test = test.replace('n', 'T')
test = test.replace('b', 'H')
test = test.replace('i', 'O')

# Then, frequent letters in order are ["n", "s", "h", "r"]
test = test.replace('h', 'N')
test = test.replace('m', 'S')

# two letters may be "of"
test = test.replace('z', 'F')
# "first'
test = test.replace('l', 'R')
# "introduction"
test = test.replace('x', 'D')
test = test.replace('o', 'U')
test = test.replace('w', 'C')
# "question"
test = test.replace('k', 'Q')
# "guide"
test = test.replace('a', 'G')
# "answer"
test = test.replace('q', 'W')
# "world"
test = test.replace('f', 'L')

# remain_count = Counter(get_lower_char(test))
# print(remain_count)

test = test.replace('s', 'Y')
test = test.replace('j', 'P')
test = test.replace('g', 'M')
test = test.replace('v', 'B')
test = test.replace('e', 'K')
test = test.replace('p', 'V')
test = test.replace('r', 'X')
test = test.replace('d', 'J')
# "realize"
test = test.replace('t', 'Z')

# print(Counter(get_lower_char(test)))
# print(test)

print('Finish decrypting. Now converting...')
decrypted_file = test.lower()

output_file = 'decrypted.txt'
with open(output_file, 'w') as f:
    f.write(decrypted_file)

print('Finish generating file:', output_file)
