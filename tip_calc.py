class tip_calc:
  def __init__(self):
    print("Welcome to the tip calculator.")
    self.bill = float(input("What was the total bill? "))
    self.percent = int(input("What percentage would you like to give as tip? 10, 12 or 15? "))
    self.count = int(input("How many people to split the bill? "))
  
  def tip(self):
    self.tip =  self.bill * self.percent / 100
    return round(self.tip,2)

  def each_pay(self):
    return round((self.bill + self.tip)/7,2)


order1 = tip_calc()

print(order1.tip())
print(order1.each_pay())