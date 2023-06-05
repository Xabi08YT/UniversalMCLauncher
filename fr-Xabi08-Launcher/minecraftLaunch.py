from platform import system, architecture
import minecraft_launcher_lib
import subprocess
import sys
from os import path, listdir
from JRE.jreLocation import *
from zipfile import *


config = None


def extractJRE(wpath):
    if "JRE8" in listdir(wpath):
        return
    else:
        with ZipFile(file=path.join(wpath,"JREs.zip")) as zip_ref:
            zip_ref.extractall(wpath)


def init():
    global CURRENT_ARCH,CURRENT_SYSTEM,JRE8_EXEC_PATH,JRE18_EXEC_PATH
    CURRENT_SYSTEM = system()
    CURRENT_ARCH = architecture()[0]


    cases = {"Linux64bit":LINUX_64_PATH,"Windows64bit":WINDOWS_64_PATH,"Darwin":None,"Windows32bit":WINDOWS_32_PATH,"Linux32bit": LINUX_32_PATH}

    if CURRENT_ARCH[0] == '64bit':
        JRE18_EXEC_PATH = END_OF_PATH.format(cases[str(CURRENT_SYSTEM+CURRENT_ARCH)]+"/JRE18")
    JRE8_EXEC_PATH = END_OF_PATH.format(cases[str(CURRENT_SYSTEM+CURRENT_ARCH)]+"/JRE8")
    if CURRENT_SYSTEM != "Darwin":
        extractJRE(cases[str(CURRENT_SYSTEM+CURRENT_ARCH)])
    else:
        print("JRE Extract process is not automated for MacOSX.")
    return


def launchInstance(instanceName):
    minecraft_directory = path.join(config["StorageParams"]["PathToStorage"],config["StorageParams"]["PathToConfigs"],instanceName)

    try:
        with open(file=minecraft_directory+"/UserLastestJRE.param",mode="rb") as f:
            excPath = JRE18_EXEC_PATH
            f.close()
    except FileNotFoundError:
        excPath = JRE8_EXEC_PATH
    
    options = {
        "username": "Xabi08",
        "uuid": "None",
        "token": "None",
        "executablePath": excPath
    }

    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("None",minecraft_directory,options=options)

    subprocess.call(minecraft_command)
    return