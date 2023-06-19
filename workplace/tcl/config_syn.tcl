
set PATH_cv32e40x_pkg "../../../../../master/cv32e40x/rtl/include/cv32e40x_pkg.sv"
set PATH_cv32e40x_RTL "../../../../../master/cv32e40x/rtl";

# Files
# set VERILOG_SOURCE_LIST { "../../src/top.sv" }
set cv32e40x_pkg $PATH_cv32e40x_pkg
set VERILOG_SOURCE_LIST [glob -directory $PATH_cv32e40x_RTL *.sv]

set VHDL_SOURCE_LIST { }

# Timing (ns) MODIFIED BY GIORGI SOLOMNISHVILI ########### BEGIN #####

# 200MHz
set clock_period 5.0

# Input delays for interrupts
set in_delay_irq          [expr $clock_period * 0.50]

# Delay for CLIC
# todo: set final constraints for CLIC signals
set in_delay_clic         [expr $clock_period * 0.50]
set out_delay_clic        [expr $clock_period * 0.50]

# Input delays for early signals

set in_delay_early [expr $clock_period * 0.10] 

# Input delay for fencei handshake
set in_delay_fencei       [expr $clock_period * 0.80]
# Output delay for fencei handshake
set out_delay_fencei      [expr $clock_period * 0.60]

# OBI inputs delays
set in_delay_instr_gnt    [expr $clock_period * 0.35]
set in_delay_instr_rvalid [expr $clock_period * 0.40]
set in_delay_instr_rdata  [expr $clock_period * 0.40]
set in_delay_instr_err    [expr $clock_period * 0.40]

set in_delay_data_gnt     [expr $clock_period * 0.35]
set in_delay_data_rvalid  [expr $clock_period * 0.40] 
set in_delay_data_rdata   [expr $clock_period * 0.35]
set in_delay_data_err     [expr $clock_period * 0.40]
set in_delay_data_exokay  [expr $clock_period * 0.40]

# OBI outputs delays
set out_delay_instr_req     [expr $clock_period * 0.30]
set out_delay_instr_addr    [expr $clock_period * 0.30]
set out_delay_instr_memtype [expr $clock_period * 0.30]
set out_delay_instr_prot    [expr $clock_period * 0.30]

set out_delay_data_req     [expr $clock_period * 0.30]
set out_delay_data_we      [expr $clock_period * 0.30]
set out_delay_data_be      [expr $clock_period * 0.30]
set out_delay_data_addr    [expr $clock_period * 0.30]
set out_delay_data_wdata   [expr $clock_period * 0.30]
set out_delay_data_atop    [expr $clock_period * 0.30]
set out_delay_data_memtype [expr $clock_period * 0.30]
set out_delay_data_prot    [expr $clock_period * 0.30]

# FOR SLOW OBI

# # OBI inputs delays
# set in_delay_instr_gnt    [expr $clock_period * 0.70]
# set in_delay_instr_rvalid [expr $clock_period * 0.80]
# set in_delay_instr_rdata  [expr $clock_period * 0.80]
# set in_delay_instr_err    [expr $clock_period * 0.80]

# set in_delay_data_gnt     [expr $clock_period * 0.70]
# set in_delay_data_rvalid  [expr $clock_period * 0.80]
# set in_delay_data_rdata   [expr $clock_period * 0.70]
# set in_delay_data_err     [expr $clock_period * 0.80]
# set in_delay_data_exokay  [expr $clock_period * 0.80]

# # OBI outputs delays
# set out_delay_instr_req     [expr $clock_period * 0.60]
# set out_delay_instr_addr    [expr $clock_period * 0.60]
# set out_delay_instr_memtype [expr $clock_period * 0.60]
# set out_delay_instr_prot    [expr $clock_period * 0.60]

# set out_delay_data_req     [expr $clock_period * 0.60]
# set out_delay_data_we      [expr $clock_period * 0.60]
# set out_delay_data_be      [expr $clock_period * 0.60]
# set out_delay_data_addr    [expr $clock_period * 0.60]
# set out_delay_data_wdata   [expr $clock_period * 0.60]
# set out_delay_data_atop    [expr $clock_period * 0.60]
# set out_delay_data_memtype [expr $clock_period * 0.60]
# set out_delay_data_prot    [expr $clock_period * 0.60]
# # END FOR SLOW OBI

# I/O delays for non RISC-V Bus Interface ports
set in_delay_other       [expr $clock_period * 0.10]
set out_delay_other      [expr $clock_period * 0.60]

# core_sleep_o output delay
set out_delay_core_sleep [expr $clock_period * 0.25]

# X-interface input delay
set in_delay_xif [expr $clock_period * 0.80]

# X-interface result data input delay
set in_delay_xif_result_data [expr $clock_period * 0.75]

# X-interface output delay
set out_delay_xif [expr $clock_period * 0.80]

# X-interface late data output delay
set out_delay_xif_data_late [expr $clock_period * 0.15]

# X-interface late control output delay
set out_delay_xif_control_late [expr $clock_period * 0.13]

# X-interface mem_if input delay
set in_delay_xif_mem_if [expr $clock_period * 0.30]

# X-interface mem_result.rdata output delay
set out_delay_xif_mem_result_rdata [expr $clock_period * 0.20]

# X-interface mem_result.result_valid output delay
set out_delay_xif_mem_result_valid [expr $clock_period * 0.15]

# All clocks
set clock_ports [list \
    clk_i \
]

# IRQ Input ports
set irq_input_ports [list \
    irq_i* \
]

# CLIC Input ports
set clic_input_ports [list \
    clic_irq*_i* \
]
# CLIC Output ports
set clic_output_ports [list \
    clic_irq*_o* \
]

# Early Input ports (ideally from register)
set early_input_ports [list \
    debug_req_i \
    boot_addr_i* \
    mtvec_addr_i* \
    dm_halt_addr_i* \
    mhartid_i* \
    mimpid_i* \
    dm_exception_addr_i* \
]

# RISC-V OBI Input ports
set obi_input_ports [list \
    instr_gnt_i \
    instr_rvalid_i \
    instr_rdata_i* \
    instr_err_i \
    data_gnt_i \
    data_rvalid_i \
    data_rdata_i* \
    data_err_i \
    data_exokay_i \
]

# RISC-V OBI Output ports
set obi_output_ports [list \
    instr_req_o \
    instr_addr_o* \
    instr_memtype_o* \
    instr_prot_o* \
    instr_dbg_o \
    data_req_o \
    data_we_o \
    data_be_o* \
    data_addr_o* \
    data_wdata_o* \
    data_atop_o* \
    data_memtype_o* \
    data_prot_o* \
    data_dbg_o \
]

# RISC-V Sleep Output ports
set sleep_output_ports [list \
    core_sleep_o \
]

# Fencei handshake output ports
set fencei_output_ports [list \
    fencei_flush_req_o \
]

# Fencei handshake input ports
set fencei_input_ports [list \
    fencei_flush_ack_i \
]

# X-interface input ports
set xif_input_ports [list \
    xif_compressed_if_compressed_ready \
    xif_compressed_if_compressed_resp* \
    xif_issue_if_issue_ready \
    xif_issue_if_issue_resp* \
    xif_mem_if_mem_valid \
    xif_mem_if_mem_req* \
    xif_result_if_result* \
]

# X-interface output ports
set xif_output_ports [list \
    xif_compressed_if_compressed_valid \
    xif_compressed_if_compressed_req* \
    xif_issue_if_issue_req_instr* \
    xif_issue_if_issue_req_mode* \
    xif_issue_if_issue_req_id* \
    xif_commit_if_commit* \
    xif_mem_if_mem_ready \
    xif_mem_if_mem_resp* \
    xif_mem_result_if_mem_result_valid \
    xif_mem_result_if_mem_result* \
    xif_result_if_result_ready \
]

# X-interface late data outputs
set xif_output_ports_data_late [list \
    xif_issue_if_issue_req_rs* \
    xif_issue_if_issue_req_ecs* \
]

set xif_output_ports_control_late [list \
    xif_issue_if_issue_req_rs_valid* \
    xif_issue_if_issue_req_ecs_valid* \
    xif_issue_if_issue_valid \
    xif_commit_if_commit_valid \
]

# X-interface result data inputs
set xif_input_ports_result_data [list \
    xif_result_if_result_data* \
    xif_result_if_result_valid \
]

# X-interface mem_if input ports
set xif_mem_if_input_ports [list \
    xif_mem_if_mem_valid \
    xif_mem_if_mem_req* \
]

# X-interface mem_result rdata output ports
set xif_mem_result_if_rdata [list \
    xif_mem_result_if_mem_result_rdata* \
]

# X-interface mem_result rdata output ports
set xif_mem_result_if_valid [list \
    xif_mem_result_if_mem_result_valid \
]

######################MODIFIED BY GIORGI SOLOMNISHVILI ### EDN ###

