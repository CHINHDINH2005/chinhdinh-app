import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title('Interactive Dashboard')
st.header('Nhóm: Đinh Văn Chính, Nguyễn Quốc Khánh, Nguyễn Xuân Toàn ')
st.header('Link website: http://localhost:8501/')
st.header("Interactive Dashboard")
st.subheader("Interact with this dashboard using the widgets on the sidebar")

#đọc dữ liệu
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")
movies_data.info()
movies_data.dropna()

#lọc dữ liệu năm điểm và thể loại phim
year_list = movies_data['year'].unique().tolist()
score_rating = movies_data['score'].unique().tolist()
genre_list = movies_data['genre'].unique().tolist()

#sidebar
st.sidebar.write('Select a range on the slider (it represents movie score) to view the total number of movies in a genre that falls within that range')
st.sidebar.slider('Choose a value:', 1.0,10.0)
st.sidebar.write('Select your preferred genre(s) and year to view the movies released that year and on that genre')
new_genre_list = st.sidebar.multiselect('Choose Genre:',genre_list)
new_year_list= st.sidebar.selectbox('Choose a Year:',year_list)

#danh sách phim lọc theo năm và thể loại
new_genre_year = (movies_data['genre'].isin(new_genre_list)) & (movies_data['year'] == new_year_list)
st.write(" Lists of movies filtered by year and Genre ")
genre_year = movies_data[new_genre_year].groupby(['name', 'genre'])['year'].sum()
genre_year = genre_year.reset_index()
st.dataframe(genre_year, width = 800)

#lấy dữ liệu điểm,đạo diễn 
director_score = movies_data[[ 'director', 'score']] 

# Tính điểm đánh giá trung bình theo từng đạo diễn 
top_directors = director_score.groupby(['director'])['score'].mean().reset_index()

#xếp thứ tự các đạo diễn có điểm đánh giá trung bình từ lớn đến bé
top_directors = top_directors.sort_values(by='score', ascending=False)
top_10_directors = top_directors.head(10)

# Vẽ biểu đồ cột
plt.figure(figsize=(18,8))
plt.bar(top_10_directors['director'], top_10_directors['score'], color='skyblue')

# Cài đặt tiêu đề và nhãn
plt.ylabel('Điểm đánh giá trung bình')
plt.xlabel('Đạo diễn')
plt.title('Các đạo diễn có điểm đánh giá trung bình cao nhất')

# Hiển thị biểu đồ
st.pyplot(plt)
