# a collection of items, but with not dups like a list
#curly brackets for sets in python (not be confused with hash)
groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'beer'}
groceries1 = ['cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'beer']
print(groceries)
print(groceries1)

#python takes on duplicates

if 'milk' in groceries:
    print("you already have it")
else:
    print("you need milk")
