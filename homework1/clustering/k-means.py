from math import sqrt
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import argparse, json, re

def visualize_data_circle(dataset, cols, output_file):
    clusters = dict()
    cluster0 = list()
    cluster1 = list()
    cluster2 = list()
    cluster3 = list()

    # create slize for dataframe that does not include the name (string)
    slice = [dataset[i][0:2] for i in range(0, len(dataset) - 1)]
    df = pd.DataFrame(slice, columns=cols)
    #  create 4 clusters using kmeans
    kmeans = KMeans(n_clusters=4, init='k-means++', random_state=0).fit(df)
    
    #  create output json in format that tika-similarity visualization can display
    for data in dataset:
        x1 = data[0]
        y1 = data[1]
        min_dist = -1
        c = 0
        for cluster_center in kmeans.cluster_centers_:
            x2 = cluster_center[0]
            y2 = cluster_center[1]
            x = (x1 - x2) * (x1 - x2)
            y = (y1 - y2) * (y1 - y2)
            distance = sqrt(x + y)
            if min_dist == -1:
                min_dist = distance
                cluster = c
            elif min_dist > distance:
                min_dist = distance
                cluster = c
            c += 1
        if cluster == 0:
            cluster0.append({"name": data[2], "size": (data[0] + data[1]) * 5})
        elif cluster == 1:
            cluster1.append({"name": data[2], "size": (data[0] + data[1]) * 5})
        elif cluster == 2:
            cluster2.append({"name": data[2], "size": (data[0] + data[1]) * 5})
        elif cluster == 3:
            cluster3.append({"name": data[2], "size": (data[0] + data[1]) * 5})
    children_list = list()
    
    children_list.append({"name": "cluster0", "children": cluster0})
    children_list.append({"name": "cluster1", "children": cluster1})
    children_list.append({"name": "cluster2", "children": cluster2})
    children_list.append({"name": "cluster3", "children": cluster3})
    clusters["name"] = "clusters"
    clusters["children"] = children_list
    
    #  write the tika-similarity file for visualization
    #  also write a file for details regarding the cluster results
    f = open("circle.json","w")
    f2 =  open(output_file,"w")
    json_string = json.dumps(clusters)
    f.write(json_string)
    f2.write(json_string)
    f.close()
    f2.close()
    
    # print(clusters)
    # sns.scatterplot(data=df, x="nbr_pubs", y="career_duration", hue=kmeans.labels_)
    # plt.show()
    
    #  display a scatter plot of the cluster data
    sns.scatterplot(data=df, x=cols[0], y=cols[1], hue=kmeans.labels_)
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 
                marker="X", c="r", s=200, label="centroids", alpha=0.5)
    plt.legend()
    plt.show()

# create clusters based on papaer data considering number of authors and
#  number of las afffiliated with the the paper 
def visualize_finding_data_circle():
    dataset = list()
    #  read the collected data from json file
    json_file = open("output/findings.json")
    findings_map = json.load(json_file)
    json_file.close()

    cols=["author_count", "affiliation_count"]

    #  for each finding (paper) with data, add to the dataset
    for finding_key in findings_map:
        finding = findings_map[finding_key]
        finding_data = list();
        if len(finding["affiliations"]) > 0 and len(finding["authors"]):
            finding_data.append(len(finding["authors"]))
            finding_data.append(len(finding["affiliations"]))
            finding_data.append(finding_key)
            dataset.append(finding_data)

    # call com,mon code to visualize data from given dataset
    visualize_data_circle(dataset, cols, "output/findings_clusters.json")

    # model = KMeans()
    # visualizer = KElbowVisualizer(model, k=(1, 5)).fit(df)
    # visualizer.show()
    
# create clusters based on author data considering author number of 
# publications and career duration
def visualize_author_data_circle():
    dataset = list()
    #  read the collected data from json file
    json_file = open("output/authors.json")
    author_info_map = json.load(json_file)
    json_file.close()

    cols=["nbr_pubs", "career_duration"]

    #  for authors with data, add to the dataset
    for author in author_info_map:
        author_info = author_info_map[author]["author_info"][author]
        author_data = list();
        if author_info["nbr_pubs"] > 0 and author_info["career_duration"]:
            author_data.append(author_info["nbr_pubs"])
            author_data.append(author_info["career_duration"])
            author_data.append(author)
            dataset.append(author_data)    
    
    # call com,mon code to visualize data from given dataset
    visualize_data_circle(dataset, cols, "output/author_clusters.json")

    # model = KMeans()
    # visualizer = KElbowVisualizer(model, k=(1, 5)).fit(df)
    # visualizer.show()

# create clusters based on university size and lab size
def visualize_lab_data_circle():
    dataset = list()
    affiliations = list()
    #  read the collected data from json file
    json_file = open("output/labs.json")
    labs_map = json.load(json_file)
    items = labs_map.keys()
    json_file.close()

    #  read the collected data from json file
    json_file = open("output/universityData.json")
    university_data_map = json.load(json_file)
    json_file.close()
    
    cols=["undergrad_student_count", "lab_size"]

    #  for each university/lab with data, add to the dataset
    for k in university_data_map:
        for item in items:
            if re.search(", " + k["Institution"], item):
                lab_data = list();
                if not item in affiliations and labs_map[item]["lab_size"] != None and k["UndergradStudentCount"] != None:
                    if labs_map[item]["lab_size"] > 0 and k["UndergradStudentCount"] > 0:
                        affiliations.append(item)
                        lab_data.append(k["UndergradStudentCount"])
                        lab_data.append(labs_map[item]["lab_size"])
                        lab_data.append(item)
                        dataset.append(lab_data)    

    # call com,mon code to visualize data from given dataset
    visualize_data_circle(dataset, cols, "output/lab_clusters.json")
    
    # model = KMeans()
    # visualizer = KElbowVisualizer(model, k=(1, 5)).fit(df)
    # visualizer.show()
    
if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add arguments
    parser.add_argument('--authors_data', action='store_true', default=False, help='A flag indicating that author data should be clustered.')
    parser.add_argument('--findings_data', action='store_true', default=False, help='A flag indicating that finding data should be clustered.')
    parser.add_argument('--lab_data', action='store_true', default=False, help='A flag indicating that lab data should be clustered.')
    parser.add_argument('--type', type=str, default="circle")

    # Parse the arguments
    args = parser.parse_args()
    
    # run a specific processing to generate clusters for different data
    if args.authors_data and args.type == "circle":
        visualize_author_data_circle()
    elif args.findings_data and args.type == "circle":
        visualize_finding_data_circle()
    elif args.lab_data and args.type == "circle":
        visualize_lab_data_circle()
