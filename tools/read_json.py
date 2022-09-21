import json


class ReadJson(object):

    def __init__(self, filename):
        self.filename = "C:/Users/samjiang/Desktop/pk/date/" + filename

    def read_json(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    data = ReadJson("service_configuration.json").read_json()

    print(data)
