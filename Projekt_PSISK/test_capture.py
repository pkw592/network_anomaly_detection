def capture():
    #otwieranie pliku do zapisu
    try:
        f = open('data_to_test.txt', 'w')
    except:
        print('Failed to open file')

    p = sub.Popen(('sudo', 'tcpdump'), stdout=sub.PIPE)
    
    for row in iter(p.stdout.readline, ''):
        x = row.rstrip().split()
        for l in range(0,len(x)):
            f.write(x[l].decode() + ', ')
    
        f.write('\n')

    f.close()