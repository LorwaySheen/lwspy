import subprocess
import os
os.system("python -m pip install --upgrade pip") #先更新pip防止出现更新提示
a = str(subprocess.check_output("pip list")) #获得更新列表
b = a.split("\\n") #分割
while '' in b:
    b.remove('')
c = b[2:-1] #除去无用元素
d = (" ".join(c)) #将列表转为字符串
e = d.split(" ")
while '' in e:
    e.remove('')
while '\\r' in e:
    e.remove('\\r')
libs = e[::2]
for lib in libs:
	try:
		os.system("pip install --upgrade "+lib)
		print("更新{}成功".format(lib))
	except:
		print("更新{}失败".format(lib))
input("")

#pip list --outdated #列出所有过期的库


#网上给出的的代码  https://www.cnblogs.com/whiterock/p/7662176.html
#import pip
#from subprocess import call
#for dist in pip.get_installed_distributions():
#    call("pip install --upgrade " + dist.project_name, shell=True)