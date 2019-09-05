while True:
    f = open('instructions.txt','a')
    i = input("Enter time:")
    d = 1 #input('Defaults to be?')
    c = tuple(map(int,i.split('.')))
    t = str(c[0]*60000+c[1]*1000+c[2])
    for j in range(1,17):
        f.write(t)
        f.write(' ')
        f.write(str(j))
        f.write(' ')
        f.write(str(d))
        f.write('\n')

    f.close()          



