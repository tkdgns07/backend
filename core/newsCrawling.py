import pandas as pd
import math
from django.http import JsonResponse

def news_crawling(request):
    page = int(request.GET.get("page", 0))
    symbol = request.GET.get("symbol", "")
    
    csv_file_path = f"core/data/News/{symbol}.csv"
    
    if page < 0 or page > 8:
        return JsonResponse({"error": "Invalid page number. Must be between 0 and 8."}, status=400)
    
    df = pd.read_csv(csv_file_path)
    df = df[["title", "link", "description", "realDate"]]  # 필요한 열만 선택
    
    total_records = len(df)
    records_per_page = math.ceil(total_records / 9)  # 전체 개수를 9등분
    
    start_idx = page * records_per_page
    end_idx = min(start_idx + records_per_page, total_records)
    
    df_page = df.iloc[start_idx:end_idx]  # 페이지 범위에 해당하는 데이터 추출
    
    result_json = df_page.to_dict(orient="records")
    return JsonResponse(result_json, safe=False)
