#!/usr/bin/env python
# coding: utf-8

# # Pandas 한번에 제대로 배우기
# 

# 
# 
# ---
# 
# 

# In[2]:


import numpy as np
import pandas as pd
pd.__version__


# ## Pandas 객체
# 

# ### Series 객체

# In[2]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
s


# In[3]:


s.values


# In[4]:


s.index


# In[5]:


s[1]


# In[6]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
              index=['a', 'b', 'c', 'd', 'e'])
s


# In[7]:


s['c']


# In[8]:


s[['c', 'd', 'e']]


# In[9]:


'b' in s


# In[10]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
              index=[2, 4, 6, 8, 10])
s


# In[11]:


s[4]


# In[12]:


s[2:]


# In[13]:


s.unique()


# In[14]:


s.value_counts()


# In[15]:


s.isin([0.25, 0.75])


# In[16]:


pop_tuple = {'서울특별시' : 9720846,
            '부산광역시' : 3404423,
            '인천광역시' : 2947217,
            '대구광역시' : 2427954,
            '대전광역시' : 1471040,
            '광주광역시' : 1455048}
population = pd.Series(pop_tuple)
population


# In[17]:


population['서울특별시']


# In[18]:


population['서울특별시' : '인천광역시']


# ### DataFrame 객체

# In[19]:


pd.DataFrame([{'A' : 2, 'B' : 4, 'D' : 3}, {'A': 4, 'B': 5, 'C': 7}])


# In[20]:


pd.DataFrame(np.random.randn(5, 5),
            columns=['A', 'B', 'C', 'D', 'E'],
            index=[1, 2, 3, 4, 5])


# In[21]:


female_tuple = {'서울특별시' : 4988571,
               '부산광역시' : 1735805,
               '인천광역시' : 1470404,
               '대구광역시' : 1229139,
               '대전광역시' : 736599,
               '광주광역시' : 734988}
female = pd.Series(female_tuple)
female


# In[22]:


male_tuple = {'서울광역시' : 4732275,
             '부산광역시' : 1668618,
             '인천광역시' : 1476813,
             '대구광역시' : 1198815,
             '대전광역시' : 734441,
             '광주광역시' : 720060}
male = pd.Series(male_tuple)
male


# In[23]:


korea_df = pd.DataFrame({'인구수': population,
                        '남자인구수': male,
                        '여자인구수' : female})
korea_df


# In[24]:


korea_df.index


# In[25]:


korea_df.columns


# In[26]:


korea_df['여자인구수']


# In[27]:


korea_df['서울특별시':'인천광역시']


# ### Index 객체
# 

# In[28]:


idx = pd.Index([2, 4, 6, 8, 10])
idx


# In[29]:


idx[1]


# In[30]:


idx[1:2:2]


# In[31]:


idx[-1::]


# In[32]:


idx[::2]


# In[33]:


print(idx)
print(idx.size)
print(idx.shape)
print(idx.ndim)
print(idx.dtype)


# #### Index 연산

# 
# 
# ---
# 
# 

# In[34]:


idx1 = pd.Index([1, 2, 4, 6, 8])
idx2 = pd.Index([2, 4, 5, 6, 7])
print(idx1.append(idx2))
print(idx1.difference(idx2))
print(idx1 - idx2)
print(idx1.intersection(idx2))
print(idx1 & idx2)
print(idx1.union(idx2))
print(idx | idx2)
print(idx1.delete(0))
print(idx1.drop(1))
print(idx1 ^ idx2)


# ## 인덱싱(Indexing)

# In[35]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
             index=['a', 'b', 'c', 'd', 'e'])
s


# In[36]:


s['b']


# In[37]:


'b' in s


# In[38]:


s.keys()


# In[39]:


list(s.items())


# In[40]:


s['f'] = 1.25
s


# In[41]:


s['a' : 'd']


# In[42]:


s[0:4]


# In[43]:


s[(s>0.4) & (s<0.8)]


# In[44]:


s[['a','c','e']]


# ### Series 인덱싱

# In[45]:


s = pd.Series(['a','b','c','d','e'],
             index=[1,3,5,7,9])
s


# In[46]:


s[1]


# In[47]:


s[2:4]


# In[48]:


s.iloc[1]


# In[49]:


s.iloc[2:4]


# In[50]:


s.reindex(range(10))


# In[51]:


s.reindex(range(10), method='bfill')


# ### DataFrame 인덱싱
# 

# In[52]:


korea_df


# In[53]:


korea_df['남자인구수']


# In[54]:


korea_df.남자인구수


# In[55]:


korea_df.여자인구수


# In[56]:


korea_df['남녀비율'] = (korea_df['남자인구수'] * 100 / korea_df['여자인구수'])


# In[57]:


korea_df.남녀비율


# In[58]:


korea_df.values


# In[59]:


korea_df.T


# In[60]:


korea_df.values[0]


# In[61]:


korea_df['인구수']


# In[62]:


korea_df.loc[:'인천광역시', :'남자인구수']


# In[63]:


korea_df.loc[(korea_df.여자인구수 > 1000000)]


# In[64]:


korea_df.loc[(korea_df.인구수 > 2000000)]


# In[65]:


korea_df.loc[(korea_df.인구수 > 2500000)]


# In[66]:


korea_df.loc[korea_df.남녀비율 > 100]


# In[67]:


korea_df.loc[(korea_df.인구수 > 2500000) & (korea_df.남녀비율 > 100)]


# In[68]:


korea_df.iloc[:3, :2]


# ### 다중 인덱싱(Multi Indexing)
# 
# * 1차원의 Series와 2차원의 DataFrame 객체를 넘어 3차원, 4차원 이상의 고차원 데이터 처리
# * 단일 인덱스 내에 여러 인덱스를 포함하는 다중 인덱싱

# #### 다중 인덱스 Series

# In[69]:


korea_df


# In[70]:


idx_tuples = [('서울특별시', 2010), ('서울특별시', 2020),
             ('부산광역시', 2010), ('부산광역시', 2020),
             ('인천광역시', 2010), ('인천광역시', 2020),
             ('대구광역시', 2010), ('대구광역시', 2020),
             ('대전광역시', 2010), ('대전광역시', 2020),
             ('광주광역시', 2010), ('광주광역시', 2020)]
idx_tuples


# In[71]:


pop_tuples = [10312545, 9720846,
             2567810, 3404423,
             2758296, 2947217,
             2511676, 2427954,
             1503664, 1471040,
             1454636, 1455048]
population = pd.Series(pop_tuples, index=idx_tuples)
population


# In[72]:


midx = pd.MultiIndex.from_tuples(idx_tuples)
midx


# In[73]:


population = population.reindex(midx)
population


# In[74]:


population[:, 2010]


# In[75]:


population['대전광역시', :]


# In[76]:


korea_mdf = population.unstack()
korea_mdf


# In[77]:


korea_mdf.stack()


# In[78]:


male_tuples = [5111259, 4732275,
              1773170, 1668618,
              1390356, 1476813,
              1255245, 1198815,
              753648, 734441,
              721780, 720060]
male_tuples


# In[79]:


korea_mdf = pd.DataFrame({'총인구수' : population,
                         '남자인구수' : male_tuples})
korea_mdf


# In[80]:


female_tuples = [5201286, 4988571,
                1794740, 1735805,
                1367940, 1470404,
                1257431, 1229139,
                750016, 736599,
                732856, 734988]
female_tuples


# In[81]:


korea_mdf = pd.DataFrame({'총인구수' : population,
                         '남자인구수' : male_tuples,
                         '여자인구수' : female_tuples})
korea_mdf


# In[82]:


ratio = korea_mdf['남자인구수'] * 100 / korea_mdf['여자인구수']
ratio


# In[83]:


ratio.unstack()


# In[84]:


korea_mdf = pd.DataFrame({'총인구수' : population,
                         '남자인구수' : male_tuples,
                         '여자인구수' : female_tuples,
                         '남녀비율' :ratio})
korea_mdf


# #### 다중 인덱스 생성

# In[85]:


df = pd.DataFrame(np.random.rand(6, 3),
                 index=[['a', 'a', 'b', 'b', 'c', 'c'], [1,2,1,2,1,2]],
                 columns=['c1', 'c2', 'c3'])
df


# In[86]:


pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b',' c', 'c'], [1,2,1,2,1,2]])


# In[87]:


pd.MultiIndex.from_arrays([('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)])


# In[88]:


pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2]])


# In[89]:


pd.MultiIndex(levels=[['a', 'b', 'c'], [1, 2]],
             codes=[[0,0,1,1,2,2],[0,1,0,1,0,1]])


# In[90]:


population


# In[91]:


population.index.names = ['행정구역', '년도']
population


# In[92]:


idx = pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2]],
                                names=['naem1', 'name2'])
cols = pd.MultiIndex.from_product([['c1', 'c2', 'c3'], [1, 2]],
                                 names=['col_name1', 'col_name2'])
data = np.round(np.random.randn(6, 6), 2)
mdf = pd.DataFrame(data, index=idx, columns=cols)
mdf


# In[93]:


mdf['c2']


# #### 인덱싱 및 슬라이싱

# In[94]:


population['인천광역시', 2010]


# In[95]:


population[:, 2010]


# In[96]:


population[population > 3000000]


# In[97]:


population[['대구광역시', '대전광역시']]


# In[98]:


mdf


# In[99]:


mdf['c2', 1]


# In[100]:


mdf.iloc[:3, :4]


# In[101]:


mdf.loc[:, ('c2', 1)]


# In[102]:


idx_slice = pd.IndexSlice
mdf.loc[idx_slice[:, 2], idx_slice[:, 2]]


# #### 다중 인덱스 재정렬

# In[103]:


korea_mdf


# In[104]:


korea_mdf = korea_mdf.sort_index()
korea_mdf


# In[105]:


korea_mdf['서울특별시' : '인천광역시']


# In[106]:


korea_mdf.unstack(level=0)


# In[107]:


korea_mdf.unstack(level=1)


# In[108]:


korea_mdf.stack()


# In[109]:


korea_mdf


# In[110]:


idx_flat = korea_mdf.reset_index(level=0)
idx_flat


# In[111]:


idx_flat = korea_mdf.reset_index(level=(0,1))
idx_flat


# In[112]:


idx_flat.set_index(['행정구역', '년도'])


# ## 데이터 연산

# In[113]:


s = pd.Series(np.random.randint(0, 10, 5))
s


# In[114]:


df = pd.DataFrame(np.random.randint(0, 10, (3, 3)),
                 columns=['A', 'B', 'C'])
df


# In[115]:


np.exp(s)


# In[116]:


np.cos(df * np.pi / 4)


# In[117]:


s1 = pd.Series([1, 3, 5, 7, 9], index=[0, 1, 2, 3, 4])
s2 = pd.Series([2, 4, 6, 8, 10], index=[1, 2, 3, 4, 5])
s1 + s2


# In[118]:


s1.add(s2, fill_value=0)


# In[122]:


df1 = pd.DataFrame(np.random.randint(0, 20, (3, 3)),
                  columns=list('ACD'))
df1


# In[123]:


s1.add(s2, fill_value=0)


# In[125]:


df2 = pd.DataFrame(np.random.randint(0, 20, (5, 5)),
                  columns=list('BAECD'))
df2


# In[126]:


df1 + df2


# In[127]:


fvalue = df1.stack().mean()
df1.add(df2, fill_value=fvalue)


# ### 연산자 범용 함수
# 

# #### add()

# In[128]:


a = np.random.randint(1, 10, size=(3, 3))
a


# In[129]:


a + a[0]


# In[130]:


df = pd.DataFrame(a, columns=list('ABC'))
df


# In[131]:


df + df.iloc[0]


# In[132]:


df.add(df.iloc[0])


# #### sub() / subtract()

# In[133]:


a


# In[134]:


a - a[0]


# In[135]:


df


# In[136]:


df - df.iloc[0]


# In[137]:


df.sub(df.iloc[0])


# In[139]:


df.subtract(df['B'], axis=0)


# #### mul() / multply()
# 
# 
# 

# In[140]:


a


# In[141]:


a * a[1]


# In[142]:


df


# In[143]:


df * df.iloc[1]


# In[144]:


df.mul(df.iloc[1])


# In[145]:


df.multiply(df.iloc[2])


# #### truediv() /  div() / divide() / floordiv()

# In[146]:


a


# In[147]:


a / a[0]


# In[148]:


df


# In[149]:


df / df.iloc[0]


# In[150]:


df.truediv(df.iloc[0])


# In[151]:


df.div(df.iloc[1])


# In[152]:


df.divide(df.iloc[2])


# In[153]:


a // a[0]


# In[154]:


df.floordiv(df.iloc[0])


# #### mod()

# In[155]:


a


# In[156]:


a % a[0]


# In[157]:


df


# In[158]:


df.mod(df.iloc[0])


# #### pow()

# In[159]:


a


# In[160]:


a ** a[0]


# In[161]:


df


# In[162]:


df.pow(df.iloc[0])


# In[163]:


row = df.iloc[0, ::2]
row


# In[164]:


df - row


# ### 정렬(Sort)

# In[166]:


s = pd.Series(range(5), index=['A', 'B', 'C',' D', 'E'])
s


# In[167]:


s.sort_index()


# In[168]:


s.sort_values()


# In[169]:


df = pd.DataFrame(np.random.randint(0, 10, (4, 4)),
                 index=[2, 4, 1, 3],
                 columns=list('BDAC'))
df


# In[170]:


df.sort_index()


# In[171]:


df.sort_index(axis=1)


# In[172]:


df.sort_values(by='A')


# In[173]:


df.sort_values(by=['A', 'C'])


# ### 순위(Ranking)
# 

# In[175]:


s = pd.Series([-2, 4, 7, 3, 0, 7, 5, -4, 2, 6])


# In[176]:


s.rank()


# In[177]:


s.rank(method='first')


# In[178]:


s.rank(method='max')


# ### 고성능 연산

# In[179]:


nrow, ncols = 100000, 100
df1, df2, df3, df4 = (pd.DataFrame(np.random.rand(nrow, ncols)) for i in range(4))


# In[180]:


get_ipython().run_line_magic('timeit', 'df1 + df2 + df3 + df4')


# In[181]:


get_ipython().run_line_magic('timeit', "pd.eval('df1 + df2 + df3 + df4')")


# In[182]:


get_ipython().run_line_magic('timeit', 'df1* -df2 / (-df3 * df4)')


# In[183]:


get_ipython().run_line_magic('timeit', "pd.eval('df1 * -df2 / (-df3 * df4)')")


# In[184]:


get_ipython().run_line_magic('timeit', '(df1 < df2) & (df2 <= df3) & (df3 != df4)')


# In[185]:


get_ipython().run_line_magic('timeit', "pd.eval('(df1 < df2) & (df2 <= df3) & (df3 != df4)')")


# In[186]:


df = pd.DataFrame(np.random.rand(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.head()


# In[187]:


get_ipython().run_line_magic('timeit', "df['A'] + df['B'] / df['C'] - df['D'] * df['E']")


# In[188]:


get_ipython().run_line_magic('timeit', "pd.eval('df.A + df.B / df.C - df.D * df.E')")


# In[189]:


get_ipython().run_line_magic('timeit', "df.eval('A + B / C - D * E')")


# In[190]:


df.eval('R = A + B / C - D * E', inplace=True)
df.head()


# In[191]:


col_mean =df.mean(1)
df['A'] * col_mean


# In[192]:


df.eval('A + @col_mean')


# In[193]:


df[(df.A < 0.5) & (df.B < 0.5) & (df.C > 0.5)]


# In[194]:


pd.eval('df[(df.A < 0.5) & (df.B < 0.5) & (df.C > 0.5)]')


# In[195]:


df.query('(A < 0.5) and (B < 0.5) and (C > 0.5)')


# In[196]:


col_mean = df['D'].mean()
df[(df.A < col_mean) & (df.B < col_mean)]


# In[197]:


df.query('A < @col_mean and B < @col_mean')


# ## 데이터 결합

# ### Concat() / Append()

# In[199]:


s1 = pd.Series(['a', 'b'], index=[1, 2])
s2 = pd.Series(['c', 'd'], index=[3, 4])
pd.concat([s1, s2])


# In[201]:


def create_df(cols, idx):
    data = {c: [str(c.lower()) + str(i) for i in idx] for c in cols}
    return pd.DataFrame(data, idx)


# In[203]:


df1 = create_df('AB', [1, 2])
df1


# In[205]:


df2 = create_df('AB', [3, 4])
df2


# In[206]:


pd.concat([df1, df2])


# In[208]:


df3 = create_df('AB', [0, 1])
df3


# In[209]:


df4 = create_df('CD', [0, 1])
df4


# In[210]:


pd.concat([df3, df4])


# In[211]:


pd.concat([df3, df4], axis=1)


# In[212]:


#pd.concat([df1, df3], verify_integrity=True)


# In[213]:


pd.concat([df1, df3], ignore_index=True)


# In[215]:


pd.concat([df1, df3], keys=['X', 'Y'])


# In[216]:


df5 = create_df('ABC', [1,2])
df6 = create_df('BCD', [3,4])
pd.concat([df5, df6])


# In[217]:


pd.concat([df5, df6], join='inner')


# In[218]:


df5.append(df6)


# ### 병합과 조인

# In[219]:


df1 = pd.DataFrame({'학생' : ['홍길동', '이순신', '임꺽정', '김유신'],
                   '학과' : ['경영학과', '교육학과', '컴퓨터학과', '통계학과']})
df1


# In[221]:


df2 = pd.DataFrame({'학생' : ['홍길동', '이순신', '임꺽정', '김유신'],
                   '입학년도' : [2012, 2016, 2019, 2020]})
df2


# In[222]:


df3 = pd.merge(df1, df2)
df3


# In[223]:


df4 = pd.DataFrame({'학과': ['경영학과', '교육학과', '컴퓨터학과', '통계학과'],
                   '학과정' : ['황희', '장영실', '안창호', '정약용']})
df4


# In[224]:


pd.merge(df3, df4)


# In[225]:


df5 = pd.DataFrame({'학과' : ['경영학과', '교육학과', '교육학과', '컴퓨터학과', '컴퓨터학과', '통계학과'],
                   '과목' : ['경영개론', '기초수학', '물리학', '프로그래밍', '운영체제', '확률론']})
df5


# In[227]:


pd.merge(df1, df5)


# In[228]:


pd.merge(df1, df2, on='학생')


# In[229]:


df6 = pd.DataFrame({'이름' : ['홍길동', '이순신', '임꺽정', '김유신'],
                   '성적' : ['A', 'A+', 'B', 'A+']})
df6


# In[230]:


pd.merge(df1, df6, left_on='학생', right_on='이름')


# In[231]:


pd.merge(df1, df6, left_on='학생', right_on='이름').drop('이름', axis=1)


# In[232]:


mdf1 = df1.set_index('학생')
mdf2 = df2.set_index('학생')


# In[233]:


mdf1


# In[234]:


mdf2


# In[235]:


pd.merge(mdf1, mdf2, left_index=True, right_index=True)


# In[237]:


mdf1.join(df2)


# In[239]:


pd.merge(mdf1, df6, left_index=True, right_on='이름')


# In[240]:


df7 = pd.DataFrame({'이름':['홍길동', '이순신', '임꺽정'],
                   '주문음식' : ['햄버거', '피자', '짜장면']})
df7


# In[241]:


df8 = pd.DataFrame({'이름' : ['홍길동', '이순신', '김유신'],
                   '주문음식' : ['콜라', '사이다', '커피']})
df8


# In[242]:


pd.merge(df7, df8)


# In[243]:


pd.merge(df7, df8, how='inner')


# In[244]:


pd.merge(df7, df8, how='outer')


# In[245]:


pd.merge(df7, df8, how='left')


# In[246]:


pd.merge(df7, df8, how='right')


# In[247]:


df9 = pd.DataFrame({'이름' : ['홍길동', '이순신', '임꺽정', '김유신'],
                   '순위' : [3, 2, 4, 1]})
df9


# In[248]:


df10 = pd.DataFrame({'이름' : ['홍길동', '이순신', '임꺽정', '김유신'],
                    '순위' : [4, 1, 3, 2]})
df10


# In[249]:


pd.merge(df9, df10, on='이름')


# In[250]:


pd.merge(df9, df10, on='이름', suffixes=['_인기', '_성적'])


# ## 데이터 집계와 그룹 연산

# #### 집계 연산(Aggregation)
# 

# In[251]:


df = pd.DataFrame([[1, 1.2, np.nan],
                  [2.4, 5.5, 4.2],
                  [np.nan, np.nan, np.nan],
                  [0.44, -3.1, -4.1]],
                 index=[1, 2, 3, 4],
                 columns=['A', 'B', 'C'])
df


# In[252]:


df.head(2)


# In[253]:


df.tail(2)


# In[254]:


df.describe()


# In[255]:


print(df)
print(np.argmin(df), np.argmax(df))


# In[256]:


print(df)
print(df.idxmin())
print(df.idxmax())


# In[258]:


print(df)
print(df.std())
print(df.var())


# In[259]:


print(df)
print(df.skew())
print(df.kurt())


# In[260]:


print(df)
print(df.sum())
print(df.cumsum())


# In[261]:


print(df)
print(df.prod())
print(df.cumprod())


# In[262]:


df.diff()


# In[263]:


df.quantile()


# In[264]:


df.pct_change()


# In[265]:


df.corr()


# In[266]:


df.corrwith(df.B)


# In[267]:


df.cov()


# In[268]:


df['B'].unique()


# In[269]:


df['A'].value_counts()


# ### GroupBy 연산

# In[3]:


df = pd.DataFrame({'c1' : ['a', 'a', 'b', 'b', 'c', 'd', 'b'],
                  'c2' : ['A', 'B', 'B', 'A', 'D', 'C', 'C'],
                  'c3' : np.random.randint(7),
                  'c4' : np.random.random(7)})
df


# In[4]:


df.dtypes


# In[5]:


df['c3'].groupby(df['c1']).mean()


# In[6]:


df['c4'].groupby(df['c2']).std()


# In[8]:


df['c4'].groupby([df['c1'], df['c2']]).mean()


# In[9]:


df['c4'].groupby([df['c1'], df['c2']]).mean().unstack()


# In[10]:


df.groupby('c1').mean()


# In[11]:


df.groupby(['c1', 'c2']).mean()


# In[12]:


df.groupby(['c1', 'c2']).size()


# In[13]:


for c1, group in df.groupby('c1'):
    print(c1)
    print(group)


# In[14]:


for (c1, c2), group in df.groupby(['c1', 'c2']):
    print((c1, c2))
    print(group)


# In[16]:


df.groupby(['c1', 'c2'])[['c4']].mean()


# In[18]:


df.groupby('c1')['c3'].quantile()


# In[19]:


df.groupby('c1')['c3'].median()


# In[20]:


df.groupby('c1')['c3'].std()


# In[22]:


df.groupby(['c1', 'c2'])['c4'].agg(['mean', 'min', 'max'])


# In[23]:


df.groupby(['c1', 'c2'], as_index=False)['c4'].mean() 


# In[24]:


df.groupby(['c1', 'c2'], group_keys=False)['c4'].mean()


# In[27]:


def top(df, n=3, column='c1'):
    return df.sort_values(by=column)[-n:]

top(df, n=5)


# In[28]:


df.groupby('c1').apply(top)


# ### 피벗 테이블(Pivot Table)
# 

# In[29]:


df.pivot_table(['c3', 'c4'],
              index=['c1'],
              columns=['c2'])


# In[30]:


df.pivot_table(['c3', 'c4'],
              index=['c1'],
              columns=['c2'],
              margins=True)


# In[31]:


df.pivot_table(['c3', 'c4'],
              index=['c1'],
              columns=['c2'],
              margins=True,
              aggfunc=sum)


# In[32]:


df.pivot_table(['c3', 'c4'],
              index=['c1'],
              columns=['c2'],
              margins=True,
              aggfunc=sum,
              fill_value=0)


# In[33]:


pd.crosstab(df.c1, df.c2)


# In[34]:


pd.crosstab(df.c1, df.c2, values=df.c3, aggfunc=sum, margins=True)


# ### 범주형(Categorical) 데이터
# 

# In[35]:


s = pd.Series(['c1', 'c2', 'c1', 'c2', 'c1'] * 2)
s


# In[36]:


pd.unique(s)


# In[37]:


pd.value_counts(s)


# In[38]:


code = pd.Series([0, 1, 0, 1, 0] * 2)
code


# In[39]:


d = pd.Series(['c1', 'c2'])
d


# In[40]:


d.take(code)


# In[41]:


df = pd.DataFrame({'id': np.arange(len(s)),
                  'c':s,
                  'v':np.random.randint(1000, 5000, size=len(s))})
df


# In[43]:


c = df['c'].astype('category')
c


# In[44]:


c.values


# In[45]:


c.values.categories


# In[46]:


c.values.codes


# In[47]:


df['c'] = c
df.c


# In[48]:


c = pd.Categorical(['c1', 'c2', 'c3', 'c1', 'c2'])
c


# In[49]:


categories = ['c1', 'c2', 'c3']
codes = [0, 1, 2, 0, 1]
c = pd.Categorical.from_codes(codes, categories)
c


# In[50]:


pd.Categorical.from_codes(code, categories, ordered=True)


# In[51]:


c.as_ordered()


# In[52]:


c.codes


# In[53]:


c.categories


# In[54]:


c = c.set_categories(['c1', 'c2', 'c3', 'c4', 'c5'])
c.categories


# In[55]:


c.value_counts()


# In[56]:


c[c.isin(['c1', 'c3'])]


# In[57]:


c = c.remove_unused_categories()


# In[58]:


c.categories


# ## 문자열 연산

# #### 문자열 연산자

# In[59]:


name_tuple = ['Suan Lee', 'Steven Jobs', 'Larry page', 'Elon Musk', None, 'Bill Gates', 'Mark Zuckerberg', 'Jeff Bezos']
names = pd.Series(name_tuple)
names


# In[60]:


names.str.lower()


# In[61]:


names.str.len()


# In[62]:


names.str.split()


# #### 기타 연산자
# 

# In[63]:


names.str[0:4]


# In[64]:


names.str.split().str.get(-1)


# In[65]:


names.str.repeat(2)


# In[66]:


names.str.join('*')


# #### 정규표현식
# 

# In[67]:


names.str.match('([A-Za-z]+)')


# In[68]:


names.str.findall('([A-Za-z]+)')


# ## 시계열 처리

# In[69]:


idx = pd.DatetimeIndex(['2019-01-01', '2020-01-01', '2020-02-01',
                       '2020-02-02', '2020-03-01'])
s = pd.Series([0, 1, 2, 3, 4], index =idx)
s


# In[70]:


s['2020-01-01':]


# In[71]:


s[:'2020-01-01']


# In[72]:


s['2019']


# #### 시계열 데이터 구조
# 

# In[73]:


from datetime import datetime
dates = pd.to_datetime(['12-12-2019', datetime(2020, 1, 1), '2nd of Feb, 2020', '2020-Mar-4', '20200701'])
dates


# In[74]:


dates.to_period('D')


# In[75]:


dates - dates[0]


# In[76]:


pd.date_range('2020-01-01', '2020-07-01')


# In[77]:


pd.date_range('2020-01-01', periods=7)


# In[78]:


pd.date_range('2020-01-01', periods=7, freq='M')


# In[79]:


pd.date_range('2020-01-01', periods=7, freq='H')


# In[80]:


idx = pd.to_datetime(['2020-01-01 12:00:00', '2020-01-02 00:00:00'] + [None])
idx


# In[81]:


idx[2]


# In[82]:


pd.isnull(idx)


# ### 시계열 기본

# In[83]:


dates= [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 4), datetime(2020, 1, 7),
       datetime(2020, 1, 10), datetime(2020, 1, 11), datetime(2020, 1, 15)]
dates


# In[84]:


ts = pd.Series(np.random.randn(7), index=dates)
ts


# In[85]:


ts.index


# In[86]:


ts.index[0]


# In[87]:


ts[ts.index[2]]


# In[88]:


ts['20200104']


# In[89]:


ts['1/4/2020']


# In[90]:


ts = pd.Series(np.random.randn(1000),
              index=pd.date_range('2017-10-01', periods=1000))
ts


# In[91]:


ts['2020']


# In[92]:


ts['2020-06']


# In[93]:


ts[datetime(2020, 6, 20):]


# In[94]:


ts['2020-06-10':'2020-06-20']


# In[95]:


tdf = pd.DataFrame(np.random.randn(1000, 4),
                  index=pd.date_range('2017-10-01', periods=1000),
                  columns=['A', 'B', 'C', 'D'])
tdf


# In[96]:


tdf['2020']


# In[97]:


tdf.loc['2020-06']


# In[98]:


tdf['2020-06-20':]


# In[99]:


tdf['C']


# In[100]:


tdf['C']


# In[102]:


ts = pd.Series(np.random.randn(10),
              index=pd.DatetimeIndex(['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02', '2020-01-03',
                                     '2020-01-04', '2020-01-05', '2020-01-05', '2020-01-06', '2020-01-07']))
ts


# In[103]:


ts.index.is_unique


# In[104]:


ts['2020-01-01']


# In[105]:


ts.groupby(level=0).mean()


# In[106]:


pd.date_range('2020-01-01', '2020-07-01')


# In[111]:


pd.date_range(start='2020-01-01', periods=10)


# In[113]:


pd.date_range(end='2020-07-01', periods=10)


# In[108]:


pd.date_range('2020-01-01', '2020-07-01', freq='B')


# ### 주기와 오프셋
# 

# In[114]:


pd.timedelta_range(0, periods=12, freq='H')


# In[115]:


pd.timedelta_range(0, periods=60, freq='T')


# In[116]:


pd.timedelta_range(0, periods=10, freq='1H30T')


# In[119]:


pd.date_range('2020-01-01', periods=20, freq='B')


# In[120]:


pd.date_range('2020-01-01', periods=30, freq='2H')


# In[121]:


pd.date_range('2020-01-01', periods=20, freq='S')


# ### 시프트(Shift)

# In[122]:


ts = pd.Series(np.random.randn(5),
              index=pd.date_range('2020-01-01', periods=5, freq='B'))
ts


# In[123]:


ts.shift(1)


# In[124]:


ts.shift(3)


# In[125]:


ts.shift(-2)


# In[126]:


ts.shift(3, freq='B')


# In[127]:


ts.shift(2, freq='W')


# ### 시간대 처리
# 
# * 국제표준시(Coordinated Universal Time, UTC)를 기준으로 떨어진 거리만큼 오프셋으로 시간대 처리
# * 전 세계의 시간대 정보를 모아놓은 올슨 데이터베이스를 활용한 라이브러리인 `pytz` 사용

# In[128]:


import pytz
pytz.common_timezones


# In[129]:


tz = pytz.timezone('Asia/Seoul')


# In[130]:


didx = pd.date_range('2020-01-01', periods=7, freq='B')
ts = pd.Series(np.random.randn(len(didx)), index=didx)
ts


# In[131]:


pd.date_range('2020-01-01 09:00', periods=7, freq='B', tz='UTC')


# In[132]:


ts_utc = ts.tz_localize('UTC')
ts_utc


# In[133]:


ts_utc.index


# In[135]:


ts_utc.tz_convert('Asia/Seoul')


# In[136]:


ts_seoul = ts.tz_localize('Asia/seoul')


# In[137]:


ts_seoul.tz_convert('UTC')


# In[138]:


ts_seoul.tz_convert('Europe/Berlin')


# In[139]:


ts.index.tz_localize('America/New_York')


# In[140]:


stamp = pd.Timestamp('2020-01-01 12:00')
stamp_utc = stamp.tz_localize('UTC')
stamp_utc


# In[141]:


stamp_utc.value


# In[142]:


stamp_utc.tz_convert('Asia/Seoul')


# In[143]:


stamp_utc.tz_convert('Asia/Seoul').value


# In[150]:


stamp_ny = pd.Timestamp('2020-01-01 12:00', tz='America/New_York')
stamp_ny


# In[151]:


stamp_ny.value


# In[146]:


stamp_utc.tz_convert('Asia/Shanghai')


# In[153]:


stamp = pd.Timestamp('2020-01-01 12:00', tz= 'Asia/Seoul')
stamp


# In[154]:


from pandas.tseries.offsets import Hour
stamp + Hour()


# In[155]:


stamp + 3 * Hour()


# In[156]:


ts_utc


# In[158]:


ts1 = ts_utc[:5].tz_convert('Europe/Berlin')
ts2 = ts_utc[2:].tz_convert('America/New_York')
ts = ts1 + ts2


# In[159]:


ts.index


# ### 기간과 기간 연산

# In[160]:


p= pd.Period(2020, freq='A-JAN')
p


# In[161]:


p + 2


# In[162]:


p - 3


# In[164]:


p1 = pd.Period(2010, freq='A-JAN')
p2 = pd.Period(2020, freq='A-JAN')
p2 - p1


# In[165]:


pr = pd.period_range('2020-01-01', '2020-06-30', freq='M')


# In[166]:


pd.Series(np.random.randn(6), index=pr)


# In[167]:


pidx =pd.PeriodIndex(['2020-1', '2020-2', '2020-4'], freq='M')
pidx


# In[168]:


p = pd.Period('2020', freq='A-FEB')
p


# In[169]:


p.asfreq('M', how='start')


# In[170]:


p.asfreq('m', how='end')


# In[171]:


p = pd.Period('2020', freq='A-OCT')
p


# In[172]:


p.asfreq('M', how='end')


# In[173]:


p = pd.Period('2020Q2', freq='Q-JAN')
p


# In[174]:


p.asfreq('D', 'start')


# In[175]:


p.asfreq('D', 'end')


# In[177]:


pr = pd.period_range('2019Q3', '2020Q3', freq='Q-JAN')
ts = pd.Series(np.arange(len(pr)), index=pr)
ts


# In[181]:


pr = pd.date_range('2019Q3', periods=5, freq='Q-JAN')
ts = pd.Series(np.random.randn(5), index=pr)
ts


# In[182]:


ts.to_period()


# In[183]:


pr = pd.date_range('2020-01-01', periods=5, freq='D')
ts = pd.Series(np.random.randn(5), index=pr)
ts


# In[185]:


p = ts.to_period('M')
p


# In[186]:


p.to_timestamp(how='start')


# ### 리샘플링(Resampling)
# 
# * 리샘플링(Resampling): 시계열의 빈도 변환
# * 다운샘플링(Down sampling): 상위 빈도 데이터를 하위 빈도 데이터로 집계
# * 업샘플링(Up sampling): 하위 빈도 데이터를 상위 빈도 데이터로 집계

# In[3]:


dr = pd.date_range('2020-01-01', periods=200, freq='D')
ts = pd.Series(np.random.randn(len(dr)), index=dr)
ts


# In[4]:


ts.resample('M').mean()


# In[5]:


ts.resample('M', kind='period').mean()


# In[6]:


dr = pd.date_range('2020-01-01', periods=10, freq='T')
ts = pd.Series(np.arange(10), index=dr)
ts


# In[7]:


ts.resample('2T', closed='left').sum()


# In[8]:


ts.resample('2T', closed='right').sum()


# In[9]:


ts.resample('2T', closed='left', label='right').sum()


# In[10]:


ts.resample('2T', closed='left', label='right', offset='-1s').sum()


# In[11]:


ts.resample('2T').ohlc()


# In[12]:


df = pd.DataFrame(np.random.randn(10, 4),
                 index=pd.date_range('2019-10-01', periods=10, freq='M'),
                 columns=['C1', 'C2', 'C3', 'C4'])
df


# In[13]:


df.resample('Y').asfreq()


# In[14]:


df.resample('W-FRI').asfreq()


# In[15]:


df.resample('H').asfreq()


# In[16]:


df.resample('H').ffill()


# In[17]:


df.resample('H').ffill(limit=2)


# In[18]:


df.resample('Q-DEC').mean()


# In[19]:


df.resample('Y').mean()


# ### 무빙 윈도우(Moving Window)

# In[20]:


df = pd.DataFrame(np.random.randn(300, 4),
                 index=pd.date_range('2020-01-01', periods=300, freq='D'),
                 columns=['C1', 'C2', 'C3', 'C4'])
df


# In[21]:


df.rolling(30).mean().plot()


# In[22]:


df.rolling(60).mean().plot()


# In[23]:


df.C1.rolling(60, min_periods=10).std().plot()


# In[25]:


df.rolling(60, min_periods=10).std()[10:50].plot()


# In[26]:


df.rolling(60, min_periods=10).std().expanding().mean().plot()


# In[27]:


df.rolling(60).mean().plot(logy=True)


# In[28]:


df.rolling('20D').mean().plot()


# In[30]:


df.C1.rolling(30, min_periods=20).mean().plot(style='--', label='Simple MA')
df.C1.ewm(span=30).mean().plot(style='-', label='EWMA')


# In[31]:


df.C1.rolling(100, min_periods=50).corr(df.C3).plot()


# In[32]:


df.C3.rolling(100, min_periods=50).corr(df.C4).plot()


# ## 데이터 읽기 및 저장
# 

# ### 텍스트 파일 읽기/쓰기

# In[33]:


get_ipython().run_cell_magic('writefile', 'example1.csv', 'a, b, c, d, e, text\n1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv')


# In[34]:


get_ipython().system('ls')


# In[35]:


pd.read_csv('example1.csv')


# In[36]:


get_ipython().run_cell_magic('writefile', 'example2.csv', '1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv')


# In[37]:


pd.read_csv('example2.csv', header=None)


# In[38]:


pd.read_csv('example2.csv', names=['a', 'b', 'c', 'd', 'e', 'text'])


# In[39]:


pd.read_csv('example2.csv', names=['a', 'b', 'c', 'd', 'e', 'text'], index_col='text')


# In[40]:


get_ipython().run_cell_magic('writefile', 'example3.txt', '    a    b    c\n1 0.1  0.2  0.3\n2 0.4  0.5  0.6\n3 0.7  0.8  0.9')


# In[41]:


pd.read_table('example3.txt', sep='\s+')


# In[42]:


get_ipython().run_cell_magic('writefile', 'example4.csv', 'a, b, c, d, e, text\n1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv')


# In[45]:


pd.read_csv('example4.csv', skiprows=[0, 2])


# In[46]:


pd.read_csv('example4.csv', skiprows=[0, 2])


# In[47]:


get_ipython().run_cell_magic('writefile', 'example5.csv', 'a, b, c, d, e, text\n1, 2, NA, 4, 5, hi\n6, 7, 8, NULL, 10 pandas\n11, NA, 13, 14, 15, csv')


# In[48]:


pd.read_csv('example5.csv')


# In[49]:


get_ipython().run_cell_magic('writefile', 'example6.csv', 'a, b, c, d, e, text\n1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv\n1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv\n1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv\n1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv\n1, 2, 3, 4, 5, hi\n6, 7, 8, 9, 10 pandas\n11, 12, 13, 14, 15, csv')


# In[50]:


pd.read_csv('example6.csv', nrows=5)


# In[51]:


df = pd.read_csv('example6.csv')
df


# In[52]:


df.to_csv('output.csv')


# In[53]:


get_ipython().system('cat output.csv')


# In[54]:


dr = pd.date_range('2020-01-01', periods=10)
ts = pd.Series(np.arange(10), index=dr)
ts


# In[55]:


ts.to_csv('ts.csv', header=['value'])


# In[56]:


get_ipython().system('cat ts.csv')


# In[57]:


get_ipython().run_cell_magic('writefile', 'example.json', '[{"a":1, "b":2, "c":3, "d":4, "e":5},\n{"a":6, "b":7, "c":8, "d":9, "e":10},\n{"a":11, "b":12, "c":13, "d":14, "e":15},]')


# In[58]:


get_ipython().system('cat example.json')


# In[59]:


pd.read_json('example.json')


# In[60]:


ts.to_json('output.json')


# In[61]:


get_ipython().system('cat output.json')


# In[62]:


df.to_json('output.json')


# In[63]:


get_ipython().system('cat output.json')


# ### 이진 데이터 파일 읽기/쓰기

# In[66]:


df = pd.read_csv('example1.csv')
df


# In[67]:


df.to_pickle('df_pickle')
pd.read_pickle('df_pickle')


# In[68]:


df = pd.DataFrame({'a': np.random.randn(100),
                  'b': np.random.randn(100),
                  'c': np.random.randn(100)})
df


# In[70]:


h = pd.HDFStore('date.h5')
h['obj1'] = df
h['obj1_col1'] = df['a']
h['obj1_col2'] = df['b']
h['obj1_col3'] = df['c']
h


# In[71]:


h['obj1']


# In[72]:


h.put('obj2', df, format='table')


# In[73]:


h.select('obj2', where=['index > 50 and index <= 60'])


# In[74]:


h.close()


# In[75]:


df.to_hdf('data.h5', 'obj3', format='table')


# In[76]:


pd.read_hdf('data.h5', 'obj3', where=['index < 10'])


# In[77]:


df.to_excel('example.xlsx', 'Sheet1')


# In[78]:


get_ipython().system('ls')


# In[79]:


pd.read_excel('example.xlsx', 'Sheet1')


# ## 데이터 정제

# ### 누락값 처리
# 
# * 대부분의 실제 데이터들은 정제되지 않고 누락값들이 존재
# * 서로 다른 데이터들은 다른 형태의 결측을 가짐
# * 결측 데이터는 `null`, `NaN`, `NA`로 표기

# #### None: 파이썬 누락 데이터

# In[81]:


a = np.array([1, 2, None, 4, 5])
a


# In[82]:


a.sum()


# #### NaN: 누락된 수치 데이터

# In[83]:


a = np.array([1, 2, np.nan, 4, 5])
a.dtype


# In[84]:


0 + np.nan


# In[85]:


np.nan + np.nan


# In[86]:


a.sum(), a.min(), a.max()


# In[87]:


np.nansum(a), np.nanmin(a), np.nanmax(a)


# In[88]:


pd.Series([1, 2, np.nan, 4, None])


# In[89]:


s = pd.Series(range(5), dtype=int)
s


# In[91]:


s[0] = None
s


# In[92]:


s[3] = np.nan


# In[93]:


s = pd.Series([True, False, None, np.nan])
s


# #### Null 값 처리
# 

# In[94]:


s = pd.Series([1, 2, np.nan, 'String', None])
s


# In[95]:


s.isnull()


# In[96]:


s[s.notnull()]


# In[97]:


s.dropna()


# In[98]:


df.dropna(axis='columns')


# In[99]:


df[3] = np.nan
df


# In[100]:


df.dropna(axis='columns', how='all')


# In[101]:


df.dropna(axis='rows', thresh=3)


# In[103]:


s


# In[104]:


s.fillna(0)


# In[105]:


s.fillna(method='ffill')


# In[106]:


s.fillna(method='bfill')


# In[109]:


df.fillna(method='ffill', axis=0)


# In[110]:


df.fillna(method='ffill', axis=1)


# In[111]:


df.fillna(method='bfill', axis=0)


# In[112]:


df.fillna(method='bfill', axis=1)


# ### 중복 제거

# In[113]:


df = pd.DataFrame({'c1': ['a', 'b', 'c'] * 2 + ['b'] + ['c'],
                  'c2': [1, 2, 1, 1, 2, 3, 3, 4]})
df


# In[114]:


df.duplicated()


# In[115]:


df.drop_duplicates()


# ### 값 치환

# In[116]:


s = pd.Series([1., 2., -999., 3., -1000., 4.])
s


# In[117]:


s.replace(-999, np.nan)


# In[118]:


s.replace([-999, -1000], np.nan)


# In[119]:


s.replace([-999, -1000], [np.nan, 0])


# ## 참고문헌
# 
# * Pandas 사이트: https://pandas.pydata.org/
# * Jake VanderPlas, "Python Data Science Handbook", O'Reilly
# * Wes Mckinney, "Python for Data Analysis", O'Reilly
