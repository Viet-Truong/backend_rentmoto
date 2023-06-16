from api.Connect import connect
from api.xuli import *
import pyodbc
import os
import json
import decimal

ERROR='error'
SUCCESS='success'
DATA_INVALID='Data invalid'
DATA_NULL='Data null'

def getALlLoi():
    conn = connect()
    cursor = conn.cursor
    
    sql='Select * from LoiPhat'
    cursor.execute(sql)
    rows= cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    
    return printRs(SUCCESS,None,rsData(rows,columnName))

def thongKe():
    conn = connect()
    cursor = conn.cursor

    # Tổng số đăng ký thuê xe
    sql_tong_so_dang_ky = 'SELECT COUNT(maThue) FROM DangKyThueXe'
    cursor.execute(sql_tong_so_dang_ky)
    tong_so_dang_ky = cursor.fetchone()[0]

    # Tổng số đăng ký thuê xe đã duyệt
    sql_tong_so_dang_ky_da_duyet = "SELECT COUNT(maThue) FROM DangKyThueXe WHERE trangThai = N'Đã duyệt'"
    cursor.execute(sql_tong_so_dang_ky_da_duyet)
    tong_so_dang_ky_da_duyet = cursor.fetchone()[0]

    # Tổng số đăng ký thuê xe chưa duyệt
    sql_tong_so_dang_ky_chua_duyet = "SELECT COUNT(maThue) FROM DangKyThueXe WHERE trangThai = N'Chưa duyệt'"
    cursor.execute(sql_tong_so_dang_ky_chua_duyet)
    tong_so_dang_ky_chua_duyet = cursor.fetchone()[0]

    # Tổng tiền đăng ký thuê xe
    sql_tong_tien_dang_ky = 'SELECT SUM(giaThue) FROM ChiTietThueXe'
    cursor.execute(sql_tong_tien_dang_ky)
    tong_tien_dang_ky = cursor.fetchone()[0]

    # Đóng kết nối cơ sở dữ liệu
    conn.close()

    # Chuyển đổi giá trị Decimal thành float
    tong_tien_dang_ky = float(tong_tien_dang_ky)

    # Tạo dictionary để lưu trữ kết quả
    thong_ke = {
        'TongSoDangKyThueXe': tong_so_dang_ky,
        'TongSoDangKyThueXeDaDuyet': tong_so_dang_ky_da_duyet,
        'TongSoDangKyThueXeChuaDuyet': tong_so_dang_ky_chua_duyet,
        'TongTienDangKyThueXe': tong_tien_dang_ky
    }
    # Trả về kết quả dưới dạng JSON
    return json.dumps(thong_ke)
