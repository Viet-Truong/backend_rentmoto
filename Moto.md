<h1 align="center"> API RENT MOTORBIKE ECOMMERCE </h1>

### GET_ALL_MOTORBIKE (CUSTOMER)

url: `/getAllMotorbike`
params: `q` (optional) -> Tên xe
method: `GET`
example:

```bash
    {
  "status": "success",
  "data": [
    {
      "maXe": "XE00000001",
      "tenXe": "Honda VARIO 160",
      "hangXe": "Honda",
      "trangThai": "Hoạt động",
      "bienSoXe": "92F1-128.46",
      "loaiXe": "Xe ga",
      "giaThue": 180,
      "moTa": "Honda VARIO 160",
      "slug": "Honda-VARIO-160",
      "hinhAnh": [
        "getUrlImg/imgXe/vario1.png",
        "getUrlImg/imgXe/vario2.png"
      ]
    },
    {
      "maXe": "XE00000002",
      "tenXe": "Honda Lead",
      "hangXe": "Honda",
      "trangThai": "Hoạt động",
      "bienSoXe": "92F1-835.12",
      "loaiXe": "Xe ga",
      "giaThue": 175,
      "moTa": "Honda Lead",
      "slug": "Honda-Lead",
      "hinhAnh": [
        "getUrlImg/imgXe/lead1.png",
        "getUrlImg/imgXe/lead2.png"
      ]
    }
  ]
}
```

### GET_ALL_MOTORBIKE (ADMIN)

url: `/admin/getAllMotorbike` || `/getAllMotorbikeAdmin`
params: `q` (optional) -> Tên xe
`page` (optional) -> Trang
`type` (optional) -> Loại xe
method: `GET`
example:

```bash
{
  "status": "success",
  "data": [
    {
      "maXe": "XE00000001",
      "tenXe": "Honda VARIO 160",
      "hangXe": "Honda",
      "trangThai": "Hoạt động",
      "bienSoXe": "92F1-128.46",
      "loaiXe": "Xe ga",
      "giaThue": 180,
      "moTa": "Honda VARIO 160",
      "slug": "Honda-VARIO-160",
      "hinhAnh": [
        "getUrlImg/imgXe/vario1.png",
        "getUrlImg/imgXe/vario2.png"
      ]
    },
    {
      "maXe": "XE00000002",
      "tenXe": "Honda Lead",
      "hangXe": "Honda",
      "trangThai": "Hoạt động",
      "bienSoXe": "92F1-835.12",
      "loaiXe": "Xe ga",
      "giaThue": 175,
      "moTa": "Honda Lead",
      "slug": "Honda-Lead",
      "hinhAnh": [
        "getUrlImg/imgXe/lead1.png",
        "getUrlImg/imgXe/lead2.png"
      ]
    }
  ],
  "soTrang": 1
}
```

### GET_MOTORBIKE

url: `/getMotorbike/{slug}`
method: `GET`
example: `http://localhost:5000/getXe/Honda-VARIO-160`

```bash
{
  "status": "success",
  "data": {
    "maXe": "XE00000001",
    "tenXe": "Honda VARIO 160",
    "hangXe": "Honda",
    "trangThai": "Hoạt động",
    "bienSoXe": "92F1-128.46",
    "loaiXe": "Xe ga",
    "giaThue": 180,
    "moTa": "Honda VARIO 160",
    "slug": "Honda-VARIO-160",
    "hinhAnh": [
      "getUrlImg/imgXe/vario1.png",
      "getUrlImg/imgXe/vario2.png"
    ],
    "lich": []
  }
}
```

### ADD_MOTORBIKE (ADMIN)

url: `/admin/addMotorbike` || `/addMotorbike`
method: `POST`
params: 'tenXe','hangXe','bienSoXe','loaiXe','giaThue','trangThai','moTa', 'slug','images'
images: type is Array

-   ERROR

```bash
{
    mess: "Lỗi SQL"
    status: "error"
}
```

-   SUCCESS

```bash
{
    mess: "Thêm xe thành công"
    status: "success"
}
```

### UPDATE_MOTORBIKE (ADMIN)

url: `/admin/updateMotorbike` || `/updateMotorbike`
method: `POST` || `PUT`
params: 'tenXe','hangXe','bienSoXe','loaiXe','giaThue','trangThai','moTa', 'slug','images'
images: type is Array

-   ERROR

```bash
{
    mess: "Lỗi"
    status: "error"
}
```

-   SUCCESS

```bash
{
    mess: "Cập nhật xe thành công"
    status: "success"
}
```

### GET_ALL_ORDER (ADMIN)

url: `/admin/getAllOrder` || `getAllOrder`
method: `GET`
params: `q` (optional) -> Tên khách hàng
`page` (optional) -> Trang
`status` (optional) -> Trạng thái của đơn hàng (Đã duyệt, chưa duyệt, hoàn tất)

```bash
{
  "status": "success",
  "data": [
    {
      "maThue": "DH00000002",
      "maKH": "NV00000001",
      "trangThai": "Đã duyệt",
      "maNVDuyet": "NV00000001",
      "ngayBD": "18-11-2023",
      "ngayKT": "20-11-2023",
      "ngayDuyet": "18-11-2023",
      "ghiChu": " NV00000001  Đã duyệt  ngày :18-11-2023; NV00000001  Đã duyệt  ngày :18-11-2023; ",
      "hoTen": "Nguyễn Văn A",
      "chiTiet": [
        {
          "maXe": "XE00000001",
          "giaThue": 180,
          "ngayTra": null,
          "maNVNhanXe": null,
          "maLoi": 3,
          "tenXe": "Honda VARIO 160",
          "loaiXe": "Xe ga",
          "hangXe": "Honda",
          "bienSoXe": "92F1-128.46",
          "loi": []
        }
      ]
    },
    {
      "maThue": "DH00000001",
      "maKH": "AD00000001",
      "trangThai": "Hoàn tất",
      "maNVDuyet": "NV00000001",
      "ngayBD": "07-11-2023",
      "ngayKT": "09-11-2023",
      "ngayDuyet": "07-11-2023",
      "ghiChu": " NV00000001  Đã duyệt  ngày :07-11-2023; ",
      "hoTen": "Viết Trường",
      "chiTiet": [
        {
          "maXe": "XE00000003",
          "giaThue": 150,
          "ngayTra": "18-11-2023",
          "maNVNhanXe": "NV00000001",
          "maLoi": 1,
          "tenXe": "Honda Wave RSX FI 110",
          "loaiXe": "Xe số",
          "hangXe": "Honda",
          "bienSoXe": "43F1-158.41",
          "loi": []
        },
        {
          "maXe": "XE00000005",
          "giaThue": 175,
          "ngayTra": "18-11-2023",
          "maNVNhanXe": "NV00000001",
          "maLoi": 2,
          "tenXe": "Honda Sh Mode 125cc",
          "loaiXe": "Xe ga",
          "hangXe": "Honda",
          "bienSoXe": "43F1-688.12",
          "loi": []
        }
      ]
    }
  ],
  "soTrang": 1
}
```

### GET_ORDER_BYID (ADMIN)

url: `/admin/getOrder/{id_order}`
method: `GET`

```bash
{
  "status": "success",
  "data": [
    {
      "maThue": "DH00000002",
      "maKH": "NV00000001",
      "trangThai": "Đã duyệt",
      "maNVDuyet": "NV00000001",
      "ngayBD": "18-11-2023",
      "ngayKT": "20-11-2023",
      "ngayDuyet": "18-11-2023",
      "ghiChu": " NV00000001  Đã duyệt  ngày :18-11-2023; NV00000001  Đã duyệt  ngày :18-11-2023; ",
      "hoTen": "Nguyễn Văn A",
      "chiTiet": [
        {
          "maXe": "XE00000001",
          "giaThue": 180,
          "ngayTra": null,
          "maNVNhanXe": null,
          "maLoi": 3,
          "tenXe": "Honda VARIO 160",
          "loaiXe": "Xe ga",
          "hangXe": "Honda",
          "bienSoXe": "92F1-128.46",
          "loi": []
        }
      ]
    },
  ]
}
```

### CONFIRM_ORDER

url: `/admin/confirmOrder`
method: `POST`
params: 'id_employee', 'id_order', 'status'

-   ERROR

```bash
{
  status: ''
  message: ''
}

- SUCCESS
{
  status: 'success'
  message: 'Success'
}
```

### ADD_ORDER

url: `/admin/addOrder`
method: `POST`
params: 'id_customer', 'startDate', 'endDate', 'ListMoto'
listMoto: type Array

-   ERROR

```bash
{
  status: ''
  message: ''
}

- SUCCESS
{
  status: 'success'
  message: 'Success'
}
```

### PAY_ORDER

url: `/admin/payOrder`
method: `POST`
params: 'id_order', 'id_employee', 'motorbike'
motorbike: ['id_order']
