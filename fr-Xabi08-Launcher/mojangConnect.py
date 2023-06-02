from mojang import client
from json import dump, load
from os import remove


currentAccountProfile = None


def getClientFromCredentials(username, password):
    return client.Client(username, password)


def getAccountFromData():
    with open(file="data/accounts.js") as accountfile:
        accounts = load(accountfile)
        accountfile.close()        
    return accounts


def recconectDefaultAccount():
    global accounts
    accounts = getAccountFromData()
    for account in accounts:
        if accounts[account]["default"] == True:
            global currentAccountProfile
            try:
                currentAccountProfile =  getClientFromCredentials(accounts[account]["username"],accounts[account]["password"])
            except client.LoginFailure:
                return "Le mot de passe ou le mail du compte par défaut est invalide. Veuillez le redéfinir."
            return
    return "Aucun compte par défaut n'est défini."


def init():
    out = recconectDefaultAccount()
    if out == None:
        return
    return out


def addAccount(username, password, default = False):
    try:
        global currentAccountProfile
        currentAccountProfile = getClientFromCredentials(username, password)
        accounts[username]["username"] = username
        accounts[username]["password"] = password
        accounts[username]["default"] = default
        remove("data/accounts.json")
        with open(file='data/accounts.json') as accountsfile:
            dump(accountsfile, accountsfile)
            accountsfile.close()
    except client.LoginFailure:
        return "Le mot de passe ou le mail du compte est invalide. Veuillez réessayer."
    except FileNotFoundError or FileExistsError or PermissionError as e:
        print(e)
        return "Impossible d'éditer le répertoire des comptes connectés. Vous restez tout de même connecté jusqu'à la fermeture du programme."