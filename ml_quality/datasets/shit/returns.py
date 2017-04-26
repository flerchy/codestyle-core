def allowed_dating_age(age):
    girls_age = age/2+7
    return girls_age

cam_limit=allowed_dating_age(27)
creepy_joe=allowed_dating_age(49)
print("cam can date girls", cam_limit, "or older")
print("creepy joe can date girls", creepy_joe, "or older")
