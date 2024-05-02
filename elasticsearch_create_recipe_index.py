from elasticsearch import Elasticsearch
import pandas as pd
import os
from config_reader import fetch_config_dict

# Function to delete the existing index
def delete_index(es, index_name):
    """
    This function is used to delete the existing Elasticsearch index
    in order to create a new one.

    Input : ElasticSearch object, name of index to be deleted.
    """

    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        print(f"Deleted index: {index_name}")


# Function to create a new index and ingest data from the CSV file
def create_index(es, index_name, csv_file, recipe_section_dict):
    """
    This function is used to create an Elasticsearch index
    after deletion (or for the first time).

    Input : ElasticSearch object, name of index to be created, path of csv file containing data 
    """

    with open(csv_file, mode='r', encoding='utf-8') as file:
        #reader = csv.DictReader(file)
        reader = pd.read_csv(csv_file)
        reader = preprocessing_pipeline(reader, recipe_section_dict)
        for index, row in reader.iterrows():
            # Convert the row to a dictionary
            row = row.fillna("")
            doc = row.to_dict()
            es.index(index=index_name, body=doc)
    print(f"Ingested data from {csv_file} into index: {index_name}")


def list_stripper(column_data):
    """
    This function returns a stripped list
    
    Used for cleaning
    """

    if isinstance(column_data, list):
        return [x.strip() for x in column_data if isinstance(x, str)]
    return column_data


def list_splitter(column_data):
    """
    This function splits the column data on ',' if it is a string.

    This function is used if the csv does not have list type data in expected columns.

    Returns a list.
    """

    if isinstance(column_data, str) and len(column_data) > 0:
        if ',' in column_data:
            return list_stripper(column_data.split(','))
        return [column_data]
    
    elif column_data is None or len(column_data)==0:
        return []
    
    else:
        return [column_data]

#Function to preprocess the csv data
def preprocessing_pipeline(df, recipe_section_dict):
    """
    This function serves as the preprocessing pipeline for the input csv file.
    Input : Pandas DataFrame
    Output : Pandas DataFrame
    """

    list_type_data = list_splitter(recipe_section_dict.get('list_type_recipe_data', []))
    

    for column in list_type_data:
        df[column] = df[column].apply(list_splitter)
    
    return df

def main():
    """
    This script is used to 
    1. Delete existing RECIPE INDEX
    2. Create RECIPE INDEX from a CSV file.
    """
    # Load config dict.
    config_dict = fetch_config_dict()
    recipe_section_dict = fetch_config_dict(section = 'RECIPE_INDEX_OBJECTS')

    # Elasticsearch connection
    es = Elasticsearch([{'host': config_dict.get('host',''), 
                         'port':int(config_dict.get('port','9200')), 
                         'scheme':config_dict.get('scheme', '')}], 
                         timeout=30, max_retries=10, retry_on_timeout=True)
    
    print("Connected to ElasticSearch")
    #print("Connected to ElasticSearch", es.info())



    # Name of the index to be created
    index_name = config_dict.get("recipe_index_name", "recipe_index")

    # CSV file containing recipe data
    csv_file = config_dict.get("recipe_csv","SyntheticRecipes.csv")

    file_path = os.path.expanduser("~/Desktop/" + csv_file)
    # Delete existing index
    delete_index(es, index_name)

    # Create new index and ingest data from CSV
    create_index(es, index_name, file_path, recipe_section_dict)

if __name__ == "__main__":
    main()


