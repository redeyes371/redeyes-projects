import subprocess
import sys
import os
import venv

# Create a virtual environment
venv_dir = "myenv"
venv.create(venv_dir, with_pip=True)

# Activate the virtual environment
if os.name == "nt":  # For Windows
    activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
else:  # For Linux/Mac
    activate_script = os.path.join(venv_dir, "bin", "activate")
subprocess.call([activate_script], shell=True)

# Install necessary packages in the virtual environment
subprocess.call(["pip", "install", "http.server"])

# Run the HTTP server within the virtual environment
subprocess.call([sys.executable, "-m", "http.server"])
