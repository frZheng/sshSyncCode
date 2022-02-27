import paramiko,os,sys

server_dir = r"/tmp/xxx/Book_gym_20220214"  #需要下载远程服务器的目标文件夹路径
local_dir = r"./Book_gym_20220214" #要保存文件的路径

hostname = 'xxx'  #服务器IP地址
username = 'root'     # 登录账号
password = 'xxx'     #登录密码
port = 22

if __name__ == '__main__':


    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

    file_list = os.listdir(local_dir)
    for i in file_list:
        if ".py" in i or ".sh" in i:
            print("put: ",i)
            sftp.put(os.path.join(local_dir,i), server_dir + "/" + i)  # 将本地的Windows.txt文件上传至服务器/root/Windows.txt

    transport.close()  # 关闭连接
