inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#How many items are in the warehouse?
inventory_len = len(inventory)

#Select the first element in inventory. Save it to a variable called first.
first = inventory[0]

#Select the last element from inventory. Save it to a variable called last.
last = inventory[-1]

#Select items from the inventory starting at index 2 and up to, but not including, index 6.
inventory_2_6 = inventory[2:6]

#Select the first 3 items of inventory. Save it to a variable called first_3.
first_3 = inventory[:3]

#How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds
twin_beds = inventory.count("twin bed")

#Remove the 5th element in the inventory. Save the value to a variable called removed_item.
removed_item = inventory.pop(4)

#There was a new item added to our inventory called "19th Century Bed Frame". Use the .insert() method to place the new item as the 11th element in our inventory.

inventory.insert(10, "19th Century Bed Frame")

#Sort inventory using the .sort() method or the sorted() function. Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted(). Print inventory to see the result.

inventory.sort()
print(inventory)
