



# Read source files

read_hdl -sv -lib "cv32e40x_pkg" $cv32e40x_pkg
foreach x $VERILOG_SOURCE_LIST {
    read_hdl -sv -library "cv32e40x_pkg" $x
}

foreach x $VHDL_SOURCE_LIST {
    read_hdl -language vhdl $x
}

# Elaborate
elaborate "cv32e40x_core"



########### Defining Default I/O constraints ###################

set all_clock_ports $clock_ports

set all_other_input_ports  [remove_from_collection [all_inputs]  [get_ports [list $all_clock_ports $obi_input_ports $irq_input_ports $clic_input_ports $early_input_ports $fencei_input_ports $xif_input_ports $xif_input_ports_result_data $xif_mem_if_input_ports]]]

set all_other_output_ports [remove_from_collection [all_outputs] [get_ports [list $all_clock_ports $obi_output_ports $clic_output_ports $sleep_output_ports $fencei_output_ports $xif_output_ports $xif_output_ports_data_late $xif_output_ports_control_late $xif_mem_result_if_rdata $xif_mem_result_if_valid]]]


# IRQs
set_input_delay  $in_delay_irq          [get_ports $irq_input_ports        ] -clock clk_i
set_input_delay  $in_delay_clic         [get_ports $clic_input_ports       ] -clock clk_i
# set_output_delay $out_delay_clic        [get_ports $clic_output_ports      ] -clock clk_i # GS we do not have any output ports that have clic_irq in it

# OBI input/output delays
set_input_delay  $in_delay_instr_gnt    [ get_ports instr_gnt_i            ] -clock clk_i
set_input_delay  $in_delay_instr_rvalid [ get_ports instr_rvalid_i         ] -clock clk_i
set_input_delay  $in_delay_instr_rdata  [ get_ports instr_rdata_i*         ] -clock clk_i
set_input_delay  $in_delay_instr_err    [ get_ports instr_err_i*           ] -clock clk_i

set_input_delay  $in_delay_data_gnt     [ get_ports data_gnt_i             ] -clock clk_i
set_input_delay  $in_delay_data_rvalid  [ get_ports data_rvalid_i          ] -clock clk_i
set_input_delay  $in_delay_data_rdata   [ get_ports data_rdata_i*          ] -clock clk_i
set_input_delay  $in_delay_data_err     [ get_ports data_err_i             ] -clock clk_i
set_input_delay  $in_delay_data_exokay  [ get_ports data_exokay_i          ] -clock clk_i

set_output_delay $out_delay_instr_req      [ get_ports instr_req_o         ] -clock clk_i
set_output_delay $out_delay_instr_addr     [ get_ports instr_addr_o*       ] -clock clk_i
set_output_delay $out_delay_instr_memtype  [ get_ports instr_memtype_o*    ] -clock clk_i
set_output_delay $out_delay_instr_prot     [ get_ports instr_prot_o*       ] -clock clk_i

set_output_delay $out_delay_data_req      [ get_ports data_req_o           ] -clock clk_i
set_output_delay $out_delay_data_we       [ get_ports data_we_o            ] -clock clk_i
set_output_delay $out_delay_data_be       [ get_ports data_be_o*           ] -clock clk_i
set_output_delay $out_delay_data_addr     [ get_ports data_addr_o*         ] -clock clk_i
set_output_delay $out_delay_data_wdata    [ get_ports data_wdata_o*        ] -clock clk_i
set_output_delay $out_delay_data_atop     [ get_ports data_atop_o*         ] -clock clk_i
set_output_delay $out_delay_data_memtype  [ get_ports data_memtype_o*      ] -clock clk_i
set_output_delay $out_delay_data_prot     [ get_ports data_prot_o*         ] -clock clk_i

# Fencei handshake
set_input_delay  $in_delay_fencei       [get_ports $fencei_input_ports     ] -clock clk_i
set_output_delay $out_delay_fencei      [get_ports $fencei_output_ports    ] -clock clk_i

# X-interface
# set_input_delay  $in_delay_xif                       [get_ports $xif_input_ports                ] -clock clk_i # TODO GS it should be uncommented
# set_input_delay  $in_delay_xif_result_data           [get_ports $xif_input_ports_result_data    ] -clock clk_i
# set_input_delay  $in_delay_xif_mem_if                [get_ports $xif_mem_if_input_ports         ] -clock clk_i
# set_output_delay $out_delay_xif_mem_result_rdata     [get_ports $xif_mem_result_if_rdata        ] -clock clk_i
# set_output_delay $out_delay_xif_mem_result_valid     [get_ports $xif_mem_result_if_valid        ] -clock clk_i

# set_output_delay $out_delay_xif                [get_ports $xif_output_ports               ] -clock clk_i
# set_output_delay $out_delay_xif_data_late      [get_ports $xif_output_ports_data_late     ] -clock clk_i
# set_output_delay $out_delay_xif_control_late   [get_ports $xif_output_ports_control_late  ] -clock clk_i


# Misc
set_input_delay  $in_delay_early        [get_ports $early_input_ports      ] -clock clk_i
set_input_delay  $in_delay_other        [get_ports $all_other_input_ports  ] -clock clk_i

set_output_delay $out_delay_other       [get_ports $all_other_output_ports ] -clock clk_i
set_output_delay $out_delay_core_sleep  [ get_ports core_sleep_o           ] -clock clk_i

######################################### END

quit
