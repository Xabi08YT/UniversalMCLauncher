from json import load, dump
from os import remove


def loadConfig():
    try:
        with open(file="data/config.json", mode="r") as cfg:
            config = load(cfg)
            cfg.close()
    except FileNotFoundError:
        config = generateDefaultConfig()
    return config


def applyConfig(config):
    remove("data/config.json")
    with open(file="data/config.json", mode="w+") as cfg:
        dump(obj=config, fp=cfg)
        cfg.close()
    return


def generateDefaultConfig():
    config = {
                "GeneralLaunchParams":
                {
                    "Xmx":1024,
                    "Xms":500,
                    "DefaultJREPath":"JRE/Java18/java.exe",
                    "StartMCFullscreen": False, 
                    "Defaultwidth": None, 
                    "DefaultHeight": None
                },
                "UserParams": 
                {
                    "lang":"fr",
                    "theme":"dark",
                    "ForceCrackedAuth": False, 
                    "EnableModDL":False, 
                    "EnableModFB":False,
                    "EnableModpackDL": False,
                    "EnableRessourcepackDL": False,
                    "EnableRessourcepackFB": False,
                    "EnableShaderDL": False,
                    "EnableShaderFB": False,
                },
                "StorageParams":
                {
                    "PathToStorage": "Storage/", 
                    "MaxDiskSpace": None,
                    "ModFBPath": "AllMods/",
                    "RessourcepackFBPath": "AllResourcepacks/",
                    "ShaderFBPath": "AllShaders/",
                    "PathToConfigs": "AllGameVersion/",
                }
            }
    with open(file="data/config.json", mode="a+") as cfg:
        dump(obj=config, fp=cfg)
        cfg.close()
    return config