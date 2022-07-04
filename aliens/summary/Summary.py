import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
from xlutils.copy import copy

# 在网页上 ctrl + shift + i -> 网页 -> 刷新 (ctrl + R) -> 名称点第一个 -> 找到最后一个 user-agent -> copy 到下面引号中，改成dict格式
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'}
excel_path = "C:\\Users\\32021\\Desktop\\暑研\\Strategy_1734_AskNature.xlsx"   # 获取excel文件地址
old_excel = xlrd.open_workbook(excel_path, encoding_override="utf-8")

sheet = old_excel.sheets()[0]   # 读取第1张工作表

new_excel = copy(old_excel)   # 备份excel用于修改
new_sheet = new_excel.get_sheet(0)   # 获取第一张sheet

sheet_row_mount = sheet.nrows
sheet_col_mount = sheet.ncols

print("该工作表有{0}行，{1}列".format(sheet_row_mount, sheet_col_mount))
# row =
col = 0   # 第一行为网址
# 限定行/列

for row in range(1,575):
    cell = sheet.cell(row, col)
    URL = cell.value   # 返回单元格的值
    html = requests.get(URL, headers=header)
    soup = BeautifulSoup(html.text, "html.parser")
    sum = soup.select('#post-content > div.wrap.text-wrap.post-hook > q')
    for sum in sum:
        sum = sum.get_text()   # 消除文本以外其他内容
        new_sheet.write(row, 8, str(sum))   # 填回到备份表的第8列
        print(sum)   # print出来实时观察结果

new_excel.save('Strategy_1734_AskNature.xls')   # 保存修改好的备份表

