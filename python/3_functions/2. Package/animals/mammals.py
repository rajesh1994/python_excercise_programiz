class mammals:
    def __init__(self):
        """ Constructor for this class"""
        # Create some members animals
        self.members = ["Tiger", "Elephant", "Wild Cat"]

    def printmembers(self):
        print "*" * 145
        print " " * 50, "1. Python Package"
        print "Printing members of the mammals class"
        for mammal in self.members:            
            print "%s" %mammal
