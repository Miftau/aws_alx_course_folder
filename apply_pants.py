from pants import Pants, SalesPerson

pant = Pants("Pink", "L", 45, 40)
print(pant.color)

print(pant.price)
pant.change_price(15)

print(pant.price)

discount = pant.discount(.2)
print(discount)

recorder = SalesPerson("Chuka", "Chumos", 11, 67)
recorder_name = f"{recorder.first_name} {recorder.last_name}"
print(recorder_name)

recorder.sell_pants(2)
recorder.sell_pants(3)
print(recorder.pants_sold)
price = pant.price



def display_sales():
        """The display_sales method prints out all pants that have been sold

        Args: None

        Returns: None

        """

        for pants in recorder.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'\
                  .format(pant.color, pant.waist_size, pant.length, pant.price))
            
display_sales()

