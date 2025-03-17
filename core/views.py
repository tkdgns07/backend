import pandas as pd
from django.http import JsonResponse
import os

def extract_csv_data(request):
    file_path = "core/APPL_Stocks.csv"  # CSV 파일 경로

    if not os.path.exists(file_path):
        return JsonResponse({"error": "파일이 존재하지 않습니다."}, status=400)

    # CSV 파일 불러오기
    df = pd.read_csv(file_path)

    # 컬럼 이름을 확인하고 변경 (만약 'date', 'price'가 아니라면)
    df.columns = ["date", "price"]

    # 최근 25개 행 선택 (최신 날짜가 위에 있다고 가정)
    df = df.head(25)

    # JSON 형태로 변환하여 [{ "date": "YYYY-MM-DD", "price": number }] 형식으로 반환
    data = df.to_dict(orient="records")

    return JsonResponse(data, safe=False)
