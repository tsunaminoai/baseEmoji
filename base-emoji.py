#!/bin/env python
import json
import struct

#https://github.com/iamcal/emoji-data
with open('emoji.json') as data_file:
  emojis = json.load(data_file)


def unichar(i):
  try:
    return unichr(i)
  except ValueError:
    return struct.pack('i', i).decode('utf-32')

def encode_emoji(e):
    a = []
    while (e > 0):
      print emojis[(e) & 0x3ff]
      a.append( unichar( int(emojis[(e) & 0x3ff]['unified'], 16) ) )
      e = e>>10
    return ''.join(reversed(a))

def decode_emoji(d):
    r = 0L
    for v in d:
        r = (r<<10) + v
        #print "%d,%d" % (d,v)
    return r


test_int = 55812284154744246476039193196145952172539893391315043784985833979844630516437646362278696338348615542440300846801332508702033661460515063536770772416733295967508908382235636654474341949690870730323623932007686028974152431493351241789591501868689325754582797161818878128054527128837461417111542928160195621495L

encode = encode_emoji(test_int)
print "%s\n\n" % encode
#decode = decode_emoji(encode)
#print decode
#print test_int == decode

