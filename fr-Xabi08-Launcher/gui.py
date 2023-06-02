import webview

def initGUI():
    webview.create_window('Minecraft Launcher (Custom)', 'fr-Xabi08-Launcher/templates/main.html',resizable=False, width=1260, height=960)
    webview.start()