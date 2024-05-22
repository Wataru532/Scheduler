from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Drive APIの認証情報を読み込む
creds = service_account.Credentials.from_service_account_file(
    'path_to_your_service_account_json_file.json',
    scopes=['https://www.googleapis.com/auth/drive'])

# Google Drive APIのリソースを構築する
drive_service = build('drive', 'v3', credentials=creds)

# ファイルのIDを指定して、ファイルの中身を取得する
file_id = 'your_file_id_here'
file = drive_service.files().get_media(fileId=file_id).execute()

# ファイルの中身を表示する
print(file)