from api.Connect import connect
from api.xuli import *
import pyodbc
from pathlib import Path
import json


ERROR='error'
SUCCESS='success'
DATA_INVALID='Data invalid'
DATA_NULL='Data null'

def getAllXe(q,role,page=None,type=None):
    #role=true khách hàng, role=False NV
    if page is not None:
        so_item=10
        vt=(page-1)*so_item

    conn = connect()
    cursor = conn.cursor
    rs = {}
    strSearch=''
    sqlRole=''
    sqlPage=''
    check=False
    if role:
        if q != '' and q is not None:
            sqlRole=" trangThai in (N'Hoạt động',N'Đang cho thuê') and "
        else:
            sqlRole=" trangThai in (N'Hoạt động',N'Đang cho thuê')"
        check=True
    else:
        sqlPage=f" ORDER BY maXe OFFSET {vt} ROWS FETCH NEXT {so_item} ROWS ONLY;"

    if q != '' and q is not None:
        strSearch=f"tenXe LIKE N'%{q}%'"
        check=True
    
    if type != '' and type is not None:
        if q!= '' and q is not None:
            where = f" WHERE loaiXe = N'{type}' and "
        else:
            where = f" WHERE loaiXe = N'{type}'"
    else:
        where = " WHERE " if check else " "
    
    sql='SELECT * FROM Xe'+where+sqlRole+strSearch+sqlPage
    print(sql)
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    dataXe=rsData(rows,columnName)
    sql='SELECT * from HinhAnhXe'
    cursor.execute(sql)
    dataHinhAnh=cursor.fetchall()
    for xe in dataXe:
        xe['hinhAnh']=[]
        hinh_anh_list = []
        for hinhAnh in dataHinhAnh:
            if xe['maXe']==hinhAnh.maXe:
                hinh_anh_list.append(getURLImg('hinhAnh',hinhAnh.hinhAnh))
        xe['hinhAnh']=hinh_anh_list
    rs = printRs(SUCCESS,None,dataXe, True)
    if not role:
        sql="SELECT count(maXe) as soluong from Xe "+where+sqlRole+strSearch
        cursor.execute(sql)
        row = cursor.fetchone()
        soLuong= row[0]
        rs['soTrang']=getSoTrang(soLuong,so_item)
    conn.close()
    return rs


def getXe(maXe):
    conn = connect()
    cursor = conn.cursor
    rs = {}
    
    cursor.execute(f"EXEC pr_get_calendar_xe @slug='{maXe}'")
    lichs =  cursor.fetchall()
    data_lich=[]
    for lich in lichs:
        data_lich.append({'ngayBD':formatDate(lich.ngayBD),'ngayKT':formatDate(lich.ngayKT)})
    sql=f"SELECT * FROM Xe where slug='{maXe}'"
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    columnName=[column[0] for column in cursor.description]
    dataXe=rsData(rows,columnName)
    sql='SELECT * from HinhAnhXe'
    cursor.execute(sql)
    dataHinhAnh=cursor.fetchall()
    for xe in dataXe:
        xe['hinhAnh']=[]
        hinh_anh_list = []
        for hinhAnh in dataHinhAnh:
            if xe['maXe']==hinhAnh.maXe:
                hinh_anh_list.append(getURLImg('hinhAnh',hinhAnh.hinhAnh))
        xe['hinhAnh']=hinh_anh_list
    dataXe[0]['lich']=data_lich
    rs = printRs(SUCCESS,None,dataXe)
    conn.close()
    return rs

async def addXe(rq,relative_path,files):
    rs={}
    paramsAccept=['tenXe','hangXe','bienSoXe','loaiXe','giaThue','trangThai','moTa', 'slug','images']
    listParams=list(rq.keys())

    
    if not checkInvalid(listParams,paramsAccept):
        rs= printRs(ERROR,DATA_INVALID,None)
    elif not checkNull(rq,paramsAccept[:-2]):
        rs= printRs(ERROR,DATA_NULL,None)
    else:
        conn = connect()
        cursor = conn.cursor
        connection= conn.connection
        try:          
            sql=f"SELECT * from Xe where bienSoXe='{rq['bienSoXe']}'"
            cursor.execute(sql)
            row = cursor.fetchone()           
            if row:
                rs= printRs(ERROR,"Biển số xe đã tồn tại",None)
            else:    
                strListHinhAnh=''
                i=0
                if files is not None:
                    for x in files:
                        duoiFile=Path(x.filename).suffix
                        tenFile=createNameImgXe(rq['tenXe'],rq['bienSoXe'])+"-"+str(i)+duoiFile
                        save_path = f"{relative_path}\{tenFile}"
                        with open(save_path, "wb") as file:
                            file.write(await x.read())
                        strListHinhAnh+=tenFile+";"
                        i+=1
                strListHinhAnh=strListHinhAnh.rstrip(";")
                cursor.execute("SET DATEFORMAT dmy")
                params=[rq['tenXe'],rq['hangXe'],rq['trangThai'],rq['bienSoXe'],rq['loaiXe'],rq['giaThue'],rq['moTa'], rq['slug']]
                sql="EXEC pr_add_Xe @tenXe=?,@hangXe=?,@trangThai=?,@bienSoXe=?,@loaiXe=?,@giaThue=?,@moTa=?, @slug=?"
                if strListHinhAnh!='':
                    sql+=",@listHinhAnh=?"
                    params.append(strListHinhAnh)
                    print(strListHinhAnh)
            
                
                cursor.execute(sql,params)
                cursor.commit()
                rs=printRs(SUCCESS,"Thêm xe thành công",None)
        except pyodbc.Error as ex:
            print(ex)
            rs=printRs(ERROR,"Lỗi SQL",None)
        except:
            print("loi")
            rs=print(ERROR,"Lỗi không xác định",None)        
        conn.close()
    return rs

async def updateXe(rq,relative_path,files):
    rs={}
    paramsAccept=['maXe','tenXe','hangXe','bienSoXe','loaiXe','giaThue','trangThai','moTa', 'slug','images']
    listParams=list(rq.keys())
    print(listParams)
    if not checkInvalid(listParams,paramsAccept):
        rs= printRs(ERROR,DATA_INVALID,None)
    elif not checkNull(rq,paramsAccept[:-1]):
        rs= printRs(ERROR,DATA_NULL,None)
    else:
        conn = connect()
        cursor = conn.cursor
        connection= conn.connection
        try:
            sql=f"SELECT * from Xe where maXe='{rq['maXe']}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            if not row:
                rs = printRs(ERROR,"Mã xe không tồn tại",None)
            else:
                if files is not None:
                    sql = f"SELECT hinhAnh from HinhAnhXe where maXe='{rq['maXe']}'"
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for x in rows:
                        
                        deleteImg(relative_path,x.hinhAnh)
                    i=0
                    listHinhAnh=[]
                    for x in files:
                        duoiFile=Path(x.filename).suffix
                        tenFile=createNameImgXe(rq['tenXe'],rq['bienSoXe'])+"-"+str(i)+duoiFile
                        save_path = f"{relative_path}\{tenFile}"
                        with open(save_path, "wb") as file:
                            file.write(await x.read())
                        listHinhAnh.append((rq['maXe'],tenFile))
                        i+=1
                    
                    sql=f"delete from HinhAnhXe where maXe='{rq['maXe']}'"
                    cursor.execute(sql)
        
                    sql=f"INSERT INTO HinhAnhXe (maXe, hinhAnh) VALUES (?,?)"
                    cursor.executemany(sql,listHinhAnh)
                
                setString = getStringSQL(paramsAccept[1:-1],"")
                sql=f"UPDATE Xe set {setString} WHERE maXe='{rq['maXe']}'"
                
                params=[rq[value] for value in paramsAccept[1:-1]]
                cursor.execute(sql,params)
                cursor.commit()
                rs=printRs(SUCCESS,"Cập nhật xe thành công",None)
        except pyodbc.Error as ex:
            print(ex)
            rs=printRs(ERROR,"Lỗi SQL",None)
        except:
            rs=printRs(ERROR,"Lỗi không xác định",None)
            
        conn.close()
    return rs


def thongKeXe():
    conn = connect()
    cursor = conn.cursor

    # Tổng số user
    sql_tong_so_xe = 'SELECT COUNT(maXe) FROM Xe'
    cursor.execute(sql_tong_so_xe)
    tong_so_xe = cursor.fetchone()[0]

    # Tổng số user role = nhan vien
    sql_tong_so_xe_dang_hoat_dong = "SELECT COUNT(maXe) FROM Xe WHERE trangThai = N'Hoạt động'"
    cursor.execute(sql_tong_so_xe_dang_hoat_dong)
    tong_so_xe_dang_hoat_dong = cursor.fetchone()[0]

    # Tổng số user role = khách hàng
    sql_tong_so_ngung_hoat_dong = "SELECT COUNT(maXe) FROM Xe WHERE trangThai in (N'Ngưng hoạt động', N'Đã mất')"
    cursor.execute(sql_tong_so_ngung_hoat_dong)
    tong_so_xe_ngung_hoat_dong = cursor.fetchone()[0]

    # Đóng kết nối cơ sở dữ liệu
    conn.close()

    # Tạo dictionary để lưu trữ kết quả
    thong_ke = {
        'SumMoto': tong_so_xe,
        'SumMotoActive': tong_so_xe_dang_hoat_dong,
        'SumMotoUnActive': tong_so_xe_ngung_hoat_dong,
    }
    # Trả về kết quả dưới dạng JSON
    return json.dumps(thong_ke)

