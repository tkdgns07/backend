import pandas as pd

# 파일 업로드
file_path = "APPL/APPL_Stocks.csv"  # 업로드한 파일 경로로 변경하세요
output_path = "APPL/APPL_Stocks.csv"  # 저장할 파일명

# CSV 파일 불러오기
df = pd.read_csv(file_path)

# 첫 두 열만 유지
df = df.iloc[:, :2]

# 두 번째 열의 이름 가져오기
second_col = df.columns[1]

# 두 번째 열에서 '$' 제거 후 숫자로 변환
df[second_col] = df[second_col].replace({'\$': ''}, regex=True).astype(float)

# 수정된 데이터 저장
df.to_csv(output_path, index=False)