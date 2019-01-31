class birds:
    def __init__(self):
        """Constructor for this class"""
    # Create some members birds
        self.members = ["Sparrow", "Robin", "Duck"]

    def printmembers(self):
        print "*" * 145
        print "Printing members of the birds class"
        for birds in self.members:
            print "%s" %birds
        print "*" * 145
