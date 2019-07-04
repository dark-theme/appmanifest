# steam_appmanifest_selenium.py

from pathlib import Path
from selenium import webdriver

def get_appid() -> str:
    while True:
        appid = input("Enter appid: ")
        if appid.isdigit():
            return appid
        else:
            print("Invalid appid.\n")

def get_details(id: str) -> (str, str):
    # using chrome webdriver
    driver = webdriver.Chrome()
    
    try:
        driver.get(f"https://steamdb.info/app/{id}/config/")
        assert "No app was found matching this AppID." not in driver.page_source
    except:
        print("Invalid appid.")
        raise
    else:
        name = driver.find_element_by_xpath \
            ("/html/body/div[1]/div[1]/div[2]/div/div/div[1]/h1").text
        installdir = driver.find_element_by_xpath \
            ("//*[contains(text(), \"installdir\")]/following-sibling::td").text
        return (name, installdir)
    finally:
        driver.close()

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
    name, installdir = get_details(appid)
    create_manifest(appid, name, installdir)

if __name__ == "__main__":
    run()
