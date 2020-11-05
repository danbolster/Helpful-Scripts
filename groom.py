import os


directory = "/home/daniel/Documents/CTF/HtB"

def getTargets():
    targetList=[]
    for entry in os.listdir(directory):
        if os.path.isdir(entry):
            targetList.append(entry)
    return targetList

def cleanUp(targetList):
    

    for target in targetList:
        nmap = []
        smb = []
        autorecon_info = []
        enum = []
        httpList = {}
        
        

        messes = os.listdir(directory+"/" + target + "/scans")
        for mess in messes:
            if "nmap" in mess:
                nmap.append(mess)
            elif "log" in mess or "manual_commands" in mess:
                autorecon_info.append(mess)
            elif "smb" in mess:
                smb.append(mess) 
            elif "enum" in mess:
                enum.append(mess)
            elif "http" in mess:
                mess_split = mess.split("_")
                if "http_" + str(mess_split[1]) not in list(httpList.keys()):
                    httpList["http_" + str(mess_split[1])] = []
                    httpList["http_" + str(mess_split[1])].append(mess)
                    
                else:
                    httpList["http_" + str(mess_split[1])].append(mess)
                    
        
                    

        
        if(len(nmap)) > 0:
            handleList("nmap",nmap,target)
        if(len(smb)) > 0:
            handleList("smb",smb,target)
        if(len(enum)) > 0:
            handleList("enum",enum,target)
        if(len(autorecon_info)) > 0:
            handleList("autorecon_info",autorecon_info,target)
        if(len(httpList.keys())) > 0:
            handleHTTP(httpList,target)
        

        




def handleHTTP(httpList,target):
    for key in httpList.keys():
        newDir = directory + '/' + target  + "/scans/" + key
        os.system("mkdir " + newDir)
        for element in httpList[key]:
            os.system("mv " + directory + '/' + target + "/scans/" + element + " " + newDir + "/" + element)


def handleList(name,category,target):
    newDir = directory + "/" + target + "/scans/" + name
    os.system("mkdir "+ newDir)
    for element in category:
        os.system("mv " + directory + "/" + target + "/scans/" +  element + " " + newDir)

def main():
    targetList = getTargets()
    httpList = cleanUp(targetList)

    

main()
