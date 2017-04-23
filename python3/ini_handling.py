'''
Arthor:		FGO
Usage:		Get ini parser object
Param:
ini_path: the ini file path

Return:		Corrected path
Example:
final_path = os.getcwd() + __os_file_path('/a/b/c.conf)
'''
def get_config_parser(ini_path):
    from configparser import ConfigParser
    con = ConfigParser()
    con.read(ini_path)
    return con

'''
Arthor:		FGO
Usage:		Read ini data with string index
Param:
section: ini section
config_obj: ini parser object

Return:		Function object which allow user to choose parse as string or int
Example:
smtp_ip = get_config_getter_w_section()('SMTP', config)
smtp_port = get_config_getter_w_section('int')('SMTP', config)
'''
def get_config_getter_w_section(section, config_obj):
    from functools import partial
    def body(var_type='str'):
        if 'str' in var_type:
            return partial(config_obj.get, section)
        elif 'int' in var_type:
            return partial(config_obj.getint, section)
    return body

'''
Arthor:		FGO
Usage:		Read ini data list with string index
Param:
section: ini section
config_obj: ini parser object

Return:		data list as string from ini conf file
Example:
white_list = get_config_list_w_section('System', 'WhiteList', config)
'''
def get_config_list_w_section(section, option, config_obj, seperator=','):
    return config_obj.get(section, option).split(seperator)
