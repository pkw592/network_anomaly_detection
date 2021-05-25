import subprocess as sub

def capture_to_learn():
    #otwieranie pliku do zapisu
    try:
        f = open('data4.txt', 'w')
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

    f.close()


def data_optimalizator():
    try:
        fo = open('data4.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    try:
        fop = open('data_test4.txt', 'w')
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
                
        #op.write('2')
        fop.write('\n')
        
    fop.close()
    fo.close()

def data_to_learn():
    try:
        fo = open('data_test4.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    try:
        fop = open('data_opt4_ready.txt', 'w')
    except:
        print('Failed to open file to write')

    lines = fo.readlines()

    for line in lines:
        splited = line.strip().split(sep='.')
        splited.pop(0)

        if(len(splited)<11):
            continue

        splited.pop(10)

        for i in range(len(splited)-1):
            fop.write(splited[i])
            if(i<len(splited)-1):
                fop.write(';')

        fop.write('\n')
        
    fop.close()
    fo.close()


def y_change():
    try:
        fo = open('data_all_ready.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    try:
        fop = open('data_i1.txt', 'w')
    except:
        print('Failed to open file to write')
    
    lines = fo.readlines()

    for line in lines:
        splited = line.strip().split(sep=';')

        if(splited[10] == '1'):
            if(splited[0] == '192'):
                splited[10] = '3'
            elif(splited[0] != '192'):
                splited[10] = '4'

        if(splited[10] == '2'):
            if(splited[0] == '192'):
                splited[10] = '5'
            elif(splited[0] != '192'):
                splited[10] = '6'

        for i in range(len(splited)):
            fop.write(splited[i])
            if(i<len(splited)-1):
                fop.write(';')

        fop.write('\n')
        
    fop.close()
    fo.close()


def last_try():
    try:
        fo = open('data_i1.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    try:
        fop = open('data_i1_heh.txt', 'w')
    except:
        print('Failed to open file to write')
    
    lines = fo.readlines()

    for line in lines:
        splited = line.strip().split(sep=';')
        
        for i in range(len(splited)):
            fop.write(splited[i])
            if(i == 0):
                fop.write('.')
            if(i == 3):
                fop.write(';')
            if(i == 4):
                fop.write(';')
            if(i == 5):
                fop.write('.')
            if(i == 8):
                fop.write(';')
            if(i == 9):
                fop.write(';')
        fop.write('\n')
        
    fop.close()
    fo.close()
