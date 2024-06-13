#Movie_recomm_system_myenv\Scripts\activate  -> to activate virtual environment

import streamlit as st
import pickle
import pandas as pd 
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']





def recommend(movie):
    movie_index = movies[movies['title'] == movie ].index[0]#fetching index of searched movie,,or movie on which we want to perform recommedation algo
    similarity = similarity_matrix[movie_index]
    movies_list = sorted(  list( enumerate( similarity ) ) , reverse=True , key=lambda x:x[1])[1:11]
    
    recommended_movies=[]
    movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id #fetch id of recommended_movie
        recommended_movies.append((movies.iloc[i[0]].title))
        #Fetch poster by hitting API of TMDB
        movies_poster.append(fetch_poster(movie_id))
    return recommended_movies , movies_poster


movie_dict = pickle.load(open('movies_dict.pkl','rb'))  #in movie_list we have copied new_df dataframe
movies = pd.DataFrame(movie_dict)

similarity_matrix = pickle.load(open('similarity_matrix','rb'))

st.title('Movie Recommendation System')

#User can i/p the text and search for particular movie..
selected_movie_name = st.selectbox('Search For Movies' , movies['title'].values)#movies['title'].values ->list of movie title (1 dimension list)

if st.button('Recommend'):
    names , posters = recommend(selected_movie_name)
    col1 , col2 , col3 , col4 , col5 , col6 , col7 , col8 , col9 , col10 = st.columns(10)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])

    
    



