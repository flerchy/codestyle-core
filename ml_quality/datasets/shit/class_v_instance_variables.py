class Girl:
    gender = 'female'

    def __init__(self, name):
    self.name = name

    ## every girl will be female, but the name will be unique

    r = Girl("rachel")
    s = Girl("lady")
    print(r.gender)
    print(s.gender)
