def dumb_sentence(name='buck', action='ate', item='tuna'):
    print(name, action, item)

    dumb_sentence()

    #uses default arguments

    dumb_sentence("sally", "farts", "gently")
    dumb_sentence(item='awesome')
    dumb_sentence(item='awesome', name='cam' )
