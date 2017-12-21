class DataPH(object):
    """docstring for DataPH."""
    def __init__(self, data, hour):
        super(DataPH, self).__init__()
        self.data = data
        self.hour = hour

    def __str__(self):
        return "Hour: " + str(self.hour) + " Data: " + str(self.data)


data_list = [{"hour":17,"data":20},{"hour":17,"data":10},{"hour":17,"data":30},{"hour":18,"data":25},{"hour":18,"data":60},{"hour":19,"data":20},{"hour":19,"data":5},{"hour":20,"data":20},{"hour":20,"data":50}]

ant = -1
result = {"hour":0,"data":0}
result_list = []
print data_list
for d in data_list:
    h = d["hour"]
    if ant == -1:
        ant = h
    if ant != h:
        dph = DataPH(result["data"],result["hour"])
        result_list.append(dph)
        result["hour"] = 0
        result["data"] = 0
    result["hour"] = h
    result["data"] += d["data"]
    ant = h
dph = DataPH(result["data"],result["hour"])
result_list.append(dph)


for dph in result_list:
    print dph
