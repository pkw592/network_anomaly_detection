import subprocess as sub

def capture_to_learn():
    #otwieranie pliku do zapisu
    try:
        f = open('data_check.txt', 'w')
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
        if (row_count >=200):
            break

    f.close()


def data_optimalizator():
    try:
        fo = open('data_check.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    try:
        fop = open('data_optimalized.txt', 'w')
    except:
        print('Failed to open file to write')
    
    lines = fo.readlines()

    for line in lines:
        splited = line.strip().split(sep=', ')
        splited.pop(3)
        splited.pop(1)

        splited[0] = splited[0][0:-7]
        if(splited[3]== 'UDP,'):
            splited[3] = 'UDP'
        splited[2] = splited[2][0:-1]

        for i in range(0, 4):
            fop.write(splited[i])
            if(i<4):
                fop.write('.')
                
        fop.write('\n')
        
    fop.close()
    fo.close()

def data_to_learn():
    try:
        fo = open('data_optimalized.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    try:
        fop = open('data_ready.txt', 'w')
    except:
        print('Failed to open file to write')

    lines = fo.readlines()

    fop.write('ip1_1;ip1_2;ip1_3;ip1_4;ip1_port;ip2_1;ip2_2;ip2_3;ip2_4;ip2_port;anomaly')

    for line in lines:
        splited = line.strip().split(sep='.')
        splited.pop(0)

        if(len(splited)<11):
            continue

        #packet type removed
        splited.pop(10)

        for i in range(len(splited)-1):
            fop.write(splited[i])
            if(i<len(splited)-1):
                fop.write(';')

        fop.write('\n')
        
    fop.close()
    fo.close()
