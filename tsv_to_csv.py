import csv
import os
import sys
import ctypes

def convert_tsv_to_csv(tsv_file):
    # 입력 파일 확인
    if not tsv_file.lower().endswith('.tsv'):
        ctypes.windll.user32.MessageBoxW(0, "The file is not a TSV file.", "Error", 1)
        return

    # .csv 파일 이름 생성
    csv_file = tsv_file.replace('.tsv', '.csv')

    try:
        with open(tsv_file, 'r', encoding='utf-8') as tsv:  # tsv 파일 열기
            tsv_reader = csv.reader(tsv, delimiter='\t')  # TSV 읽기
            with open(csv_file, 'w', encoding='utf-8', newline='') as csv_out:  # csv 파일 열기
                csv_writer = csv.writer(csv_out, delimiter=',')  # CSV 쓰기 준비
                for row in tsv_reader:
                    csv_writer.writerow(row)  # 데이터 쓰기
        ctypes.windll.user32.MessageBoxW(0, f"Successfully converted to: {csv_file}", "Success", 1)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"Failed to convert file: {e}", "Error", 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:  # 파일 경로가 명령줄 인자로 전달되었는지 확인
        input_file = sys.argv[1]
        convert_tsv_to_csv(input_file)
    else:
        ctypes.windll.user32.MessageBoxW(0, "No file provided. Please run this program with a .tsv file.", "Error", 1)
# pyinstaller --onefile --noconsole tsv_to_csv.py