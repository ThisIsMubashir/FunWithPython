#!/usr/bin/env python


LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'


def encrypt(msg, key):
    encMsg = ''
    for char in msg:
        if char in LETTERS:
            num = LETTERS.find(char)
            num += key
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            encMsg += LETTERS[num]
        else:
            encMsg += char
    return encMsg


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
    print '~*~*~*~*~*~*~*~*~ Ceasar Cipher ~*~*~*~*~*~*~*~*~'

    while True:
        op = raw_input('Do you want to continue (y/n)? ')
        if (op.lower() == 'y'):
            action = raw_input(
                'Please enter the action to perform (encrypt/decrypt): ')
            if (action != 'encrypt') and (action != 'decrypt'):
                print 'You have entered wrong choice\n'
            else:
                msg = raw_input('Please enter the message: ')
                key = int(raw_input('Please enter the key: '))
                if action == 'encrypt':
                    encMsg = encrypt(msg, key)
                    print 'Encrypted Message: ', encMsg
                elif action == 'decrypt':
                    decMsg = decrypt(msg, key)
                    print 'Decrpted Message: ', decMsg
                else:
                    pass

        elif (op.lower() == 'n'):
            print 'Good Bye!\n'
            break
        else:
            print 'You have entered wrong choice\n'


if __name__ == '__main__':
    main()
