'''
Arthor:		FGO
Usage:		Get active SSH connection object
Param:
args: not in used
kwargs: related param of paramiko SSH client connection

Return:		Active SSH connection object
Example:
client = get_ssh_client(hostname='1.2.3.4', port=8080, username=root, password=12345678)
'''
def get_ssh_client(*args, **kwargs):
    assert 'hostname' in kwargs \
    and 'port' in kwargs \
    and 'username' in kwargs \
    and 'password' in kwargs, \
    'Parameter missing, hostname/port/username/password must be included'

    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(kwargs['hostname'], kwargs['port'], kwargs['username'], kwargs['password'])
    return client

'''
Arthor:		FGO
Usage:		Execute funtion that require SSH connection directly
Param:
fun: function that needed to be executed, the ssh client will be passed to function as parameter
kwargs: related param of paramiko SSH client connection

Return:		Function result
Example:
client = ssh_con_w_fun(function1, hostname='1.2.3.4', port=8080, username=root, password=12345678)
'''
def ssh_con_w_fun(fun, **kwargs):
    assert 'hostname' in kwargs \
    and 'port' in kwargs \
    and 'username' in kwargs \
    and 'password' in kwargs, \
    'Parameter missing, hostname/port/username/password must be included'

    return fun(get_ssh_client(fun, kwargs))
