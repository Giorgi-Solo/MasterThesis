DESIGN_NAME=cv32e40x

work_sim_hello_world:
	
	echo "Makefile from workplace/simulation is running work_sim_hello_world"
	cd ../../core-v-verif/cv32e40x/sim/uvmt/ && make clean_all test TEST=hello-world CV_CORE=cv32e40x USE_ISS=0 WAVES=0 CV_CORE_PATH=/home/giorgis/project/master/cv32e40x   run hello-world test
	
work_sim_coremark:
	
	echo "Makefile from workplace/simulation is running work_sim_coremark"
	cd ../../core-v-verif/cv32e40x/sim/uvmt/ && make clean_all test TEST=coremark CV_CORE=cv32e40x USE_ISS=0 WAVES=0 CV_CORE_PATH=/home/giorgis/project/master/cv32e40x   run coremark test


work_synth:
	@echo "Makefile from workplace/simulation is running work_synth"
	cd ../../asic-flow-main/stm28/cv32e40x_core/ && make clean syn
	
