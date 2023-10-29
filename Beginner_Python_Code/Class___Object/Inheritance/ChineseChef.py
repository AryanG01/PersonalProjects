"""
class ChineseChef():

     def make_chicken(self):
        print("The Chef makes a Chicken.")

    def make_salad(self):
        print("The Chef makes a Salad.")

    def make_special_dish(self):
        print("The Chef makes BBQ Ribs.")

    def make_fried_rice(self):
        print("The Chef makes Fried rice.")
"""
from Chef import Chef

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The Chef makes Fried Rice.")
