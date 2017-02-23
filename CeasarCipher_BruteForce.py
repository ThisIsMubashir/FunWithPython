#!/usr/bin/env python

# For brute force you should know the location of letters. This only works
# with following Letters

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'


def decrypt(msg, key):
    decMsg = ''
    for char in msg:
        if char in LETTERS:
            num = LETTERS.find(char)
            num -= key
            if num < 0:
                num = num + len(LETTERS)
            decMsg += LETTERS[num]
        else:
            decMsg += char
    return decMsg


def main():
    print '~*~*~*~*~*~*~*~*~ Brute Force Attack on Ceasar Cipher ~*~*~*~*~*~*~*~*~'
    msg = raw_input('Please enter the cipher text: ')
    for key in range(len(LETTERS)):
        decMsg = decrypt(msg, key)
        #print 'Key:', key, ' ', decMsg
        # String formatting technique 1 old
        # print 'Key #%s: %s'%(key,decMsg)
        # String formatting technique 2 new
        print 'Key #{}: {}'.format(key,decMsg)


if __name__ == '__main__':
    main()
