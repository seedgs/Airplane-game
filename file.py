import pickle


# filename = 'file/stats.pkl'
# 存储信息到文件
def save_file(obj, filename):
    statsObj = load_file(filename)
    if statsObj == 0:
        # 不存在文件时，直接保存字典
        with open(filename, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    else:
        # 存在文件时，只修改文件中的最高分
        for key, val in statsObj.items():
            # 获取文件最高分的值（当文件字段不止一个时候使用）
            if key == 'highScore':
                statsObj[key] = obj['highScore']
        obj = statsObj
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


# 读取信息
def load_file(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        # 不存在文件则输入错误信息
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)

