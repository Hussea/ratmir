from fastapi import FastAPI, Query
from typing import Optional
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from datetime import datetime, date, time


app = FastAPI()

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
        host='localhost',
        user='root',
        password='',        # ← غيّر إذا عندك كلمة سر
        database='ratmer'
    )



#====================================================
@app.post("/add-emp")
def add_employee(id: int = Form(0), 
                 name: str = Form(...), 
                 num_T: str = Form(...),
                 data_prth: str = Form(...),
                 address: str = Form(...),
                 Salary: str = Form(...), 
                 Job: str = Form(...), 
                 nots: str = Form(...)):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = "INSERT INTO employee (id, name, num_T, data_prth, address, Salary, Job, nots) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (id, name, num_T, data_prth, address, Salary, Job, nots))
        conn.commit()
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        return {"error": str(e)}
#====================================================
@app.post("/add-category")
def add_category(id: int = Form(0), 
                 title: str = Form(...), 
                 address: str = Form(...),
                 q_person: str = Form(...), 
                 ses_work: str = Form(...), 
                 sum_of_proj: str = Form(...), 
                 pers_of_proj: str = Form(...), 
                 n_phone: str = Form(...), 
                 sel_emp: str = Form(...),
                 nots: str = Form(...)):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = "INSERT INTO projuct (id, title, address, q_person, ses_work, sum_of_proj, pers_of_proj, n_phone, sel_emp, nots) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (id, title, address, q_person, ses_work, sum_of_proj, pers_of_proj, n_phone, sel_emp, nots))
        conn.commit()
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        return {"error": str(e)}
#====================================================
@app.post("/add-project-guards")
def add_project_guards(
    project_id: int = Form(...), 
    project_name: str = Form(...), 
    employee_id: int = Form(...),
    employee_name: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    emp: str = Form(...),  
    nots: str = Form(...)
):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO project_guards 
            (project_id, project_name, employee_id, employee_name, end_date, emp, nots) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (project_id, project_name, employee_id, employee_name, end_date, emp, nots))
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
        cur.execute("SELECT title FROM projuct")  # أو اسم العمود اللي تريده
        rows = cur.fetchall()
        category = [row[0] for row in rows]
        return {"category": category}
    except mysql.connector.Error as e:
        return {"error": str(e)}

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
    
    query = "SELECT * FROM project_guards WHERE 1=1"
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
    notes: str = Form(None)
):
    try:
        print("🚀 بدء حفظ البيانات...")
        print("الموظف:", emp_id_send)
        print("المشروع:", proj_id_send)
        print("التواريخ:", mySelect, pay_month, sum_pay, notes)
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO salary_history 
            (emp_id, project_id, pay_method, pay_for, sum, nots) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (emp_id_send, proj_id_send, mySelect, pay_month, sum_pay, notes))
        conn.commit()
        print("✅ تم الحفظ بنجاح")
        return {"message": "تمت الإضافة بنجاح ✅"}
    except mysql.connector.Error as e:
        print("❌ خطأ في قاعدة البيانات:", str(e))
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
#====================================================
@app.post("/add_work_shifts")
def add_work_shifts(
    employee_id_input: int = Form(...), 
    project_id_input: int = Form(...), 
    start_date: date = Form(...),
    start_time: time = Form(...),
    end_date: date = Form(...),
    end_time: time = Form(...)
):
    try:
        print("🚀 بدء حفظ البيانات...")
        print("الموظف:", employee_id_input)
        print("المشروع:", project_id_input)
        print("التواريخ:", start_date, start_time, end_date, end_time)

        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO work_shifts 
            (employee_id_input, project_id_input, start_day, start_time, end_day, end_time) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (employee_id_input, project_id_input, start_date, start_time, end_date, end_time))
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
            employee.name AS employee_name,
            projuct.title AS projuct_title,
            projuct.sel_emp AS projuct_sel_emp
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
    cursor.close()
    conn.close()
    return results
#===============================================
@app.get("/show_salary_history")
def get_show_salary_history(
    employee_id_input: Optional[str] = Query(None),
    project_id_input: Optional[str] = Query(None),
    start_day: Optional[date] = Query(None)
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
    """
    values = []

    if employee_id_input:
        query += " AND salary_history.emp_id = %s"
        values.append(employee_id_input)

    if project_id_input:
        query += " AND salary_history.project_id = %s"
        values.append(project_id_input)

    

    cursor.execute(query, values)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


#=========================================================

       # حساب مجموع sale_price
   # total_sale_price = sum(item['sale_price'] for item in results if item['sale_price'] is not None)
   # print("Total Sale Price:", total_sale_price)
    
    


r"""
uvicorn main:app --reload
cd C:\Users\Acer\Desktop\work\working
uvicorn main:app --host 127.0.0.1 --port 8001
in link add /docs
"""





