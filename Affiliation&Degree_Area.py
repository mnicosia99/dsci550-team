import requests
import json
from lxml import etree
from lxml.html.soupparser import fromstring

min_row = 0
max_row =216



affiliations = list()
findings = list()

bik_tsv_dataset_name = "Bik_dataset-papers_with_endpoint_reached.tsv"
bf = open(bik_tsv_dataset_name, encoding="utf-8")

bik_dataset_column_headers = dict()
bik_dataset_column_headers['authors'] = 0
bik_dataset_column_headers['title'] = 1
bik_dataset_column_headers['citation'] = 2
bik_dataset_column_headers['doi'] = 3
bik_dataset_column_headers['year'] = 4
bik_dataset_column_headers['month'] = 5
bik_dataset_column_headers['dup'] = 6
bik_dataset_column_headers['dup_with_repos'] = 7
bik_dataset_column_headers['dup_with_alter'] = 8
bik_dataset_column_headers['cut_beautification'] = 9
bik_dataset_column_headers['findings'] = 10
bik_dataset_column_headers['reported'] = 11
bik_dataset_column_headers['correction_date'] = 12
bik_dataset_column_headers['retraction'] = 13
bik_dataset_column_headers['correction'] = 14
bik_dataset_column_headers['no_action'] = 15


# for each row in the dataset, extract useful data and query url for additional data
Affiliation = []
Degree_Area = []
for position, line in enumerate(bf):
    if (position) > min_row and (position) <= max_row:
        authors = list()
        affiliations = list()

        row_data = line.split("\t")
        authors_data = row_data[bik_dataset_column_headers['authors']].replace('and', '').replace('"', '').split(",")
        title = row_data[bik_dataset_column_headers['title']].strip()
        citation = row_data[bik_dataset_column_headers['citation']].strip()

        #Find paper in PubMed
        doi = row_data[bik_dataset_column_headers['doi']].strip().replace('�','-')
        if doi == '10.1016/S0169-5002(01)00212-4':
            url = 'https://pubmed.ncbi.nlm.nih.gov/11557119/'
        elif doi == '10.1016/S0169-5002(03)00239-3':
            url = 'https://pubmed.ncbi.nlm.nih.gov/12928127/'
        else:
            url = ('https://pubmed.ncbi.nlm.nih.gov/?term='+ doi)
        page =  requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        xpath_filter = './/a[@class="affiliation-link"]/@title'
        root = fromstring(page.text)
        nodes = root.xpath(xpath_filter)
        if nodes != []:
            words = nodes[0].split(',')
            if url == 'https://pubmed.ncbi.nlm.nih.gov/?term=10.1371/journal.pone.0071127':
                school = 'University of Glasgow School of Medicine'
                dep = 'Institute of Medical Genetics, Yorkhill Hospital'
            elif url == 'https://pubmed.ncbi.nlm.nih.gov/24176123/':
                school = 'Baylor College of Medicine'
                dep = 'Molecular and Cellular Biology; Education, Innovation and Technology (EIT)'
            elif url == 'https://pubmed.ncbi.nlm.nih.gov/22995475/':
                school = 'McGill University Health Center'
                dep = 'Division of Medical Oncology, Department of Medicine'
            elif url == 'https://pubmed.ncbi.nlm.nih.gov/23786849/':
                school = 'McGill University Health Center'
                dep = 'Division of Medical Oncology, Department of Medicine'
            elif url == 'https://pubmed.ncbi.nlm.nih.gov/25022892/':
                school = 'University of Saskatchewan'
                dep = 'Department of Microbiology and Immunology'
            else:
                for word in words:
                    if 'University' in word or "College" in word or 'Universidad' in word or 'Pfizer' in word or 'Blood Transfusion' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Centre' in word and 'Department' not in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Medical School' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'National Medicines' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Virginia Tech' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Chinese Academy' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'National Institutes of Health' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'IDIBELL' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Université' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'National Jewish Medical and Research Center' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'National Institute of Health' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Universitätsklinikum' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Faculté de Médecine' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Universitario' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Crete Veterinary Clinic' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Universiti' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Centro de Investigación ' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Università' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Indian Veterinary Research Institute' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'National Institute of Biomedical Genomics' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Royal Adelaide Hospital and Hanson Institute' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Yale School of Medicine' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Department of Medical Research' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Academy of Sciences of the Czech Republic' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Center of Excellence in Sickle Cell Disease and Division of Hematology/Oncology' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Dana-Farber Cancer Institute' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'National Center for Cell Science' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'Institut National de la Santé et de la Recherche Médicale' in word:
                        school = word
                        department = words[:words.index(school)]

                    elif 'IRCCS Istituto Scientifico Romagnolo per lo Studio e la Cura dei Tumori' in word:
                        school = word
                        department = words[:words.index(school)]
                if department == []:
                    department.append(school)
                dep =  ",".join(str(x) for x in department)
            school_dict = {}
            school_dict[row_data[bik_dataset_column_headers['authors']]] = school
            dep_dict = {}
            dep_dict[row_data[bik_dataset_column_headers['authors']]] = dep
            Affiliation.append(school_dict)
            Degree_Area.append(dep_dict)

            out_file = open("Affiliation.json", "w")
            json.dump(Affiliation, out_file, indent = 4)
            out_file.close()

            out_file = open("Degree_Area.json", "w")
            json.dump(Degree_Area, out_file, indent = 4)
            out_file.close()
            
