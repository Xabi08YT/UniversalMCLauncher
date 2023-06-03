from minecraft_launcher_lib.install import install_minecraft_version
from wget import download
from json import load
from os import remove, path, getcwd


config = None
APP_PATH = None
snapshotList = []
releaseList = []
oldalphaList = []
oldbetaList = []


def init():
    file = path.join(APP_PATH,"data/currentVersionList.json")
    try:
        remove(file)
    except FileNotFoundError:
        pass
    download("https://launchermeta.mojang.com/mc/game/version_manifest_v2.json","data/currentVersionList.json")
    global version_list
    with open(file=file, mode = "r") as vList:
        version_list = load(vList)
        vList.close()
    buildVersionList()
    return
    

def create_instance(vid,instancename = None):
    if instancename is None:
        instancename = vid
    if config["StorageParams"]["PathToStorage"] == "Storage/":
        storagePath = getcwd()+"/"+config["StorageParams"]["PathToStorage"]+config["StorageParams"]["PathToConfigs"]+instancename+"/"
    else:
        storagePath = config["StorageParams"]["PathToStorage"]+config["Storage"]["PathToConfigs"]+instancename+"/"
    install_minecraft_version(vid, storagePath)
    remove(path.join(storagePath, "runtime"))
    if formatBuildDate(getBuildDate(vid)) > "202001171003520000":
        with open(file="UseLastestJRE.param") as tmp:
            tmp.close()
    

def buildVersionList():
    for v in version_list["versions"]:
        if v["type"] == "snapshot":
            snapshotList.append(v)
        elif v["type"] == "release":
            releaseList.append(v)
        elif v["type"] == "old_alpha":
            oldalphaList.append(v)
        else:
            oldbetaList.append(v)
    return


def getBuildDate(vid):
    for v in version_list["versions"]:
        if v["id"] == vid:
            return v["releaseTime"]
    return None


def formatBuildDate(buildDate):
    buildDate.replace("-",",")
    buildDate.replace("T",",")
    buildDate.replace(":",",")
    buildDate.replace("+",",")
    buildDate = buildDate.split(",")
    buildDate = int(buildDate[0]+buildDate[1]+buildDate[2])
    return buildDate