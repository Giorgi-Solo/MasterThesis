sim_log_path = "sim_log.txt"
syn_log_path = "syn_log.txt"

try:
    with open(sim_log_path, "r") as sim_log_ptr:
        for line in sim_log_ptr.readlines():
            print(line)
except:
    print("Simulation log does not exist")


try:
    with open(syn_log_path, "r") as syn_log_ptr:
        for line in syn_log_ptr.readlines():
            print(line)
except:
    print("Synthesis log does not exist")