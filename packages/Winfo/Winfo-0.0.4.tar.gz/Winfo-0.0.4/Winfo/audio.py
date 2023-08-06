from subprocess import check_output

def listall():
    raw = check_output(["wmic", "sounddev", "get", "caption"], shell=True)
    rawdecoded = raw.decode()
    audlist = [line.replace("Caption", "").strip() for line in rawdecoded.split("\n")[1:] if line.strip() != ""]
    return audlist

def listmanufacturers():
    raw = check_output(["wmic", "sounddev", "get", "manufacturer"], shell=True)
    rawdecoded = raw.decode()
    manulist = [line.replace("Caption", "").strip() for line in rawdecoded.split("\n")[1:] if line.strip() != ""]
    return manulist