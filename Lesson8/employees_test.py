import requests
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
    
    name = "Sea products Co"
    descr = "sea products"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    body = api.get_employees_list(companyId)
    len_before = len(body)
   
    firstName = "Daria"
    lastName = "Abramovich"
    middleName = "Dmitrievna"
    company = companyId
    email = "abramovichdash@mail.ru"
    url = "string"
    phone = "89670425734"
    birthdate = "1991-11-24"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    
    body = api.get_employees_list(companyId) 
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Daria"
    assert body[-1]["lastName"] == "Abramovich"
    assert body[-1]["middleName"] == "Dmitrievna"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89670425734"
    assert body[-1]["birthdate"] == "1991-11-24"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    name = "Aviasales"
    descr = "авиакомпания"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
  
    new_company = api.get_company(new_id)
    companyId = new_company['id']
   
    body = api.get_employees_list(companyId)
    begin_list = len(body) 
   
    firstName = "Oleg"
    lastName = "Tinkoff"
    middleName = "Alexandrovich"
    company = companyId
    email = "tinkoff777@yandex.ru"
    url = "string"
    phone = "89035145997"
    birthdate = "1971-06-04"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
 
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Oleg"
    assert body[-1]["lastName"] ==  "Tinkoff"
    assert body[-1]["middleName"] == "Alexandrovich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "89035145997"
    assert body[-1]["birthdate"] == "1971-06-04"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    name = "McDonalds"
    descr = "fast food"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    firstName = "Vladimir"
    lastName = "Arseniev"
    middleName = "Konstantinovich"
    company = companyId
    email = "vlars@mail.ru"
    url = "string"
    phone = "89051112350"
    birthdate = "1992-08-17"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employees_list(companyId) 
   
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]

    new_email = "popov@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "popov@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False