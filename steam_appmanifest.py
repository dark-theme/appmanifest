# steam_appmanifest.py

from pathlib import Path

def get_appid() -> str:
    while True:
        appid = input("Enter appid: ")
        if appid.isdigit():
            return appid
        else:
            print("Invalid appid.\n")

def get_name() -> str:
    while True:
        name = input("Enter game name: ")
        if name != "":
            return name
        else:
            print("Name must not be blank.\n")

def get_installdir() -> str or None:
    while True:
        get = input("Custom installdir? (False) ")
        if get == "" or get.lower().startswith("f"):
            return None
        elif get.lower().startswith("t"):
            break
        else:
            print("Input must be '(T)rue' or '(F)alse'\n")
            
    while True:
        installdir = input("Enter installdir: ")
        if installdir != "":
            return installdir
        else:
            print("Installdir must not be blank.\n")

def create_manifest(appid: str, name: str, installdir: str):
    manifest = f"""\
"AppState"
{{
	"appid"		"{appid}"
	"Universe"		"1"
	"name"		"{name}"
	"StateFlags"		"4"
	"installdir"		"{installdir}"
	"LastUpdated"		"0"
	"UpdateResult"		"0"
	"SizeOnDisk"		"0"
	"buildid"		"0"
	"LastOwner"		"0"
	"BytesToDownload"		"0"
	"BytesDownloaded"		"0"
	"AutoUpdateBehavior"		"0"
	"AllowOtherDownloadsWhileRunning"		"0"
	"ScheduledAutoUpdate"		"0"
	"InstalledDepots"
	{{
	}}
	"MountedDepots"
	{{
	}}
	"UserConfig"
	{{
	}}
}}
"""
    
    p = Path(f'appmanifest_{appid}.acf')
    p.write_text(manifest)
    print("\n" + p.read_text())

def run():
    appid = get_appid()
    name = get_name()
    installdir = get_installdir()
    if installdir == None:
        installdir = name

    create_manifest(appid, name, installdir)

if __name__ == "__main__":
    run()
