a = int(input('hanyadik lettél a versenyen ?'))

if a == 1:
    helyezet = "első helyen vagy !"
elif a == 2:
    helyezet = "második helyezet vagy !"
elif a == 3:
    helyezet = "harmadik helyezet lettél !"
elif a > 3:
    helyezet = "majd legközelebb"
    
print(helyezet)