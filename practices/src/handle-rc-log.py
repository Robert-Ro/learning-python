import re
from datetime import datetime
import matplotlib.pyplot as plt


def read_file_lines(file_path):
    lines_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除每行末尾的换行符
            line = line.strip()
            lines_list.append(line)
    return lines_list


def replace_text(line):
    # 使用正则表达式进行替换
    pattern = r'\[(.*)\]\[D\](.*)'
    result = re.sub(pattern, lambda match: match.group(1), line)
    return result


lines = read_file_lines('./remoteDriveSrv.log')
filtered_lines = [
    item for item in lines if "当前档位:" in item
    ]

dates = []
for line in filtered_lines:
    dates.append(replace_text(line))


def time_gap(date1, date2):
    time_obj1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S.%f")
    time_obj2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S.%f")
    res =  float(time_obj2.timestamp()) - float(time_obj1.timestamp())
   
    return res



sub_dates = dates[1:]
prev_date = dates[0]
gaps = []
for item in sub_dates:
    gap = time_gap(prev_date, item)*1000
    gaps.append(int(gap))
    prev_date = item


def chart(data):
    # 生成横坐标列表，从0开始
    x = list(range(len(data)))

    # 绘制折线图
    plt.plot(x, data, marker='o', linestyle='-')

    # 添加标签和标题
    plt.xlabel('Index')
    plt.ylabel('Delay')
    plt.title('Command delay analysis')

    # 显示图表
    plt.show()
lst = [i for i in gaps if i == 0]
print(lst)

chart(gaps)
