import subprocess

class Crawler():
    ports, filename, base_ip, subnet, target

    def __init__(self, target, base_ip, ports=[80,443], subnet=24):
        self.ports = ports
        self.base_ip = base_ip
        self.target = target
        self.subnet = subnet

    def crawl(self):
        # write code for crawler to crawl and generate output xml somewhere on the disk



"""
ports = '80,443'
filename = 'rlt.xml'
base_ip = '27.7.6.123'
subnet = str(24)
call = subprocess.Popen(['masscan','-p'+ports,base_ip+'/'+subnet,'--banners','-oX',filename])
"""
