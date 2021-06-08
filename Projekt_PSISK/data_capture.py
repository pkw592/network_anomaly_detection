import subprocess as sub

def capture_to_learn():
    #otwieranie pliku do zapisu
    try:
        f = open('data_check.txt', 'w')
    except:
        print('Failed to open file')

    #uruchomienie skanowania sieci za pomocą tcpdump'a w systemie windows
    p = sub.Popen(('sudo', 'tcpdump','-n', 'not arp'), stdout=sub.PIPE)
    
    row_count = 0

    #wpisywanie danych o każdym pakiecie w oddzielnej linii pliku tekstowego
    for row in iter(p.stdout.readline, ''):
        row_count +=1
        x = row.rstrip().split()
        for l in range(0,len(x)):
            f.write(x[l].decode() + ', ')
    
        f.write('\n')

        #zatrzymanie skanowania po 2000 pakietów w celu uniknięcia dużych plików
        if (row_count >=200):
            break

    f.close()


def data_optimalizator():
    #otwieranie pliku do odczytu
    try:
        fo = open('data_check.txt', 'r')
    except:
        print('Failed to open file to optimalize')
    
    #otwieranie pliku do zapisu
    try:
        fop = open('data_optimalized.txt', 'w')
    except:
        print('Failed to open file to write')
    
    #wczytywanie z pliku oddzielnych linii tj. pakietów
    lines = fo.readlines()

    #usuwanie nieodpowiadających danych dla każdego pakietu i zapis do nowego pliku
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
    #otwieranie pliku do odczytu
    try:
        fo = open('data_optimalized.txt', 'r')
    except:
        print('Failed to open file to optimalize')

    #otwieranie pliku do zapisu
    try:
        fop = open('data_ready.txt', 'w')
    except:
        print('Failed to open file to write')

    #wczytywanie z pliku oddzielnych linii tj. pakietów
    lines = fo.readlines()

    #zapis do pliku nagłówków kolumn dla lepszego czytania przez pakiet pandas
    fop.write('ip1_1;ip1_2;ip1_3;ip1_4\n')

    #odpowiednie podzielenie danych na kolumny w celu przygotowania do uczenia modelu
    for line in lines:
        splited = line.strip().split(sep='.')
        
        #usunięcie dancyh o godzinie przyjścia pakietu
        splited.pop(0)

        #pozbycie się małej ilości pakietów niezawierających wystarczającej ilości danych
        if(len(splited)<11):
            continue

        #packet type removed
        splited.pop(10)

        #zapis gotowych danych do pliku
        for i in range(0,4):

            fop.write(splited[i])
            if(i<3):
                fop.write(';')

        fop.write('\n')
        
    fop.close()
    fo.close()
