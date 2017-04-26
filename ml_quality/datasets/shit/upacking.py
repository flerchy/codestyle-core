item = ["december, 23, 2015", "cam", 343]
date = item [0]
name = item [1]
price = item [2]

date, name, price = ["december, 23, 2015", "cam", 343]

def drop_first_last(grades):
first,*middle,last = grades
avg = sum(middle / len(middle))
print(avg)



drop_first_last([65,67,46,34,98,21])
