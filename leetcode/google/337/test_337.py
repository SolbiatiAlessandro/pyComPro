import unittest
import l337


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l337.Solution()
    
    def test_helper(self):

       got = l337.populateHelper( "abcxyz123", ["abc","123"] ) 
       self.assertEqual( got, [1,1,1,-1,-1,-1,1,1,1] )

       got = l337.populateHelper( "aaabbcc" , ["aaa","aab","bc"] )
       self.assertEqual( got, [1,1,1,1,1,1,-1] )

       got = l337.populateHelper( "aabbaabbaa" , ["aa"] )
       self.assertEqual( got, [1,1,-1,-1,1,1,-1,-1,1,1] )

       got = l337.populateHelper( "aaabaa", ["aa"] ) 
       self.assertEqual( got, [1,1,1,-1,1,1])

       got = l337.populateHelper( "abcdef", ["a","c","e","g"] ) 
       self.assertEqual( got, [1,-1,1,-1,1,-1])


    #@unittest.skip("wait")
    def test_solution(self):

       got = self.s.addBoldTag( "aaabbcc" , ["aaa","aab","bc"] ) 
       self.assertEqual( got, "<b>aaabbc</b>c")

       got = self.s.addBoldTag( "abcxyz123", ["abc","123"] ) 
       self.assertEqual( got, "<b>abc</b>xyz<b>123</b>")

       got = self.s.addBoldTag( "aaabaa", ["aa"] ) 
       self.assertEqual( got, "<b>aaa</b>b<b>aa</b>")

       got = self.s.addBoldTag( "aaabbcc", ["a","b","c"]) 
       self.assertEqual( got, "<b>aaabbcc</b>")

       got = self.s.addBoldTag( "aaabbcc", ["b","cc"]) 
       self.assertEqual( got, "aaa<b>bbcc</b>")

       got = self.s.addBoldTag( "aaabbcc", ["a","c"]) 
       self.assertEqual( got, "<b>aaa</b>bb<b>cc</b>")

       got = self.s.addBoldTag( "aaabbcc", []) 
       self.assertEqual( got, "aaabbcc")

       got = self.s.addBoldTag( "", ["aa"]) 
       self.assertEqual( got, "")

       got = self.s.addBoldTag( "abcdef", ["a","c","e","g"]) 
       self.assertEqual( got, "<b>a</b>b<b>c</b>d<b>e</b>f")



if __name__ == "__main__":
    unittest.main()
