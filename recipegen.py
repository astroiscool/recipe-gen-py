import json

# datavalues
while True:  
  craftingitem = input("The item to be used to craft is: ")
  numberitem = int(input("The amount of said item is: ")) 
  craftingitem2 = input("The item to be used to craft is: ")
  numberitem2 = int(input("The amount of said item is: ")) 
  result = input("resulting item: ")
  numberresult = int(input("The amount of resulting item is: ")) 

# needed item for crafting 1

  print("The item to be used to craft is:", craftingitem)
  print("The amount of said item is:", numberitem)

# needed item for crafting 2

  print("The item to be used to craft is:", craftingitem2)
  print("The amount of said item is:", numberitem2)

# result item and number of item

  print("Resulting item:", result)
  print("The amount of resulting item is:", numberresult)

# defines first set of variables such as the item needed and amount of said item

  ingredient = dict()
  ingredient["name"] = craftingitem
  ingredient["count"] = numberitem

# defines second set of variables such as the item needed and amount of said item

  ingredient2 = dict()
  ingredient2["name"] = craftingitem2
  ingredient2["count"] = numberitem2

# defines result

  recipeend = dict()
  recipeend["name"] = result
  recipeend["count"] = numberresult

# finishes structure of recipe

  recipe = dict()
  recipe["recipe"] = [ingredient,ingredient2]
  recipe["result"] = recipeend

  print("|")
  print(" Paste text below into 'recipes.json' file to add the recipe.")
  print("|")
  print(", "+json.dumps(recipe))
  print("|")
  print(" Press the 'X' in the corner to quit, or look below to continue")
  print("|")

