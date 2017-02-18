#!/usr/bin/env python

# BSD 3-Clause License

# Copyright (c) 2017, Mubashir Hussain
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import pygame
import time

# International Morse code ITU-R M.1677-1 (10/2009)
# https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf

morseCode = {
    'A': '.-',		'B': '-...',	'C': '-.-.',	'D': '-..',		'E': '.',
    'F': '..-.',	'G': '--.',		'H': '....',	'I': '..',		'J': '.---',
    'K': '-.-',	    'L': '.-..',	'M': '--',	    'N': '-.',	    'O': '---',
    'P': '.--.',    'Q': '--.-',    'R': '.-.',    	'S': '...',    	'T': '-',
    'U': '..-',    	'V': '...-',    'W': '.--',    	'X': '-..-',    'Y': '-.--',
    'Z': '--..',

    '1': '.----',   '2': '..---',	'3': '...--',	'4': '....-',	'5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',   '9': '----.',   '0': '-----',

    '1': '.----',   '2': '..---',	'3': '...--',	'4': '....-',	'5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',   '9': '----.',   '0': '-----',

    '.': '.-.-.-',	',': '--..--',	':': '---...',	'?': '..--..',	"'": '.----.',
    '-': '-....-',	'/': '-..-.',	'(': '-.--.',	')': '-.--.-',	'=': '-...-',
    ' ': '/',		"@": ".--.-.",
}

revmorseCode = {y: x for x, y in morseCode.iteritems()}

ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT  # Wait between letters
SEVEN_UNITS = 7 * ONE_UNIT  # Wait between words
PATH = 'morse_sound_files/'


def encode(msg):
    pygame.init()

    keys = morseCode.keys()
    encMsg = ''
    for char in msg:
        if char.upper() not in keys:
            print "Error the character " + char + " cannot be translated to Morse Code"
        else:
            encMsg += morseCode[char.upper()] + ' '
            if char == ' ':
                time.sleep(SEVEN_UNITS)
            else:
                pygame.mixer.music.load(
                    PATH + char.upper() + '_morse_code.ogg')
                pygame.mixer.music.play()
                time.sleep(THREE_UNITS)
    print encMsg
    return encMsg


def decode(msg):
    keys = revmorseCode.keys()
    decMsg = ''
    msg = msg.split(' ')
    msg = filter(None, msg)
    for char in msg:
        if char not in keys:
            print "Error the character " + char + " cannot be translated to text"
        else:
            decMsg += revmorseCode[char]
    print decMsg
    return decMsg


def main():
    print "Morse Code Encoder/Decoder"

    while True:
        op = raw_input("Do you want to continue (y/n)? ")
        if (op.lower() == 'y'):
            action = raw_input(
                "Please enter the action to perform (encode/decode): ")
            if action == "encode":
                msg = raw_input("Please enter the message: ")
                encMsg = encode(msg)
            elif action == "decode":
                msg = raw_input("Please enter the message: ")
                decMsg = decode(msg)
            else:
                print "You have entered wrong choice\n"
        elif (op.lower() == 'n'):
            print "Good Bye!\n"
            break
        else:
            print "You have entered wrong choice\n"

if __name__ == '__main__':
    main()
