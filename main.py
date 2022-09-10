#python code ide in terminal

q = ""
while True:
    w = input(">>>")
    if w == "end":
        break
    else:
        if q == '':
            q += w
        else:
            q += '\n' + w
    print(q)
exec(q)
