from json import load, dump
from os import remove


def loadConfig():
    with open(file="data/config.json", mode="r") as cfg:
        config = load(cfg)
        cfg.close()
    return config


def applyConfig(config):
    remove("data/config.json")
    with open(file="data/config.json", mode="w+") as cfg:
        dump(obj=config, fp=cfg)
        cfg.close()
    return