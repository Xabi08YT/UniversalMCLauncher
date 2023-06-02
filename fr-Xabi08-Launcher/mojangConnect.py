from mojang import client
from json import dumps, load


currentAccountProfile = None


def getClientFromCredentials(username, password):
    return client.Client(username, password)


def getAccountFromData():
    with open(file="data/accounts.js") as accountfile:
        accounts = load(accountfile)
        accountfile.close()        
    return accounts


def recconectDefaultAccount():
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
