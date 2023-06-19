import subprocess
import os
import shutil

path     = "../master/cv32e40x/rtl/cv32e40x_if_stage.sv" # path to cv32e40x_if_stage module
testName = "hello-world" # set this to coremark to run coremark test

mk_target = "work_sim_hello_world"

if testName == "hello-world":
    mk_target = "work_sim_hello_world"
elif testName == "coremark":
    mk_target = "work_sim_coremark"

searched_line       = "  // BTB_BHT cache signals"
line_to_change      = "  localparam int size  = 258;" # "  localparam int size  = 256;"
number_iterations   = 128 # run 127 times

simulation_folder_path = "simulations/sim_results"
btb_cache_stat_path    = "../core-v-verif/cv32e40x/sim/uvmt/vsim_results/default/"+ testName + "/0/btb_cache_statistics.txt"
uvm_test_log_path      = "../core-v-verif/cv32e40x/sim/uvmt/vsim_results/default/"+ testName + "/0/uvm_test_top.env.rvfi_agent.trn.log"

original_logPath  = "simulations" + "/Original_uvm_test_top.env.rvfi_agent.trn.log"
generated_name    = "uvm_test_top.env.rvfi_agent.trn.log"

error       = 0
warning     = 0
errorMsg    = ""
warningMsg  = ""

try:
    os.system("mkdir simulations/sim_results") # make result directory
except:
    pass

for it in range(number_iterations):
    with open(path, "r+") as file:
# Change BTB_BHT_Cache size
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

# Run Hello-Wrold simulation
    os.system("cd simulations && make "+mk_target) # TODO pass name of the test program as an argument 

# Extract generated log file and btb statistics

    dir_path = os.path.join(simulation_folder_path,"sim_"+ str(size) +"_cache_entry")
    # mk dir
    try:
        os.mkdir(dir_path)
    except:
        warning += 1
        warningMsg += "\nWARNING - Cant create dir for size " + str(size)
        pass
    # Extract btb statistics
    try:
        # print(btb_cache_stat_path)
        # print(dir_path)
        shutil.copy(btb_cache_stat_path,dir_path)
    except:
        error += 1
        errorMsg += "\nERROR - Cant extract btb statistics for size " + str(size)
        pass
    # Extract uvm log
    try:
        shutil.copy(uvm_test_log_path,dir_path)
    except:
        error += 1
        errorMsg += "\nERROR - Cant extract uvm log for size " + str(size)
        pass

# Compare extracted log with the original log

    generated_logPath = os.path.join(dir_path, generated_name)
    # check if the instruction order in original log matches the instruction order in generated log
    try:
        with open(original_logPath, "r") as original_logPath_ptr,  open(generated_logPath, "r") as generated_logPath_ptr:
            for i in range(3):
                original_line  = original_logPath_ptr.readline()
                generated_line = generated_logPath_ptr.readline()

            dash = original_line[44:54]
            dash = dash + dash + dash + dash + dash + dash + dash + dash + dash

            print(dash)
            i = 0
            num_inst_original = 0
            num_inst_generated = 0
            ans = "y"
            for original_line in original_logPath_ptr.readlines():
                generated_line = generated_logPath_ptr.readline()
                i = i + 1
                num_inst_original = num_inst_original + 1
                num_inst_generated = num_inst_generated + 1

                if(original_line[44:54] != generated_line[44:54]):
                    # print(i)
                    ans = "n" # TODO instead of printing, come up with better way to report errors
                    break

            if (ans=="n"):
                print("NOT CORRECT - order of instruction is not correct")
                print(i)
                error += 1
                errorMsg += "\n ERROR - order of instruction is not correct for size " + str(size) + " at instr " + str(i)
            else:
                print("CORRECT  - order of instruction is correct")

            print(dash)
            for original_line in original_logPath_ptr.readlines():
                num_inst_original = num_inst_original+1
            for generated_line in generated_logPath_ptr.readlines():
                num_inst_generated = num_inst_generated + 1

            if num_inst_original==num_inst_generated:
                print("CORRECT - number of instructions match")
            else:
                print("INCORRECT  - number of instructions do not match")
                print("original "+str(num_inst_original))
                print("generated "+str(num_inst_generated))
                error += 1
                errorMsg += "\n ERROR - number of instructions do not match for size " + str(size)
            print(dash)
    except:
        warning += 1
        warningMsg += "\n WARNING - cant compare for size " + str(size)
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

sim_log_path = "sim_log.txt"

with open(sim_log_path, "w") as sim_log_ptr:
    msgs = "SIMULATION LOGS \n\n"
    msgs = msgs + "Number of warnings: " + str(warning) + warningMsg + "\nNumber of errors  : " + str(error) + errorMsg
    sim_log_ptr.writelines(msgs)
