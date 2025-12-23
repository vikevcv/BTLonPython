import pandas as pd
import numpy as np

def clean_data(df):
    """
    Làm gọn dữ liệu: Xử lý dòng trùng lặp và giá trị null/NaN.
    """
    print("[Đang xử lý làm sạch dữ liệu...]")
    
    # 1. Kiểm tra và xóa dữ liệu trùng lặp
    initial_rows = df.shape[0]
    df_cleaned = df.drop_duplicates()
    deleted_rows = initial_rows - df_cleaned.shape[0]
    
    if deleted_rows > 0:
        print(f"- Đã xóa {deleted_rows} dòng trùng lặp.")
    else:
        print("- Không có dữ liệu trùng lặp.")

    # 2. Xử lý giá trị thiếu (Null/NaN)
    if df_cleaned.isnull().sum().sum() > 0:
        # Chỉ điền giá trị trung bình cho các cột số (numeric columns)
        numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
        df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].mean())
        print("- Đã điền giá trị trung bình vào các ô trống.")
    else:
        print("- Không phát hiện giá trị thiếu (Null).")
        
    return df_cleaned

def normalize_data(df):
    """
    Chuẩn hóa Min-Max Scaling cho các cột dữ liệu số (trừ cột wine_type).
    Công thức: (X - min) / (max - min)
    """
    print("\n[Đang xử lý chuẩn hóa dữ liệu...]")
    df_norm = df.copy()
    
    # Lấy danh sách các cột là số (loại bỏ cột string 'wine_type')
    numeric_cols = df_norm.select_dtypes(include=[np.number]).columns
    
    # Có thể loại bỏ cột 'quality' khỏi việc chuẩn hóa nếu muốn giữ nguyên điểm số gốc (3-9)
    # Tuy nhiên, đề bài yêu cầu chuẩn hóa chung nên ta làm hết.
    for col in numeric_cols:
        max_val = df_norm[col].max()
        min_val = df_norm[col].min()
        if max_val != min_val: # Tránh chia cho 0
            df_norm[col] = (df_norm[col] - min_val) / (max_val - min_val)
            
    print("- Đã chuẩn hóa dữ liệu về đoạn [0, 1].")
    return df_norm
