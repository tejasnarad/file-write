#run script in only windowed mode
#show window while running the script in background
#user interface by pyqt5
#for displaing the output of the script in a text box



#read text file and give content in string
f = open('file.txt', 'r')

a=f.read()
f.close()

#log data in file test.txt
f = open('file.txt', 'a')
f.write('\nThis is a new line '+a+'\n')
f.close()
i=0

while True:
    if i==8760:
        break
    f = open('file.txt', 'a')
    f.write('\nThis is a new line '+str(i)+'\n')
    f.close()
    i+=1
