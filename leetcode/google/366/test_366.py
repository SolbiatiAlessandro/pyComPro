import unittest
import l366

def clean():
    """clean globals"""
    l366.CHILDREN = {}
    l366.COLOR = {}
    l366.PARENT = {}

class testSolution(unittest.TestCase):

    def setUp(self):
        self.s = l366.Solution()
    
    def test_last_edge(self):
        l366.CHILDREN = {1: [[4, 3]], 2: [[1, 0]], 3: [[1, 1]], 4: [[2, 2], [5,4]]}
        got = l366.last_edge_in_cycle()
        self.assertEqual(got, 3)

    def test_last_edge_base_example(self):
        l366.CHILDREN = {1: [[2, 0], [5, 4]], 2: [[3, 1]], 3: [[4, 2]], 4: [[1, 3]]}
        l366.COLOR = {}
        got = l366.last_edge_in_cycle()
        self.assertEqual(got, 3)
        clean()

        #import pdb;pdb.set_trace()
        l366.CHILDREN = {1: [[5, 3], [2, 4]], 2: [[3, 0]], 3: [[4, 1]], 4: [[1, 2]]}
        l366.COLOR = {}
        got = l366.last_edge_in_cycle()
        self.assertEqual(got, 4)

        print "ok2"
        

    #@unittest.skip("wait")
    def test_solution(self):
        #import pdb;pdb.set_trace()
        test_input = [[1, 2], [1, 3], [2, 3]]
        expected = [2, 3]
        got = self.s.findRedundantDirectedConnection(test_input)
        self.assertEqual(got, expected)

        #import pdb;pdb.set_trace()
        test_input = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
        expected = [4, 1]
        got = self.s.findRedundantDirectedConnection(test_input)
        self.assertEqual(got, expected)

        #import pdb;pdb.set_trace()
        test_input = [[2, 3], [3, 4], [4, 1], [1, 5], [1, 2]]
        expected = [1, 2]
        got = self.s.findRedundantDirectedConnection(test_input)
        self.assertEqual(got, expected)

        test_input = [[1, 2], [2, 3], [3, 4], [3, 3], [1, 5]]
        expected = [3, 3]
        got = self.s.findRedundantDirectedConnection(test_input)
        self.assertEqual(got, expected)

        test_input = [[2, 1], [3, 1], [4, 2], [4, 5], [1, 4]]
        expected = [2, 1]
        got = self.s.findRedundantDirectedConnection(test_input)
        self.assertEqual(got, expected)

        print "okk"


if __name__ == "__main__":
    unittest.main()
