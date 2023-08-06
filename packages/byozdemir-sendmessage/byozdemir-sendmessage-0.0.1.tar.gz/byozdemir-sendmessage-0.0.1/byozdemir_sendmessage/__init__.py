import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)


#Returns the provider which is you choised
def getProvider(name,**data):
    provider = __import__(name)
    messager = provider.Messager(**data)

    return messager

