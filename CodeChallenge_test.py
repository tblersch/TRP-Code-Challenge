import unittest
import CodeChallenge as cc

class TestStringMethods(unittest.TestCase):
    def test_longestWord(self):
        #simple test to find longest word
        rslt = cc.Word()
        s = 'The quick brown fox jumped over the lazy dog.'
        rslt = cc.FindLongestWord(s)
        self.assertTrue(rslt.word=='jumped')
        self.assertTrue(rslt.length==6)

    def test_shortestWord(self):
        #simple test to find shortest word
        rslt = cc.Word()
        s = 'The quick brown fox jumped over the lazy dog.'
        rslt = cc.FindShortestWord(s)
        self.assertTrue(rslt.word=='The')
        self.assertTrue(rslt.length==3)

    def test_emptyString(self):
        #Empty string returns empty string
        rslt = cc.Word()
        s = ''
        rslt = cc.FindShortestWord(s)
        self.assertTrue(rslt.word=='')
        self.assertTrue(rslt.length==0)

    def test_PunctuationIsRemoved(self):
        rslt = cc.Word()
        #If punctuation is properly removed, the longest word should be "words," not "short,"
        s = "The old words when short, are best of all."
        rslt = cc.FindLongestWord(s)
        self.assertTrue(rslt.word=='words')
        self.assertTrue(rslt.length==5)

    def test_firstLongestWordIsSelected(self):
        rslt = cc.Word()
        #"wasteful" and "possible" are both 8 characters.  Function should return "wasteful"
        s = "If one has to submit, it is wasteful not to do so with the best grace possible."
        rslt = cc.FindLongestWord(s)
        self.assertTrue(rslt.word=='wasteful')
        self.assertTrue(rslt.length==8)


    def test_sentenceWithHypenatedWord(self):
        rslt = cc.Word()
        #last word of the quote was "inevitable."  Removed it, so the longest word should be "so-called"
        s = "The English know how to make the best of things. Their so-called muddling through is simply skill at dealing with the..."
        rslt = cc.FindShortestWord(s)
        self.assertTrue(rslt.word=='to')
        self.assertTrue(rslt.length==2)
        rslt = cc.FindLongestWord(s)
        self.assertTrue(rslt.word=='so-called')
        self.assertTrue(rslt.length==9)

    def test_sentenceWithWordWithApostrophe(self):
        rslt = cc.Word()
        s = "Employ your time in improving yourself by reading other men's writings."
        rslt = cc.FindShortestWord(s)
        #If the regex is NOT accounting for the apostrophe correctly, the shortest word will be "s".  Otherwise, it should be "in"
        self.assertFalse(rslt.word=='s')
        self.assertFalse(rslt.length==1)


if __name__ == '__main__':
    unittest.main()