import time as t
import serial
import subprocess

def rounder_x(number, interval):
    output = 0

    if (number%interval) >= interval/2:
        output = number + (interval-(number%interval))
    else:
        output = number - (number%interval)

    return output


ERROR = False
max_freq_in = 10000
interval = 500

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
    def write_data():
        data = arduino.readline()
        data = data.decode()
        data = data.rstrip("\r\n")
        data = data.split(" ")
        return data
    
    print(write_data())

    freq_in = write_data()[0]
    sign = write_data()[1]

    #-------------- Set arrays -------------------


    in_word = word_bank[(rounder_x(freq_in, interval)/interval)]

    if sign == 0:
        neg_list.append(in_word)
    elif sign == 1:
        pos_list.append(in_word)
    else:
        print("ERROR -- Failed to determine sign")
        ERROR = True
        break

    # ------------ Send to AI -----------------
    prompt = "a phtograph containing" + pos_list + "but not " + neg_list

    subprocess.call("python", "scripts/txt2img.py", "--prompt ", prompt, "--plms " )


    #Refreshing image checker --- Set at 12 words maximum

    if (len(neg_list) + len(pos_list)) >= 12:
        neg_list = []
        pos_list = []
