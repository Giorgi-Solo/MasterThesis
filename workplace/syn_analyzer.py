import os

# Paths
simulation_folder_path = "simulations/syn_results"
first_cache_size       = 2
sim_result_path        = "syn_"+ str(first_cache_size) +"_cache_entry"

area_reprt_name        = "reports/area.txt"
power_reprt_name       = "reports/power.txt"
timing_reprt_name      = "reports/timing.txt"


lists_path = simulation_folder_path + "/lists/"

# variables

num_iteration = 128 # 128

# lists     
## Area lists
cell_count_list  = ["cell_count_list  "]
cell_area_list   = ["cell_area_list   "]
net_area_list    = ["net_area_list    "]
total_area_list  = ["total_area_list  "] 
total_power_list = ["total_power_list "]
regis_power_list = ["regis_power_list "]
frac_reg_pwr_list= ["frac_reg_pwr_list"] 
slack_list       = ["slack_list       "]


lists = ["cell_count_list", "cell_area_list", "net_area_list", "total_area_list",
         "total_power_list", "regis_power_list","frac_reg_pwr_list", "slack_list"]

try:
    os.system("mkdir simulations/syn_results/lists")
except:
    pass

def print_lists():
    print(cell_count_list)
    print(cell_area_list)
    print(net_area_list)
    print(total_area_list)
    print(total_power_list)
    print(regis_power_list)
    print(frac_reg_pwr_list)
    print(slack_list)

def extract_information():
    cache_size = first_cache_size
    num_neg_slack = 0
    for it in range(num_iteration):
        # print(cache_size)
        path_dir       = os.path.join(simulation_folder_path,"syn_"+ str(cache_size) +"_cache_entry")
        path_area      = os.path.join(path_dir,area_reprt_name)
        path_power     = os.path.join(path_dir,power_reprt_name)
        path_timing    = os.path.join(path_dir,timing_reprt_name)

        with open(path_area, "r") as area_ptr, open(path_power,"r") as power_ptr, open(path_timing, "r") as timing_ptr:
        # Extract information from area.txt
            lines = area_ptr.readlines()
            indx = 0
            for line in lines:
                indx += 1
                if "Total Area" in line:
                    indx += 1
                    break

            line = ""
            line = lines[indx]

            area_data_list = []
            
            line = line[line.index("core") + 4 : len(line)] 
            
            for _ in range(4):
                i = 0
                char = ""
                for char in line:
                    if(char != " "):
                        break
                    i += 1
                line = line[i : len(line)]
                indx = line.index(" ")
                area_data_entry = line[0:indx]
                area_data_list.append(float(area_data_entry))

                line = line[line.index(area_data_entry)+len(area_data_entry):len(line)]

            # Exctract Cell Count
            cell_count_list.append(area_data_list[0])
            # Exctract Cell Area
            cell_area_list.append(area_data_list[1])
            # Exctract Net Area
            net_area_list.append(area_data_list[2])
            # Exctract Total Area
            total_area_list.append(area_data_list[3])
            
        # Extract information from power.txt
            lines = []
            lines = power_ptr.readlines()

            rep_power_line  = ""
            tot_power_line  = ""
            prct_power_line = ""
            for line in lines:
                if "register" in line:
                    rep_power_line = line
                if "Subtotal" in line:
                    tot_power_line = line
                if "Percentage" in line:
                    prct_power_line = line
                    break
            
            # Extract total_power_list
            line = tot_power_line
            i = -1
            for _ in range(len(line)):
                if " " == line[i]:
                    break
                
                i -= 1
                                    # len(line)+i == i
            line = line[0: len(line)+i]

            i = -1
            for _ in range(len(line)):
                if "." == line[i]:
                    i -= 1
                    break
                
                i -= 1
            total_power_entry = line[len(line)+i:len(line)]
            total_power_list.append(float(total_power_entry))

            # Extract regis_power_list
            line = rep_power_line
            i = -1
            for _ in range(len(line)):
                if " " == line[i]:
                    break
                i -= 1
            end_indx = i

            line = line[0:end_indx]
            i = -1
            for _ in range(len(line)):
                if "." == line[i]:
                    break
                i -= 1
            str_indx = i-1

            regis_power_entry = line[str_indx : -1] 
            regis_power_list.append(float(regis_power_entry))

            # Extract frac_reg_pwr_list
            frac_reg_pwr_entry = 100 * float(regis_power_entry)/float(total_power_entry)
            frac_reg_pwr_list.append(frac_reg_pwr_entry)
        
        # Extract informaiton from timing.txt

            # Extract slack_list
            lines = []
            lines = timing_ptr.readlines()

            # neg_slack 
            for line in lines:
                if "Path 1:" in line:
                    break
            
            if "MET" in line:
                line = line[line.index("MET")+len("MET")+2: len(line)]
            else:
                line = line[line.index("VIOLATED")+len("MET")+2: len(line)]
                num_neg_slack += 1
            
            slack_list_entry = line[0:line.index(" ")]
            slack_list.append(float(slack_list_entry))
            
            

            


        cache_size += 2


    # Save lists to lists.txt     
    with open(lists_path+"lists.txt", "w") as lists_path_ptr:
        lists_path_ptr.writelines(str(cell_count_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(cell_area_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(net_area_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(total_area_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(total_power_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(regis_power_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(frac_reg_pwr_list))
        lists_path_ptr.writelines("\n")
        lists_path_ptr.writelines(str(slack_list))
        lists_path_ptr.writelines("\n")
       
    for a_list in lists:
        with open(lists_path+a_list+".txt", "w") as list_path_ptr:
            if(a_list=="cell_count_list"):
                for entry in cell_count_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="cell_area_list"):
                for entry in cell_area_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="net_area_list"):
                for entry in net_area_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="total_area_list"):
                for entry in total_area_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="total_power_list"):
                for entry in total_power_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="regis_power_list"):
                for entry in regis_power_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="frac_reg_pwr_list"):
                for entry in frac_reg_pwr_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            elif(a_list=="slack_list"):
                for entry in slack_list:
                    list_path_ptr.writelines(str(entry)+"\n")
            
    print("Number of timing violating cases: " + str(num_neg_slack) + "\n")
    return cache_size

extract_information()
# print_lists()

