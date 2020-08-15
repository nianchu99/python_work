import curses
# random 模块用来生成随机数
from random import randrange, choice
# collections 提供了一个字典的子类 defaultdict。可以指定 key 值不存在时，value 的默认值。
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

# ord() 函数以一个字符作为参数，返回参数对应的 ASCII 数值，便于和后面捕捉的键位关联
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes, actions * 2))

def main(stdscr):

    def init():
        # 初始化游戏棋盘
        return 'Game'

    def not_game(state):
        '''画出 GameOver 或者 Win 的界面
        读取用户输入得到 action，判断是重启游戏还是结束游戏
        '''
        # 默认是当前状态，没有'Restart'或'Exit'行为就会一直保持当前状态
        responses = defaultdict(lambda: state)
        # 新建键值对，将行为和状态对应
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        # 画出当前棋盘状态
        # 读取用户输入得到 action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        # if 成功移动了一步:
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
    }

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()
# 阻塞＋循环，直到获得用户有效输入才返回对应行为：
def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        # 返回按下键位的 ASCII　码值
        char = keyboard.getch()
    # 返回输入键位对应的行为
    return actions_dict[char]
class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height       # 高
        self.width = width         # 宽
        self.win_value = 2048      # 过关分数
        self.score = 0             # 当前分数
        self.highscore = 0         # 最高分
        self.reset()               # 棋盘重置

    def spawn(self):#随机生成一个2或4
    # 从 100 中取一个随机数，如果这个随机数大于 89，new_element 等于 4，否则等于 2
        new_element = 4 if randrange(100) > 89 else 2
    # 得到一个随机空白位置的元组坐标
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def reset(self):#重置棋盘
    #更新分数
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        #初始化游戏开始界面
        self.field = [[0 for i in range (self.width) for j in range(self.height)]]
        self.spawn()
        self.spawn()

    def move_row_left(row):#一行向左合并 ## ?这一行括号中是self还是row ？
        def tighten(row):
            '''把零散的非零单元挤到一块'''
            # 先把非零的元素全拿出来加入到新列表
            new_row = [i for i in row if i != 0]
            new_row += [0 for i in range(len(row) - len(new_row))]
            return new_row

        def merge(row):
            '''对临近元素进行合并'''
            pair = False
            new_row = []
            for i in range(len(row)):
                if pair:
                    #合并后，加入乘2后的元素放在0元素后面
                    new_row.append(2 * row[i])
                    #更新分数
                    self.score += 2 *row[i]
                    pair =False
                else:
                    # 判断临近元素能否合并
                    if i + 1 <len(row) and row[i] == row[i + 1]:
                        pair = True
                        new_row.append(0)
                    else:
                        # 不能合并，新列表中加入该元素
                        new_row.append(row[i])
        # 断言合并后不会改变行列大小，否则会报错
            assert len(new_row) == len(row)
            return new_row
        # 先挤到一块再合并再挤到一块
        return tighten(merge(tighten(row)))
