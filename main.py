import time as t
import subprocess
import socket

def rounder_x(number, interval):
    output = 0

    if (number%interval) >= interval/2:
        output = number + (interval-(number%interval))
    else:
        output = number - (number%interval)

    return int(output)

print("Initalising...")

#initalise Variables
ERROR = False
SENT = False
max_freq_in = 10000 #Hz
interval = 500 #Hz
NUM_OF_PROMPTS = 3 #number of prompts in image
PROMPT_FRAMES = 50
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#File Definitions
Word_Prompts_PATH = "prompts.txt"
Animation_Settings_Temp_PATH = "AnimationSettings_temp.txt"
Animation_Settings_PATH = "DeforumStableDiffusionLocal/runSettings.txt"


prompts = [] #Sentences to be loaded 
Config_file = [] #Temporary loading of file to be altered 
prompt_list = [] #Loaded Prompts


# --------------- Establish UDP Connection ------------------
# sock = socket.socket(socket.AF_INET, # Internet
#                      socket.SOCK_DGRAM) # UDP
# sock.bind((UDP_IP, UDP_PORT))

# --------------- Read Word file and load into array-------------------
with open(Word_Prompts_PATH,"r") as openfileobject:
    for line in openfileobject:
        prompts.append(line.replace('\n', ''))

openfileobject.close()

#---------------- Read Config FIle for editing ------------------------
with open(Animation_Settings_Temp_PATH,"r") as openfileobject:
    for line in openfileobject:
        Config_file.append(line)

openfileobject.close()

print("Initalisation Complete")

## MAIN ##
while ERROR == False:
    #inits
    print("")
    data = -1
    SENT = False

    #Load new Data
    while SENT == False:
        data, addr = ["300","0x3425425352"]#sock.recvfrom(1024) # buffer size is 1024 bytes
        #print("received message: %s" % data)
        
        #Check if New Data Avalible
        if data != -1:
            freq_in = int(data)
            SENT = True
            print("Data Received")
        else:
            print("No Data Received")
    

    #Set small timer may be changed depends on how inputs from max live are managed 
    t.sleep(1)

    #Load new prompts
    prompt_list.append( prompts[int(rounder_x(freq_in, interval)/interval)] )

    #print(prompt_list)

    #Once ENought prompts
    if (len(prompt_list) >= NUM_OF_PROMPTS):

        #init
        FrameCounter = 0 

        #Open new file to write to
        Settings_file = open(Animation_Settings_PATH,"w") 

        #Load Data into written file till prompt inputs
        for i in range(len(Config_file)):
            if (Config_file[i] == "    prompts_ani\n"):
                print("Configuring Prompts")

                ani_prompt_line = '    "animation_prompts":{'

                for pr in range(len(prompt_list)):
                    ani_prompt_line = ani_prompt_line + '"'+ str(FrameCounter) + '"' + ':' + '"' + prompt_list[pr] +'"'

                    if(pr < len(prompt_list)-1):
                        ani_prompt_line = ani_prompt_line + ","

                    FrameCounter = FrameCounter + PROMPT_FRAMES #incremnt Frames

                ani_prompt_line = ani_prompt_line + "},\n"

                Settings_file.writelines(ani_prompt_line)
            else:
                Settings_file.writelines(Config_file[i])
            
        

        #Close File
        Settings_file.close()

        #Call AI Generation
        res = subprocess.run(["python3", "DeforumStableDiffusionLocal/run.py", "--enable_animation_mode", "--settings", "DeforumStableDiffusionLocal/runSettings.txt"], capture_output=True, text=True)
        print(res.stdout)
        print(res.stderr)
        #Clean Inputs
        prompt_list = []


