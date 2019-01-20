import subprocess

ports = '80,443'
filename = 'rlt.xml'
base_ip = '27.7.6.123'
subnet = str(24)
call = subprocess.Popen(['masscan','-p'+ports,base_ip+'/'+subnet,'--banners','-oX',filename])

