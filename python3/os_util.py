'''
Arthor:		FGO
Usage:		Call OS shell to execute command on SSH client
Param:
client: SSH client
cmd: command to be executed

Return:		tuple of stdin, stdout, stderr channel of shell
Example:
result = __run_cmd(client, "ls /dev | grep sd")[1].readlines()
'''
def __run_cmd(client, cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    return stdin, stdout, stderr

'''
Arthor:		FGO
Usage:		Replace OS path seperator among multi platform
Param:
full_path_w_name: full path with file name

Return:		Corrected path
Example:
final_path = os.getcwd() + __os_file_path('/a/b/c.conf)
'''
def __os_file_path(full_path_w_name):
    import platform
    return (full_path_w_name.replace('/', '\\')
            if platform.system() == 'Windows'
            else full_path_w_name.replace('\\', '/'))

