import paramiko,os,sys

input_dir = r"/tmp/xxx/Book_gym_20220214"  #需要下载远程服务器的目标文件夹路径
output_dir = r"./Book_gym_20220214" #要保存文件的路径

hostname = 'xxx'  #服务器IP地址
username = 'root'     # 登录账号
password = 'xxx'     #登录密码
port = 22


def list_dir(root):
    cmd = 'ls --file-type '+root
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read()
    return result.decode().split('\n')

def save_file(root,name):
    try:
        save_path = output_dir + root.split(input_dir)[-1]
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_file_path = save_path + name
        cmd = 'cat '+ root + name
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        if not result:
            return
        with open(save_file_path,'wb+') as fd:
            fd.write(result)
            print('save file:'+save_file_path)
    except :
        print('save path:'+save_file_path)
        print("Unexpected error:", sys.exc_info()[0])

def traverse_dir(root):
    nodes = list(item for item in list_dir(root) if len(item) > 0)
    for node in nodes:
        #如果该节点是文件夹，继续遍历
        if node.endswith('/'):
            traverse_dir(root + node)
        else:
            #如果该节点是文件  则保存该文件
            save_file(root,node)

if __name__ == '__main__':
    if len(output_dir) > 0  and output_dir[-1] != '/':
        output_dir += '/'
    if len(input_dir) > 0 and input_dir[-1] != '/':
        input_dir += '/'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=password)
    traverse_dir(input_dir)
    ssh.close()
