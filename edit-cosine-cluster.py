#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import argparse
import csv
import sys


def createCluster(inputCSV,argNum):
    row=[]
    if(argNum not in [0,1,2]):
        print("Input Error! \nPass argument to --cluster as one of the following\n0 for clustering based on x-coordinate, \n1 for clustering based on y-coordinate, \n2 for clustering based on similarity score")
        sys.exit()

    csvPath = inputCSV          #Input Path to csv file
    with open(csvPath,"r") as f:
        lines = [line.strip() for line in f]
        for line in lines:
            row.append(line)

    data={}
    for i in range(len(row)):
        if "x-coordinate" in row[i].split(","):
            continue
        else:
            column = row[i].split(",")
            data[column[argNum]]=[]         #Cluster based on the argument number passed

    for i in range(len(row)):
        if "x-coordinate" in row[i].split(","):
            continue
        else:
            column = row[i].split(",")
            second={}
            second["name"]=column[1]+"  "+column[2]
            second["size"]=column[2]
            data[column[argNum]].append(second)         #Cluster based on the argument number passed

    clusterList = []
    i=0
    for elem in list(data.keys()):
        first={}
        first["name"]="cluster "+str(i)
        first["children"]=data[elem]
        clusterList.append(first)
        i+=1


    print(json.dumps(clusterList, sort_keys=True, indent=4, separators=(',', ': ')))

    clusterStruct = {"name":"clusters", "children":clusterList}
    with open("clusters.json", "w") as f:             #Pass the json file as input to cluster-d3.html or dynamic-cluster.html
        f.write(json.dumps(clusterStruct, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ == '__main__':
    argParser = argparse.ArgumentParser('Edit/Cosine Similarity Cluster-D3')
    argParser.add_argument('--inputCSV', required=True, help='path to directory containing CSV File, containing pair-wise similarity scores based on edit/cosine similarity distance')
    argParser.add_argument('--cluster', required=True, type=int, help='Cluster based on the x-coordinate/y-coordinate/similarity score. Pass 0 for clustering based on x-coordinate, 1 for clustering based on y-coordinate, 2 for clustering based on similarity score')
    args = argParser.parse_args()

    createCluster(args.inputCSV, args.cluster)

