# sshSyncCode
使用ssh进行代码同步

put_codes.py是在上传代码的电脑用的.
get_codes.py是下载代码的电脑用的.

put_codes.py在main函数里面添加了`if ".py" in i or ".sh" in i:`用来筛选上传文件.

get_codes.py将文件夹里面的所有文件下载下来到本地, 文件夹下的子目录没测试. 一键下载文件这个功能在进行科研中服务器画图经常用到, 画图后直接运行代码就可以同步文件, 大大解放生产力.
