# basic_info.py
import platform
def print_system_info():
    print("Informations about your system :" )
    print(platform.system())
    print(platform.release())
    print(platform.version())
    print(platform.architecture())
    print(platform.processor())
    print(platform.python_version())

