import os
import subprocess

def run_command(command):
    """Run a shell command."""
    process = subprocess.Popen(command, shell=True)
    process.communicate()

if os.name == 'nt':
    run_command("setup_env.bat")
else:
    run_command("./setup_env.sh")
