class School():
    def __init__(self, name):
        self.name=name
        self._roster={}
    
    def roster(self):
        return self._roster

    def add_student(self, student_name, grade_level):
        if grade_level in self._roster:
            self._roster[grade_level].append(student_name)
        else: 
            self._roster[grade_level] = [student_name]
        return self._roster
                 
                 
                 #, orders=[], location=None):
       # self.name=name
       # self.orders = orders
        #self.location = location
        #self.total_spent = sum([i['item_cost']*i['quantity'] for i in orders])
   # def add_order(self, item_name, item_cost, quantity):
    #    self.orders.append({'item_name': item_name, 'item_cost':item_cost, 'quantity':quantity})
     #   self.total_spent += item_cost * quantity
 