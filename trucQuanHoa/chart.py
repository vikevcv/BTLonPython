import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def draw_quality_distribution(df):
    """Vẽ biểu đồ phân phối điểm chất lượng (Quality)"""
    plt.figure(figsize=(8, 5))
    
    # Đếm số lượng từng điểm chất lượng
    counts = df['quality'].value_counts().sort_index()
    
    plt.bar(counts.index, counts.values, color='#800020', alpha=0.7)
    plt.title('Phân phối điểm chất lượng rượu (Quality Distribution)')
    plt.xlabel('Điểm chất lượng (3 - 9)')
    plt.ylabel('Số lượng mẫu')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def draw_alcohol_comparison(df):
    """Vẽ biểu đồ so sánh nồng độ cồn giữa rượu Đỏ và Trắng"""
    red_alcohol = df[df['wine_type'] == 'Red']['alcohol']
    white_alcohol = df[df['wine_type'] == 'White']['alcohol']
    
    plt.figure(figsize=(10, 6))
    plt.hist(red_alcohol, bins=20, alpha=0.5, label='Rượu Đỏ', color='red')
    plt.hist(white_alcohol, bins=20, alpha=0.5, label='Rượu Trắng', color='gold')
    
    plt.title('So sánh nồng độ cồn (Alcohol) giữa 2 loại rượu')
    plt.xlabel('Nồng độ cồn (%)')
    plt.ylabel('Tần suất')
    plt.legend()
    plt.show()

def draw_correlation_matrix(df):
    """Vẽ ma trận tương quan (Heatmap) đơn giản bằng Matplotlib"""
    # Chỉ lấy các cột số để tính tương quan
    df_numeric = df.select_dtypes(include=[np.number])
    corr = df_numeric.corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    cax = ax.matshow(corr, cmap='coolwarm')
    fig.colorbar(cax)
    
    # Gán nhãn trục
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha='left')
    plt.yticks(range(len(corr.columns)), corr.columns)
    
    plt.title('Ma trận tương quan giữa các thành phần', pad=20)
    plt.show()