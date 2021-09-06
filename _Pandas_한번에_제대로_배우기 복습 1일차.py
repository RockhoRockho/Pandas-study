#!/usr/bin/env python
# coding: utf-8

# # Pandas 한번에 제대로 배우기
# 

# 
# 
# ---
# 
# 

# In[1]:


import numpy as np
import pandas as pd
pd.__version__


# ## Pandas 객체
# 

# ### Series 객체

# In[3]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
s


# In[4]:


s.values


# In[5]:


s.index


# In[6]:


s[1]


# In[8]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
              index=['a', 'b', 'c', 'd', 'e'])
s


# In[9]:


s['c']


# In[10]:


s[['c', 'd', 'e']]


# In[11]:


'b' in s


# In[12]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
              index=[2, 4, 6, 8, 10])
s


# In[13]:


s[4]


# In[14]:


s[2:]


# In[15]:


s.unique()


# In[16]:


s.value_counts()


# In[17]:


s.isin([0.25, 0.75])


# In[21]:


pop_tuple = {'서울특별시' : 9720846,
            '부산광역시' : 3404423,
            '인천광역시' : 2947217,
            '대구광역시' : 2427954,
            '대전광역시' : 1471040,
            '광주광역시' : 1455048}
population = pd.Series(pop_tuple)
population


# In[22]:


population['서울특별시']


# In[23]:


population['서울특별시' : '인천광역시']


# ### DataFrame 객체

# In[24]:


pd.DataFrame([{'A' : 2, 'B' : 4, 'D' : 3}, {'A': 4, 'B': 5, 'C': 7}])


# In[25]:


pd.DataFrame(np.random.randn(5, 5),
            columns=['A', 'B', 'C', 'D', 'E'],
            index=[1, 2, 3, 4, 5])


# In[27]:


female_tuple = {'서울특별시' : 4988571,
               '부산광역시' : 1735805,
               '인천광역시' : 1470404,
               '대구광역시' : 1229139,
               '대전광역시' : 736599,
               '광주광역시' : 734988}
female = pd.Series(female_tuple)
female


# In[28]:


male_tuple = {'서울광역시' : 4732275,
             '부산광역시' : 1668618,
             '인천광역시' : 1476813,
             '대구광역시' : 1198815,
             '대전광역시' : 734441,
             '광주광역시' : 720060}
male = pd.Series(male_tuple)
male


# In[30]:


korea_df = pd.DataFrame({'인구수': population,
                        '남자인구수': male,
                        '여자인구수' : female})
korea_df


# In[31]:


korea_df.index


# In[32]:


korea_df.columns


# In[33]:


korea_df['여자인구수']


# In[34]:


korea_df['서울특별시':'인천광역시']


# ### Index 객체
# 

# In[36]:


idx = pd.Index([2, 4, 6, 8, 10])
idx


# In[37]:


idx[1]


# In[41]:


idx[1:2:2]


# In[42]:


idx[-1::]


# In[43]:


idx[::2]


# In[44]:


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

# In[47]:


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

# In[49]:


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
             index=['a', 'b', 'c', 'd', 'e'])
s


# In[50]:


s['b']


# In[51]:


'b' in s


# In[52]:


s.keys()


# In[53]:


list(s.items())


# In[54]:


s['f'] = 1.25
s


# In[55]:


s['a' : 'd']


# In[56]:


s[0:4]


# In[57]:


s[(s>0.4) & (s<0.8)]


# In[58]:


s[['a','c','e']]


# ### Series 인덱싱

# In[60]:


s = pd.Series(['a','b','c','d','e'],
             index=[1,3,5,7,9])
s


# In[61]:


s[1]


# In[62]:


s[2:4]


# In[63]:


s.iloc[1]


# In[66]:


s.iloc[2:4]


# In[64]:


s.reindex(range(10))


# In[65]:


s.reindex(range(10), method='bfill')


# ### DataFrame 인덱싱
# 

# In[67]:


korea_df


# In[68]:


korea_df['남자인구수']


# In[69]:


korea_df.남자인구수


# In[70]:


korea_df.여자인구수


# In[71]:


korea_df['남녀비율'] = (korea_df['남자인구수'] * 100 / korea_df['여자인구수'])


# In[72]:


korea_df.남녀비율


# In[73]:


korea_df.values


# In[74]:


korea_df.T


# In[75]:


korea_df.values[0]


# In[76]:


korea_df['인구수']


# In[77]:


korea_df.loc[:'인천광역시', :'남자인구수']


# In[78]:


korea_df.loc[(korea_df.여자인구수 > 1000000)]


# In[79]:


korea_df.loc[(korea_df.인구수 > 2000000)]


# In[80]:


korea_df.loc[(korea_df.인구수 > 2500000)]


# In[81]:


korea_df.loc[korea_df.남녀비율 > 100]


# In[83]:


korea_df.loc[(korea_df.인구수 > 2500000) & (korea_df.남녀비율 > 100)]


# In[84]:


korea_df.iloc[:3, :2]


# ### 다중 인덱싱(Multi Indexing)
# 
# * 1차원의 Series와 2차원의 DataFrame 객체를 넘어 3차원, 4차원 이상의 고차원 데이터 처리
# * 단일 인덱스 내에 여러 인덱스를 포함하는 다중 인덱싱

# #### 다중 인덱스 Series

# In[85]:


korea_df


# In[87]:


idx_tuples = [('서울특별시', 2010), ('서울특별시', 2020),
             ('부산광역시', 2010), ('부산광역시', 2020),
             ('인천광역시', 2010), ('인천광역시', 2020),
             ('대구광역시', 2010), ('대구광역시', 2020),
             ('대전광역시', 2010), ('대전광역시', 2020),
             ('광주광역시', 2010), ('광주광역시', 2020)]
idx_tuples


# In[88]:


pop_tuples = [10312545, 9720846,
             2567810, 3404423,
             2758296, 2947217,
             2511676, 2427954,
             1503664, 1471040,
             1454636, 1455048]
population = pd.Series(pop_tuples, index=idx_tuples)
population


# In[89]:


midx = pd.MultiIndex.from_tuples(idx_tuples)
midx


# In[90]:


population = population.reindex(midx)
population


# In[91]:


population[:, 2010]


# In[92]:


population['대전광역시', :]


# In[94]:


korea_mdf = population.unstack()
korea_mdf


# In[95]:


korea_mdf.stack()


# In[96]:


male_tuples = [5111259, 4732275,
              1773170, 1668618,
              1390356, 1476813,
              1255245, 1198815,
              753648, 734441,
              721780, 720060]
male_tuples


# In[97]:


korea_mdf = pd.DataFrame({'총인구수' : population,
                         '남자인구수' : male_tuples})
korea_mdf


# In[98]:


female_tuples = [5201286, 4988571,
                1794740, 1735805,
                1367940, 1470404,
                1257431, 1229139,
                750016, 736599,
                732856, 734988]
female_tuples


# In[99]:


korea_mdf = pd.DataFrame({'총인구수' : population,
                         '남자인구수' : male_tuples,
                         '여자인구수' : female_tuples})
korea_mdf


# In[100]:


ratio = korea_mdf['남자인구수'] * 100 / korea_mdf['여자인구수']
ratio


# In[101]:


ratio.unstack()


# In[102]:


korea_mdf = pd.DataFrame({'총인구수' : population,
                         '남자인구수' : male_tuples,
                         '여자인구수' : female_tuples,
                         '남녀비율' :ratio})
korea_mdf


# #### 다중 인덱스 생성

# In[103]:


df = pd.DataFrame(np.random.rand(6, 3),
                 index=[['a', 'a', 'b', 'b', 'c', 'c'], [1,2,1,2,1,2]],
                 columns=['c1', 'c2', 'c3'])
df


# In[104]:


pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b',' c', 'c'], [1,2,1,2,1,2]])


# In[105]:


pd.MultiIndex.from_arrays([('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)])


# In[106]:


pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2]])


# In[107]:


pd.MultiIndex(levels=[['a', 'b', 'c'], [1, 2]],
             codes=[[0,0,1,1,2,2],[0,1,0,1,0,1]])


# In[108]:


population


# In[109]:


population.index.names = ['행정구역', '년도']
population


# In[110]:


idx = pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2]],
                                names=['naem1', 'name2'])
cols = pd.MultiIndex.from_product([['c1', 'c2', 'c3'], [1, 2]],
                                 names=['col_name1', 'col_name2'])
data = np.round(np.random.randn(6, 6), 2)
mdf = pd.DataFrame(data, index=idx, columns=cols)
mdf


# In[111]:


mdf['c2']


# #### 인덱싱 및 슬라이싱

# In[112]:


population['인천광역시', 2010]


# In[113]:


population[:, 2010]


# In[114]:


population[population > 3000000]


# In[115]:


population[['대구광역시', '대전광역시']]


# In[116]:


mdf


# In[117]:


mdf['c2', 1]


# In[118]:


mdf.iloc[:3, :4]


# In[119]:


mdf.loc[:, ('c2', 1)]


# In[120]:


idx_slice = pd.IndexSlice
mdf.loc[idx_slice[:, 2], idx_slice[:, 2]]


# #### 다중 인덱스 재정렬

# In[121]:


korea_mdf


# In[122]:


korea_mdf = korea_mdf.sort_index()
korea_mdf


# In[123]:


korea_mdf['서울특별시' : '인천광역시']


# In[124]:


korea_mdf.unstack(level=0)


# In[125]:


korea_mdf.unstack(level=1)


# In[126]:


korea_mdf.stack()


# In[127]:


korea_mdf


# In[128]:


idx_flat = korea_mdf.reset_index(level=0)
idx_flat


# In[129]:


idx_flat = korea_mdf.reset_index(level=(0,1))
idx_flat


# In[132]:


idx_flat.set_index(['행정구역', '년도'])


# ## 데이터 연산

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 연산자 범용 함수
# 

# #### add()

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### sub() / subtract()

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### mul() / multply()
# 
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### truediv() /  div() / divide() / floordiv()

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### mod()

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### pow()

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 정렬(Sort)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 순위(Ranking)
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 고성능 연산

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 데이터 결합

# ### Concat() / Append()

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 병합과 조인

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 데이터 집계와 그룹 연산

# #### 집계 연산(Aggregation)
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### GroupBy 연산

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 피벗 테이블(Pivot Table)
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 범주형(Categorical) 데이터
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 문자열 연산

# #### 문자열 연산자

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 기타 연산자
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 정규표현식
# 

# In[ ]:





# In[ ]:





# ## 시계열 처리

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 시계열 데이터 구조
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 시계열 기본

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 주기와 오프셋
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 시프트(Shift)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 시간대 처리
# 
# * 국제표준시(Coordinated Universal Time, UTC)를 기준으로 떨어진 거리만큼 오프셋으로 시간대 처리
# * 전 세계의 시간대 정보를 모아놓은 올슨 데이터베이스를 활용한 라이브러리인 `pytz` 사용

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 기간과 기간 연산

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 리샘플링(Resampling)
# 
# * 리샘플링(Resampling): 시계열의 빈도 변환
# * 다운샘플링(Down sampling): 상위 빈도 데이터를 하위 빈도 데이터로 집계
# * 업샘플링(Up sampling): 하위 빈도 데이터를 상위 빈도 데이터로 집계

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 무빙 윈도우(Moving Window)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 데이터 읽기 및 저장
# 

# ### 텍스트 파일 읽기/쓰기

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 이진 데이터 파일 읽기/쓰기

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 데이터 정제

# ### 누락값 처리
# 
# * 대부분의 실제 데이터들은 정제되지 않고 누락값들이 존재
# * 서로 다른 데이터들은 다른 형태의 결측을 가짐
# * 결측 데이터는 `null`, `NaN`, `NA`로 표기

# #### None: 파이썬 누락 데이터

# In[ ]:





# In[ ]:





# #### NaN: 누락된 수치 데이터

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### Null 값 처리
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 중복 제거

# In[ ]:





# In[ ]:





# In[ ]:





# ### 값 치환

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 참고문헌
# 
# * Pandas 사이트: https://pandas.pydata.org/
# * Jake VanderPlas, "Python Data Science Handbook", O'Reilly
# * Wes Mckinney, "Python for Data Analysis", O'Reilly
