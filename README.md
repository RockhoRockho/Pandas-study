# Pandas-study
Pandas 복습 

---

## Day 1 (2021-09-06)

- Pandas 특징학습
- Series, DataFrame, index 객체학습
- Series, DataFrame 인덱싱 학습 (`stack()`, `unstack()`)
- 다중 인덱싱 생성(Series, DataFrame), 인덱싱 및 슬라이싱, 재정렬 학습

---

## Day 2 (2021-09-07)

- 데이터 연산학습
- 연산자 범용함수 학습
  - `add()`, `sub()`/`subtract()`
  - `mul()`/`multply()`
  - `truediv()`/`div()`/`divide()`/`floordiv()`
  - `mod()`
  - `pow()`
  - 정렬 `sort()`
  - 순위 `rank()`
  - 고성능연산 `%timeit`
- 데이터결합 학습
  - `concat()`/`append()`
  - `merge()`/`join()`
- 집계 연산 학습
  - `count()`
  - `head()`, `tail()`
  - `describe()`
  - `min()`, `max()`
  - `cummin()`, `cummax()`
  - `argmin()`, `argmax()`
  - `idxmin()`, `idxmax()`
  - `mean()`, `median()`
  - `std()`, `var()`
  - `skew()`
  - `kurt()`
  - `mad()`
  - `sum()`/`cumsum()`
  - `prod()`/`cumprod()`
  - `quantile()`
  - `diff()`
  - `pct_change()`
  - `corr()`/`cov()`

---

## Day 3 (2021-09-08)

- Groupby 연산 학습

- 피벗 테이블 학습
  - `values()`
  - `index()`
  - `columns()`
  - `aggfunc()`
  - `fill_value()`
  - `dropna()`
  - `margins()`

- 범주형 데이터 학습(`categories()`, `categorical()`, `remove_unused_categories()`)
  - `add_categories()`
  - `as_ordered()`
  - `as_unordered()`
  - `remove_categories()`
  - `remove_unused_categories()`
  - `rename_categories()`
  - `reorder_categories()`
  - `set_categories()`

- 문자열 연산 학습  
  - `capitalize()` | 첫 문자를 대문자로하고, 나머지 문자를 소문자로 하는 문자열 반환  
  - `casefold()` | 모든 대소문자 구분을 제거  
  - `count(sub, [, start[, end]])` | [start, end] 범위에서 부분 문자열 sub의 중복되지 않는 수를 반환  
  - `find(sub [, start [, end]])` | [start, end] 범위에서 부분 문자열 sub가 문자열의 가장 작은 인덱스를 반환. sub가 발견되지 않는 경우는 -1 반환  
  - `rfind(sub [, start [ , end]])` | [start, end] 범위에서 부분 문자열 sub가 문자열의 가장 큰 인덱스를 반환. sub가 발견되지 않는 경우는 -1 반환  
  - `index(sub [, start [, end]])` | find()과 유사하지만 부분 문자열 sub가 없으면 ValueError 발생  
  - `rindex(sub [, start [, end]])` | rfind()과 유사하지만 부분 문자열 sub가 없으면 ValueError 발생  
  - `isalnum()` | 문자열의 모든 문자가 영숫자로 1개 이상 있으면 True, 아니면 False반환  
  - `isalpha()` | 문자열의 모든 문자가 영문자로 1개 이상 있으면 True, 아니면 False반환  
  - `isdecimal()` | 문자열의 모든 문자가 10진수 문자이며 1개 이상 있으면 True, 아니면 False반환  
  - `isdigit()` | 문자열의 모든 문자가 숫자이며 1개 이상 있으면 True, 아니면 False반환  
  - `isidentifier()` | 문자열의 모든 문자가 수치형이며 1개 이상 있으면 True, 아니면 False반환  
  - `isidentifier()` | 문자열이 유효한 식별자인 경우 True 반환  
  - `isspace()` | 문자열 내에 공백 문자가 있고, 문자가 1개 이상 있으면 True, 아니면 False반환  
  - `istitle()` | 문자열이 제목이 있는 문자열에 문자가 1개 이상 있으면 True, 아니면 False반환  
  - `islower()` | 문자열의 모든 문자가 소문자이며 1개 이상 있으면 True, 아니면 False반환  
  - `isupper()` | 문자열의 문자가 모두 대문자에 문자가 1개 이상 있으면 True, 아니면 False반환  
  - `join(literable)` | iterable에 있는 문자열에 연결된 문자열을 반환  
  - `center(width [, fillchar])` | 길이 너비만큼 중앙정렬된 문자열 반환  
  - `ljust(width [, fillchar])` | 너비만큼의 문자열에서 왼쪽 정렬된 문자열을 반환  
  - `rjust(width [, fillchar])` | 너비만큼의 문자열에서 오른쪽 정렬된 문자열을 반환  
  - `lower()` | 모든 대소문자가 소문자로 변환된 문자열을 반환  
  - `upper()` | 문자열에서 모든 문자를 대문자로 변환한 문자열을 반환  
  - `title()` | 문자열에서 첫 글자만 대문자이고 나머지는 소문자인 문자열을 반환  
  - `swapcase()` | 문자열에서 소문자를 대문자로 대문자를 소문자로 변환한 문자열 반환  
  - `strip([chars])` | 문자열 양쪽에 지정된 chars 또는 공백을 제거한 문자열을 반환  
  - `lstrip([chars])` | 문자열 왼쪽에 지정된 chars 또는 공백을 제거한 문자열을 반환  
  - `rstrip([chars])` | 문자열 오른쪽에 지정된 chars 또는 공백을 제거한 문자열을 반환  
  - `partition(sep)` | 문자열에서 첫번째 sep를 기준으로 분할하여 3개의 튜플을 반환  
  - `rpartition(sep)` | 문자열에서 마지막 sep를 기준으로 분할하여 3개의 튜플을 반환  
  - `replace(old [, new[count]])` | 문자열의 모든 old를 new로 교체한 문자열을 반환  
  - `split(sep=None, maxsplit=1)` | sep를 구분자 문자열로 사용하여 문자열의 단어 목록을 반환  
  - `rsplit(sep=None, maxsplit=1)` | sep를 구분자 문자열로 사용하여 문자열의 단어 목록을 반환  
  - `splitlines([keepends])` | 문자열에서 라인 단위로 구분하여 리스트를 반환  
  - `startswith(prefix [, start[, end]])` | [start, end] 범위에서 지정한 prefix로 시작하면 True, 아니면 False 반환  
  - `endswith(prefix [, start[, end]])` | [start, end] 범위에서 지정한 suffix로 시작하면 True, 아니면 False 반환  
  - `zfill(width)` | 너비만큼의 문자열에서 비어있는 부분에 '0'이 채워진 문자열 반환  

- 기타 연산자  
  - `get()` | 각 요소에 인덱스 지정  
  - `slice()` | 각 요소에 슬라이스 적용
  - `slice_replace()` | 각 요소의 슬라이스를 특정 값으로 대체
  - `cat()` | 문자열 연결
  - `repeat()` | 값 반복
  - `normalize()` | 문자열의 유니코드 형태로 반환
  - `pad()` | 문자열 왼쪽, 오른쪽, 또는 양쪽 공백 추가
  - `wrap()` | 긴 문자열을 주어진 너비보다 짧은 길이의 여러 줄로 나눔
  - `join()` | Series의 각요소에 있는 문자열을 전달된 구분자와 결합
  - `get_dummies()` | DataFrame으로 가변수(dummy value)추출

- 정규표현식
  - `match()` | 각 요소에 `re.match()`호출. 불리언 값 반환
  - `extract()` | 각 요소에 `re.match()`호출. 문자열로 매칭된 그룹 반환
  - `findall()` | 각 요소에 `re.findall()`호출.
  - `replace()` | 패턴이 발생한 곳을 다른 문자열로 대체
  - `contains()` | 각 요소에 `re.search()`호출. 불리언 값 반환
  - `count()` | 패턴 발생 건수 집계
  - `split()` | `str.split()`과 동일하지만 정규 표현식 사용
  - `rsplit()` | `str.rsplit()`과 동일하지만 정규 표현식 사용

- 시계열 처리 학습
  - 시계열 데이터 구조 학습
| 타임스탬프(timestamp) | 기간(time period) | 시간 델타 또는 지속시간 |
|-----------------------|-------------------|-------------------------|
| Pandas`Timestamp`타입 제공 | Pandas`Period`타입 제공 | Pandas`Timedelta`타입 제공|
| 파이썬`datetime`대체 타입 | | 파이썬`datetime.timedelta`대체 타입 |
| `numpy.datetime64`타입 기반 | `numpy.datetime64`타입 기반 | `numpy.timedelta64`타입 기반 |
| `DatetimeIndex`인덱스 구조 |`PeriodIndex`인덱스 구조 | `TImedeltaIndex`인덱스 구조|

  - 시계열 기본 학습

  - 주기와 오프셋 학습

  - `D` | Day | 달력상 일
  - `B` | BusinessDay | 영업일
  - `W-MON`, `W-TUE`, ... | Week | 월별 주차와 요일
  - `W-MON`, `W-2MON`, ... | WeekOfMonth | 월별 주차와 요일
  - `MS` | `MonthBegin` | 월 시작일
  - `BMS` | BusinessMonthBegin | 영업일 기준 월 시작일
  - `M` | `MonthEnd` | 월 마지막일
  - `BM` | `BusinessMonthEnd` | 영업일 기준 월 마지막일
  - `QS-JAN`, `QS-FEB`, ... | QuarterBegin | 분기 시
  - `BQS-FEB`, `BQS-FEB`, ... | BusinessQuarterBegin | 영업일 기준 분기 시작
  - `Q-JAN`, `Q-FEB`, ... | QuarterEnd | 분기 마지막
  - `BQ-JAN`, `BQ-FEB`, ... | BusinessQuarterEnd | 영업일 기준 분기 마지막
  - `AS-JAN`, `AS-FEB`, ... | YearBegin | 연초
  - `BAS-JAN`, `BAS-FEB`, ... | BusinessYearEnd | 영업일 기준 연초
  - `A-JAN`, `A-FEB`, ... | YearEnd | 연말
  - `BA-JAN`, `BA-FEB`, ... | BusinessYearEnd | 영업일 기준 연말
  - `H` | Hour | 시간
  - `BH` | BusinessHour | 영업 시간
  - `T`또는`min` | Minute | 분
  - `S` | Second | 초
  - `L`또는`ms` | Milli | 밀로초
  - `U` | Micro | 마이크로초
  - `N` | Nano | 나노초

  - 시프트 학습(`shift()`)
  - 시간대 처리 학습(`pytz()`)
  - 기간과 기간 연산 학습

---

## Day 4 (2021-09-09)

- 리샘플링 학습

  * 리샘플링(Resampling): 시계열의 빈도 변환
  * 다운샘플링(Down sampling): 상위 빈도 데이터를 하위 빈도 데이터로 집계
  * 업샘플링(Up sampling): 하위 빈도 데이터를 상위 빈도 데이터로 집계

  - `freq` | 리샘플링 빈도
  - `axis` | 리샘플링 축(기본값 `axis=0`)
  - `fill_method` | 업샘플링시 보간 수행(`None`, `ffill`, `bfill`)
  - `closed` | 다운샘플링 시 각 간격의 포함 위치(`right`, `left`)
  - `label` | 다운샘플링 시 각 집계된 결과 라벨 결정(`right`, `left`)
  - `loffset` | 나뉜 그룹의 라벨을 맞추기 위한 오프셋
  - `limit` | 보간법을 사용할 때 보간을 적용할 최대 기간
  - `kind` |  기간(`period`) 또는 타임스탬프(`timestamp`) 집계 구분
  - `convention` | 기간을 리샘플링할 때 하위 빈도 기간에서 상위 빈도로 변환 시 방식(`start`또는`end`)

- 무빙 윈도우 학습

- 데이터 읽기 및 저장 학습
  - `read_csv` | 파일, URL, 객체로부터 구분된 데이터 읽기(기본 구분자:',')
  - `read_table` | 파일, URL, 객체로부터 구분된 데이터 읽기(기본 구분자:'\t')
  - `read_fwf` | 고정폭 컬럼 형식에서 데이터 읽기(구분자 없는 데이터)
  - `read_clipboard` | 클립보드에 있는 데이터 읽기. 웹페이지에 있는 표를 읽어올 때 유용
  - `read_excel` | 엑셀 파일(xls, xlsx)에서 표 형식 데이터 읽기
  - `read_hdf` | Pandas에서 저장한 HDFS 파일의 데이터 읽기
  - `read_html` | HTML 문서 내의 모든 테이블 데이터 읽기
  - `read_json` | JSON에서 데이터 읽기
  - `read_msgpack` | 메시지팩 바이너리 포맷으로 인코딩된 pandas 데이터 읽기
  - `read_pickle` | 파이썬 피클 포맷으로 저장된 객체 읽기
  - `read_sas` | SAS 시스템의 사용자 정의 저장 포멧 데이터 읽기
  - `read_sql` | SQL 질의 결과를 DataFrame 형식으로 읽기
  - `read_stata` | Stata 파일에서 데이터 읽기
  - `read_feather` | Feather 바이너리 파일 포맷의 데이터 읽기

  - 텍스트 파일 읽기/쓰기(`read_csv()`, `%%writefile`
  - 이진 데이터 파일 읽기/쓰기(`to_pickle()`, `read_pickle()`, `HDFStore()`, `to_hdf()`, read_hdf()`, `to_excel()`

- 데이터 정제학습
  - 누락값 처리 학습(`dropna()`, `fillna()`, `np.nan`, `None`)
  - 중복제거 학습(`duplicated()`, `drop_duplicateds()`)
  - 값 치환학습(`replace()`)

---

# Day 5 (2021-10-04)

- melt
  - id_vars : 속성으로 지정한 열을 제외한 나머지 정보열이 variable 열로, 정보 데이터는 value열로 정리됨
  - value_vars : 속성을 지정하면 지정한 열만을 대상으로 피벗 / 열이 2개이상이라면 리스트로 묶음
  - var_name : variable 표시되는 열이름 변경
  - var_name : value 표시되는 열이름 변경 

- to_numeric()
  - 문자열을 숫자로 변환가능
  - errors 속성을 사용하여 어느정도 오류를 제어할 수 있음
    - raise : 기본값
    - ignore : 오류 발생시 무시하고 가능한 것만 진행
    - coerce : 오류 발생시 NaN으로 변경하고 진행

- agg()
  - 판다스에서 제공하는 집계함수가 아닌 다른 함수를 사용하기 위함
  - 함수의 인수가 2개일 경우 2번째 인수의 이름과 변경값을 넣어주어 따로 실행
```
def my_mean_diff(values, diff_value):
    n = len(values)
    total = 0
    for value in values:
        total += value
    mean = total / n
    return mean - diff_value
    
age_mean_diff = df.groupby('year').lifeExp.agg(my_mean_diff, diff_value = global_mean)
```

------
# Day 6 (2021-10-07)

- transform()
  - 브로드캐스팅을 실행해야 하는 사용자 정의 함수를 실행해야 한다면 transform() 함수를 사용한다.

```
def my_zscore(x):
    return (x - x.mean()) / x.std()

df['zscore'] = df.groupby('year').lifeExp.transform(my_zscore)
```

- permutation()
  - 원본이 유지되고 배열을 복사   
- shuffle()
  - 원본도 수정하고 배열을 복사   
