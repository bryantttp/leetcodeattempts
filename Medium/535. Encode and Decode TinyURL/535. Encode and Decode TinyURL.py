class Codec:
    def __init__(self):
        pass

    originalURL, changedURL = defaultdict(), defaultdict()

    def generatelink(self):
        link = "http://tinyurl.com/" + ''.join(random.choice(string.ascii_letters + string_digits) for i in range(6))
        return link

    def encode(self, longUrl):
        temp_shortUrl = self.generatelink()
        self.originalURL[longUrl] = temp_shortUrl
        self.changedURL[temp_shortUrl] = longUrl

        return temp_shortUrl
        # """Encodes a URL to a shortened URL.
        #
        # :type longUrl: str
        # :rtype: str
        # """

    def decode(self, shortUrl):
        return self.changedURL[shortUrl]
        # """Decodes a shortened URL to its original URL.
        #
        # :type shortUrl: str
        # :rtype: str
        # """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))