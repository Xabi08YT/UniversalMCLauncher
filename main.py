Launcher = __import__("fr-Xabi08-Launcher", locals(), globals(), ["gui","configmgr","mojangConnect"])


config = None


def init():
    global config
    config = Launcher.configmgr.loadConfig()
    Launcher.gui.initGUI()

init()