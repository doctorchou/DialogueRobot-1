from enum import Enum
import jieba
import os

# NLP模块的状态类
class Status(Enum):
    prepro = 1
    navi = 2
    que = 3
    reser = 4
    recom = 5
    unclear = 6

# NLP模块类
class Preprocess(object):
    def __init__(self, msg):
        self.status = Status.prepro
        self.msg = msg

        #载入自定义词典
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'myDict.txt')
        jieba.load_userdict(file_path)

    #todo
    #根据分词结果判断需求类型
    #可能需要进行词性分析标出地点等类型
    #这里单纯地使用if来判断不是一个好方法
    #我们需要用语义分析来辅助判断需求类型
    def MsgProcess(self):
        words = jieba.cut(self.msg)
        # 根据分词结果构建语法树
        # tree =
        # 根据语法树判断需求类型

        # 根据需求类型设置NLP状态和需求相关关键信息


        # 下面是简单的测试代码，只能简单判断需求类型，无法设置需求相关的关键信息，例如地点等
        for w in words:
            if w == "去" or w == "走":
                self.status = Status.navi
                break
            elif w == "活动":
                self.status = Status.recom
                break
            elif w == "天气":
                self.status = Status.que
                break
            elif w == "预约":
                self.status = Status.reser
                break

        if self.status == Status.prepro:
            self.status = Status.unclear










