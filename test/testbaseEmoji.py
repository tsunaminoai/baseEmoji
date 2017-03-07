# -*- coding: utf-8 -*-

import baseEmoji
import unittest
import random
import string

class baseEmojiTest(unittest.TestCase):
    def testEncodeDecodeInt(self):
      for i in range(1000):
        test_int = random.getrandbits(128)
        encoded_string = baseEmoji.encode(test_int)
        decoded_int = baseEmoji.decode(encoded_string)
        self.assertEqual(test_int, decoded_int, "Failed on %d" % test_int)

    def testEncodeDecodeString(self):
        for i in range(1000):
            test_string = ''.join(random.choice(string.printable) for _ in range(random.randint(10,140)))
            encoded_string = baseEmoji.encodeStr(test_string)
            decoded_string = baseEmoji.decodeStr(encoded_string)
            self.assertEqual(test_string, decoded_string, "Failed on %s" % test_string)


    def testEncodeDecodeStringWithSpacing(self):
        test_string = ''.join(random.choice(string.printable) for _ in range(random.randint(10,140)))
        encoded_string = baseEmoji.encodeStr(test_string," ")
        decoded_string = baseEmoji.decodeStr(encoded_string," ")
        self.assertEqual(test_string, decoded_string, "Failed on %s" % test_string)

    def testEncodeDecodeIntWithSpacing(self):
        test_int = random.getrandbits(128)
        encoded_string = baseEmoji.encode(test_int," ")
        decoded_int = baseEmoji.decode(encoded_string," ")
        self.assertEqual(test_int, decoded_int, "Failed on %d" % test_int)