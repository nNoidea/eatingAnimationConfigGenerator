# Get all the folder names in the current directory

import os

currentDir = os.path.dirname(os.path.realpath(__file__))

# Get the location of this file
def getFolderNames():
    # Get the folder names in the current directory
    folderNames = [f for f in os.listdir(currentDir) if os.path.isdir(os.path.join(currentDir, f))]
    return folderNames

def generateJsonFiles(itemName, modName):
    # load the string from currentDir +/+ mainFileTemplate.txt file
    with open(os.path.join(currentDir, "mainFileTemplate.txt"), "r") as mainFileTemplate:
        string = mainFileTemplate.read()
        # replace MODNAME with the modName
        string = string.replace("MODNAME", modName)
        # replace ITEM_NAME with the itemName
        string = string.replace("ITEM_NAME", itemName)

    # create the directories if they do not exist
    dir_path = os.path.join(currentDir, modName, "models", "item")
    os.makedirs(dir_path, exist_ok=True)

    # create the main json file
    with open(os.path.join(dir_path, itemName + ".json"), "w") as mainFile:
        mainFile.write(string)

    # for range of 0 to 2

    for i in range(3):
        with open(os.path.join(currentDir, "secondaryFilesTemplate.txt"), "r") as secondaryFile:
            string = secondaryFile.read()
            # replace MODNAME with the modName
            string = string.replace("MODNAME", modName)
            # replace ITEM_NAME with the itemName
            string = string.replace("ITEM_NAME", itemName)
            string = string.replace("NUMBER", str(i))

        with open(os.path.join(dir_path, itemName + f"_eating_{i}.json"), "w") as mainFile:
            mainFile.write(string)

    


# iterate through the array
for i in range(len(getFolderNames())):
    modName = getFolderNames()[i]

    # generate models/textures folders if they don't exist
    if not os.path.exists(modName + "/models"):
        os.makedirs(modName + "/models")
    if not os.path.exists(modName + "/item"):
        os.makedirs(modName + "/item")
    
    # get all the .png file names in currentfilelocation/modName/textures/item folder
    textures = [f for f in os.listdir(currentDir + "/" + modName + "/textures/item") if f.endswith('.png')]

    # Only use the ones that end with "_0.png"
    textures = [x for x in textures if x.endswith("_0.png")]

    # iterate through the array _0.png files

    for i in range(len(textures)):
        texture = textures[i]
        # remove the _0.png from the texture name
        texture = texture.split("_eating_0.png")[0]
        # generate the json files
        generateJsonFiles(texture, modName)


