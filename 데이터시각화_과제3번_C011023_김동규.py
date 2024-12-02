import pyogrio
pyogrio.list_drivers()
import streamlit as st

st.title('C011023김동규 - 지도시각화 과제3번')

st.header('geojson파일 전처리')

import geopandas as gpd
import pandas as pd

st.write('+ geojson파일 불러오기')
gdf_korea_sigoongoo = gpd.read_file("./법정구역_시군구_simplified.geojson")
st.dataframe(gdf_korea_sigoongoo)

st.write('+ 영어로 된 열 이름을, 이해하기 좋게 한글로 바꾼 후, 동명인 지역이 있나 value count해보기')
gdf_korea_sigoongoo.rename(columns={'SIG_KOR_NM':'시군구별'},
                           inplace = True)
st.dataframe(gdf_korea_sigoongoo.시군구별.value_counts()) 

st.write('### 이름이 같은 동명 지역들 존재')
col_1, col_2, col_3,col_4 = st.columns([1,1,1,1])

col_1.write('##### 6지역 동명')
col_1.write('+ 동구')
col_1.write('+ 중구')

col_2.write('##### 5지역 동명')
col_2.write('+ 서구')

col_3.write('##### 4지역 동명')
col_3.write('+ 남구')
col_3.write('+ 북구')

col_4.write('##### 2지역 동명')
col_4.write('+ 강서구')
col_4.write('+ 고성군')


st.write('##### 동명지역 처리: 상위지역-하위지역 꼴로 구분하여 주기')
# 서울 지역
gdf_korea_sigoongoo.시군구별[1] = '서울-중구'
# 부산 지역
gdf_korea_sigoongoo.시군구별[25] = '부산-중구'
gdf_korea_sigoongoo.시군구별[26] = '부산-서구'
gdf_korea_sigoongoo.시군구별[27] = '부산-동구'
gdf_korea_sigoongoo.시군구별[31] = '부산-남구'
gdf_korea_sigoongoo.시군구별[32] = '부산-북구'
# 대구 지역
gdf_korea_sigoongoo.시군구별[41] = '대구-중구'
gdf_korea_sigoongoo.시군구별[42] = '대구-동구'
gdf_korea_sigoongoo.시군구별[43] = '대구-서구'
gdf_korea_sigoongoo.시군구별[44] = '대구-남구'
gdf_korea_sigoongoo.시군구별[45] = '대구-북구'
# 인천 지역
gdf_korea_sigoongoo.시군구별[50] = '인천-중구'
gdf_korea_sigoongoo.시군구별[51] = '인천-동구'
gdf_korea_sigoongoo.시군구별[57] = '인천-서구'
# 광주 지역
gdf_korea_sigoongoo.시군구별[60] = '광주-동구'
gdf_korea_sigoongoo.시군구별[61] = '광주-서구'
gdf_korea_sigoongoo.시군구별[62] = '광주-남구'
gdf_korea_sigoongoo.시군구별[63] = '광주-북구'
# 대전 지역
gdf_korea_sigoongoo.시군구별[65] = '대전-동구'
gdf_korea_sigoongoo.시군구별[66] = '대전-중구'
gdf_korea_sigoongoo.시군구별[67] = '대전-서구'
# 울산 지역
gdf_korea_sigoongoo.시군구별[70] = '울산-중구'
gdf_korea_sigoongoo.시군구별[71] = '울산-남구'
gdf_korea_sigoongoo.시군구별[72] = '울산-동구'
gdf_korea_sigoongoo.시군구별[73] = '울산-북구'
# 고성군
gdf_korea_sigoongoo.시군구별[223] = '경남-고성군'
gdf_korea_sigoongoo.시군구별[248] = '강원-고성군'
# 강서구
gdf_korea_sigoongoo.시군구별[15] = '서울-강서구'
gdf_korea_sigoongoo.시군구별[36] = '부산-강서구'

st.dataframe(gdf_korea_sigoongoo.시군구별.value_counts())

st.write('이제 동명 지역이 없이, 모든 count가 1임')

st.write('##### 출산율df와 지역 명칭 통일시키기 작업 실행')

gdf_korea_sigoongoo.시군구별[185] = '포항-남구'
gdf_korea_sigoongoo.시군구별[186] = '포항-북구'

gdf_korea_sigoongoo.시군구별[210] = '마산합포시'
gdf_korea_sigoongoo.시군구별[211] = '마산회원시'


gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('수원시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('성남시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('안양시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('안산시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('고양시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('용인시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('청주시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('천안시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('전주시 ','')
gdf_korea_sigoongoo['시군구별'] = gdf_korea_sigoongoo['시군구별'].str.replace('창원시 ','')


st.header('출산율 파일 전처리')
st.write('+ 출산율 excel파일 불러오기')

df_korea_birth_sig = pd.read_excel("./연령별_출산율_및_합계출산율_행정구역별_시군구별_20241125111756.xlsx",
                               sheet_name = '데이터',
                               header=1)
st.dataframe(df_korea_birth_sig)

st.write('+ 시군구별,출산율 2개의 열만 추출 후, 열이름 변경')

df_korea_birth_sig = df_korea_birth_sig[['행정구역별','합계출산율 (가임여성 1명당 명)']]
df_korea_birth_sig.columns = ['시군구별','출산율']
st.dataframe(df_korea_birth_sig)

st.write('+ 위의 행정구역열에서, 전국,서울특별시 등 상위 행정구역을 없애주고, 시군구 데이터만 남겨놓는 작업 실행')

#띄어쓰기(\u3000)를 포함한 문자열만 남기기 > 띄어쓰기 포함한 것만 하위 행정구역(시군구임)
df = df_korea_birth_sig[df_korea_birth_sig['시군구별'].str.contains('\u3000')]
df.reset_index(inplace=True) #인덱스 초기화
#문자열 공백 없애기
df['시군구별'] = df['시군구별'].str.replace('\u3000\u3000\u3000','')
#geojson과 명칭 통일(ex. 세종시 > 세종특별자치시)
df.시군구별[1] = '서울-중구'
df.시군구별[15] = '서울-강서구'
df.시군구별[26] = '부산-서구'
df.시군구별[27] = '부산-동구'
df.시군구별[31] = '부산-남구'
df.시군구별[32] = '부산-북구'
df.시군구별[252] = '경남-고성군'
df.시군구별[75] = '세종특별자치시'

st.dataframe(df)
st.write('+ 전처리 끝. 지도 시각화 실행해보기.')

import folium

gu_map_sigoongoo = folium.Map(location = [37.5,127], #서울을 중앙으로
                              zoom_start = 7,
                              tiles='cartodbpositron')

folium.Choropleth(
    geo_data = gdf_korea_sigoongoo,
    data = df,
    columns = ('시군구별','출산율'),
    key_on = 'feature.properties.시군구별',
    fill_color = 'BuPu',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '출생율'
).add_to(gu_map_sigoongoo)

#streamlit_folium활용하여, streamlit에서 folium 지도 시각화 가능
from streamlit_folium import folium_static
folium_static(gu_map_sigoongoo)



st.header('같은 방식으로 시.도별 출산율 지도 구현')



# geojson파일 불러오기
gdf_korea_sido = gpd.read_file("./법정구역_시도_simplified.geojson")
# 컬럼명 변경
gdf_korea_sido.rename(columns={'CTP_KOR_NM':'시도별'},
                      inplace = True)
# 출생율 excel파일 df으로 불러오기
df_korea_birth = pd.read_excel("./연령별_출산율_및_합계출산율_행정구역별__20241125111756.xlsx",
                               sheet_name = '데이터',
                               header=1)
# 행정구역과 출생율 2개의 열만 사용
df_korea_birth = df_korea_birth[['행정구역별','합계출산율 (가임여성 1명당 명)']]
# 컬럼명 변경
df_korea_birth.columns = ['시도별','출산율']
# 전국 평균 출산율에 해당하는 행 제거
df_korea_birth.drop([0], axis=0, inplace=True)

# 지도 시각화
gu_map_sido = folium.Map(location = [37.5,127], #서울 시작
                         zoom_start = 7,
                         tiles='cartodbpositron')

folium.Choropleth(
    geo_data = gdf_korea_sido,
    data = df_korea_birth,
    columns = ('시도별','출산율'),
    key_on = 'feature.properties.시도별',
    fill_color = 'BuPu',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '출생율'
).add_to(gu_map_sido)

check = st.checkbox('시도별 출산율 지도 보기')
if check:
    folium_static(gu_map_sido)