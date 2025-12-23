import pandas as pd
import os

def load_and_merge_data(red_path, white_path):
    """
    Đọc dữ liệu từ 2 file csv chất lượng rượu vang đỏ và trắng, thêm cột phân loại và gộp lại.
    """
    # Kiểm tra file có tồn tại không
    if not os.path.exists(red_path) or not os.path.exists(white_path):
        print("Lỗi: Không tìm thấy file dữ liệu trong thư mục 'data/'")
        return None

    try:
        # sep=';' vì Dữ liệu này dùng ';' để ngăn cách
        df_red = pd.read_csv(red_path, sep=';')
        df_white = pd.read_csv(white_path, sep=';')

        # Thêm cột 'wine_type' để phân biệt: 0 là Đỏ, 1 là Trắng (hoặc để string cho dễ đọc)
        df_red['wine_type'] = 'Red'
        df_white['wine_type'] = 'White'

        # dùng axis = 0 để Gộp 2 bảng theo chiều dọc
        df_final = pd.concat([df_red, df_white], axis=0)
        
        # Reset lại index để các dòng có số thứ tự liên tục
        df_final.reset_index(drop=True, inplace=True)

        print(f"TẢI DỮ LIỆU THÀNH CÔNG!")
        print(f"Số lượng rượu đỏ: {df_red.shape[0]}")
        print(f"Số lượng rượu trắng: {df_white.shape[0]}")
        print(f"Tổng kích thước sau khi gộp: {df_final.shape}")
        
        return df_final

    except Exception as e:
        print(f"Có lỗi khi đọc file: {e}")
        return None