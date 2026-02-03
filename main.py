from fastapi import FastAPI, Query
from typing import Optional
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from datetime import datetime, date, time
from datetime import time, timedelta
from fastapi import FastAPI, UploadFile, File, Form
import base64, os, re
from pydantic import BaseModel
import psutil
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi import FastAPI, Form, UploadFile, File, HTTPException, status

app = FastAPI()

# mount static foldervv
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("admen.html", {"request": request})

#----------------------------------------------

 
@app.get("/try", response_class=HTMLResponse)
def login_page0(request: Request):
    return templates.TemplateResponse("try.html", {"request": request})

@app.get("/components", response_class=HTMLResponse)
def login_page1(request: Request):
    return templates.TemplateResponse("components.html", {"request": request})

@app.get("/details", response_class=HTMLResponse)
def login_page2(request: Request):
    return templates.TemplateResponse("details.html", {"request": request})

@app.get("/fils", response_class=HTMLResponse)
def login_page3(request: Request):
    return templates.TemplateResponse("fils.html", {"request": request})

@app.get("/navbar", response_class=HTMLResponse)
def login_page4(request: Request):
    return templates.TemplateResponse("navbar.html", {"request": request})

@app.get("/new_chick_point", response_class=HTMLResponse)
def login_page5(request: Request):
    return templates.TemplateResponse("new_chick_point.html", {"request": request})

@app.get("/Payroll", response_class=HTMLResponse)
def login_page6(request: Request):
    return templates.TemplateResponse("Payroll.html", {"request": request})

@app.get("/project_list", response_class=HTMLResponse)
def login_page7(request: Request):
    return templates.TemplateResponse("project_list.html", {"request": request})

@app.get("/project_salary_history", response_class=HTMLResponse)
def login_page8(request: Request):
    return templates.TemplateResponse("project_salary_history.html", {"request": request})

@app.get("/show", response_class=HTMLResponse)
def login_page9(request: Request):
    return templates.TemplateResponse("show.html", {"request": request})

@app.get("/show_admin", response_class=HTMLResponse)
def login_page10(request: Request):
    return templates.TemplateResponse("show_admin.html", {"request": request})

@app.get("/show_guards", response_class=HTMLResponse)
def login_page11(request: Request):
    return templates.TemplateResponse("show_guards.html", {"request": request})

@app.get("/show_info_chick_point", response_class=HTMLResponse)
def login_page12(request: Request):
    return templates.TemplateResponse("show_info_chick_point.html", {"request": request})
    
@app.get("/show_obxod", response_class=HTMLResponse)
def login_page13(request: Request):
    return templates.TemplateResponse("show_obxod.html", {"request": request})
    
@app.get("/show_project", response_class=HTMLResponse)
def login_page14(request: Request):
    return templates.TemplateResponse("show_project.html", {"request": request})
    
@app.get("/show_qr_code_fro_check_point", response_class=HTMLResponse)
def login_page15(request: Request):
    return templates.TemplateResponse("show_qr_code_fro_check_point.html", {"request": request})

    
@app.get("/show_qr_code_point_project", response_class=HTMLResponse)
def login_page16(request: Request):
    return templates.TemplateResponse("show_qr_code_point_project.html", {"request": request})



@app.get("/work_shift", response_class=HTMLResponse)
def login_page17(request: Request):
    return templates.TemplateResponse("work_shift.html", {"request": request})

@app.get("/admen", response_class=HTMLResponse)
def login_page18(request: Request):
    return templates.TemplateResponse("admen.html", {"request": request})

@app.get("/add_emp", response_class=HTMLResponse)
def login_page19(request: Request):
    return templates.TemplateResponse("add_emp.html", {"request": request})

@app.get("/add_project", response_class=HTMLResponse)
def login_page20(request: Request):
    return templates.TemplateResponse("add_project.html", {"request": request})

@app.get("/log_in", response_class=HTMLResponse)
def login_page0(request: Request):
    return templates.TemplateResponse("log_in.html", {"request": request})


app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
#----------------------------------------------



# للسماح للـ HTML من متصفح مختلف
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



# الاتصال بقاعدة البيانات
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "ratmer")
    )



#====================================================
@app.get("/stats")
def stats():
    p = psutil.Process()

    cpu_percent = p.cpu_percent(interval=0.1)
    memory_usage = p.memory_info().rss / (1024 * 1024)

    return {
        "cpu_percent": cpu_percent,
        "memory_mb": memory_usage
    }

#====================================================
@app.post("/check_password")
def check_password(password: str = Form(...)):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users WHERE password = %s", (password,))
    (count,) = cur.fetchone()

    if count > 0:
        return {"exists": True}   # كلمة المرور موجودة مسبقاً
    else:
        return {"exists": False}  # كلمة المرور فريدة

#====================================================
@app.post("/add_admin")
def add_category(name: str = Form(...), 
                 pasword: str = Form(...),
                 rool: str = Form(...)):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
        INSERT INTO users 
        (username, password, role)
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (name, pasword, rool))
        conn.commit()
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        return {"error": str(e)}
#====================================================
@app.post("/add-emp")
def add_employee(
    id: int = Form(0), 
    name: str = Form(...), 
    num_T: str = Form(...),
    data_prth: str = Form(...),
    address: str = Form(...),
    Salary: str = Form(...), 
    Job: str = Form(...), 
    nots: str = Form(...),
    image: UploadFile = File(None)
):
    try:
        image_path = None

        if image:
            os.makedirs("uploads", exist_ok=True)

            # احصل على التاريخ والوقت الحالي بصيغة: YYYYMMDD_HHMMSS
            now = datetime.now().strftime("%Y-%m-%d-T-%H-%M")

            # أنشئ اسم ملف جديد: مثلا name_YYYYMMDD_HHMMSS.jpg
            extension = os.path.splitext(image.filename)[1]  # .jpg أو .png
            filename = f"{name}-DT{now}{extension}"

            # مسار حفظ الصورة
            image_path = f"uploads/{filename}"

            # حفظ الصورة في المجلد
            with open(image_path, "wb") as f:
                f.write(image.file.read())

        # حفظ البيانات في قاعدة البيانات
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO employee (id, name, num_T, data_prth, address, Salary, Job, nots, image_path)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id, name, num_T, data_prth, address, Salary, Job, nots, image_path))
        conn.commit()
        conn.close()

        return {"message": "تمت الإضافة بنجاح ✅", "image_saved": image_path}

    except mysql.connector.Error as e:
        return {"error": str(e)}
#====================================================
@app.post("/add-category")
def add_category(title: str = Form(...), 
                 address: str = Form(...),
                 Coordinates: str = Form(...),
                 q_person: str = Form(...), 
                 ses_work: str = Form(...), 
                 start_time_work: str = Form(...), 
                 sum_of_proj: str = Form(...), 
                 pers_of_proj: str = Form(...), 
                 n_phone: str = Form(...), 
                 sel_emp: str = Form(...),
                 nots: str = Form(...)):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
        INSERT INTO projuct 
        (title, address, Coordinates, q_person, ses_work, start_time_work, sum_of_proj, pers_of_proj, n_phone, sel_emp, nots)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (title, address, Coordinates, q_person, ses_work, start_time_work, sum_of_proj, pers_of_proj, n_phone, sel_emp, nots))
        conn.commit()
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        return {"error": str(e)}

#====================================================
class UpdateCategory(BaseModel):
    id: int
    title: str
    address: str
    q_person: str
    ses_work: str
    sum_of_proj: str
    pers_of_proj: str
    sel_emp: str
    n_phone: str
    nots: str
    is_active: bool   # ✅ الحقل الجديد


@app.put("/update_category")
def update_category(data: UpdateCategory):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            UPDATE projuct
            SET title=%s, address=%s, q_person=%s, ses_work=%s,
                sum_of_proj=%s, pers_of_proj=%s, sel_emp=%s,
                n_phone=%s, nots=%s, is_active=%s
            WHERE id=%s
        """
        cur.execute(query, (
            data.title, data.address, data.q_person, data.ses_work,
            data.sum_of_proj, data.pers_of_proj, data.sel_emp,
            data.n_phone, data.nots, data.is_active, data.id
        ))
        conn.commit()
        return {"message": "Обновлено успешно ✅"}
    except Exception as e:
        return {"error": str(e)}
#====================================================
class UpdateCategory(BaseModel):
    id: int
    name: str
    num_T: str
    data_prth: str
    address: str
    Salary: str
    Job: str
    nots: str
    image_path: str
    is_active: bool   # ✅ الحقل الجديد


@app.put("/update_guard")
def update_guard(data: UpdateCategory):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            UPDATE employee
            SET name=%s, num_T=%s, data_prth=%s, address=%s,
                Salary=%s, Job=%s, nots=%s,
                image_path=%s, is_active=%s
            WHERE id=%s
        """
        cur.execute(query, (
            data.name, data.num_T, data.data_prth, data.address,
            data.Salary, data.Job, data.nots,
            data.image_path, data.is_active, data.id
        ))
        conn.commit()
        return {"message": "Обновлено успешно ✅"}
    except Exception as e:
        return {"error": str(e)}
#====================================================
# ✅ موديل بيانات الاستقبال
class GuardUpdate(BaseModel):
    id: int
    is_active: int
    # ✅ API لتحديث الحالة
@app.put("/update_project_guards")
def update_project_guards(data: GuardUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "UPDATE project_guards SET is_active = %s WHERE id = %s"
    cursor.execute(sql, (data.is_active, data.id))

    conn.commit()
    cursor.close()
    conn.close()

    return {"success": True, "id": data.id, "new_state": data.is_active}
    

#====================================================
@app.post("/add-project-guards")
def add_project_guards(
    project_id: int = Form(...), 
    project_name: str = Form(...), 
    employee_id: int = Form(...),
    employee_name: str = Form(...),
    start_date: date = Form(...),
    end_date: date = Form(...),
    emp: str = Form(...),  
    nots: str = Form(...)
):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO project_guards 
            (project_id, project_name, employee_id, employee_name, start_date, end_date, emp, nots) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (project_id, project_name, employee_id, employee_name, start_date, end_date, emp, nots))
        conn.commit()
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
#====================================================

@app.get("/get-product-by-name/")
def get_product_by_name(title: str):
    try:
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM projuct WHERE title = %s", (title,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return row
        else:
            return {}
    except mysql.connector.Error as e:
        return {"error": str(e)}
#====================================================

@app.get("/get-guards-by-name/")
def get_guards_by_name(Ename: str):
    try:
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM employee WHERE name = %s", (Ename,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return row
        else:
            return {}
    except mysql.connector.Error as e:
        return {"error": str(e)}
#====================================================

@app.get("/get-categories")
def get_categories():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT title, is_active FROM projuct")
        rows = cur.fetchall()

        # استخراج كل عمود في مصفوفة مستقلة
        titles = [row[0] for row in rows]
        is_active = [row[1] for row in rows]

        # نرجعهم في JSON يحتوي على مصفوفتين
        return {
            "titles": titles,
            "is_active": is_active
        }

    except mysql.connector.Error as e:
        return {"error": str(e)}

 
#====================================================

@app.get("/get_admin")
def get_categories():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # استخراج كل عمود في مصفوفة مستقلة
        idu = [row[0] for row in rows]
        username = [row[1] for row in rows]
        password = [row[2] for row in rows]
        role = [row[3] for row in rows]
        conn.close()  # مهم لإغلاق الاتصال

        # نرجعهم في JSON يحتوي على مصفوفتين
        return {
            "idu": idu,
            "username": username,
            "password": password,
            "role": role
        }

    except mysql.connector.Error as e:
        return {"error": str(e)}

#====================================================
@app.get("/delet_admin")
def delet_admin(idu: int):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = %s", (idu,))
        conn.commit()  # ضروري لتأكيد الحذف

        if cur.rowcount == 0:
            return {"message": "❌Пользователь не найден."}

        return {"message": "✅ Пользователь успешно удалён."}

    except mysql.connector.Error as e:
        return {"error": str(e)}

    finally:
        conn.close()


#===============================================
@app.get("/get_all_guards")
def get_all_guards(
    id: Optional[int] = Query(None),
    project_id: Optional[int] = Query(None),
    employee_id: Optional[int] = Query(None),
    nots: Optional[float] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM project_guards WHERE is_active = TRUE"
    values = []

    if id is not None:
        query += " AND id = %s"
        values.append(id)
    if project_id is not None:
        query += " AND project_id = %s"
        values.append(project_id)
    if employee_id is not None:
        query += " AND employee_id = %s"
        values.append(employee_id)
    
    if nots is not None:
        query += " AND nots = %s"
        values.append(nots)

    cursor.execute(query, values)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results
#===============================================
@app.get("/get_guards")
def get_guards(
    id: Optional[int] = Query(None),
    project_id: Optional[int] = Query(None),
    employee_id: Optional[int] = Query(None),
    nots: Optional[float] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    today = date.today()

    # 1️⃣ جلب الحرس
    query = "SELECT * FROM project_guards WHERE is_active = TRUE"
    values = []

    if project_id is not None:
        query += " AND project_id = %s"
        values.append(project_id)

    cursor.execute(query, values)
    guards = cursor.fetchall()

    result = []

    # 2️⃣ فلترة غير المسجّلين
    for guard in guards:
        cursor.execute(
            """
            SELECT 1 FROM work_shifts
            WHERE employee_id_input = %s
            AND start_day = %s
            LIMIT 1
            """,
            (guard["employee_id"], today)
        )

        if cursor.fetchone() is None:
            # غير مسجّل اليوم ➜ نرجعه
            result.append(guard)

    cursor.close()
    conn.close()
    
    return result
#===============================================
@app.get("/get_guards0")
def get_guards0(
    id: Optional[int] = Query(None),
    project_id: Optional[int] = Query(None),
    employee_id: Optional[int] = Query(None),
    nots: Optional[float] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM project_guards WHERE is_active = TRUE"
    values = []

    if id is not None:
        query += " AND id = %s"
        values.append(id)
    if project_id is not None:
        query += " AND project_id = %s"
        values.append(project_id)
    if employee_id is not None:
        query += " AND employee_id = %s"
        values.append(employee_id)
    
    if nots is not None:
        query += " AND nots = %s"
        values.append(nots)

    cursor.execute(query, values)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results
#===============================================
@app.get("/get_check_point")
def get_check_point(
  
    check_point_id: Optional[int] = Query(None),
    project_check_point_id: Optional[int] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM points_chick WHERE 1=1"
    values = []

    if check_point_id is not None:
        query += " AND id = %s"
        values.append(check_point_id)

    if project_check_point_id is not None:
        query += " AND id_project = %s"
        values.append(project_check_point_id)

    cursor.execute(query, values)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results
#===============================================
@app.get("/payroll")
def payroll(
    id: Optional[int] = Query(None),
    project_id: Optional[int] = Query(None),
    employee_id: Optional[int] = Query(None),
    nots: Optional[float] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM work_shifts WHERE 1=1"
    values = []

    if id is not None:
        query += " AND id = %s"
        values.append(id)
    if project_id is not None:
        query += " AND project_id = %s"
        values.append(project_id)
    if employee_id is not None:
        query += " AND employee_id = %s"
        values.append(employee_id)
    if nots is not None:
        query += " AND nots = %s"
        values.append(nots)

    cursor.execute(query, values)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results
#====================================================
@app.post("/salary_history")
def salary_history(
    emp_id_send: int = Form(None), 
    proj_id_send: int = Form(None), 
    mySelect: str = Form(None),  
    pay_month: str = Form(None), 
    sum_pay: int = Form(None),
    emp_ent: str = Form(...), 
    notes: str = Form(None)
    
):
    try:
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO salary_history 
            (emp_id, project_id, pay_method, pay_for, sum, data_entry_clerk_id, nots) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (emp_id_send, proj_id_send, mySelect, pay_month, sum_pay, emp_ent, notes))
        conn.commit()
        return {"status": "success", "message": "Отправлено успешно ✅"}
    except mysql.connector.Error as e:
        return {"status": "error", "message": f"Произошла ошибка при отправке.❌: {str(e)}"}
    
    finally:
        cur.close()
        conn.close()
#====================================================
@app.post("/add_work_shifts", status_code=status.HTTP_201_CREATED)
async def add_work_shifts(
    employee_id: int = Form(...),
    project_id: int = Form(...),
    start_date: date = Form(...),
    start_time: str = Form(...),
    end_date: date = Form(...),
    end_time: str = Form(...),
    image: UploadFile = File(...)
):
    # ✅ تحقق من الصورة
    if not image:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="لم يتم التقاط الصورة"
        )

    try:
        # 📁 حفظ الصورة
        os.makedirs("obxod", exist_ok=True)
        now = datetime.now().strftime("%Y-%m-%d-T-%H-%M")
        filename = f"id{employee_id}-DT{now}.jpg"
        file_path = os.path.join("obxod", filename)

        with open(file_path, "wb") as f:
            f.write(await image.read())

        # 💾 حفظ البيانات
        conn = get_db_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO work_shifts
        (employee_id_input, project_id_input, start_day, start_time, end_day, end_time, file_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            employee_id,
            project_id,
            start_date,
            start_time,
            end_date,
            end_time,
            file_path
        ))
        conn.commit()

        return {
            "message": "تمت الإضافة بنجاح ✅",
            "file": file_path
        }

    except mysql.connector.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"خطأ في قاعدة البيانات: {str(e)}"
        )

    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass
        #====================================================
@app.post("/add_chick_point")
def add_chick_point(
    name_projct: int = Form(...), 
    name_point: str = Form(...), 
    crrdint: str = Form(...),
    id_entry_emp: str = Form(...)
):
    try:
        print("🚀 بدء حفظ البيانات...")
        print("id projact:", name_projct)
        print("name point:", name_point)
        print("cardinat & id emp:", crrdint, id_entry_emp)

        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO points_chick 
            (id_project, name_point, Coordinates, id_entry_emp) 
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (name_projct, name_point, crrdint, id_entry_emp))
        conn.commit()
        print("✅ تم الحفظ بنجاح")
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        print("❌ خطأ في قاعدة البيانات:", str(e))
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
#===============================================
@app.get("/show_work_shift")
def get_show_work_shift(
    employee_id_input: Optional[str] = Query(None),
    project_id_input: Optional[str] = Query(None),
    start_day: Optional[date] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            work_shifts.employee_id_input,
            work_shifts.project_id_input,
            work_shifts.start_day,
            work_shifts.start_time,
            work_shifts.end_day,
            work_shifts.end_time,
            work_shifts.file_path,
            employee.name AS employee_name,
            projuct.title AS projuct_title,
            employee.Salary AS projuct_sel_emp
        FROM work_shifts
        JOIN employee ON work_shifts.employee_id_input = employee.id
        JOIN projuct ON work_shifts.project_id_input = projuct.id
        WHERE 1=1
    """
    values = []

    if employee_id_input:
        query += " AND work_shifts.employee_id_input = %s"
        values.append(employee_id_input)

    if project_id_input:
        query += " AND work_shifts.project_id_input = %s"
        values.append(project_id_input)

    if start_day:
        query += " AND YEAR(work_shifts.start_day) = %s AND MONTH(work_shifts.start_day) = %s"
        values.append(start_day.year)
        values.append(start_day.month)

    cursor.execute(query, values)
    results = cursor.fetchall()
      # 🔥 الحل هنا
    for row in results:
    # تحويل start_time
        start_time_val = row.get("start_time")
        if isinstance(start_time_val, timedelta):
            total_seconds = int(start_time_val.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            row["start_time"] = f"{hours:02}:{minutes:02}:{seconds:02}"
        elif isinstance(start_time_val, time):
            row["start_time"] = start_time_val.strftime("%H:%M:%S")
        else:
            row["start_time"] = None

        # تحويل end_time
        end_time_val = row.get("end_time")
        if isinstance(end_time_val, timedelta):
            total_seconds = int(end_time_val.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            row["end_time"] = f"{hours:02}:{minutes:02}:{seconds:02}"
        elif isinstance(end_time_val, time):
            row["end_time"] = end_time_val.strftime("%H:%M:%S")
        else:
            row["end_time"] = None

        # تحويل التاريخ
        for date_field in ["start_day", "end_day"]:
            if isinstance(row.get(date_field), (date, datetime)):
                row[date_field] = row[date_field].strftime("%Y-%m-%d")
            
    cursor.close()
    conn.close()
    return results
#===============================================
@app.get("/show_info_chick_point", response_class=HTMLResponse)
def show_info_chick_point_page(
    request: Request,
    employee_id_input: Optional[str] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT 
            points_chick.id,
            points_chick.id_project,
            points_chick.name_point,
            points_chick.Coordinates,
            points_chick.id_entry_emp,
            projuct.title AS projuct_title
        FROM points_chick
        JOIN projuct ON points_chick.id_project = projuct.id
        WHERE 1=1
    """
    values = []
    if employee_id_input:
        query += " AND points_chick.id_project = %s"
        values.append(employee_id_input)
    cursor.execute(query, values)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    # تمرير البيانات إلى HTML
    return templates.TemplateResponse(
        "show_info_chick_point.html",
        {"request": request, "results": results}
    )

#===============================================
@app.get("/api/show_info_chick_point")
def show_info_chick_point_api(
    employee_id_input: Optional[str] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            points_chick.id,
            points_chick.id_project,
            points_chick.name_point,
            points_chick.Coordinates,
            points_chick.id_entry_emp,
            projuct.title AS projuct_title
        FROM points_chick
        JOIN projuct ON points_chick.id_project = projuct.id
        WHERE 1=1
    """
    values = []

    if employee_id_input:
        query += " AND points_chick.id_project = %s"
        values.append(employee_id_input)

    cursor.execute(query, values)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

#===============================================
@app.get("/show_salary_history")
def get_show_salary_history(
    employee_id_input: Optional[str] = Query(None),
    project_id_input: Optional[str] = Query(None),
    datas: Optional[str] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            salary_history.emp_id,
            salary_history.project_id,
            salary_history.pay_method,
            salary_history.pay_for,
            salary_history.sum,
            salary_history.data_entry_clerk_id,
            salary_history.process_supervisor_id,
            salary_history.responsible_emp_id,
            salary_history.nots,
            salary_history.done_or_not,
            employee.name AS employee_name,
            projuct.title AS projuct_title
        FROM salary_history
        JOIN employee ON salary_history.emp_id = employee.id
        JOIN projuct ON salary_history.project_id = projuct.id
        WHERE 1=1
         AND employee.is_active = TRUE
         AND projuct.is_active = TRUE
    """
    values = []

    if employee_id_input:
        query += " AND salary_history.emp_id = %s"
        values.append(employee_id_input)

    if project_id_input:
        query += " AND salary_history.project_id = %s"
        values.append(project_id_input)

    if datas:
        query += " AND salary_history.pay_for = %s"
        values.append(datas)

    

    cursor.execute(query, values)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


@app.get("/show_salary_history_page", response_class=HTMLResponse)
def show_salary_history_page(request: Request):
    return templates.TemplateResponse(
        "show_salary_history.html",  # ملف الـ HTML
        {"request": request}
    )

#=========================================================
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cur.execute(query, (username, password))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        return {
            "success": True,
            "message": "✅ Вход выполнен успешно",
            "role": user["role"],  # ترجع دور المستخدم هنا
            "username": user["username"]  # ترجع دور المستخدم هنا
        }
    else:
        return {
            "success": False,
            "error": "❌ Неверный логин или пароль"
        }
     #====================================================
@app.post("/add_chickd_point_datatame")
def add_chickd_point_datatame(id_check_point: int = Form(...)):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO list_points_checkd (id_check_point) 
            VALUES (%s)
        """
        cur.execute(query, (id_check_point,))
        conn.commit()
        print("✅ تم الحفظ بنجاح")
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        print("❌ خطأ في قاعدة البيانات:", str(e))
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()



#=========================================================
@app.get("/search_points")
def get_search_points(
    project_id_input: Optional[int] = Query(None),
    data_tame_input: Optional[str] = Query(None)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
       SELECT 
    p.id,
    p.name_point,
    p.Coordinates,
    p.id_project,
    DATE(l.dataD) AS dataD,
    TIME(l.timeD) AS timeD
    FROM list_points_checkd l
    JOIN points_chick p ON l.id_check_point = p.id
    """
    values = []

    # لو أدخل المستخدم id_project
    if project_id_input:
        query += " AND p.id_project = %s"
        values.append(project_id_input)

    # لو أدخل المستخدم data_tame
    if data_tame_input:
        query += " AND l.dataD = %s"
        values.append(data_tame_input)

    cursor.execute(query, values)
    results = cursor.fetchall()
     # 📌 هنا تضيف الكود اللي ينسّق الوقت
    from datetime import timedelta
    for row in results:
        if isinstance(row["timeD"], timedelta):
            seconds = row["timeD"].seconds
            h = seconds // 3600
            m = (seconds % 3600) // 60
            s = seconds % 60
            row["timeD"] = f"{h:02}:{m:02}:{s:02}"

    cursor.close()
    conn.close()
    return results

#=========================================================
# Endpoint لجلب كل project (Dropdown)
@app.get("/Dropdown_project")
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title FROM projuct")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products  # FastAPI ترجع JSON تلقائيًا

#=========================================================
# Endpoint لجلب كل emplye (Dropdown)
@app.get("/Dropdown_employee")
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name	 FROM employee")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products  # FastAPI ترجع JSON تلقائيًا
#=========================================================
app.mount("/obxod", StaticFiles(directory="obxod"), name="obxod")

       # حساب مجموع sale_price
   # total_sale_price = sum(item['sale_price'] for item in results if item['sale_price'] is not None)
   # print("Total Sale Price:", total_sale_price)
    
    


r"""
uvicorn main:app --reload
cd C:\Users\alame\OneDrive\Desktop\python\ratmir_from_git\ratmir
uvicorn main:app --host 127.0.0.1 --port 8001
in link add /docs

uvicorn C:\Users\alame\OneDrive\Desktop\python.main:app --reload

"""


 
