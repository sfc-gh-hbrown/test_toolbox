import os
import base64
import pickle
import codecs

def encode(obj):
    pickled = pickle.dumps(obj)
    return codecs.encode(pickled, 'base64').decode()   

def decode(obj):
    pickled = codecs.decode(obj.encode(), 'base64')
    return pickle.loads(pickled)



def main():

    files_dict = {}

    file_dir = os.getenv('CI_PROJECT_DIR')
    file_dir = file_dir+'/solution'

    for file in os.listdir(file_dir):
        with open(file_dir + "/" + file, "rb") as current_file:
            files_dict[file] = current_file.read()

    obj = {
    "files": files_dict,
    "images": images_base64_dict
    }

    # Encode object
    encoded_obj = encode(obj)

    # Print pickle string
    print(encoded_obj)

    with open(file_dir+/"pickle.txt", "w") as f:
      f.write(encoded_obj)


if __name__ == '__main__':
  main()
