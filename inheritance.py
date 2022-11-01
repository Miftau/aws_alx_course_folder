class Clothing:
    """The Pants class represents an article of clothing sold in a store
    """
    
    def __init__(self, color, waist_size, length, price):
        """Method for initializing an object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of an object
            length (str): length of an object
            price (float): price of an object
        """
        
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
class Pants(Clothing):
    """The Pants class represents an article of clothing sold in a store
    """
    
    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """
        Clothing.__init__(self, color, waist_size, length, price)
        
    