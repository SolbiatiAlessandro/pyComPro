import unittest
import l341

class testHelpers( unittest.TestCase ):

    @unittest.skip("wait")
    def test_lsearch( self ):

        l = [(3,-1),(4,-1),(5,-1)]
        self.assertEqual( l341.lsearch( l, 0 ), 0 )
        self.assertEqual( l341.lsearch( l, 1 ), 0 )
        self.assertEqual( l341.lsearch( l, 2 ), 0 )
        self.assertEqual( l341.lsearch( l, 3 ), 1 )
        self.assertEqual( l341.lsearch( l, 4 ), 2 )
        self.assertEqual( l341.lsearch( l, 5 ), 3 )
        self.assertEqual( l341.lsearch( l, 6 ), 3 )
        self.assertEqual( l341.lsearch( l, 7 ), 3 )

        l = [(1,0),(2,0),(5,0),(6,0)]
        self.assertEqual( l341.lsearch( l, 0 ), 0 )
        self.assertEqual( l341.lsearch( l, 1 ), 1 )
        self.assertEqual( l341.lsearch( l, 2 ), 2 )
        self.assertEqual( l341.lsearch( l, 3 ), 2 )
        self.assertEqual( l341.lsearch( l, 4 ), 2 )
        self.assertEqual( l341.lsearch( l, 5 ), 3 )
        self.assertEqual( l341.lsearch( l, 6 ), 4 )
        self.assertEqual( l341.lsearch( l, 7 ), 4 )


    @unittest.skip("wait")
    def test_query( self ):

        l = [(1,2),(2,1)]
        end = 0
        got = l341.query( l, end, 3, 3 )
        self.assertEqual( got, 3 )

        l = [(2,2),(3,1)]
        end = 0
        got = l341.query( l, end, 2, 3 )
        self.assertEqual( got, 2 )

        l = [(2,2),(3,1)]
        end = 0
        got = l341.query( l, end, 3, 3 )
        self.assertEqual( got, 4 )

        l = [(2,2),(3,1)]
        end = 0
        got = l341.query( l, end, 5, 3 )
        self.assertEqual( got, 4 )

        l = [(2,2),(3,1)]
        end = 0
        got = l341.query( l, end, 5, 3 )
        self.assertEqual( got, 4 )

        l = [(2,2),(3,1)]
        end = 0
        got = l341.query( l, end, 5, 3 )
        self.assertEqual( got, 4 )

        l = [(1,2),(2,1)]
        end = 0
        got = l341.query( l, end, 1, 3 )
        self.assertEqual( got, 1 )

    @unittest.skip("wait")
    def test_queryReverse( self ):
        l = [(3,0)]
        end = 0
        got = l341.query( l, end, 1, 1 )
        self.assertEqual( got, 1 )

class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l341.Solution()

    @unittest.skip("wait")
    def test_solution( self ):
        l = [0,1,0,2,1,0,1,3,2,1,2,1]
        got  =self.s.trap( l )
        self.assertEqual( got, 6 )

        #import pdb;pdb.set_trace()
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 6 )

        l = [2,1,0,3]
        got  =self.s.trap( l )
        self.assertEqual( got, 3 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 3 )

        l = [2,1,0,1,0,2]
        got  =self.s.trap( l )
        self.assertEqual( got, 6 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 6 )

        l = [3,2,0,2,0,4]
        got  =self.s.trap( l )
        self.assertEqual( got, 8 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 8 )

        l = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]
        got  =self.s.trap( l )
        self.assertEqual( got, 0 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 0 )

        l = [4,3,2,1,2,3,4]
        got  =self.s.trap( l )
        self.assertEqual( got, 9 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 9 )

        l = [5]
        got  =self.s.trap( l )
        self.assertEqual( got, 0 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 0 )

        l = []
        got  =self.s.trap( l )
        self.assertEqual( got, 0 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 0 )

        l = [5,5,5,5,5,5,5,5]
        got  =self.s.trap( l )
        self.assertEqual( got, 0 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 0 )
        
    @unittest.skip("wait")
    def test_breakingInverse( self ):
        l = [2,1,0,3]
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 3 )

        l = [10,0,1]
        got  =self.s.trap( l )
        self.assertEqual( got, 1 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 1 )

        l = [10,0,3]
        got  =self.s.trap( l )
        self.assertEqual( got, 3 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 3 )

        l = [4,3,2,1,0,1,2]
        got  =self.s.trap( l )
        self.assertEqual( got, 4 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 4 )
        

    @unittest.skip("wait")
    def test_waterOnTop( self ):

        l = [5,3,1,0,5]
        got  =self.s.trap( l )
        self.assertEqual( got, 11 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 11 )

        l = [9,5,3,0,3,5,9]
        got  =self.s.trap( l )
        self.assertEqual( got, 29 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 29 )

        l = [100,0,1]
        got  =self.s.trap( l )
        self.assertEqual( got, 1 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 1 )

        l = [100,50,51]
        got  =self.s.trap( l )
        self.assertEqual( got, 1 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 1 )

        l = [5,2,1,2,1,5]
        got  =self.s.trap( l )
        self.assertEqual( got, 14 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 14)

    @unittest.skip("Wait")
    def test_stillBreaking( self ):

        l = [4,2,0,3,2,5]
        got  =self.s.trap( l )
        self.assertEqual( got, 9 )
        got  =self.s.trap( l[::-1] )
        self.assertEqual( got, 9)



if __name__=="__main__":
    unittest.main()
