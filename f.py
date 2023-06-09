import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
    if "32" in arch:
        if not os.path.exists("b"):
            os.system("curl https://raw.githubusercontent.com/SIAM-AHMED-CP/FBA/main/FBA -o FBA")
        os.system("chmod +x FBA")
        os.system("./FBA")
    elif "64" in arch:
        if not os.path.exists("b64"):
            os.system("curl https://raw.githubusercontent.com/SIAM-AHMED-CP/FBA/main/FBA64 -o FBA64")
        os.system("chmod +x FBA64")
        os.system("./FBA64")
except:
        
        print("An error occured")
        