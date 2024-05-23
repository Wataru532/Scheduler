import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # CSVファイルを読み込む
    with open(csv_file_path, 'r', encoding='cp932') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        
        # JSONファイルに書き込む
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_data = json.dumps([row for row in csv_reader], indent=1, ensure_ascii=False)
            json_file.write(json_data)

if __name__ == '__main__':
    csv_file_path = 'data/クラス一覧_may24.csv'    # 入力となるCSVファイルのパス
    json_file_path = 'data/schedule_data.json' # 出力するJSONファイルのパス
    
    csv_to_json(csv_file_path, json_file_path)
