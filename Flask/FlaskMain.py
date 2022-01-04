import inspect
import os
import sys
import owlready2


current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from Flask.FlaskApp import FlaskAppWrapper
from example.controller import MachineController_FIFO2
#if not set as path variable
#owlready2.owlready2.JAVA_EXE = java path

#path to example

from ProductionSimulation.init.Initializer import Initializer;


init=Initializer(current_dir)

production_config_path="/Flask/Assets/DefaultFiles/production_config_lvl3.ini"
owl_config_path="/Flask/Assets/DefaultFiles/owl_config.ini"
controller_config_path="/Flask/Assets/DefaultFiles/controller_config.ini"
logger_config_path="/Flask/Assets/DefaultFiles/logger_config_lvl3.ini"

if( __name__ == "__main__"):

    a = FlaskAppWrapper('wrap',init,{'production':production_config_path,'owl':owl_config_path,'controller':controller_config_path,'logger':logger_config_path})
    a.addSwaggerUI()
    a.run()