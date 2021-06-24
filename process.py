import os
import hjson
import dataset

db = dataset.connect('sqlite:///./data/udise_schools.sqlite')
table = db["udise_schools"]


raw_data_folder = "./raw/"
raw_data_file_name = "./raw/{file_name}"
data_folder = "./data/"

def get_data_files():
    l = os.listdir(raw_data_folder)
    l.sort()
    return l

def process_file(file_name):
    print("Processing {file_name}".format(file_name=file_name))
    source_raw_data_file_path = raw_data_file_name.format(file_name=file_name)
    file_obj = open(source_raw_data_file_path, "r")    
    file_data = file_obj.read()
    file_obj.close()
    
    data = hjson.loads(file_data)
    insert_array = []
    for feature in data["features"]:
        record = feature["properties"]
        record["id"] = feature["id"]
        record["lon"] = feature["geometry"]["coordinates"][0]
        record["lat"] = feature["geometry"]["coordinates"][1]
        insert_array.append(record)
    table.insert_many(insert_array)      

def main():
    file_list = get_data_files()
    for file_name in file_list:
        process_file(file_name)   

if __name__ == "__main__":
    main()