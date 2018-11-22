import unittest
import l479


class testSolution(unittest.TestCase):
    

    #@unittest.skip("w")
    def test_solution( self ):
        
        v1, v2 = [1,2,3,4,5],[6,7,8,9,9]
        i, v = l479.ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        got = (x for x in v)
        vv = [v1, v2]
        for i in xrange(max(len(v) for v in vv)):
            for iv in vv:
                try: num = iv[i]
                except: num = None
                if num is not None:
                    self.assertEqual(num, got.next())

        v1, v2 = [1,2,3,4,5],[6,7,8]
        i, v = l479.ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        got = (x for x in v)
        vv = [v1, v2]
        for i in xrange(max(len(v) for v in vv)):
            for iv in vv:
                try: num = iv[i]
                except: num = None
                if num is not None:
                    self.assertEqual(num, got.next())

        v1, v2 = [1],[6,7,8]
        i, v = l479.ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        got = (x for x in v)
        vv = [v1, v2]
        for i in xrange(max(len(v) for v in vv)):
            for iv in vv:
                try: num = iv[i]
                except: num = None
                if num is not None:
                    self.assertEqual(num, got.next())

        v1, v2 = [],[6,7,8]
        i, v = l479.ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        got = (x for x in v)
        vv = [v1, v2]
        for i in xrange(max(len(v) for v in vv)):
            for iv in vv:
                try: num = iv[i]
                except: num = None
                if num is not None:
                    self.assertEqual(num, got.next())

        v1, v2 = [5],[]
        i, v = l479.ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        got = (x for x in v)
        vv = [v1, v2]
        for i in xrange(max(len(v) for v in vv)):
            for iv in vv:
                try: num = iv[i]
                except: num = None
                if num is not None:
                    self.assertEqual(num, got.next())

        v1, v2 = [],[]
        i, v = l479.ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        got = (x for x in v)
        vv = [v1, v2]
        for i in xrange(max(len(v) for v in vv)):
            for iv in vv:
                try: num = iv[i]
                except: num = None
                if num is not None:
                    self.assertEqual(num, got.next())

    @unittest.skip("w")
    def test_multivector(self):
        v1, v2, v3 = [1,2,3,4,5],[6,7,8,9,9],[0,0,0]
        i, v = l479.ZigzagIterator([v1, v2, v3]), []
        while i.hasNext(): v.append(i.next())
        print v
        got = (x for x in v)
        vv = [v1, v2, v3]
        for i in xrange(max(len(v) for v in vv)):
            for iv in vv:
                try: num = iv[i]
                except: num = None
                if num is not None:
                    self.assertEqual(num, got.next())

if __name__ == "__main__":
    unittest.main()

