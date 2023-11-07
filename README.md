<h1 align="center"> API RENT MOTORBIKE ECOMMERCE </h1>

## How to run the project

### Step 1: Clone project

In the project directory, you can run:

### Step 2: Install env

```bash
python -m venv env
```

### Step 3: Restart vscode and check in the terminal (env) activated

-   If (env) is not activated:

`Create file test1.py and write print('hello') and run to activate env`

-   If (env) is not activated:

1.
```bash
cd env
```
2.
```bash
cd Scripts
```
3.
```bash
activate.bat
```

### Step 4: Install lib

```bash
pip install -r requirements.txt
```

### Step 5: Run file index

```bash
python index.py
```

### API:

-   GetURLImg

-   Account user:

1. Login
2. Register
3. ChangePass
4. UpdateUser
5. GetAllUser

-   Motorbike:

1. GetAllMotorbike
2. GetMotorbike/{idMotor}
3. AddMotorbike
4. Update

-   Order:

1. AddOrder
2. PayOrder
3. AcceptOrder
4. DoneOrder
5. GetAllOrder
6. GetOrderByIdUser/{idUser}
7. GetOrder/{idOrder}

-   Admin:

1. StatisticsUser
2. StatisticsMotorbike
3. StatisticsOrder
4. StatisticsOrderDone
