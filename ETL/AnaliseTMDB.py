import pandas as pd 
import requests as rqt
import json

read_movies = pd.read_csv('movies.csv', dtype={'anoLancamento': str}, sep='|')

df_movies = pd.DataFrame(read_movies)

df_movies['anoLancamento'] = pd.to_numeric(df_movies['anoLancamento'], errors='coerce')

df1 = df_movies.loc[(df_movies['genero'] == 'Animation') & (df_movies['notaMedia'] > 7.1), ['id', 'tituloOriginal', 'genero', 'notaMedia', 'numeroVotos', 'anoLancamento']]
df2 = df_movies.loc[(df_movies['genero'] == 'Adventure,Animation,Comedy') & (df_movies['notaMedia'] > 7.1), ['id', 'tituloOriginal', 'genero', 'notaMedia', 'numeroVotos', 'anoLancamento']]
df3 = df_movies.loc[(df_movies['genero'] == 'Comedy') & (df_movies['notaMedia'] > 7.1), ['id', 'tituloOriginal', 'genero', 'notaMedia', 'numeroVotos', 'anoLancamento']]

df_merge = pd.concat([df1, df2, df3, df4])

df_year = df_merge.loc[df_merge['anoLancamento'] >= 2020]

names_movies = df_year['tituloOriginal']

# api_key = '6c54ccaf29be2d55b2edf80de4ba53cb'



title = []
popularity = []
list_json = []
lote = 1

for movie in names_movies:
    url = f"https://api.themoviedb.org/3/search/movie?api_key=6c54ccaf29be2d55b2edf80de4ba53cb"

    headers = {"query": movie}
    rsp = rqt.get(url, headers)
    data = rsp.json()

    if len(data['results']) != 0:
        popularity.append(data['results'][0]['popularity'])
        title.append(data['results'][0]['title'])

        if len(popularity) == 100:
            with open(f'lote{lote}.json', 'w') as file:
                json.dump({"popularity": popularity, "title": title}, file)
            popularity.clear()
            title.clear()
            lote += 1

    else:
        pass


# if popularity:
#     with open(f'lote{lote}.json', 'w') as file:
#         json.dump({"popularity": popularity, "title": title}, file)
