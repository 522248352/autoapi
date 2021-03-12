import yaml


def read_yaml(filePath):
    with open(filePath, "r+", encoding="utf-8") as f:
        datas = yaml.load_all(f.read(), Loader=yaml.SafeLoader)
        return datas



if __name__ == "__main__":
    a = read_yaml("../data/sale.yml")
    for i in a:
        print(i)