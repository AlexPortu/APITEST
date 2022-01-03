y = {'yep':[{'dog': 1}, {'cat': 2},{'fish': 3}]}

x = next((i for i, item in enumerate(y['yep']) if item['dog'] == 1), None)
#y = next(i for i, item in enumerate(lista) if item["dog"] == 1)
print(x)