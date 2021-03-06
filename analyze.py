#! /usr/bin/env python3

import json
import sys
import pandas as pd
import json

def count_contractions(pressure_data):
    """
    Count the number of contractions for a pressure curve

    :param pressure_data: a list of pressure points
    :return: The total number of contractions
    """
    # FIXME
    count=0
    bHigh=False
    bLow=False
    for k in range(0, len(pressure_data)):
        if pressure_data[k]["pressure"]>95:
            if bLow: 
                count+=1
                bLow=False 
            bHigh=True
        elif pressure_data[k]["pressure"]<85:
            if bHigh: 
                bLow=True

    return count

def contractions_per_sec(pressure_data):
    """
    Calculate the mean contractions / secs for a pressure curve

    :param pressure_data: a list of pressure points
    :return: The mean frequency of contraction / secs
    """
    # FIXME
    
    contractTimeArr=[]
    bHigh=False
    bLow=False
    count=0
    initialTime=pressure_data[0]["ms"]
    for k in range(0, len(pressure_data)):
        if pressure_data[k]["pressure"]>95:
            if bLow: 
                contractTimeArr.append(pressure_data[k]["ms"] - initialTime)
                initialTime=pressure_data[k]["ms"]
                count+=1
                bLow=False 
            bHigh=True
        elif pressure_data[k]["pressure"]<85:
            if bHigh: 
                bLow=True
  
    meanTime=sum(contractTimeArr)/1000

    return round((len(contractTimeArr)/meanTime),2)

def main():
    pressure_file = sys.argv[1]

    inputData = pd.read_csv(pressure_file, skiprows=0).fillna(value=0)
    pressure_data=[]
    
    for k in range(0, len(inputData)):
        dictPressure = {"ms":0,"pressure":0}
        dictPressure["ms"]=int(inputData.iloc[k, 0])
        dictPressure["pressure"]=float(inputData.iloc[k, 1])
        pressure_data.append(dictPressure)


    n = count_contractions(pressure_data)
    f = contractions_per_sec(pressure_data)


    #n = 0 # FIXME
    #f = 0 # FIXME
    print("---")
    print("For {}:".format(pressure_file))
    print("* Number of contraction = {}".format(n))
    print("* Contraction / s = {}".format(f))

    result={ "pressure_data": pressure_data, "count_contractions": int(n),"contraction_per_sec": float(f) }
    json_object = json.dumps(result, indent = 4)
  
    # Writing to sample.json
    with open("pressure.json", "w") as outfile:
        outfile.write(json_object)

    return 0

if __name__ == '__main__':
    sys.exit(main())
