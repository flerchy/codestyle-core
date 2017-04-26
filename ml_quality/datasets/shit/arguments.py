# arguments are needed to set default values

def get_gender(sex="Unknown"):
#setting it to unknown so that something goes into DB
if sex is "m":
    sex = "Male"
elif sex is "f":
    sex = "Female"
    print(sex)

    get_gender("m")
    get_gender("f")
    get_gender()
    
