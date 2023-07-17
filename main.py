import time as t
import serial
import --- as image_ai

ERROR = False
max_freq_in = 130
interval = 10

neg_list = []
pos_list = []

arduino = serial.Serial(port='COM1', baudrate=115200, timeout=.1)

# --------------- Read Word file and load into array-------------------
word_file = open("words.txt","r")

word_bank = [] #Word bank array to query from 

for x in max_freq_in/interval:
    word_bank.append(word_file.readline())

word_file.close()


while 1:
    #Set small timer may be changed depends on how inputs from max live are managed 
    t.sleep(4)
    
    # take inputs from max live --- EXAMPLE CODE -------------

    def write_read():
        data = arduino.readline()
        return data

    freq_in = write_read()
    

    #-------------- Set arrays -------------------

    in_word = word_bank[(freq_in/interval)]

    if sign == 0:
        neg_list.append(in_word)
    elif pos == 1:
        pos_list.append(in_word)
    else:
        print("ERROR -- Failed to determine sign")
        ERROR = True
        break

    # ------------ Send to AI -----------------

    image_ai(pos_list, neg_list)


    #Refreshing image checker --- Set at 12 words maximum

    if (len(neg_list) + len(pos_list)) >= 12:
        neg_list = []
        pos_list = []

