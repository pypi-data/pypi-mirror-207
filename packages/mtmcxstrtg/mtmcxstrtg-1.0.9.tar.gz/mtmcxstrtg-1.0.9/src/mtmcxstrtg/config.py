from mtmtool.io import read_yaml, read_json, json


class PyConfig(dict):
    def __init__(self, config_path: str, config_type="yaml") -> None:
        self.config_path = config_path
        self.config_type = config_type
        self._config_dict = {}
        self.read_config()
        pass

    def __getitem__(self, __name: str):
        if __name != "_config_dict" and __name in self._config_dict:
            return self._config_dict[__name]
        return dict.__getitem__(self, __name)

    def read_config(self):
        if self.config_type == "yaml":
            self._config_dict = read_yaml(self.config_path)
        if self.config_type == "json":
            self._config_dict = read_json(self.config_path)

    @staticmethod
    def dict2formattext(text_dict, separators=("\n", ":"), **kwargs):
        text_dict = {key: value for key, value in text_dict.items() if value is not None}

        # 获取最大长度
        keylen = max([len(str(key)) for key in text_dict.keys()]) + 1
        seplen = len(str(separators[1]))
        valuestrlen = max([len(str(value)) for value in text_dict.values() if isinstance(value, str)] + [0]) + 1
        valuefloatlen = max([
            len("{:.3f}".format(value))
            for value in text_dict.values() if isinstance(value, float) or isinstance(value, int)
        ] + [0]) + 1
        valuelen = max(valuestrlen, valuefloatlen)

        # 构造格式化字符串
        text_format = "{:<keylens}{:<seplens}{:>valuelens}"
        text_format = text_format.replace("keylen", str(keylen)) \
                                 .replace("seplen", str(seplen)) \
                                 .replace("valuelen", str(valuelen))

        # 构造文本
        text_list = []
        for key, value in text_dict.items():
            if isinstance(value, float):
                if key in ["profit"]:
                    value = "{:>valuelen.3%}".replace("valuelen", str(valuelen)).format(value)
                else:
                    value = "{:>valuelen.3f}".replace("valuelen", str(valuelen)).format(value)
            if isinstance(value, int):
                value = "{:>valuelend}".replace("valuelen", str(valuelen)).format(value)
            text_list.append(text_format.format(key, separators[1], value))
        return separators[0].join(text_list)


if __name__ == '__main__':
    c = PyConfig("src\grid_trading\examples\yaml.template")
    print(c["grid"]["id_preffix"])