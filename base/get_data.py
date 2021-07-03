import yaml


def get_data():
    """获取yml数据"""
    with open("../data/data.yml", "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        result = []
        for key, val in data.items():
            result.append(tuple([val]))
        return result


if __name__ == '__main__':
    print(get_data())
