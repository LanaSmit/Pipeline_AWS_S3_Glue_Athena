import sys
import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from io import StringIO


def extract_spotify_tracks(client_id, client_secret, artist_name="Drake", limit=50):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    ))

    results = sp.search(q=f'artist:{artist_name}', type='track', limit=limit)
    tracks = results['tracks']['items']

    data = []
    for track in tracks:
        data.append({
            'track_name': track['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'track_id': track['id']
        })

    return pd.DataFrame(data)


def transform_data(df):
    df = df.drop_duplicates(subset='track_id')
    df = df.dropna(subset=['track_name', 'track_id'])

    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df.dropna(subset=['release_date'])

    return df


def load_to_s3(df, bucket_name, key):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=key, Body=csv_buffer.getvalue())

    print("Data successfully uploaded to S3!")


def main():
    client_id = sys.argv[sys.argv.index('--SPOTIPY_CLIENT_ID') + 1]
    client_secret = sys.argv[sys.argv.index('--SPOTIPY_CLIENT_SECRET') + 1]
    bucket_name = sys.argv[sys.argv.index('--S3_BUCKET_NAME') + 1]

    try:
        # Extract
        df_raw = extract_spotify_tracks(client_id, client_secret)

        # Transform
        df_clean = transform_data(df_raw)

        # Load
        s3_key = 'spotify/clean_tracks.csv'
        load_to_s3(df_clean, bucket_name, s3_key)

        print("ETL pipeline executed successfully!")

    except Exception as e:
        print("Job failed")
        raise e


if __name__ == "__main__":
    main()
