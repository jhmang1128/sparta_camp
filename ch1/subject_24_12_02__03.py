import pandas as pd

# 데이터 로드
df_pop = pd.read_csv('./data/pop_kor.csv')
df_criminal = pd.read_excel('./data/관서별 5대범죄 발생 및 검거.xlsx')


office_dict = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
'서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
'혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
'마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
'광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
'강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
'구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
'방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}

# '구별' 열 추가
office_list = df_criminal.loc[:, '관서명']
temp_office_list = []
for i in office_list:
    try: temp_office_list.append(office_dict[i])
    except: temp_office_list.append('구 없음')
    
office_list = temp_office_list

test = df_criminal.insert(1, '구별', office_list)


# 구별 데이터 기준으로 sum 그룹바이
columns_list = list(df_criminal.columns)

df_criminal = pd.pivot_table(df_criminal,
                index = columns_list[1],
                values = columns_list[2:],
                aggfunc = 'sum'
                )

df_criminal = df_criminal.drop('구 없음')


# 검거율 열 6개 추가
category_list = ['강간', '강도', '살인', '소계', '절도', '폭력']
for cate in category_list:
    df_criminal[cate+'검거율'] = df_criminal[cate+'(검거)']/df_criminal[cate+'(발생)']

df_criminal = df_criminal.rename(columns = {'소계검거율' : '검거율'})


# 컬럼 삭제
drop_list = ['강간(검거)', '강도(검거)',
             '살인(검거)','절도(검거)',
             '폭력(검거)', '소계(발생)',
             '소계(검거)']

# df_criminal = df_criminal.drop(columns = drop_list)
for col in drop_list:
    del df_criminal[col]


# 컬럼 이름 변경
rename_dict = {'강간(발생)':'강간',
                '강도(발생)':'강도',
                '살인(발생)':'살인',
                '절도(발생)':'절도',
                '폭력(발생)':'폭력'}
df_criminal = df_criminal.rename(columns = rename_dict)

print(df_criminal)
exit()