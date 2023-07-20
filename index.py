from fastapi import FastAPI, Request,Body,Form, UploadFile, File
from fastapi.responses import FileResponse
from typing import List
from api import get,user,xe,order
import json
import pyodbc
import uvicorn
import os



from fastapi.middleware.cors import CORSMiddleware
# uvicorn index:app --reload


app = FastAPI()
#Lấy đường dẫn hiện tại
current_file_path = os.path.abspath(__file__)

#lấy đường dẫn Project
current_directory = os.path.dirname(current_file_path)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def main():
    return json.dumps({"message": 'hello'})

@app.post("/login")
def login(rq = Body()):
    return user.checkLogin(rq)


@app.get("/thongkeRent")
def thong_ke_dang_ky_thue_xe():
    return order.thongKeRent()

@app.get("/thongkeReturn")
def thong_ke_dang_ky_thue_xe():
    return order.thongKeReturn()

@app.get("/thongkeUser")
def thong_ke_dang_ky_thue_xe():
    return user.thongKeUser()


@app.get("/getAllUser")
def getAllUser(page:int=None,role:str=None,q:str=None):
    if page is None:
        page=1
    return user.getAllUser(page,role,q)

@app.get("/getAllCustomer")
def getAllUser(page:int=None,q:str=None):
    if page is None:
        page=1
    return user.getAllCustomer(page,q)

@app.get("/getAllEmployees")
def getAllUser(page:int=None,q:str=None):
    if page is None:
        page=1
    return user.getAllEmployees(page,q)


@app.post('/addAccount')
def addAccount(rq=Body()):
    return user.addAccount(rq)

@app.post('/changePass')
def changePass(rq=Body()):
    return user.changePass(rq)

@app.post('/updateInfoUser')
async def updateInfo(request: Request):
    form_data = await request.form()
    relative_path = os.path.join(current_directory, 'img\imgAvatar')
    return await user.updateInfoUser(form_data,relative_path)


@app.get("/getAllXe")
def getall(q:str=None):
    return xe.getAllXe(q,True)

@app.get("/getAllXeAdmin")
def getall(q:str=None,page:int=None,type:str=None):
    if page is None:
        page=1
    return xe.getAllXe(q,False,page,type)

@app.get("/thongkeXe")
def thong_ke_xe():
    return xe.thongKeXe()


@app.get("/getXe/{maXe}")
def getall(maXe:str):
    return xe.getXe(maXe)

@app.get("/getOrderByIdUser/{id_user}")
def getOrder(id_user,trangThai:str=None):
    return order.getOrderByIdUser(id_user,trangThai)


@app.post("/addXe")
async def addXe(request: Request,images: List[UploadFile] =  Form(None)):
    form_data = await request.form()
    
    relative_path = os.path.join(current_directory, 'img\imgXe')
    return await xe.addXe(form_data,relative_path,images)

@app.post("/updateXe")
async def updateXe(request: Request,images: List[UploadFile] =  Form(None)):
    form_data = await request.form()

    relative_path = os.path.join(current_directory, 'img\imgXe')
    return await xe.updateXe(form_data,relative_path,images)

    
@app.get("/getAllOrder")
def getDonHang(q:str=None,page:int=None):
    if page is None:
        page=1
    return order.getAllOrder(page,q)

@app.get("/getOrderAccepted")
def getDonHang(q:str=None,page:int=None):
    if page is None:
        page=1
    return order.getOrderAccepted(page,q)

@app.get("/getOrderUnAccepted")
def getDonHang(q:str=None,page:int=None):
    if page is None:
        page=1
    return order.getOrderUnAccepted(page,q)

@app.get("/getOrderDone")
def getDonHang(q:str=None,page:int=None):
    if page is None:
        page=1
    return order.getOrderDone(page,q)

@app.get("/getOrder/{id_order}")
def getOrder(id_order):
    return order.getOrder(id_order)

@app.post("/nvSetOrder")
def nvSetOrder(rq=Body()):
    return order.nvSetOrder(rq)

@app.post("/addOrder")
def addOrder(rq=Body()):   
    return order.addOrder(rq)

@app.post("/payOrder")
def payOrder(rq=Body()):   
    return order.payOrder(rq)


@app.get("/getAllLoi")
def getAllLoi():
    return get.getALlLoi()

@app.get("/getUrlImg/{folder}/{filename}")
async def getUrlImg(folder:str,filename:str):
    url = os.path.join(current_directory, 'img',folder,filename)
    return FileResponse(url)
if __name__ == "__main__":    
    uvicorn.run(app, host="localhost", port=5000)










