import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

path_sim_res = "Simulations/sim_results/lists"
path_syn_res = "Simulations/syn_results/lists"

# Baseline Values

baseline_cell_area  = [16704.662 for x in range(128)]
baseline_net_area   = [5874.265 for x in range(128)]
baseline_total_area = [22578.927 for x in range(128)]

baseline_total_power    = [2.70943e-04 for x in range(128)]
baseline_reg_power      = [1.15329e-04 for x in range(128)]
baseline_frac_reg_pwr   = [42.57 for x in range(128)]

# Lists for Synthesis Results

cache_size_list = []

##############################################################################################
# AREA
cell_area_list  = []
net_area_list   = []
total_area_list = []

cell_area_list_increase  = []
net_area_list_increase   = []
total_area_list_increase = []

##############################################################################################
# Power
total_power_list  = []
regis_power_list  = []
frac_reg_pwr_list = []

total_power_list_increase  = []
regis_power_list_increase  = []
frac_reg_pwr_list_increase = []

##############################################################################################
# Helper Functions
def readFile(path, type):

    with open(path, "r") as ptr:
        tmp = ptr.readlines()
        tmp.pop(0)

        if type == "int":
            file_data = [int(x) for x in tmp]
        elif type == "float":
            file_data = [float(x) for x in tmp]

        return file_data

def plotGraph(x, y, xlabel, ylabel, title, y1, y2, y3, y4, y5, label, label1, label2,
              label3, label4, label5):

    if("Increase" in title):
        pass
    else:
        plt.text(x[3], y[3], "(" + str(x[3]) + ", " + str(y[3]) + ")")
        pass
    plt.text(x[y.index(max(y))], max(y), "(" + str(x[y.index(max(y))]) + ", " + str(max(y)) + ")")
    plt.plot(x, y, label = label)

    if("Baseline" in title or "Fraction" in title):
        plt.text(-10, mean(y), str(int(mean(y))))
        plt.axhline(y=(mean(y)), color='violet', label="Average")

    if(label1 != "none"):
        if("Increase" in title):
            pass
        else:
            plt.text(x[3], y1[3], "(" + str(x[3]) + ", " + str(y1[3]) + ")")
        plt.text(x[y1.index(max(y1))], max(y1), "(" + str(x[y1.index(max(y1))]) + ", " + str(max(y1)) + ")")
        plt.plot(x, y1, label=label1)
    if (label2 != "none"):
        if ("Increase" in title):
            pass
        else:
            plt.text(x[3], y2[3], "(" + str(x[3]) + ", " + str(y2[3]) + ")")
        plt.text(x[y2.index(max(y2))], max(y2), "(" + str(x[y2.index(max(y2))]) + ", " + str(max(y2)) + ")")
        plt.plot(x, y2, label=label2)
    # if (label3 != "none"):
    #     if ("Increase" in title):
    #         pass
    #     else:
    #         plt.text(x[3], y3[3], "(" + str(x[3]) + ", " + str(y3[3]) + ")")
    #     plt.plot(x, y3, label=label3)
    # if (label4 != "none"):
    #     if ("Increase" in title):
    #         pass
    #     else:
    #         plt.text(x[3], y4[3], "(" + str(x[3]) + ", " + str(y4[3]) + ")")
    #     plt.plot(x, y4, label=label4)
    # if (label5 != "none"):
    #     if ("Increase" in title):
    #         pass
    #     else:
    #         plt.text(x[3], y5[3], "(" + str(x[3]) + ", " + str(y5[3]) + ")")
    #     plt.plot(x, y5, label=label5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


##############################################################################################
# Plot the results

path = path_sim_res + "/cache_size_list.txt"
cache_size_list = readFile(path, "int")
x = cache_size_list
xlabel = "Number of Cachelines"

#########################################################################################################
path = path_syn_res + "/cell_area_list.txt"
cell_area_list = readFile(path, "float")
#########################################################################################################

#########################################################################################################
path = path_syn_res + "/net_area_list.txt"
net_area_list = readFile(path, "float")
#########################################################################################################

#########################################################################################################
path = path_syn_res + "/total_area_list.txt"
total_area_list = readFile(path, "float")
#########################################################################################################

cell_area_list_increase  = [100*(cell_area_list[i] - baseline_cell_area[i])/baseline_cell_area[i] for i in range(128)]
net_area_list_increase   = [100*(net_area_list[i] - baseline_net_area[i])/baseline_net_area[i] for i in range(128)]
total_area_list_increase = [100*(total_area_list[i] - baseline_total_area[i])/baseline_total_area[i] for i in range(128)]

# plotGraph(x=x, y=cell_area_list, xlabel=xlabel, ylabel="Area",
#           title="Area with Respect to Cache Size",
#           y1=net_area_list, y2=total_area_list,
#           y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
#           label="Cell Area",label1="Net Area", label2="Total Area",
#           label3="none", label4="none", label5="none")

plotGraph(x=x, y=cell_area_list_increase, xlabel=xlabel, ylabel="Area (%)",
          title="Area Increase with Respect to Cache Size",
          y1=net_area_list_increase, y2=total_area_list_increase,
          y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
          label="Cell Area Increase (%)",label1="Net Area Increase (%)", label2="Total Area Increase (%)",
          label3="none", label4="none", label5="none")

plotGraph(x=x, y=cell_area_list, xlabel=xlabel, ylabel="Cell Area",
          title="Cell Area Compared to Baseline",
          y1=baseline_cell_area, y2=total_area_list,
          y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
          label="Cell Area",label1="Baseline Cell Area", label2="none",
          label3="none", label4="none", label5="none")

plotGraph(x=x, y=net_area_list, xlabel=xlabel, ylabel="Net Area",
          title="Net Area Compared to Baseline",
          y1=baseline_net_area, y2=total_area_list,
          y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
          label="Cell Area",label1="Baseline Cell Area", label2="none",
          label3="none", label4="none", label5="none")

plotGraph(x=x, y=total_area_list, xlabel=xlabel, ylabel="total Area",
          title="total Area Compared to Baseline",
          y1=baseline_total_area, y2=total_area_list,
          y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
          label="Cell Area",label1="Baseline Cell Area", label2="none",
          label3="none", label4="none", label5="none")
#########################################################################################################
path = path_syn_res + "/total_power_list.txt"
total_power_list = readFile(path, "float")
#########################################################################################################

#########################################################################################################
path = path_syn_res + "/regis_power_list.txt"
regis_power_list = readFile(path, "float")
#########################################################################################################

plotGraph(x=x, y=total_power_list, xlabel=xlabel, ylabel="Power (W)",
          title="total Power and Power Consumed by Registers",
          y1=regis_power_list, y2=total_area_list,
          y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
          label="Total Power",label1="Power Consumed by Registers", label2="none",
          label3="none", label4="none", label5="none")

#########################################################################################################
path = path_syn_res + "/frac_reg_pwr_list.txt"
frac_reg_pwr_list = readFile(path, "float")

plotGraph(x=x, y=frac_reg_pwr_list, xlabel=xlabel, ylabel="Power by Registers (%)",
          title="Fraction of total Power Consumed by Registers",
          y1=regis_power_list, y2=total_area_list,
          y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
          label="Power Consumed by Registers (%)",label1="none", label2="none",
          label3="none", label4="none", label5="none")
#########################################################################################################

total_power_list_increase  = [100*(total_power_list[i] - baseline_total_power[i])/baseline_total_power[i] for i in range(128)]
regis_power_list_increase  = [100*(regis_power_list[i] - baseline_reg_power[i])/baseline_reg_power[i] for i in range(128)]
frac_reg_pwr_list_increase = [100*(frac_reg_pwr_list[i] - baseline_frac_reg_pwr[i])/baseline_frac_reg_pwr[i] for i in range(128)]

plotGraph(x=x, y=total_power_list_increase, xlabel=xlabel, ylabel="Power Increase (%)",
          title="Increase of Consumed Power",
          y1=regis_power_list_increase, y2=frac_reg_pwr_list_increase,
          y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
          label="Total Power Increase (%)",label1="Register  Power Increase (%)", label2="Frac_Reg_Pwr  Power Increase (%)",
          label3="none", label4="none", label5="none")

# plotGraph(x=x, y=total_power_list, xlabel=xlabel, ylabel="Total Power",
#           title="Total Power Compared to Baseline",
#           y1=baseline_total_power, y2=total_area_list,
#           y3=baseline_cell_area, y4=baseline_net_area, y5=baseline_total_area,
#           label="Cell Area",label1="Baseline Total Power", label2="none",
#           label3="none", label4="none", label5="none")
print("Hello World")