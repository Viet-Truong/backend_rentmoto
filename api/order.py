from api.Connect import connect
from api.xuli import *
import pyodbc
from pathlib import Path
from datetime import date
import json
import decimal

ERROR='error'
SUCCESS='success'
DATA_INVALID='Data invalid'
DATA_NULL='Data null'

def getAllOrder(page,q=None,maTaiKhoan=None):
    so_item=10
    vt=(page-1)*so_item

    # kt=(page-1)*10+10
    conn = connect()
    cursor = conn.cursor 
    rs={}
    strSearch=""
    if q is not None:     
        strSearch+=f" and hoTen LIKE N'%{q}%'"
    sql=f"SELECT DangKyThueXe.*, hoTen from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan"+strSearch +f" order by ngayBD desc OFFSET {vt} ROWS FETCH NEXT {so_item} ROWS ONLY;"
    cursor.execute(sql)
    data_don = cursor.fetchall()
    
    columnName=[column[0] for column in cursor.description]
    data_don=rsData(data_don,columnName)
    sql=f"SELECT count(*) from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan"+strSearch +f""
    cursor.execute(sql)
    row = cursor.fetchone()
    soLuong = row[0]
    soTrang=getSoTrang(soLuong,so_item)

    

    sql="SELECT ChiTietThueXe.*,tenXe,loaiXe,hangXe,bienSoXe from ChiTietThueXe,Xe where ChiTietThueXe.maXe=Xe.maXe"
    cursor.execute(sql)
    data_chitiet = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_chitiet=rsData(data_chitiet,columnName)
    
    sql="SELECT ct.maLoi as maLoi,lp.noiDungLoi as noiDungLoi,ct.ghiChu as ghiChu,ct.tienPhat as tienPhat FROM ChiTietLoiPhat as ct, LoiPhat as lp WHERE ct.maLoaiLoi = lp.maLoaiLoi"
    cursor.execute(sql)
    data_loi = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_loi=rsData(data_loi,columnName)
    
    new_data_chitiet=mergeData(data_chitiet,data_loi,"maLoi","loi")
    
    
    new_data=mergeData(data_don,new_data_chitiet,"maThue","chiTiet")
    
    rs = printRs(SUCCESS,None,new_data,True)
    rs['soTrang'] = soTrang
    conn.close()
    return rs

def getOrderAccepted(page,q=None,maTaiKhoan=None):
    so_item=10
    vt=(page-1)*so_item

    # kt=(page-1)*10+10
    conn = connect()
    cursor = conn.cursor 
    rs={}
    strSearch=""
    if q is not None:     
        strSearch+=f" and hoTen LIKE N'%{q}%'"
    sql=f"SELECT DangKyThueXe.*, hoTen from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan and DangKyThueXe.trangThai = N'Đã duyệt'"+strSearch +f" order by ngayBD desc OFFSET {vt} ROWS FETCH NEXT {so_item} ROWS ONLY;"
    cursor.execute(sql)
    data_don = cursor.fetchall()
    
    columnName=[column[0] for column in cursor.description]
    data_don=rsData(data_don,columnName)
    sql=f"SELECT count(*) from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan and DangKyThueXe.trangThai = N'Đã duyệt'"+strSearch +f""
    cursor.execute(sql)
    row = cursor.fetchone()
    soLuong = row[0]
    soTrang=getSoTrang(soLuong,so_item)

    

    sql="SELECT ChiTietThueXe.*,tenXe,loaiXe,hangXe,bienSoXe from ChiTietThueXe,Xe where ChiTietThueXe.maXe=Xe.maXe"
    cursor.execute(sql)
    data_chitiet = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_chitiet=rsData(data_chitiet,columnName)
    
    sql="SELECT ct.maLoi as maLoi,lp.noiDungLoi as noiDungLoi,ct.ghiChu as ghiChu,ct.tienPhat as tienPhat FROM ChiTietLoiPhat as ct, LoiPhat as lp WHERE ct.maLoaiLoi = lp.maLoaiLoi"
    cursor.execute(sql)
    data_loi = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_loi=rsData(data_loi,columnName)
    
    new_data_chitiet=mergeData(data_chitiet,data_loi,"maLoi","loi")
    
    
    new_data=mergeData(data_don,new_data_chitiet,"maThue","chiTiet")
    
    rs = printRs(SUCCESS,None,new_data,True)
    rs['soTrang'] = soTrang
    conn.close()
    return rs

def getOrderUnAccepted(page,q=None,maTaiKhoan=None):
    so_item=10
    vt=(page-1)*so_item

    # kt=(page-1)*10+10
    conn = connect()
    cursor = conn.cursor 
    rs={}
    strSearch=""
    if q is not None:     
        strSearch+=f" and hoTen LIKE N'%{q}%'"
    sql=f"SELECT DangKyThueXe.*, hoTen from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan and DangKyThueXe.trangThai = N'Chưa duyệt'"+strSearch +f" order by ngayBD desc OFFSET {vt} ROWS FETCH NEXT {so_item} ROWS ONLY;"
    cursor.execute(sql)
    data_don = cursor.fetchall()
    
    columnName=[column[0] for column in cursor.description]
    data_don=rsData(data_don,columnName)
    sql=f"SELECT count(*) from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan and DangKyThueXe.trangThai = N'Chưa duyệt'"+strSearch +f""
    cursor.execute(sql)
    row = cursor.fetchone()
    soLuong = row[0]
    soTrang=getSoTrang(soLuong,so_item)

    

    sql="SELECT ChiTietThueXe.*,tenXe,loaiXe,hangXe,bienSoXe from ChiTietThueXe,Xe where ChiTietThueXe.maXe=Xe.maXe"
    cursor.execute(sql)
    data_chitiet = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_chitiet=rsData(data_chitiet,columnName)
    
    sql="SELECT ct.maLoi as maLoi,lp.noiDungLoi as noiDungLoi,ct.ghiChu as ghiChu,ct.tienPhat as tienPhat FROM ChiTietLoiPhat as ct, LoiPhat as lp WHERE ct.maLoaiLoi = lp.maLoaiLoi"
    cursor.execute(sql)
    data_loi = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_loi=rsData(data_loi,columnName)
    
    new_data_chitiet=mergeData(data_chitiet,data_loi,"maLoi","loi")
    
    
    new_data=mergeData(data_don,new_data_chitiet,"maThue","chiTiet")
    
    rs = printRs(SUCCESS,None,new_data,True)
    rs['soTrang'] = soTrang
    conn.close()
    return rs

def getOrderDone(page,q=None,maTaiKhoan=None):
    so_item=10
    vt=(page-1)*so_item

    # kt=(page-1)*10+10
    conn = connect()
    cursor = conn.cursor 
    rs={}
    strSearch=""
    if q is not None:     
        strSearch+=f" and hoTen LIKE N'%{q}%'"
    sql=f"SELECT DangKyThueXe.*, hoTen from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan and DangKyThueXe.trangThai = N'Hoàn tất'"+strSearch +f" order by ngayBD desc OFFSET {vt} ROWS FETCH NEXT {so_item} ROWS ONLY;"
    cursor.execute(sql)
    data_don = cursor.fetchall()
    
    columnName=[column[0] for column in cursor.description]
    data_don=rsData(data_don,columnName)
    sql=f"SELECT count(*) from DangKyThueXe, TaiKhoan where DangKyThueXe.maKH = TaiKhoan.maTaiKhoan and DangKyThueXe.trangThai = N'Hoàn tất'"+strSearch +f""
    cursor.execute(sql)
    row = cursor.fetchone()
    soLuong = row[0]
    soTrang=getSoTrang(soLuong,so_item)

    

    sql="SELECT ChiTietThueXe.*,tenXe,loaiXe,hangXe,bienSoXe from ChiTietThueXe,Xe where ChiTietThueXe.maXe=Xe.maXe"
    cursor.execute(sql)
    data_chitiet = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_chitiet=rsData(data_chitiet,columnName)
    
    sql="SELECT ct.maLoi as maLoi,lp.noiDungLoi as noiDungLoi,ct.ghiChu as ghiChu,ct.tienPhat as tienPhat FROM ChiTietLoiPhat as ct, LoiPhat as lp WHERE ct.maLoaiLoi = lp.maLoaiLoi"
    cursor.execute(sql)
    data_loi = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_loi=rsData(data_loi,columnName)
    
    new_data_chitiet=mergeData(data_chitiet,data_loi,"maLoi","loi")
    
    
    new_data=mergeData(data_don,new_data_chitiet,"maThue","chiTiet")
    
    rs = printRs(SUCCESS,None,new_data,True)
    rs['soTrang'] = soTrang
    conn.close()
    return rs

def getOrder(id_order):
    
    # kt=(page-1)*10+10
    conn = connect()
    cursor = conn.cursor 
    rs={}
    
    sql=f"SELECT * from DangKyThueXe where maThue='{id_order}'"
    
    
    cursor.execute(sql)
    data_don = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_don=rsData(data_don,columnName)

    
    
    sql=f"SELECT ChiTietThueXe.*,tenXe,loaiXe,hangXe,bienSoXe from ChiTietThueXe,Xe where ChiTietThueXe.maXe=Xe.maXe and ChiTietThueXe.maThue='{data_don[0]['maThue']}'"
    cursor.execute(sql)
    data_chitiet = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_chitiet=rsData(data_chitiet,columnName)

    sql=f"SELECT ct.maLoi as maLoi,lp.noiDungLoi as noiDungLoi,ct.ghiChu as ghiChu,ct.tienPhat as tienPhat FROM ChiTietLoiPhat as ct, LoiPhat as lp WHERE ct.maLoaiLoi = lp.maLoaiLoi and ct.maLoi='{data_chitiet[0]['maLoi']}'"
    cursor.execute(sql)
    data_loi = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_loi=rsData(data_loi,columnName)
    
    new_data_chitiet=mergeData(data_chitiet,data_loi,"maLoi","loi")
    new_data=mergeData(data_don,new_data_chitiet,"maThue","chiTiet")

    
    
    rs = printRs(SUCCESS,None,new_data)
   
    conn.close()
    return rs

def nvSetOrder(rq):
    paramsAcceep=['maNVDuyet','maThue','trangThai']
    
    rs={}
    if not checkInvalid(rq,paramsAcceep):
        rs = printRs(ERROR,DATA_INVALID,None)
    elif not checkNull(rq,paramsAcceep):
        rs = printRs(ERROR,DATA_INVALID,None)
    else:
        conn = connect()
        cursor = conn.cursor 
        # try:
        sql=f"SELECT * from TaiKhoan WHERE maTaiKhoan='{rq['maNVDuyet']}'" 
        cursor.execute(sql)
        row = cursor.fetchone
        if not row:
            rs = printRs(ERROR,"Mã nhân viên không tồn tại",None)
        else:
            sql=f"SELECT * from DangKyThueXe WHERE maThue='{rq['maThue']}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            
            
            stringGhiChu= row.ghiChu if row.ghiChu is not None else " "
 
            stringGhiChu+= rq['maNVDuyet'] + "  " + rq['trangThai'] + f"  ngày :{str(getDateNow())}; "
     
            if not row:
                rs = printRs(ERROR,"Mã thuê không tồn tại",None)
            else:
                new_value=[rq['trangThai'],stringGhiChu,str(getDateNow())]
                stringSQL=""
                if rq['trangThai']=='Đã duyệt':
                    stringSQL=f",maNVDuyet=?"
                    new_value.append(rq['maNVDuyet'])
                new_value.append(rq['maThue'])
                sql="UPDATE DangKyThueXe SET trangThai=?,ghiChu=?,ngayDuyet=?"+stringSQL+" WHERE maThue=?"
                cursor.execute('SET DATEFORMAT dmy')
                cursor.execute(sql,new_value)
                cursor.commit()
                rs= printRs(SUCCESS,"Set trạng thái thành công",None)
        # except:
        #     rs = printRs(ERROR,"Lỗi không xác định",None)
        conn.close()
    return rs

def addOrder(rq):
    rs={}    
    paramsAcess=['maKH','ngayBD','ngayKT','listMoto']
    if not checkInvalid(rq,paramsAcess):
        print(DATA_INVALID)
        rs=printRs(ERROR,DATA_INVALID,None)
    if not checkNull(rq,rq):
        print(DATA_NULL)
        rs = printRs(ERROR,DATA_NULL,None)
    else:
        conn = connect()
        cursor = conn.cursor
        sql=f"EXEC pr_getFreeMoto @ngayBD=?,@ngayKT=?"
        cursor.execute('SET DATEFORMAT dmy')
        cursor.execute(sql,[rq['ngayBD'],rq['ngayKT']])
        rows = cursor.fetchall()
        # for car in rq['listMoto']:
        #     if car
        new_rows = [row[0] for row in rows]
        
        xe_not_correct=set(rq['listMoto']) - set(new_rows)
        if len(xe_not_correct)!=0:
            rs= printRs(ERROR,"Xe đã được đặt thuê",list(xe_not_correct))
        else:
            
            sql="{CALL pr_add_dangKyThueXe(?, ?, ?, ?)}"
            cursor.execute("SET DATEFORMAT dmy")
            cursor.execute(sql, (rq['maKH'],rq['ngayBD'],rq['ngayKT'],'-'.join(rq['listMoto'])))
            cursor.commit()
            rs = printRs(SUCCESS,"Thêm đơn hàng thành công",None)
        conn.close()
    return rs

def payOrder(rq):
    rs={}    
    paramsAcess=['maThue','xe','maNVNhanXe']
    if not checkInvalid(rq,paramsAcess):
        rs = printRs(ERROR,DATA_INVALID,None)
    elif not checkNull(rq,rq):
        rs = printRs(ERROR,DATA_NULL,None)
    else:
        conn = connect()
        cursor = conn.cursor
        if conn.dataNotExist('DangKyThueXe','maThue',rq['maThue']):
            rs= printRs(ERROR,"Mã thuê không tồn tại",None)
        elif conn.dataNotExist('TaiKhoan','maTaiKhoan',rq['maNVNhanXe']):
            rs= printRs(ERROR,"Mã nhân viên không tồn tại",None)
        else:
            
            for xe in rq['xe']:
                #Update Chi tiet thue xe
                cursor.execute("SET DATEFORMAT dmy")
                sql=f"UPDATE ChiTietThueXe SET ngayTra=?,maNVNhanXe=? WHERE maThue=? and maXe=?"
                new_value=[getDateNow(),rq['maNVNhanXe'],rq['maThue'],xe['maXe']]
                cursor.execute(sql,new_value)

                #Update lỗi xe
                sql=f"INSERT INTO ChiTietLoiPhat (maLoi, maLoaiLoi,ghiChu,tienPhat) VALUES (?,?,?,?)"
                new_value_loi=[]
                for loi in xe['loi']:
                    txtGhiChu=''
                    if 'ghiChu' in loi:
                        txtGhiChu=loi['ghiChu']
                    new_value_loi_item=(xe['maLoi'],loi['maLoaiLoi'],txtGhiChu,loi['tienPhat'])
                    new_value_loi.append(new_value_loi_item)
                if(len(new_value_loi)!=0):
                    cursor.executemany(sql,new_value_loi)
            rs = printRs(SUCCESS,"Thanh toán hoàn tất",None)
            cursor.commit()
        conn.close()
    return rs


def getOrderByIdUser(id_user,trang_thai=None):
    
    # kt=(page-1)*10+10
    conn = connect()
    cursor = conn.cursor 
    rs={}
    strSearch=""
    if trang_thai is not None:
        strSearch+=f" and trangThai=N'{trang_thai}' "
    
    sql=f"SELECT * from DangKyThueXe where maKH='{id_user}' "+strSearch +f" order by ngayBD desc "
    print(sql)
    cursor.execute(sql)
    data_don = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_don=rsData(data_don,columnName)
    

    sql="SELECT ChiTietThueXe.*,tenXe,loaiXe,hangXe,bienSoXe from ChiTietThueXe,Xe where ChiTietThueXe.maXe=Xe.maXe"
    cursor.execute(sql)
    data_chitiet = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_chitiet=rsData(data_chitiet,columnName)
    
    sql="SELECT ct.maLoi as maLoi,lp.noiDungLoi as noiDungLoi,ct.ghiChu as ghiChu,ct.tienPhat as tienPhat FROM ChiTietLoiPhat as ct, LoiPhat as lp WHERE ct.maLoaiLoi = lp.maLoaiLoi"
    cursor.execute(sql)
    data_loi = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    data_loi=rsData(data_loi,columnName)
    
    sql='SELECT * from HinhAnhXe'
    cursor.execute(sql)
    dataHinhAnh=cursor.fetchall()
    for xe in data_chitiet:
        xe['hinhAnh']=[]
        hinh_anh_list = []
        for hinhAnh in dataHinhAnh:
            if xe['maXe']==hinhAnh.maXe:
                hinh_anh_list.append(getURLImg('hinhAnh',hinhAnh.hinhAnh))
        xe['hinhAnh']=hinh_anh_list
    

    new_data_chitiet=mergeData(data_chitiet,data_loi,"maLoi","loi")
    
    
    new_data=mergeData(data_don,new_data_chitiet,"maThue","chiTiet")
    
    rs = printRs(SUCCESS,None,new_data,True)
    
    conn.close()
    return rs


def thongKeRent():
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


def thongKeReturn():
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
    sql_tong_so_thue_xe_da_tra = "SELECT COUNT(maThue) FROM DangKyThueXe WHERE trangThai = N'Hoàn tất'"
    cursor.execute(sql_tong_so_thue_xe_da_tra)
    tong_so_thue_xe_da_tra = cursor.fetchone()[0]

    # Tổng tiền đăng ký thuê xe
    sql_tong_tien_da_nhan = 'SELECT SUM(giaThue) FROM ChiTietThueXe where ngayTra is not null'
    cursor.execute(sql_tong_tien_da_nhan)
    tong_tien_da_nhan = cursor.fetchone()[0]

    # Đóng kết nối cơ sở dữ liệu
    conn.close()

    # Chuyển đổi giá trị Decimal thành float
    if tong_tien_da_nhan != None: 
        tong_tien_da_nhan = float(tong_tien_da_nhan)
    else:
        tong_tien_da_nhan = 0

    # Tạo dictionary để lưu trữ kết quả
    thong_ke = {
        'TongSoDangKyThueXe': tong_so_dang_ky,
        'TongSoDangKyThueXeDaDuyet': tong_so_dang_ky_da_duyet,
        'TongSoDangKyThueXeHoanTat': tong_so_thue_xe_da_tra,
        'TongTienHoanTat': tong_tien_da_nhan
    }
    # Trả về kết quả dưới dạng JSON
    return json.dumps(thong_ke)