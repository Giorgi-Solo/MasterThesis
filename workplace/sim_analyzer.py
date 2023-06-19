import os

# Paths
simulation_folder_path = "simulations/sim_results"
first_cache_size       = 2
sim_result_path        = "sim_"+ str(first_cache_size) +"_cache_entry"
btb_stat_name          = "btb_cache_statistics.txt"
uvm_log_name           = "uvm_test_top.env.rvfi_agent.trn.log"

lists_path = simulation_folder_path + "/lists/"

# variables
num_bits_cach_entry = 66

num_instr           = 9929
num_cycles_original = 21377

CPI_original        = num_cycles_original/num_instr

num_iteration       = 128 # 128

# lists
num_cycles_list               = ["num_cycles_list              "]
CPI_list                      = ["CPI_list                     "]

cache_size_list               = ["cache_size_list              "]
num_valid_entries_list        = ["num_valid_entries_list       "] 

num_branch_instr_list         = ["num_branch_instr_list        "]
num_predictions_list          = ["num_predictions_list         "]

num_corr_predictions_list     = ["num_corr_predictions_list    "]
num_incorr_inpredictions_list = ["num_incorr_inpredictions_list"]

fract_used_cache_list         = ["fract_used_cache_list        "] # num_valid_entries_list/cache_size_list in %
fract_unused_cache_list       = ["fract_unused_cache_list      "] # 100 - num_valid_entries_list/cache_size_list in %

fract_predicted_branch_list   = ["fract_predicted_branch_list  "] # num_predictions_list/num_branch_instr_list

fract_corr_predictions_list   = ["fract_corr_predictions_list  "] # num_corr_predictions_list/num_predictions_list
fract_incorr_predictions_list = ["fract_incorr_predictions_list"] # num_incorr_inpredictions_list/num_predictions_list

CPI_improvement_list          = ["CPI_improvement_list         "]

lists = ["num_cycles_list", "CPI_list", "cache_size_list", "num_valid_entries_list", "num_branch_instr_list", 
         "num_predictions_list", "num_corr_predictions_list", "num_incorr_inpredictions_list",
         "fract_used_cache_list", "fract_unused_cache_list", "fract_predicted_branch_list",
         "fract_corr_predictions_list", "fract_incorr_predictions_list", "CPI_improvement_list"]

try:
    os.system("mkdir simulations/sim_results/lists")
except:
    pass

def print_lists():
    print(cache_size_list)
    print(num_valid_entries_list)
    print(num_branch_instr_list)
    print(num_predictions_list)
    print(num_corr_predictions_list)
    print(num_incorr_inpredictions_list)
    print(num_cycles_list)
    print(CPI_list)

def extract_information():
    cache_size = first_cache_size
    for it in range(num_iteration):
        # print(cache_size)
        path_dir       = os.path.join(simulation_folder_path,"sim_"+ str(cache_size) +"_cache_entry")
        path_stats     = os.path.join(path_dir,btb_stat_name)
        path_uvm_logs  = os.path.join(path_dir,uvm_log_name)

        with open(path_stats, "r") as stats_ptr, open(path_uvm_logs,"r") as uvm_log_ptr:
            # Extract information from btb_statistics
            lines = stats_ptr.readlines()

            # Exctract cahce size 
            line = lines[0]
            cache_size_entry = line[line.index("= ") + 2 : len(line)]
            cache_size_entry = cache_size_entry[0 : cache_size_entry.index(" ")]

            cache_size_list.append(int(cache_size_entry))

            # Exctract number of valid entries
            line = lines[2]
            num_valid_entries_entry = line[line.index("= ") + 2 : len(line)]
            num_valid_entries_entry = num_valid_entries_entry[0 : num_valid_entries_entry.index(" ")]

            num_valid_entries_list.append(int(num_valid_entries_entry))

            # Exctract number of branch instrs
            line = lines[3]
            num_branch_instr_entry = line[line.index("= ") + 2 : len(line)]

            num_branch_instr_list.append(int(num_branch_instr_entry))

            # Exctract number of predictions
            line = lines[4]
            num_predictions_entry = line[line.index("= ") + 2 : len(line)]

            num_predictions_list.append(int(num_predictions_entry))   

            # Extract number of correct predictions   
            line = lines[5]  
            num_corr_predictions_entry = line[line.index("= ") + 2 : len(line)]

            num_corr_predictions_list.append(int(num_corr_predictions_entry))

            # Extract number of incorrect inpredictions
            line = lines[6]
            num_incorr_inpredictions_entry = line[line.index("= ") + 2 : len(line)]

            num_incorr_inpredictions_list.append(int(num_incorr_inpredictions_entry))
            
            # Exctract information from uvm log
            uvm_log_lines = uvm_log_ptr.readlines()
            
            cycle_str_indx = uvm_log_lines[1].index("    CYCLE |  ORDER |")
            cycle_end_indx = uvm_log_lines[1].index("|  ORDER |")

            order_str_indx = uvm_log_lines[1].index("  ORDER |")
            order_end_indx = uvm_log_lines[1].index("|       PC ")

            num_cycles_entry = uvm_log_lines[-1][cycle_str_indx:cycle_end_indx]
            num_cycles_list.append(int(num_cycles_entry))


        cache_size += 2

    # Calculate CPIs
    tmp_list = num_cycles_list[1 : len(num_cycles_list)]
    for x in tmp_list:
        
        entry = x/num_instr
        CPI_list.append(entry)
    
    for i in range(len(cache_size_list)):
        if i == 0:
            continue
        else:
            fract_used_cache_list.append(100 * num_valid_entries_list[i]/cache_size_list[i])
            fract_unused_cache_list.append(100 - fract_used_cache_list[i])
            fract_predicted_branch_list.append(100 * num_predictions_list[i]/num_branch_instr_list[i])
            fract_corr_predictions_list.append(100 * num_corr_predictions_list[i]/num_predictions_list[i])
            fract_incorr_predictions_list.append(100 - fract_corr_predictions_list[i])

            CPI         = float(CPI_list[i])
            improvement = 100 * (CPI_original - CPI)/CPI_original
            CPI_improvement_list.append(improvement)

    # Save lists to lists.txt
    with open(lists_path+"lists.txt", "w") as lists_path_ptr:
        lists_path_ptr.writelines(str(num_cycles_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(CPI_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(cache_size_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(num_valid_entries_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(num_branch_instr_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(num_predictions_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(num_corr_predictions_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(num_incorr_inpredictions_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(fract_used_cache_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(fract_unused_cache_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(fract_predicted_branch_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(fract_corr_predictions_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(fract_incorr_predictions_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(CPI_improvement_list))
        lists_path_ptr.writelines("\n")
       
    for a_list in lists:
        with open(lists_path+a_list+".txt", "w") as list_path_ptr:
            if(a_list=="num_cycles_list"):
                for entry in num_cycles_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="fract_incorr_predictions_list"):
                for entry in fract_incorr_predictions_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="fract_corr_predictions_list"):
                for entry in fract_corr_predictions_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="fract_predicted_branch_list"):
                for entry in fract_predicted_branch_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="fract_unused_cache_list"):
                for entry in fract_unused_cache_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="fract_used_cache_list"):
                for entry in fract_used_cache_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="num_incorr_inpredictions_list"):
                for entry in num_incorr_inpredictions_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="num_corr_predictions_list"):
                for entry in num_corr_predictions_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="num_predictions_list"):
                for entry in num_predictions_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="num_branch_instr_list"):
                for entry in num_branch_instr_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="num_valid_entries_list"):
                for entry in num_valid_entries_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="cache_size_list"):
                for entry in cache_size_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="CPI_list"):
                for entry in CPI_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="CPI_improvement_list"):
                for entry in CPI_improvement_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            

    return cache_size

extract_information()
# print_lists()

