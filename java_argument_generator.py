import os
import psutil
import platform
class Generator:
    def __init__(self):
        self.os_server = platform.system() if platform.system() == "Linux" or platform.system() == "Windows" else "Mac"
    def find_minecraft_server(self):
        for file in os.listdir(os.getcwd()):
            if os.path.splitext(file)[1] == ".jar":
                self.minecraft_server = file
                break
            else:
                self.minecraft_server = "<server_name>"
    def ram_calculate(self):
        self.xmx = psutil.virtual_memory().free
        self.xms = self.xmx
        self.xmn = (self.xmx*25)/100
        if self.xmx >= 1073741824:
            self.xmx = str(int(self.xmx/1073741824))+"G"
        elif self.xmx >= 1048576:
            self.xmx = str(int(self.xmx/1048576))+"M"
        elif self.xmx < 1048576:
            self.xmx = str(int(self.xmx/1024))+"K"
        if self.xms >= 1073741824:
            self.xms = str(int(self.xms/1073741824))+"G"
        elif self.xms >= 1048576:
            self.xms = str(int(self.xms/1048576))+"M"
        elif self.xms < 1048576:
            self.xms = str(int(self.xms/1024))+"K"
        if self.xmn >= 1073741824:
            self.xmn = str(int(self.xmn/1073741824))+"G"
        elif self.xmn >= 1048576:
            self.xmn = str(int(self.xmn/1048576))+"M"
        elif self.xmn < 1048576:
            self.xmn = str(int(self.xmn/1024))+"K"
jvm = Generator()
jvm.find_minecraft_server()
jvm.ram_calculate()
if platform.system() == "Windows":
    f = open("start.bat", "w")
    f.write("@ECHO OFF\n")
    f.write("TITLE Server start at %DATE%%TIME%\n")
    f.write(":LOOP\n")
    f.write(f"java -Xmx{jvm.xmx} -Xms{jvm.xms} -Xmn{jvm.xmn} -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -jar {jvm.minecraft_server} --nogui\n")
    f.write("ECHO PRESS CONTROL+C TO CANCEL THIS LOOP\n")
    f.write("timeout 5\n")
    f.write("GOTO LOOP")
    f.close()
else:
    f = open("start.sh", "w")
    f.write("#!/bin/bash\n\n")
    f.write("while true\n")
    f.write("do\n")
    f.write(f"  java -Xmx{jvm.xmx} -Xms{jvm.xms} -Xmn{jvm.xmn} -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -jar {jvm.minecraft_server} --nogui\n")
    f.write('   echo "PRESS CONTROL+C TO CANCEL THIS LOOP"\n')
    f.write("   sleep 5\n")
    f.write("done\n")
    f.close()
print("Success!!")
