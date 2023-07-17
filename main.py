import time as t
import --- as image_ai

ERROR = False

# --------------- Read Word file and load into array-------------------
word_file = open("words.txt","r")

word_bank = [] #Word bank array to query from 

for x in freq_in/interval:
    word_bank.append(word_file.readline())

word_file.close()


while 1:
    #Set small timer may be changed depends on how inputs from max live are managed 
    t.sleep(4)
    
    # take inputs from max live --- EXAMPLE CODE -------------

    freq_in = 250
    sign = 0
    interval = 10


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
