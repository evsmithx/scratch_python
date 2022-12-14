import os
import subprocess
from pathlib import Path

"""
Simple utility to generate the git commands for commiting files with the commit time equal to 
 their last modification time. The commands are only printed and not executed!
"""
GIT_DIR = ''
MESSAGE = "Solution for "

command = "git status -s"
cp = subprocess.run(command, shell=True, capture_output=True, cwd=GIT_DIR)
stdout = cp.stdout.decode('utf-8')

# iterate through, find modification time, make git command
commands = []
for line in stdout.split('\n'):
    line = line.strip()
    if line == "":
        continue
    status, fl = line.split(' ')
    if status == "??":
        continue
    mtime = os.path.getmtime(Path(GIT_DIR) / fl)
    comm = f"git add {fl} && git commit -m \"{MESSAGE} {fl}\" --date={mtime}"
    commands.append((mtime, comm))

# sort by increasing modification time
commands.sort(key=lambda x: x[0])

for comm in commands:
    print(comm[1])
