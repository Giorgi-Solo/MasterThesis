import os
import shutil

path         = "../master/cv32e40x/rtl/cv32e40x_if_stage.sv" # path to cv32e40x_if_stage module
reports_path = "../asic-flow-main/stm28/cv32e40x_core/build/syn/reports"

searched_line       = "  // BTB_BHT cache signals"
line_to_change      = "  localparam int size  = 258;" # "  localparam int size  = 256;"
number_iterations   = 128 # run 127 times

mk_target = "work_synth"

simulation_folder_path = "simulations/syn_results"

error       = 0
warning     = 0
errorMsg    = ""
warningMsg  = ""

try:
    os.system("mkdir "+simulation_folder_path) # make result directory
except:
    pass

for it in range(number_iterations):
# Change BTB_BHT_Cache size
    with open(path, "r+") as file:
        line = ""
        i = 0
        while True:
            char = file.read(1)
            i += 1
            if (char == "\n"):
                if (line == searched_line):
                    # print(line)
                    # print("break")
                    break
                line = ""
            else:
                line += char

        old_size = line_to_change[-4:-1]
        size = (int(old_size) - 2)

        new_size = str(size)

       
        if size < 10:
            new_size = " " + " " + new_size
        elif size < 100:
            new_size = " " + new_size

        
        line_to_change = line_to_change.replace(old_size,new_size)

        file.seek(i,0)
        print(line_to_change)
        file.write(line_to_change)

# Run synthesis
    os.system("cd simulations && make "+mk_target) # TODO pass name of the test program as an argument 

# Extract generated reports

    dir_path = os.path.join(simulation_folder_path,"syn_"+ str(size) +"_cache_entry")
    # mk dir
    try:
        os.mkdir(dir_path)
    except:
        pass

    # # Extract files
    try:
        os.system("cp -r " + reports_path + " " + dir_path)
    except:
        error += 1
        errorMsg += "\nERROR - Synthesis failed and Cant extract reports for size " + str(size)
        pass








print("Number of warnings: " + str(warning))
print("Number of errors  : " + str(error))

if(warning != 0):
    print("WARNINGS######################### BEGIN #############")
    print(warningMsg)
    print("WARNINGS######################### END   #############")

if(error != 0):
    print("ERRORS######################### BEGIN #############")
    print(errorMsg)
    print("ERRORS######################### END   #############")


syn_log_path = "syn_log.txt"

with open(syn_log_path, "w") as syn_log_ptr:
    msgs = "SYNTHESIS LOGS\n\n"
    msgs = msgs + "Number of warnings: " + str(warning) + warningMsg + "\nNumber of errors  : " + str(error) + errorMsg
    syn_log_ptr.writelines(msgs)

