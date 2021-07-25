from os import listdir
import os
import importlib
from inspect import getmembers, isfunction, ismethod, isclass
import glob

#Get the directory of the cogs folder
dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'cogs')
#Grab the names of all the .py files in the cogs folder
modules = [ fl for fl in listdir(dir) if fl.endswith('.py') ]

cogs = []
#for i in range o to amount of cogs
for i in range (0,len(modules)):
    #Cut off the .py extension
    modules[i] = modules[i][:-3]
    #Import the library and store it in cogs
    cogs.append(__import__('cogs.'+modules[i]))

    #get the refernce to the burrent library
    #E.g. cogs.Announce
    currentLib = getattr(cogs[i], modules[i])

    #Store all of the classes of the cog in classes
    classes = [ obj for obj in getmembers(currentLib) if isclass(obj[1]) ]
    print(f'Current classes: {classes}') 

    for cls in classes:
        #Store the functions of each classes in class_funcs
        class_funcs = [ obj for obj in getmembers(cls[1]) if ismethod(obj[1]) ]

        print(f'{cls[0]} class functions: {class_funcs}')


"""
TODO find a method of getting the bot function commands from each class
class_funcs doesn't store bot functions, when it should
"""


#print (getattr(getattr(cogs[0], modules[0]),modules[0]).announce.help)

"""
def get_cogs_filenames(dir: str):
    files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    cogs = []
    for file in files:
        if (file[-3:] == '.py'):
            cogs.append(file)
    return cogs
"""

#dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'cogs')
#modules = glob.glob(os.path.join(os.path.dirname(__file__),'cogs', "*.py"))
#__all__ = [ os.path.basename(f)[:-3] for f in modules if os.path.isfile(f) and not f.endswith('__init__.py')]
#print(__all__)

#onlyfiles = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) ]


#for module in modules:
    #i = importlib.import_module(f'cogs.{module}.{module}')
    #print(i.description)