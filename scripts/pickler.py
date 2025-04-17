import gitlab
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

    file_dir = os.getenv('CI_PROJECT_DIR')
    file_dir = file_dir+'/solution'

    gl = gitlab.Gitlab('https://app.dataops.live/snowflake/solutions/snowflake-labs-emerging-solutions-toolbox-63f264', private_token=os.getenv('GITLAB_TOKEN'))

    project = gl.projects.get(project_id)
    encoded_content = base64.b64encode("Hello World".encode('utf-8')).decode('utf-8')
    data = {
        'file_path': file_dir,
        'branch': "main",
        'content': encoded_content,
        'encoding': 'base64',
        'commit_message': "hello"
    }

    project.files.create(data)

    files_dict = {}



    for file in os.listdir(file_dir):
        print(file)
        # with open(file_dir + "/" + file, "rb") as current_file:
        #     files_dict[file] = current_file.read()

    obj = {
    "files": files_dict
    }

    # Encode object
    encoded_obj = encode(obj)

    # Print pickle string
    print(encoded_obj)

    with open(file_dir+"/pickle.txt", "w") as f:
      f.write("hello there")


if __name__ == '__main__':
  main()
