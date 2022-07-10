class Codec:
    def __init__(self):
        self.baseurl = 'http://tinyurl.com/'
        self.encodeMap = dict()
        self.decodeMap = dict()
        self.new_ = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            s = self.baseurl + str(self.new_)
            self.new_ += 1
            self.encodeMap[longUrl] = s
            self.decodeMap[s] = longUrl
        
        return self.encodeMap[longUrl]
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))