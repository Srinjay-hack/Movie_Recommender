import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
  response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3243e328049f33aabaf3dcf1ebd94e2c&language=en-US'.format(movie_id))
  data=response.json()
  return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
  
 
def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:10]


  recommend_movies=[]
  recommend_movies_poster=[]
  for i in movies_list:
    movie_id=movies.iloc[i[0]].movie_id
    recommend_movies.append(movies.iloc[i[0]].title)
    recommend_movies_poster.append(fetch_poster(movie_id))
  
  return recommend_movies,recommend_movies_poster


movies_dict=pickle.load(open('model/movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('model/similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
  'How you want to get contacted?',
  movies['title'].values
)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 ,col6,col7,col8= st.columns(8)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])


