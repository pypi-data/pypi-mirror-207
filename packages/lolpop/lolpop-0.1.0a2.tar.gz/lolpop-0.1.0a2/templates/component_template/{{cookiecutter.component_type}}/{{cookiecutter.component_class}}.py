from .base_{{cookiecutter.component_type}} import Base{{cookiecutter.ComponentType}}
from lolpop.utils import common_utils as utils
#import your libraries here

@utils.decorate_all_methods([utils.error_handler, utils.log_execution()])
class {{cookiecutter.ComponentClass}}(Base{{cookiecutter.ComponentType}}):
    #Override required or default configurations here for your class
    ##Add required configuration here
    #__REQUIRED_CONF__ = {
    #    "config": []
    #}
    ##Add default configuration here
    #__DEFAULT_CONF__ = {
    #    "config": {}
    #}

    def __init__(self, conf, pipeline_conf, runner_conf, **kwargs):
        #set normal config
        super().__init__(conf, pipeline_conf, runner_conf, **kwargs)
        #Add any additional class initialization code here.

    # Write your functions here. Implement Base class functions and actually write them! 
    def my_function(self, required_arg1, required_arg2, *args, **kwargs):
        #Your code goes here!
        pass

    def my_other_function(self, required_arg1, required_arg2, *args, **kwargs):
        #Your code goes here!
        pass
