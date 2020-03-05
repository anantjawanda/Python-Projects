#Anant Jawanda
#lab05

import unittest


#test collision
#test if list resizes when reaches factor
from hashing import HashTable
class testHash(unittest.TestCase):

    def testPut(self):
        H=HashTable()
        H.put(54, "cat")
        H.put(26, "dog")
        H.put(93, "lion")
        H.put(17, "tiger")
        H.put(31, "cow")
        H.put(44, "goat")
        answer="goat"
        self.assertEqual(answer, H.get(44))

    def testResize(self):           #shows that if list gets close to filling up, the size is increased by 1 everytime leading factor > 0.5
        H=HashTable()
        H.put(54, "cat")
        H.put(26, "dog")
        H.put(93, "lion")
        H.put(17, "tiger")
        H.put(77, "bird")
        H.put(31, "cow")
        H.put(44, "goat")
        H.put(55, "pig")
        H.put(20, "chicken")
        H.put(9, "elephant")
        H.put(24, "pigeon")
        H.put(93, "turtle")
        answer=15
        self.assertEqual(answer, len(H.slots))

    def testSameKey(self):
        H=HashTable()
        H.put(11, "cat")
        H.put(26, "dog")
        H.put(93, "lion")
        H.put(11, "tiger")    #tests to see if this element is replaced at same key as first element
        answer= ['tiger', None, None, None, 'dog', 'lion', None, None, None, None, None]
        self.assertEqual(answer, H.data)

    def testCollision(self):            #if different key but same value after modulo operations
        H=HashTable()
        H.put(11, "cat")
        H.put(26, "dog")
        H.put(93, "lion")
        H.put(22, "tiger")    #moves tiger to next slot after cat because of collision
        answer= ['cat', 'tiger', None, None, 'dog', 'lion', None, None, None, None, None]
        self.assertEqual(answer, H.data)

if __name__ == '__main__':
    unittest.main()

