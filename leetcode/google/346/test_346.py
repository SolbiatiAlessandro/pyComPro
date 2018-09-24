import unittest
import l336


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l336.Solution()

    def test_solution( self ):

        inputBoard =  [
                      [0,1,0],
                      [0,0,1],
                      [1,1,1],
                      [0,0,0]
                      ]
        outputBoard = [
                      [0,0,0],
                      [1,0,1],
                      [0,1,1],
                      [0,1,0]
                      ]
        self.s.gameOfLife( inputBoard )
        self.assertEqual( inputBoard, outputBoard )
    

if __name__ == "__main__":
    unittest.main()
