import pandas as pd
import requests
import io

def load_nba_box_score_data():
    # download from google sheets
    google_drive_sharing_url = "https://drive.google.com/file/d/1kWZC9aJf3KCboVfqN8x83kyh6aVSVDWd/view?usp=sharing"
    path ='https://drive.google.com/uc?id=' + google_drive_sharing_url.split('/')[-2]
    df = pd.read_csv(path)
    return df
    #download from github
    #github_url = "https://raw.githubusercontent.com/MylesThomas/nba-box-score-predictions/main/nba_games_data.csv"
    #download = requests.get(github_url).content
    #df = pd.read_csv(io.StringIO(download.decode('utf-8')))
    #return df