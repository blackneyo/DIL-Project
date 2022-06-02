import pandas
import DIL
datas = pandas.read_csv('./Sample/test_100.csv', index_col=0)
print(datas.head())

datas = pandas.read_csv('./Sample/test_100.csv')


# 삭제 기술 - 일반 삭제
# from DIL import Suppression
DIL.suppression(datas).general(["이름", "생년월일", "성별", "직업"])

print(datas.head())