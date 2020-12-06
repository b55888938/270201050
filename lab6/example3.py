books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
    i = i.replace("'","")
    i = i.replace(" ","")
    letters = len(i)
    unique = len(set(i))
    average = (letters+unique) / 2
    book_dict[i] = (letters, unique, average)
print(book_dict)