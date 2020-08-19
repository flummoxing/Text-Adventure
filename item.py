from printNice import printNice as pr

class Item():
    """
    Represents an item in the game.
    """

    def __init__(self,
                 name,
                 shortDesc,
                 longDesc,
                 pickUpText=None,
                 canPickUp=False,
                 isVisible=True,
                 preconditions=None
                 ):
        self.name = name    
        self.shortDesc = shortDesc  # Default item description
        self.longDesc = longDesc    # More detailed description
        self.contents = contents    # list of objects contained in this one
        self.isVisible = isVisible  # If the player can see the item
        self.canPickUp = canPickUp  # If player can acquire the item
        if canPickUp:   
            self.pickUpText = pickUpText
        else:
            self.pickUpText = "You can't pick up the %s" % self.name

        # Dictionary describing the actions that can be performed on this item
        self.actionMap = {}

        self.preconditions = preconditions # key: method name, value: precondition,
                                            # e.g. "open" : "player has key"

    def getPrecondition(self, action):
        """Returns any preconditions for the desired action."""

        if action in self.preconditions:
            return self.preconditions[action]
        return None

    def do(self, action, preconditionMet):
        """Perform an action (other than examine) on this specific item."""

        if action in self.actionMap:
            self.actionMap[action](preconditionMet)
        else:
            pr("You failed to " + action + " the %s" % self.name)

    # def doWith(self, action, item):
    #     """
    #     Perform an action on this specific item, involving another item.
    #     e.g. open door with key.
    #     """
    #     if not self.isVisible:
    #         pr("You don't notice any %s." % self.name)
    #         return

    #     if action in self.actionMap:
    #         self.actionMap[action](item)
    #     else:
    #         pr("You failed to " + action + " the %s" % self.name)

    def describe(self):
        """Returns the short description of the item."""
        pr(self.shortDesc)

    def examine(self):
        """Returns the more detailed description of the item."""
        pr(self.longDesc)

    def addAction(self, actionName, actionFunction):
        """
        Add an action to the object's action map.
        
        Action must be added to the instance's bound methods with __get__
        """
        
        self.actionMap[actionName] = actionFunction

    def getNameIndef(self):
        """
        Gets the objects name with the appropriate indirect article,
        e.g. "an apple", "a banana"
        """
        if self.name[0] in ["a", "e", "i", "o", "u"]:
            return "an " + self.name
        else:
            return "a " + self.name
    
class Container(Item):
    """Represents an object in the game that can contain other Items."""

    def __init__(self,
                 name,
                 shortDesc,
                 longDesc,
                 pickUpText=None,
                 canPickUp=False,
                 contents=None,
                 isVisible=True,
                 preconditions=None,
                 unlocked=True
                 ):
        super().__init__(name, shortDesc, longDesc, pickUpText, canPickUp, isVisible, precondtiions)

        self.isOpen = False
        self.unlocked = unlocked
        self.contents = contents
        self.actionMap["open"] = self.open
        self.actionMap["unlock"] = self.unlock
        self.preconditions["open"] = { self.unlocked == True}

    def open(self, preconditionMet):
        if self.isOpen:
            pr("The %s is already open." % self.name)
        else:
            if self.unlocked or preconditionMet:
                self.isOpen = True
                pr("You open the %s. Inside, you find " % self.name)
                pr(self.getContents())
            else:
                pr("The %s is locked." % self.name)
        
    def getContents(self):
        """Returns this item's contents, if any."""
        output = ""
        if self.contents:
            i = len(self.contents)
            while i > 2:
                output += self.contents[i - 1].getNameIndirect() + ", "
                i -= 1
            output += self.contents[i - 1].getNameIndirect() + " and " + self.contents[i - 2].getNameIndirect() + "."
        else:
            output = "The " + self.name + " is empty."
        return output

def main():
    pass




    # EXAMPLE OF HOW TO ADD METHOD TO CLASS INSTANCE
    # banana = Item("banana", "b", "B")
    # def eat(self):
    #     print("you ate the %s" %self.name)
    # banana.eat = eat.__get__(banana, banana.__class__)
    # banana.eat()
    # banana.addAction("eat", banana.eat)
    # banana.do("eat")

    # apple = Item("apple", "a", "A")
    # print(apple.do("eat"))

if __name__ == "__main__":
    main()

        