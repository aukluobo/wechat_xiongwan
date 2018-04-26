import os
import sys

class user:
    def __init__(self):
        self.time='1m' # 1h 是一个小时，1m是一分钟，以此类推
        self.user=[] #设置你想要发的人，写他在你在微信上的备注名，用单引号括起来，多个人用逗号分开,注意标点符号要在“英文状态”下输入，不然会报错
        self.userSepecial={}  #默认发送下面的message，但是可以在这里给特定的人设置不一样的信息
        self.message="快交表！！"
        #在你设置的时间间隔里，修改这个文件就会影响下一次的发送消息。
        #如果不需要发送了，就把user和userSpecial里面清空，只留下[]和{},然后就会自动结束了。
