from pathlib import Path
from xml.dom.minidom import parseString

def numbRecipes(txtFilesFolder):
    count = 0
    for file in txtFilesFolder.iterdir():
        if file.is_file():
            tags = getFileTags(file)
            count += len(tags.getElementsByTagName('recipe'))
    return count

def recipeNames(txtFilesFolder):
    recipes = []
    for file in txtFilesFolder.iterdir():
        if file.is_file():
            tags = getFileTags(file)
            for recipe in tags.getElementsByTagName('recipe'):
                try:
                    titleTag = recipe.getElementsByTagName('purpose')[0]
                    title = titleTag.firstChild.data
                    recipes.append(title)
                except:
                    pass
    return recipes

def printRecipeNames(recipeNames):
    print("Names of recipes:")
    for index in range(len(recipeNames)):
        print(str(index) + ': ' + recipeNames[index])

def getFileTags(file):
    txtFile = open(str(file), 'r')
    txt = txtFile.read()
    txtFile.close()
    tags = parseString(txt)
    return tags

if __name__ == '__main__':
    recipeFilesFolder = Path('C:\\Python36\\cookbook_textencoded')
    print("Number of recipes:", numbRecipes(recipeFilesFolder))
    printRecipeNames(recipeNames(recipeFilesFolder))
    
