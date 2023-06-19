DESIGN_NAME=cv32e40x

clone_sim_env:
	@echo "Simulation/Verification environment is being cloned from openhwgroup github public repository"
	@cd ../ && git clone https://github.com/openhwgroup/core-v-verif.git

clone_synth_env:
	@echo "Synthesis environment is being cloned from NTNU asic-flow github private Repository"
	@cd ../ && git clone https://github.com/EECS-NTNU/asic-flow.git

sim:
	@echo "Makefile from workplace is running simulations"
	@python3 sim.py
	@echo "Running simulations analysis"
	@python3 sim_analyzer.py
	@cd ../master/cv32e40x/rtl/ && git stash && git stash drop


syn:
	@echo "Makefile from workplace is running synthesis"
	@python3 synth.py
	@echo "Running synthesis analysis"
	@python3 syn_analyzer.py
	@cd ../master/cv32e40x/rtl/ && git stash && git stash drop


reportLogs:

	@echo "Reporting simulation and synthesis logs"
	@echo ""
	@python3 show_log.py

model:
	@echo "Running Model of the core with Predictor"
	@python3 logParser.py

sim_data_analyzer:
	@echo "Running simulation data analyzer"
	@python3 sim_data_analyzer.py

syn_data_analyzer.py:
	@echo "Running synthesis data analyzer"
	@python3 syn_data_analyzer.py

clean: 

	rm -rf syn_log.txt
	rm -rf sim_log.txt
	rm -rf newUVMLogs/*

	

