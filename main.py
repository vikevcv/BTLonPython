#Hoa Vĩ Khang
#24110240
from xuLyDuLieu.loader import load_and_merge_data
from xuLyDuLieu.cleaner import clean_data, normalize_data
from trucQuanHoa.chart import draw_quality_distribution, draw_correlation_matrix ,draw_alcohol_comparison
def main():
    print("=== CHƯƠNG TRÌNH PHÂN TÍCH CHẤT LƯỢNG RƯỢU VANG ===")
    
    red_file = 'data/winequality-red.csv'
    white_file = 'data/winequality-white.csv'
    # 2. Đọc và gộp dữ liệu
    df = load_and_merge_data(red_file, white_file)
    
    if df is not None:
        # Hiển thị vài dòng đầu để kiểm tra
        print("Dữ liệu gốc: ")
        print(df.head())
        
        # 3. Làm sạch dữ liệu
        df_clean = clean_data(df)
        
        # 4. Trực quan hóa dữ liệu TRƯỚC khi chuẩn hóa (để giữ giá trị thực dễ đọc)
        print("Vẽ biểu đồ")
        print("1. Đang vẽ biểu đồ phân phối điểm chất lượng...")
        draw_quality_distribution(df_clean)
        
        print("2. Đang vẽ biểu đồ so sánh nồng độ cồn...")
        draw_alcohol_comparison(df_clean)
        
        print("3. Đang vẽ ma trận tương quan...")
        draw_correlation_matrix(df_clean)
        
        # 5. Chuẩn hóa dữ liệu (Bước cuối cùng để chuẩn bị cho Machine Learning nếu cần)
        df_normalized = normalize_data(df_clean)
        print("Dữ liệu sau khi chuẩn hóa: ")
        print(df_normalized.head())
        
        # Ghi file kết quả ra csv (Optional)
        # df_normalized.to_csv('data/winequality_processed.csv', index=False)
        print("HOÀN TẤT CHƯƠNG TRÌNH!!!")
        print("Thank you for using our Program! ")

if __name__ == "__main__":
    main()

#Tester
#Võ Cao Quốc Khánh
#24110252
