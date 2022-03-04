#Steps on how to run code 



#For edit similarity refered to this link to reference
https://github.com/chrismattmann/tika-similarity

#tikasimilarity contents
tikasimilarity folder holds 50 individual rows from Bik et al dataset that compare each other

#this will run edit_value_similarity.py to find the similarities btwn rows and output to .csv file
python edit_value_similarity.py --fileInput tikasimilarity --outCSV edit_value_similarity.csv

#this transforms the information from csv into json which is labeled into clusters 
python edit-cosine-cluster.py --inputCSV edit_value_similarity.csv --cluster 0

#this transforms the information from csv into json which is labeled into clusters 
python edit-cosine-cluster.py --inputCSV edit_value_similarity.csv --cluster 1

#this transforms the information from csv into json which is labeled into clusters 
python edit-cosine-cluster.py --inputCSV edit_value_similarity.csv --cluster 2

#download web server for chrome 
https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb

#edit_distance_cluster0
clusters.json and html webpage in here.
When you go to this folder using web server for chrome, and click on the html webpage, visualization will open up

#edit_distance_cluster1
clusters.json and html webpage in here.
When you go to this folder using web server for chrome, and click on the html webpage, visualization will open up

#edit_distance_cluster2
clusters.json and html webpage in here.
When you go to this folder using web server for chrome, and click on the html webpage, visualization will open up
