# project-group-2
project-group-2 created by GitHub Classroom

For this project, we create a directory docs which includes a python package sir, a scripts directory, and a test directory for sir package.

The scripts directory includes the scripts for running basic, spatial agent-based, ODE simulation and three variations. The scripts.py is used for running the basic ode and agent-based simulation model. The improveagentscript.py is used for running the spatial agent-based model, and the pdesimulation.py is used for running spatial pde model. The map.py, time_series_plot.py, mask.py,covidsir.py are used for all three variations. Apart from the python files, we also include the required html files for interactive visualization in scripts directory. All these files will be regenerated as we run the github action. Thus, we just put all the files in scripts directory.

The sir package includes ode.py, odemask.py, improveagent.py, agent.py, pde.py. The __init__.py is used for claiming that sir is a package. We import other files in __init__.py so that we can import sir in test directory. The ode.py is used for basic continuous ode generation model and the variation for fitting the Covid-19 data with sir model. The agent.py is used for basic agent-based sir model. The improveagent.py is used for spatial agent-based sir model. The pde.py is used for spatial pde model. The odemask.py is used for for mask variation.

The test package include test.py, testimproveagent.py, and testpde.py. The test.py is used for testing functions in sir.agent; the testimproveagent.py is used for testing functions in sir.improveagent; the testpde.py is used for testing functions in sir.pde.

To run the scripts, you may change to the scripts directory and run scripts. To be specific, "cd scripts/" and "python improveagentscript.py".

To test the files, you may change to the test directory and test files. For instance, "cd test/" and "pytest test.py".

For the midterm checkpoint, we have midtermreport.pdf as well its latex version included in the doc directory.
For the final checkpoint, we have finalreport.pdf with its latex version included in the doc directory.
All the visualization html files are included in scripts directory.
