class Pants:
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
        
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
    def get_price(self):
      return self.price
        
    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args: 
            new_price (float): the new price of the pants object

        Returns: None

        """
        self.price = new_price
    
    def discount(self, discount):
        return self.price *(1 - discount)
    

class SalesPerson(Pants):
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0
        
    
    def sell_pants(self, sales):
        """The sell_pants method appends a pants object to the pants_sold attribute

        Args: 
            pants_object (obj): a pants object that was sold

        Returns: None

        """

        self.pants_sold.append(sales)
        
    def calculate_sales(self):
        """The calculate_sales method sums the total price of all pants sold

        Args: None

        Returns:
            float: sum of the price for all pants sold
        
        """

        total = sum(pants.price for pants in self.pants_sold)
        self.total_sales = total

        return total
        
    def calculate_commissions(self, commission): 
        sold_pants = self.calculate_sales
        return sold_pants * commission
    
    def display_sales(self):
        """The display_sales method prints out all pants that have been sold

        Args: None

        Returns: None

        """

        for pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'\
                  .format(pants.color, pants.waist_size, pants.length, pants.price))