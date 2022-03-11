with open('a.txt','r') as file:
    count=0
    content=file.read()
    for i in content:
        if i.islower():
            count+=1

print(count)
