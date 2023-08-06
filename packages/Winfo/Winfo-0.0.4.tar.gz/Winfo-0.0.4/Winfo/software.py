from subprocess import check_output

def version():
    raw = check_output(["ver"], shell=True)
    rawdecoded = raw.decode()
    winversion = rawdecoded.replace("Microsoft Windows [Version ", "").replace("]", "").replace("\n", "")
    return winversion

def system():
    versionformatted = version().replace("\r", "")
    if versionformatted.startswith("10.0.2"):
        return "11" # because Windows 11 version says 10.0.20 or higher (Microsoft was kinda lazy)
    elif versionformatted.startswith("10.0"):
        return "10"
    elif versionformatted.startswith("8.1"):
        return "8.1"
    elif versionformatted.startswith("8"):
        return "8"
    elif versionformatted.startswith("7"):
        return "7"
    else:
        return None # None means not found
    
def devicename():
    raw = check_output(["wmic", "cpu", "get", "SystemName"])
    rawdecoded = raw.decode()
    getdevname = rawdecoded.strip("SystemName").rstrip("\n").replace("\n", "")
    return getdevname

def username():
    raw = check_output(["echo", "%USERNAME%"], shell=True)
    rawdecoded = raw.decode()
    getusername = rawdecoded.replace("\n", "")
    return getusername

def where():
    raw = check_output(["wmic", "bootconfig", "get", "Caption"])
    rawdecoded = raw.decode()
    getpart = rawdecoded.replace("Caption", "", 1).replace("\n", "")
    return getpart