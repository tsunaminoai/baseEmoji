# baseEmoji #

baseEmoji is a base1024 encoding scheme that uses emoji as its lookup table. The primary purpose is to represent otherwise ugly data in more "pleasing" form in social media.

## What is it? ##
baseEmoji is a representation of data in base1024 mapped into emoji. The main methods available are:

### Encoding / Decoding ###
```
#!python
encString = encode_emoji(messageLong, spacing='')
messageLong = decode_emoji(encString, spacing='')
```
These methods are symmetrical operations. encode_emoji() takes message data in the form of a long and produces a string of emoji that represents the base1024 of that data. An optional spacing character can be specified that will be placed between each emoji. To decode, the same spacing character must be known.

### String Encoding / Decoding ###
```
#!python
encString = encode_emoji_string(messageStr, spacing='')
messageStr = decode_emoji_string(encString, spacing='')
```
These methods are symmetrical operations. encode_emoji() takes message data in the form of a string, converts it to a long internally, and produces a string of emoji that represents the base1024 of that data. An optional spacing character can be specified that will be placed between each emoji. To decode, the same spacing character must be known.



### Use Case ###

The impetus for this module was to represent digital signatures in social media in a less obtrusive way. A signature on a tweet from a user to a bot is useful in alerting the bot to run commands that can be trusted to have come from a specific source. However, these signatures look like jibberish to human readers. Instead, this signature could be represented by emoji using baseEmoji and appear to a human reader like a typical Instagram user.

#### "Practical" Example: Signing a Tweet ####
**Signing**
```
#!python

import sys
import tweepy
import baseEmoji
from ecdsa import SigningKey

CONSUMER_KEY = '********'
CONSUMER_SECRET = '********'
ACCESS_KEY = '********'
ACCESS_SECRET = '********'

#set up tweepy and connect to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#create a signing key. In practice this would be saved
signKey = SigningKey.generate()

#our message
message = "This tweet is signed"

#sign the message
signature = signKey.sign(message)

#convert the signature into an emoji signature
emSig = baseEmoji.encode_emoji_string(signature," ")

#create the tweet with a delimiter for later parsing
tweet = message + " #blessed " + emSig

#send the tweet
t = api.update_status(tweet)

#...
```

**Tweet**

![Screenshot 2017-03-04 15.04.17.png](https://bitbucket.org/repo/rxLy6y/images/802293399-Screenshot%202017-03-04%2015.04.17.png)

**Verification**
```
#!python
#...
#get the verification key
verifyKey = signKey.get_verifying_key()

#retrieve a tweet (in this case the tweet we just sent)
v = api.get_status(t.id)

#split the text of the tweet into the message and the signature
(rmessage,remSig) = v.text.split(" #blessed ",1)

#convert the emoji signature back to its original form
rsignature = baseEmoji.decode_emoji_string(remSig," ")

#verify that the signature is valid for the message
assert verifyKey.verify(rsignature, rmessage)
```

In the wild, it may be advantageous to use a smaller digital signature algorithm and to also check that the length of the message plus the delimiter and signature don't go beyond 140 characters. While the signature itself can be a fixed size of bytes, because some emoji require more than one code point, the emoji signature could be a few characters longer according to Twitter's counting.

## Credits ##

Emoji list initially sourced from https://github.com/iamcal/emoji-data commit 6c6cb1481c7d1ee3529614e5fbe1434d65bfe701