class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
    
    def remove_item(self, item):
        try:
            self.shopping_list.remove(item)
        except:
            print('Item not currently in shopping list.')

    def view_list(self):
        print(self.list_name)
        for item in self.shopping_list:
            print(' - ' + str(item))

pet_store_list = ShoppingList('Pet Store Shopping List')

pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')

pet_store_list.remove_item('flea collars')

pet_store_list.add_item('frisbee')

pet_store_list.view_list()
