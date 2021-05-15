import subprocess as sub

def capture_to_learn():
    #otwieranie pliku do zapisu
    try:
        f = open('data2.txt', 'w')
    except:
        print('Failed to open file')

    p = sub.Popen(('sudo', 'tcpdump','-n', 'not arp'), stdout=sub.PIPE)
    
    row_count = 0

    for row in iter(p.stdout.readline, ''):
        row_count +=1
        x = row.rstrip().split()
        for l in range(0,len(x)):
            f.write(x[l].decode() + ', ')
    
        f.write('\n')

        if(row_count >= 200):
            break

    f.close()


def data_optimalizator():
    try:
        fo = open('data1.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    try:
        fop = open('data_opt1.txt', 'w')
    except:
        print('Failed to open file to write')
    
    lines = fo.readlines()

    for line in lines:
        splited = line.strip().split(sep=', ')
        splited.pop(3)
        splited.pop(1)

        if(splited[3]== 'UDP,'):
            splited[3] = 'UDP'

        for i in range(0, 4):
            fop.write(splited[i])
            if(i<3):
                fop.write(';')

        fop.write('\n')
        
    fop.close()
    fo.close()