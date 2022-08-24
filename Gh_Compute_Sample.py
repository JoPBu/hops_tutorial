import requests
import json
import os
import sys
import compute_rhino3d.Util as rcutil
import compute_rhino3d.Grasshopper as rcgh


# Set the compute server connection
compute_url = "http://localhost:5000/"
post_url = compute_url + "grasshopper"

dir_path = os.path.dirname(os.path.realpath(__file__))
ghDefinition_path = os.path.join(dir_path, 'ghCompute.gh')

rcutil.url = compute_url
rcutil.authToken = "" # no auth token required as it is a local service

# Test the compute server connection, should return version object

try: 
    version_test = requests.get(compute_url + '/version')
    print("[INFO] Compute server connection established")
except:
    print("[ERROR] Can not establish a connection to the compute server!")
    sys.exit(1)

#Define the inputs:
inputTree1 = rcgh.DataTree("RH_IN:number1")
inputTree2 = rcgh.DataTree("number2")

#Filling the trees:
for i in range(1,6):   #1,2,3,4,5 
    inputTree1.Append([i], [i]) #Beides müssen listen sein!

inputTree2.Append([0], [3])

# Merge all inputs:
trees = [inputTree1, inputTree2]

# Run the grasshopper script
output = rcgh.EvaluateDefinition(ghDefinition_path, trees)

# Process the formatted output:
print(json.dumps(output,indent=4))