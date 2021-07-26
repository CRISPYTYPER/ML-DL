import pandas as pd

#엑셀 파일 열기
filename = "stat_104102.xls"
sheet_name = "Sheet0"
book = pd.read_excel(filename, sheet_name=sheet_name,header=1)

#2018년 인구로 정렬
book = book.sort_values(by=2018,ascending=False)
print(book)