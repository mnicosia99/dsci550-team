# Steps on how to run code 

# Data Collection
## scrape_data.py
scrape_data.py is a script that will extract various data related to the Bik et, al dataset.

Requirements:  lxml, alive_progress, requests_html, bs4, asyncio and pyppeteer.

### Running scrape_data.py
To run scrape_data.py it must be run in a single mode (collects features for a specific subject such as author data or lab data).  See subsections below for details.

#### Collecting author data
Publication Rate:<br/>
- Approach is to scrape data for each author in each article and count total number of publications for each author.

Other Journals Published In:<br/>
- Approach is to identify all journals the author was published in.

Duration of Career (Years):<br/> 
- Approach is to scrape data for each author and identify the start and end years that the author was publishing.  Subtract the start and end to get the numebr of years actively publishing.

Example:<br/>

    python3 scrape_data.py --author_data

Optionally, a start and end can be specified to run data collection for a subset of the rows in the Bik et, al dataset.

Example:<br/>

    python3 scrape_data.py --author_data --author_data_start 10 -author_data_end 20

#### Collecting lab data
Lab Size (number of students):<br/>
- Approach is to scrape all affiliations of each article and for each affiliation scrape all papers for the affiliated dept/university.  Using that information count how many authors are affiliated with the same dept/university.

Example:<br/>

    python3 scrape_data.py --affiliations

Optionally, a start and end can be specified to run data collection for a subset of the rows in the Bik et, al dataset.

Example:<br/>

    python3 scrape_data.py --affiliations --affiliations_start 10 -affiliations_end 20

#### Collecting affiliation data
Affiliation University:<br/>
- Approach is to scrape all articles and for each author for the papae, identify each authors affiliation(s).

Example:<br/>

    python3 scrape_data.py --bik_dataset

Optionally, a start and end can be specified to run data collection for a subset of the rows in the Bik et, al dataset.

Example:<br/>

    python3 scrape_data.py --bik_dataset --bik_dataset_start 10 -bik_dataset_end 20

#### Collecting U.S. Department of Education data data

Example:<br/>

    python institutions.py --inputCSV MERGED2019_20_PP.csv --outJSON universityData.json

#### Combine Collected Data witrh Bik et, al dataset
This combines all data json outputs to a single tsv.

Example:<br/>

    python mergingdata.py --input Bik_dataset-papers_with_endpoint_reached.tsv, findings.json, labs.json, authors.json, Affiliation.json, Career_Duration.json, Degree_Area.json, degrees.json, universityData (2).json, universities_ranking.json, citycrimestats.json, "uni_locations.json --output merged_data.tsv

# Data Visualization

## Tika-Similarity

For edit similarity refered to this link to reference [https://github.com/chrismattmann/tika-similarity] (https://github.com/chrismattmann/tika-similarity)

### Find similarities between rows 

The tikasimilarity folder holds 50 individual rows from the Bik et al dataset.  These rows will be used for the comparison.  The output will be to a csv file.

Example:<br/>

    python edit_value_similarity.py --fileInput tikasimilarity --outCSV edit_value_similarity.csv

### Transform csv into json labeled clusters
Examples:<br/>

    python edit-cosine-cluster.py --inputCSV edit_value_similarity.csv --cluster 0

    python edit-cosine-cluster.py --inputCSV edit_value_similarity.csv --cluster 1

    python edit-cosine-cluster.py --inputCSV edit_value_similarity.csv --cluster 2

### View clusters in Chrome web browser

Download the web server for Chrome at [https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb)

The web pages can be found in the edit_distance_clusterN folder where N is 1, 2 or 3.  Within the folder there is a clusters.json file and the html web page.  Navigate to the folder in the Web Server for Chrome and click on the html file to open the visualization.  This can be done for the 3 edit_distance_cluster folders.

## K-Means Clustering

### Collect Clustering Data

The k-means.py file located in the clustering directory provides a data collection capability using the k-means from the sklearn library.

Requirements:  sklearn, pandas, seaborn and matplotlib for some plot visulaizations.

There are 3 different modes to collect clustering data:  
- authors_data: considers the number of publications and the career duration of an author associated to the paper for clustering.
- findings_data: considers the number of authors and number of associated labs associated to the paper for clustering.
- lab_data: considers the number of undergraduate students at the university and the number of people working in the lab associated to the paper for clustering.

Example:<br/>

    python3 k-means.py --authors_data

    python3 k-means.py --findings_data

    python3 k-means.py --lab_data

The output will be a json file called circle.json.

### Visualize Clustering Data

To visualize the cluster data from k-means the tika-similarity project should be cloned from GitHub [https://github.com/chrismattmann/tika-similarity] (https://github.com/chrismattmann/tika-similarity).

Example:<br/>

    git clone https://github.com/chrismattmann/tika-similarity

Open a command line window and change to the tika-similarity directory that was cloned.  Copy the circle.json file into that directory and start a web server.

Example:<br/>

    python -m SimpleHTTPServer 7777

In Chrome web browser open the url http://localhost:7777/circlepacking.html