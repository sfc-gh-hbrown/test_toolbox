import gitlab
import os
import base64
import pickle
import codecs
import nbformat

def encode(obj):
    pickled = pickle.dumps(obj)
    return codecs.encode(pickled, 'base64').decode()   

def decode(obj):
    pickled = codecs.decode(obj.encode(), 'base64')
    return pickle.loads(pickled)

def read_files(file_dir, name, files_dict):
    
    for file in os.listdir(file_dir):
        full_file_path = file_dir + "/" + file
        if os.path.isdir(full_file_path):
            read_files(full_file_path, f'{name}{file}/', files_dict)
        else:
            with open(file_dir + "/" + file, "rb") as current_file:
                files_dict[name+file] = current_file.read()
    return files_dict
    
def main():

    file_dir = os.getenv('CI_PROJECT_DIR')
    script_dir = file_dir+"/scripts"
    file_dir = file_dir+'/solution'

    files_dict = {}



    # for file in os.listdir(file_dir):
    #     full_file_path = file_dir + "/" + file
    #     if os.path.isdir(full_file_path):
    #         pass
    #     else:
    #         with open(file_dir + "/" + file, "rb") as current_file:
    #             files_dict[file] = current_file.read()

    files_dict = read_files(file_dir, '', files_dict)

    obj = {
        "files": files_dict
    }
    print(obj["files"].keys())
    # Encode object
    encoded_obj = encode(obj)

    # Print pickle string
    # print(encoded_obj)

    with open(script_dir+"/install_test.ipynb", "r") as notebook:
	    nb = nbformat.read(notebook, as_version=4)

    for cell in nb.cells:
        if cell["metadata"]["name"] == "encoded_object":
            cell.source = f"\"\"\"{encoded_obj}\"\"\""
            # cell.source = f"\"\"\"Hello_World\"\"\""


    with open(script_dir+"/my_new_nb.ipynb", "w") as f:
        nbformat.write(nb, f)


if __name__ == '__main__':
  main()
