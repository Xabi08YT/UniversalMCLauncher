Launcher = __import__("fr-Xabi08-Launcher", locals(), globals(), ["gui","configmgr","mojangConnect","versionDownloader","minecraftLaunch"])
from os import getcwd


config = None
APP_PATH = getcwd()


def init():
    global config
    config = Launcher.configmgr.loadConfig()
    Launcher.versionDownloader.APP_PATH = APP_PATH
    Launcher.versionDownloader.init()
    Launcher.versionDownloader.config = config
    Launcher.minecraftLaunch.config = config
    Launcher.minecraftLaunch.init()
    Launcher.gui.initGUI()

init()