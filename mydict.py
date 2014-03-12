#!/usr/bin/python
#===============================================================================
# @Mikematic
# 01.31.2011
# 
# Extending the dictionary class to implement filtering methods.
# Dictionary filtering methods like minus, absoluteMinus, intersection, 
# absoluteIntersection etc
#===============================================================================

class mydict(dict):
    
    #
    # Name: minus
    #
    # Desc: This method takes itself and another mydict and returns all the key/value pairs 
    #       whose key is present in that are in self but not present in mydic2.
    #         e.g: if x = {a:1, b:2, c:3} and y = {a:1, c:5} then x.minus(y) = {b:3}
    #
    # Para: @self - the mydict itself
    #                e.g: x = {a:1, b:2, c:3}
    #       @mydict2 - same parameter as above
    #
    def minus(self, mydict2):
        operatedDict = mydict()
        for keyInSelf in self.iterkeys(): # Big O value is O(N)
            if not mydict2.has_key(keyInSelf): # Big O value is O(1)...supposedly faster than any search tree (wiki)
                operatedDict[keyInSelf] = self[keyInSelf]
        return operatedDict
    
    #
    # Name: absoluteMinus
    #
    # Desc: This method takes its own self(mydict) and another mydict2 and returns all the key/value pairs 
    #       whose key/value is not present in self's key/value pairing. This method is different from minus 
    #       method
    #         e.g: if x = {a:1, b:2, c:3} and y = {a:1, c:5} then x.intersection(y) = {a:1, c:3}
    #
    # Para: @self - the mydict itself
    #                e.g: x = {a:1, b:2, c:3}
    #       @mydict2 - same parameter as above
    #
    def absoluteMinus(self, mydict2):
        print "Yet to be implemented..."
    
    #
    # Name: intersection
    #
    # Desc: This method takes itself(mydict) and another mydict and returns all the key/value pairs 
    #       whose key is present in self and also present in mydict2
    #         e.g: if x = {a:1, b:2, c:3} and y = {a:1, c:5} then x.intersection(y) = {a:1, c:3}
    #
    # Para: @self - the mydict itself
    #                e.g: x = {a:1, b:2, c:3}
    #       @mydict2 - same parameter as above
    #
    def intersection(self, mydict2):
        operatedDict = mydict()
        for key in self.iterkeys():
            if mydict2.has_key(key):
                operatedDict[key] = self[key]
        return operatedDict
    
    #
    # Name: absoluteIntersection
    #
    # Desc: This method takes itself(mydict) and another mydict and returns all the key/value pairs 
    #       whose key is present in self and also present in mydict2
    #         e.g: if x = {a:1, b:2, c:3} and y = {a:1, c:5} then x.intersection(y) = {a:1, c:3}
    #
    # Para: @self - the mydict itself
    #                e.g: x = {a:1, b:2, c:3}
    #       @mydict2 - same parameter as above
    #
    def absoluteIntersection(self, mydict2):     
            print "Yet to be implemented..."
    
    #
    # Name: union
    #
    # Desc: This method takes itself(mydict) and another mydict and returns all the key/value pairs 
    #       that is a union of both sets
    #         e.g: if x = {a:1, b:2, c:3} and y = {a:1, c:5, k:9} then x.union(y) = {a:1, b:2, c:3, k:9}
    #
    # Para: @self - the mydict itself
    #                e.g: x = {a:1, b:2, c:3}
    #       @mydict2 - same parameter as above
    #
    def union(self, mydict2):     
            print "Yet to be implemented..."
            
        
    
