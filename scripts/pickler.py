import os
import base64
import pickle
import codecs


def main():
    file_dir = os.getenv('CI_PROJECT_DIR')
    file_dir = file_dir+'/solution'
    for file in os.listdir(file_dir):
        print(file)


if __name__ == '__main__':
  main()
