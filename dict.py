# Python 3.4

class dictionary(): # Create dictionary class
    
    def __init__(self): # Create properties
        self.dict = {} # Dictionary
        self.passed = 0 # <<<<< Unit test variables 
        self.errors = 0 # <<<<< Unit test variables 

    def append(self, key, value): # Add/update keys in a dictionary 
       key = str(key) # Make sure key is a string
       if key in self.dict: # if key is in the dictionary
         self.dict[key] = value # update key
         print("['%s'] updated" % key )
         return "updated"
       else:
         self.dict[key] = value # Create new key
         print("['%s'] added" % key )
         return "added"

    def remove(self, key): # Remove key from a dictionary 
        if key in self.dict: 
            del self.dict[key] # delete the key
            print("Data removed")
            return "removed"
        else:
            print("Could not find key")
            return "not found"
        
    def get(self): # Return the dictioanry 
        print("Output: %s" % self.dict)
        return "got"
    
    def test(self): # Unit tests
        self.passed = 0
        self.errors = 0

        if self.append("dog", "1234") is "added" or self.append("dog", "1234") is "updated": # Check append() method
            print("Append test passed!")
            self.passed += 1 # Add to passed
        else:
            print("Append test failed!")
            self.errors += 1 # Add to errors


        
        if self.remove("dog") is "removed" or self.remove("dog") is "not found": # Check remove() method
            print("Remove test passed!")
            self.passed += 1
        else:
            print("Remove test failed!")
            self.errors += 1
            

        if self.get() is "got": # Check get() method
            print("Get test passed!")
            self.passed += 1
        else:
            print("Get test failed!")
            self.errors += 1


        print("{0} tests passed, {1} tests failed".format(self.passed, self.errors)) # e.g: 3 tests passed, 0 tests failed




    

































    
    
