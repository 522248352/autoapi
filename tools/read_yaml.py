import yaml

from config import BASE_PATH
import os

def read_yaml(fileName):
    file_path = os.path.join(BASE_PATH, 'data', fileName)
    # print(file_path)
    with open(file_path, "r+", encoding="utf-8") as f:
        datas = yaml.load_all(f.read(), Loader=yaml.SafeLoader)
        return datas



if __name__ == "__main__":
    a = read_yaml("sale.yml")
    for i in a:
        print(i)