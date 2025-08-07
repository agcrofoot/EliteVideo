import pandas as pd
import sqlite3
import os

# Make sure the db folder exists
os.makedirs('C:/Users/birdc/source/repos/EliteVideo/db', exist_ok=True)

# Connect to a local SQLite database (it will be created if it doesn’t exist)
conn = sqlite3.connect('C:/Users/birdc/source/repos/EliteVideo/db/movies.db')

# === Load new video from file ===
excel_path = 'C:/Users/birdc/source/repos/EliteVideo/data/EliteVideo_data.xlsx'
videos_new = pd.read_excel(excel_path, sheet_name='Video')

# === Get existing video IDs from the database ===
existing_videos = pd.read_sql_query("SELECT VID_NUM FROM Video", conn)

# === Filter: only keep videos not already in the DB ===
videos_to_insert = videos_new[~videos_new['VID_NUM'].isin(existing_videos['VID_NUM'])]

# === Insert new videos ===
if not videos_to_insert.empty:
    videos_to_insert.to_sql('Video', conn, if_exists='append', index=False)
    print(f"Inserted {len(videos_to_insert)} new video(s).")
else:
    print("No new videos to insert.")



# === Load new price from file ===
excel_path = 'C:/Users/birdc/source/repos/EliteVideo/data/EliteVideo_data.xlsx'
prices_new = pd.read_excel(excel_path, sheet_name='Price')

# === Get existing price IDs from the database ===
existing_prices = pd.read_sql_query("SELECT PRICE_CODE FROM Price", conn)

# === Filter: only keep prices not already in the DB ===
prices_to_insert = prices_new[~prices_new['PRICE_CODE'].isin(existing_prices['PRICE_CODE'])]

# === Insert new prices ===
if not prices_to_insert.empty:
    prices_to_insert.to_sql('Price', conn, if_exists='append', index=False)
    print(f"Inserted {len(prices_to_insert)} new price(s).")
else:
    print("No new prices to insert.")



# === Load new movie from file ===
excel_path = 'C:/Users/birdc/source/repos/EliteVideo/data/EliteVideo_data.xlsx'
movies_new = pd.read_excel(excel_path, sheet_name='Movie')

# === Get existing movie IDs from the database ===
existing_movies = pd.read_sql_query("SELECT MOVIE_NUM FROM Movie", conn)

# === Filter: only keep movie not already in the DB ===
movies_to_insert = movies_new[~movies_new['MOVIE_NUM'].isin(existing_movies['MOVIE_NUM'])]

# === Insert new movies ===
if not movies_to_insert.empty:
    movies_to_insert.to_sql('Movie', conn, if_exists='append', index=False)
    print(f"Inserted {len(movies_to_insert)} new movie(s).")
else:
    print("No new movies to insert.")
    
    

# === Load new membership from file ===
excel_path = 'C:/Users/birdc/source/repos/EliteVideo/data/EliteVideo_data.xlsx'
memberships_new = pd.read_excel(excel_path, sheet_name='Membership')

# === Get existing membership IDs from the database ===
existing_memberships = pd.read_sql_query("SELECT MEM_NUM FROM Membership", conn)

# === Filter: only keep membership not already in the DB ===
memberships_to_insert = memberships_new[~memberships_new['MEM_NUM'].isin(existing_memberships['MEM_NUM'])]

# === Insert new memberships ===
if not memberships_to_insert.empty:
    memberships_to_insert.to_sql('Membership', conn, if_exists='append', index=False)
    print(f"Inserted {len(memberships_to_insert)} new membership(s).")
else:
    print("No new memberships to insert.")
   
   
    
# === Load new rental from file ===
excel_path = 'C:/Users/birdc/source/repos/EliteVideo/data/EliteVideo_data.xlsx'
rentals_new = pd.read_excel(excel_path, sheet_name='Rental')

# === Get existing rental IDs from the database ===
existing_rentals = pd.read_sql_query("SELECT RENT_NUM FROM Rental", conn)

# === Filter: only keep rentals not already in the DB ===
rentals_to_insert = rentals_new[~rentals_new['RENT_NUM'].isin(existing_rentals['RENT_NUM'])]

# === Insert new rentals ===
if not rentals_to_insert.empty:
    rentals_to_insert.to_sql('Rental', conn, if_exists='append', index=False)
    print(f"Inserted {len(rentals_to_insert)} new rental(s).")
else:
    print("No new rentals to insert.")
    
    
    
# === Load new detail rental from file ===
excel_path = 'C:/Users/birdc/source/repos/EliteVideo/data/EliteVideo_data.xlsx'
details_new = pd.read_excel(excel_path, sheet_name='DetailRental')

# === Get existing detail rentals IDs from the database ===
existing_details = pd.read_sql_query("SELECT RENT_NUM, VID_NUM FROM DetailRental", conn)

# === Create composite keys in both ===
existing_details['composite_key'] = (
    existing_details['RENT_NUM'].astype(str) + '-' + existing_details['VID_NUM'].astype(str)
)
details_new['composite_key'] = (
    details_new['RENT_NUM'].astype(str) + '-' + details_new['VID_NUM'].astype(str)
)

# === Filter: only keep detail rentals not already in the DB ===
details_to_insert = details_new[~details_new['composite_key'].isin(existing_details['composite_key'])]

# === Drop helper column before inserting ===
details_to_insert = details_to_insert.drop(columns=['composite_key'])

# === Insert new detail rentals ===
if not details_to_insert.empty:
    details_to_insert.to_sql('DetailRental', conn, if_exists='append', index=False)
    print(f"Inserted {len(details_to_insert)} new detail(s).")
else:
    print("No new details to insert.")
    