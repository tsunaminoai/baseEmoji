#!/bin/env python
import json
import struct
import collections

#https://github.com/iamcal/emoji-data
with open('emoji.json') as data_file:
  data = json.load(data_file)
  emojis = collections.OrderedDict(sorted( (x['unified'].lstrip('0'),ind) for ind, x in enumerate(data) if x['has_img_twitter']))



def unichar(i):
  try:
    return unichr(i)
  except ValueError:
    return struct.pack('i', i).decode('utf-32')

def encode_emoji(e,spacing=''):
    a = []
    while (e > 0):
      emoji = ''
      for x in emojis.items()[(e) & 0x3ff][0].split('-'):
        print "%s %d" %(x,int(x, 16))
        emoji += unichar( int(x, 16) )

      a.append( emoji.encode('utf-8') )
      e = e>>10
    return spacing.join(reversed(a))

def decode_emoji(d,spacing=''):
    r = 0L
    print d
    for v in unicode(d,'utf-8'):
      if v == spacing:
        continue
      print ord(v)
      i = format(ord(v),'x').upper()
      numeric = emojis[i][1]
      r = (r<<10) + v
      #print "%d,%d" % (d,v)
    return r


test_int = 55812284154744246476039193196145952172539893391315043784985833979844630516437646362278696338348615542440300846801332508702033661460515063536770772416733295967508908382235636654474341949690870730323623932007686028974152431493351241789591501868689325754582797161818878128054527128837461417111542928160195621495L
test_int = 2147483647L
encode = encode_emoji(test_int,spacing=" ")
print "%s\n\n" % encode
decode = decode_emoji(encode,spacing=" ")
#print decode
#print test_int == decode

