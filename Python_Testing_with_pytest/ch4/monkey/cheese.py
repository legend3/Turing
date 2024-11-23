import os
import json


def read_cheese_preferences():
    full_path = os.path.expanduser(
        "~/.cheese.json"
    )  # 扩展Administrator目录    (cmd根目录：/)
    # full_path = os.path.abspath('C:\\Users\\Administrator\\.cheese.json')
    with open(full_path, "r") as f:
        prefs = json.load(f)
    return prefs


def write_cheese_preferences(prefs):
    full_path = os.path.expanduser("~/.cheese.json")  # 切换到指定默认根目录的扩展目录下
    # full_path = os.path.abspath('C:\\Users\\Administrator\\.cheese.json')
    with open(full_path, "w") as f:
        json.dump(prefs, f, indent=4)


# 让我们来看看如何测试write_default_cheese_preferences()。
# 它是一个不带参数且不返回任何东西的函数。
# 但它确实有我们可以测试的副作用。它将文件写入当前用户的主目录。
def write_default_cheese_preferences():
    write_cheese_preferences(_default_prefs)


_default_prefs = {
    "slicing": ["manchego", "sharp cheddar"],
    "spreadable": [
        "Saint Andre",
        "camembert",
        "bucheron",
        "goat",
        "humbolt fog",
        "cambozola",
    ],
    "salads": ["crumbled feta"],
}

if __name__ == "__main__":
    write_default_cheese_preferences()
