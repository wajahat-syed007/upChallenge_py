from fastapi import FastAPI, File, UploadFile, Form
from starlette.responses import FileResponse
from authlib.jose import JsonWebToken
import http.client
import uvicorn 
import router
import json
import check_jwt

app = FastAPI()

config = {
  "column": "",
  "delimiter": "",
  "path":"./uploads/",
  "filename":""
}

log = {
    "error":"none",
    "resolution":"n/a",
    "fail":"no"
}

master = {"sid" : ""}


@app.get("/")
async def main():
    return FileResponse('./views/index.html')

@app.get("/uploadfile/chart.js")
async def chart():
    return FileResponse('./public/js/chart.js')  

@app.get("/uploadfile/localdb.json")
async def localdb():
    return FileResponse('./db/localdb.json')
    
@app.get("/uploadfile/chart_1.js")
async def chart_1():
    return FileResponse('./public/js/chart_1.js')    
    
@app.get("/svg_webserver.svg")
async def result():
    return FileResponse('./public/components/svg_webserver.svg')

@app.get("/test")
async def test():
    status = await check_jwt.check()
    print(status)
    #token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhEcjc0clNBNjdlVmZTeWJWMmhYRiJ9.eyJpc3MiOiJodHRwczovL2Rldi02eTk0di1kci51cy5hdXRoMC5jb20vIiwic3ViIjoiYkN2UTdtNjBNdkExZWhlZnBIOUR5bEgza1dmSmFQT1dAY2xpZW50cyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODAwMC8iLCJpYXQiOjE2ODA5ODkwMTEsImV4cCI6MTY4MTA3NTQxMSwiYXpwIjoiYkN2UTdtNjBNdkExZWhlZnBIOUR5bEgza1dmSmFQT1ciLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.LqglOCQejbyrURApSVSGpzn-6aZXPzu20xUi_NOZNQPpnRnmvdFJylGZ-7LkgKXIrsbffsHRbEmUe5muhgLrQupoB6g3BTZKhO-maaoBvVC3tVwMgU7QsOjmA-VjBNQ8YWtfr82u5HoeSm6IssE9r5HKWbgJqgM6mhkvcJPk-VVi5_qblKrtdPBW7A5G5x7vWMQYbG9oF_4hU8NiTlf10R51EI5dznzulmlO9Zl8BG8ZftPlUrlOk2JKWNcIoT1dRQ4NHcnbIq330svQJk9ev23tYUM63UgvMSZvuCjXQ5Y0OxR87-AQTPG8wtXIzRMqXaV4IY5l3aeqtaLXVJe8TA"
    #rsa_pub_key = await POST()
    #jwt = JsonWebToken(['RS256'])
    #print(rsa_pub_key)
    #claims = jwt.decode(token, rsa_pub_key)
    #print(claims)
    

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, delimiter: str = Form(), column: str = Form(), sid: str = Form()): #Check form input
    #print(log)
    #await check_jwt.check()
    await router.test(file, delimiter, column, sid, config, log) #Check csv file size and extension 
    return log,config #return error and resolution for the user

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')        
