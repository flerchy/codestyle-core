stocks = {
    'goog':520.83,
    'fb':74.56,
    'yhoo':38.85,
    'amzn':306.98,
    'appl':99.28
}

cam = zip(stocks.values(), stocks.keys())
print(min(cam))
print(max(cam))
print(sorted(cam))
buck = zip(stocks.keys(),stocks.values())
print(sorted(buck))
