import requests
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")

#проверка кода у сайта
def test_status():
    resp = requests.get('https://x-clients-be.onrender.com/employee')
    assert resp.status_code == 500

#создание сотрудника без обязательных полей
def test_add_noname_employee():
    
    name = "Sea products Co2"
    descr = "sea products2"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    body = api.get_employees_list(companyId)
    len_before = len(body)
   
    firstName = ""
    lastName = "Abramovich"
    middleName = "Dmitrievna"
    company = companyId
    email = "abramovichdash@mail.ru"
    url = "string"
    phone = "89670425734"
    birthdate = "1991-11-24"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    resp = requests.get("https://x-clients-be.onrender.com")
    assert resp.status_code == 404

#создание сотрудника с некорректными данными
def test_add_incorrect_data_employee():
    
    name = "Sea"
    descr = "sea"
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
    email = "mailru"
    url = "string"
    phone = "89670425734"
    birthdate = "1991-11-24"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    resp = requests.get("https://x-clients-be.onrender.com")
    assert resp.status_code == 404
#получение несуществующего сотрудника
def test_add_non_existent_employee():
    
    name = "Sea3"
    descr = "sea4"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    body = api.get_employees_list(companyId)
    len_before = len(body)
   
    firstName = "Noname"
    lastName = "Nolastlame"
    middleName = "NomiddleName"
    company = companyId
    email = "noname@mail.ru"
    url = "string"
    phone = "89670425734"
    birthdate = "1991-11-24"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    resp = requests.get("https://x-clients-be.onrender.com")
    assert resp.status_code == 404

#получение сотрудника с дублирующимися данными:
def test_add_duplicate_data_employee():
    
    name = "Solo"
    descr = "Mio"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    body = api.get_employees_list(companyId)
    len_before = len(body)
   
    firstName = "Zina"
    lastName = "Alimova"
    middleName = "Olegovna"
    company = companyId
    email = "guseva.darya@mail.ru"
    url = "string"
    phone = "89098765432"
    birthdate = "1992-11-24"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    resp = requests.get("https://x-clients-be.onrender.com")
    assert resp.status_code == 404

#редактирование несуществующего сотрудника
def test_patch_non_existent_employee():
    name = "McDonalds"
    descr = "fast food"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    firstName = "No"
    lastName = "No"
    middleName = "No"
    company = companyId
    email = "no@mail.ru"
    url = "string"
    phone = "no"
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
    
    resp = requests.get("https://x-clients-be.onrender.com")
    assert resp.status_code == 404

   
