# Scss Generator

MULTIPLE_PROPERTIES_CLASS = {
    "mx" : ("margin-left", "margin-right"),
    "my" : ("margin-top", "margin-bottom"),
    "px" : ("padding-left", "padding-right"),
    "py" : ("padding-top", "padding-bottom"),
}

SIGLE_PROPERTI_CLASS = {
    "mt" : "margin-top",
    "mr" : "margin-right",
    "mb" : "margin-bottom",
    "ml" : "margin-left",
    "pt" : "padding-top",
    "pr" : "padding-right",
    "pb" : "padding-bottom",
    "pl" : "padding-left",
}

# 디자인 시스템에서 사용하는 간격이 4배수 값
spacing_multiple = 4
size_list = [x for x in range(1, 100) if x % spacing_multiple == 0]
    
# Abstraction
class SIGLE_PROPERTIY_UTILITY:
    _data:dict = {}
    
    def __init__(self, data:dict):
        self._data = data

    def generateSCSS(self, px_size_list:list, file_name: str = "utility.scss"):
        if (len(px_size_list) < 0):
            raise Exception("px_size_list is empty")

        for size in px_size_list:
            for class_name, propertiy in self._data.items():
                with open(f"./dist/{file_name}", "a+") as f:
                    f.write(f".{class_name}-{size}{{{propertiy}: {size}px;}}")

class DOUBLE_PROPERTIY_UTILITY:
    _data:dict = {}
    
    def __init__(self, data:dict):
        self._data = data

    def generateSCSS(self, px_size_list:list, file_name: str = "utility.scss"):
        if (len(px_size_list) < 0):
            raise Exception("px_size_list is empty")

        for size in px_size_list:
            for class_name, properties in MULTIPLE_PROPERTIES_CLASS.items():
                with open(f"./dist/{file_name}", "a+") as f:
                    f.write(f".{class_name}-{size}{{{properties[0]}: {size}px; {properties[1]}: {size}px;}}")

# TODO multiple property utility