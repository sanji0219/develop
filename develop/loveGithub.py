import datetime
import subprocess

# 現在の日付を取得
today = datetime.datetime.now().strftime('%Y-%m-%d')

# ファイルの内容を読み込む
with open('/Users/naitokota/develop/log.txt', 'r') as f:
    lines = f.readlines()
    lines.append("\n"+today)

# # ファイルに書き込む
with open('/Users/naitokota/develop/log.txt', 'w') as f:
    f.writelines(lines)

subprocess.run(['cd', '/Users/naitokota/develop/'], stdout=subprocess.PIPE)
subprocess.run(['git','add',"*"], stdout=subprocess.PIPE)
subprocess.run(['git','commit',"-m",today], stdout=subprocess.PIPE)
subprocess.run(['git','push'], stdout=subprocess.PIPE)