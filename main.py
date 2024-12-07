import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

url = "movies_metadata.csv"
movies_df = pd.read_csv (url)

print(movies_df.isnull().sum())


print(movies_df)
print(movies_df['belongs_to_collection'])

movies_df['belongs_to_collection'].fillna(movies_df['belongs_to_collection'].mean(),inplace=True)

def extract_generes(generes_str):
  try:
    genres = ast.literal_eval(generes_str)
    return [genres['name']for genere in genres]
  except (ValueError, TypeError):
    return []


movies_df['genres'] = movies_df['genres'].apply(extract_generes)
# print(movies_df['genres'])


movies_df['budget'] = pd.to_numeric (movies_df['budget ], errors='coerce")
movies_df['revenue'] = pd. to_numeric (movies_df ['revenue'], errors='coerce")
                                       
movies_df.dropna (subset=[ 'budget', 'revenuel'], inplace=True)

  #--------------------------------------
  movies_df['release_year'] = pd.to_datetime(movies_df['release_date'])
  print(movies_df['release_year])


    #--------------------------------------

genre_exploded = movies_df[[ 'title' ,'release_year', 'budget', 'revenue', 'genres ]]. explode ('genres")
print(genre_exploded)

genre_counts = genre_exploded['genres'].value_count()

pet.figure(figsize=(10,6))
sns.barplot(x=genres_counts.index, y=genre_counts.values)
plt.title("кількість фільмів за жанрами")
plt.xlabel("жан")
plt.xlabel("кiлькiсть")


plt.show()


    
