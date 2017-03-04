# -*- coding: utf-8 -*-

import baseEmoji
import unittest
import random
import string

class baseEmojiTest(unittest.TestCase):
    def testEncodeDecodeInt(self):
      for i in range(100):
        test_int = random.getrandbits(128)
        encoded_string = baseEmoji.encode_emoji(test_int)
        decoded_int = baseEmoji.decode_emoji(encoded_string)
        self.assertEqual(test_int, decoded_int)

    def testEncodeDecodeString(self):
        for i in range(100):
            test_string = ''.join(random.choice(string.printable) for _ in range(random.randint(10,140)))
            encoded_string = baseEmoji.encode_emoji_string(test_string)
            decoded_string = baseEmoji.decode_emoji_string(encoded_string)
            self.assertEqual(test_string, decoded_string)


    def testEncodeDecodeStringWithSpacing(self):
        test_string = ''.join(random.choice(string.printable) for _ in range(random.randint(10,140)))
        encoded_string = baseEmoji.encode_emoji_string(test_string," ")
        decoded_string = baseEmoji.decode_emoji_string(encoded_string," ")
        self.assertEqual(test_string, decoded_string)

    def testEncodeDecodeIntWithSpacing(self):
        test_int = random.getrandbits(128)
        encoded_string = baseEmoji.encode_emoji(test_int," ")
        decoded_int = baseEmoji.decode_emoji(encoded_string," ")
        self.assertEqual(test_int, decoded_int)