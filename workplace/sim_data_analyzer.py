
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

path_sim_res = "Simulations/sim_results/lists"
path_syn_res = "Simulations/syn_results/lists"

original_IPC        = 0.46

# Baseline Measures
baseline_IPC = [original_IPC for x in range(128)]
baseline_cycles = [21377 for x in range(128)]
num_bits_cache_line = 66

# lists for simulation
cache_size_list = []

##############################################################################################
#IPC
num_cycles_list      = []
IPC_list             = []
IPC_improvement_list = []

##############################################################################################
# Statistics about Cache usage
num_valid_entries_list  = []
fract_used_cache_list   = []
fract_unused_cache_list = []

##############################################################################################
# number of branches - maybe not needed
num_branch_instr_list = []

##############################################################################################
# statistics about number of predictions
num_predictions_list        = []
fract_predicted_branch_list = []

##############################################################################################
# statistics about correct predictions
num_corr_predictions_list   = []
fract_corr_predictions_list = []

##############################################################################################
# statistics about correct predictions
num_incorr_inpredictions_list = []
fract_incorr_predictions_list = []

def readFile(path, type):
    with open(path, "r") as ptr:
        tmp = ptr.readlines()
        tmp.pop(0)

        if type == "int":
            file_data = [int(x) for x in tmp]
        elif type == "float":
            file_data = [float(x) for x in tmp]

        return file_data

def plotGraph(x, y, xlabel, ylabel, title, y1, label, label1):
    # print(x)
    plt.text(x[3],y[3], "("+str(x[3]) + ", "+str(y[3])+")")
    plt.text(x[-1], y[-1], "(" + str(x[-1]) + ", " + str(y[-1]) + ")")
    if("IPC" in ylabel):
        plt.text(x[y.index(min(y))], min(y), "(" + str(x[y.index(min(y))]) + ", " + str(min(y)) + ")")
    if ("Cycles" in ylabel):
        plt.text(x[y.index(max(y))], max(y), "(" + str(x[y.index(max(y))]) + ", " + str(max(y)) + ")")
    plt.plot(x, y, label = label)

    average = str(mean(y))
    average = average[0:average.index(".")]+average[average.index("."):average.index(".")+3]
    plt.text(-10, mean(y), average)
    plt.axhline(y=(mean(y)), color='violet', label="Average")

    if(label1 != "none"):
        plt.text(x[3], y1[3], "(" + str(x[3]) + ", " + str(y1[3]) + ")")
        plt.text(x[-1], y1[-1], "(" + str(x[-1]) + ", " + str(y1[-1]) + ")")
        plt.plot(x, y1, label=label1)

        average = str(mean(y1))
        try:
            average = average[0:average.index(".")] + average[average.index("."):average.index(".") + 3]
        except:
            pass
        if("Used" in ylabel or "correct/incorrect" in ylabel):
            plt.text(-10, mean(y1), average)
            plt.axhline(y=(mean(y1)), color='violet', label="Average")

    plt.axvline(x=8, color='y', label='Cache Size is 8')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

path = path_sim_res + "/cache_size_list.txt"
cache_size_list = readFile(path, "int")
x = cache_size_list
xlabel = "Number of Cachelines"

#########################################################################################################
path = path_sim_res + "/num_cycles_list.txt"
num_cycles_list = readFile(path, "int")

plotGraph(x=x, y=num_cycles_list, xlabel=xlabel, ylabel="Number of Cycles",
          title="Number of Clk Cycles Required for Test Program Execution",
          y1=baseline_cycles, label="Cycles for Core with Predictor",label1="none")
plotGraph(x=x, y=num_cycles_list, xlabel=xlabel, ylabel="Number of Cycles",
          title="Number of Clk Cycles Required for Test Program Execution",
          y1=baseline_cycles, label="Number of Cycles",label1="Baseline Number of Cycles")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/CPI_list.txt"
IPC_list = [1/x for x in readFile(path, "float")]

plotGraph(x=x, y=IPC_list, xlabel=xlabel, ylabel="IPC",
          title="Instruction Per Clock Cycle (IPC)",
          y1=baseline_IPC, label="IPC of Core with Predictor",label1="none")
plotGraph(x=x, y=IPC_list, xlabel=xlabel, ylabel="IPC",
          title="Instruction Per Clock Cycle (IPC)",
          y1=baseline_IPC, label="IPC of Core with Predictor",label1="Baseline IPC")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/CPI_improvement_list.txt" # TODO do it on your own
IPC_improvement_list = [(x-original_IPC)*100/original_IPC for x in IPC_list]

plotGraph(x=x, y=IPC_improvement_list, xlabel=xlabel, ylabel="IPC Increase (%)",
          title="IPC Increase",
          y1=baseline_IPC, label="IPC vs Cache Size",label1="none")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/num_valid_entries_list.txt"
num_valid_entries_list = readFile(path, "int")

plotGraph(x=x, y=num_valid_entries_list, xlabel=xlabel, ylabel="Number of Valid Entries in Cache",
          title="Cache Usage",
          y1=baseline_IPC, label="Valid Entries vs Cache Size",label1="none")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/fract_used_cache_list.txt"
fract_used_cache_list = readFile(path, "float")

path = path_sim_res + "/fract_unused_cache_list.txt"
fract_unused_cache_list = readFile(path, "float")

plotGraph(x=x, y=fract_used_cache_list, xlabel=xlabel, ylabel="Used Cachelines (%)",
          title="Cache Usage in %",
          y1=fract_unused_cache_list, label="Used Cache (%)",label1="Unused Cache (%)")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/num_branch_instr_list.txt"
num_branch_instr_list = readFile(path, "int")

plotGraph(x=x, y=num_branch_instr_list, xlabel=xlabel, ylabel="Number of Branch Instructions",
          title="Number of Branches",
          y1=fract_unused_cache_list, label="NUmber of Branch vs Cache Size",label1="none")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/num_predictions_list.txt"
num_predictions_list = readFile(path, "int")

plotGraph(x=x, y=num_predictions_list, xlabel=xlabel, ylabel="Number of Predictions",
          title="Number of Predictions",
          y1=fract_unused_cache_list, label="NUmber of Predictions vs Cache Size",label1="none")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/fract_predicted_branch_list.txt"
fract_predicted_branch_list = readFile(path, "float")

plotGraph(x=x, y=fract_predicted_branch_list, xlabel=xlabel, ylabel="Number of Predictions (%)",
          title="Number of Predictions",
          y1=fract_unused_cache_list, label="NUmber of Predictions (%) vs Cache Size",label1="none")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/num_corr_predictions_list.txt"
num_corr_predictions_list = readFile(path, "int")

path = path_sim_res + "/num_incorr_inpredictions_list.txt"
num_incorr_inpredictions_list = readFile(path, "int")

plotGraph(x=x, y=num_corr_predictions_list, xlabel=xlabel, ylabel="Number of correct/incorrect Predictions",
          title="Number of Predictions",
          y1=num_incorr_inpredictions_list, label="Number of Correct Predictions",label1="Number of Incorrect Predictions")
#########################################################################################################

#########################################################################################################
path = path_sim_res + "/fract_corr_predictions_list.txt"
fract_corr_predictions_list = readFile(path, "float")

path = path_sim_res + "/fract_incorr_predictions_list.txt"
fract_incorr_predictions_list = readFile(path, "float")

plotGraph(x=x, y=fract_corr_predictions_list, xlabel=xlabel, ylabel="Number of correct/incorrect Predictions (%)",
          title="Number of Predictions",
          y1=fract_incorr_predictions_list, label="Number of Correct Predictions (%)",label1="Number of Incorrect Predictions (%)")
#########################################################################################################



























print("Hello World")