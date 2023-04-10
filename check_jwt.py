from authlib.jose import JsonWebToken
import http.client
import json
claims_options = {
    "iss": { "essential": True, "value": "https://dev-6y94v-dr.us.auth0.com/" },
    "aud": { "essential": True, "value": "http://localhost:8000/" }
}

async def check():
    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhEcjc0clNBNjdlVmZTeWJWMmhYRiJ9.eyJpc3MiOiJodHRwczovL2Rldi02eTk0di1kci51cy5hdXRoMC5jb20vIiwic3ViIjoiYkN2UTdtNjBNdkExZWhlZnBIOUR5bEgza1dmSmFQT1dAY2xpZW50cyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODAwMC8iLCJpYXQiOjE2ODExMDA2NjQsImV4cCI6MTY4MTE4NzA2NCwiYXpwIjoiYkN2UTdtNjBNdkExZWhlZnBIOUR5bEgza1dmSmFQT1ciLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.a118sSPOQktOsyhgPUQIrCio9zmz_-Lm_CGMgbhjVsthbwWc-d-ilYhap69HmPpSSC7Xhui9cEaU_2TWAq3kVaTfsz3yH76N9UFV7RInNVGXIgGXLVcsspb6tDhqX3wm5yGkoQ3_a-ETyfuF9kZESNloeH6tubA0EVLsR0PsBDcUzSKYOjEi58UDPNOotejDhp-IdWZQ1Fln59i6L3bsiYuxFptzfaXUlPj1wuVVj-JJgixLwslvpvWsFBkXGnUhFIpsKxfKGQck3NqqF5W0VxIxC9RcKfWFAnjlbj47DVMyTsi-3HuEv0VMO-0OCt2oHNwKEs77KyOtZf0bn6IgPg"
    rsa_pub_key = await POST()
    jwt = JsonWebToken(['RS256'])
    print(rsa_pub_key)
    claims = jwt.decode(token, rsa_pub_key, claims_options=claims_options)
    try:
        claims.validate()
        status = "Authorized"
    except Exception as e:
        status = "Not Authorized because " + e 
    return status    

async def POST():
    conn = http.client.HTTPSConnection("dev-6y94v-dr.us.auth0.com")
    headers = {
        'content-type':  "application/json",
        'cache-control': "no-cache"
        }
    conn.request("GET", "/.well-known/jwks.json")
    res = conn.getresponse()
    rsa_pub_key = res.read()
    rsa_pub_key = json.loads(rsa_pub_key.decode("utf-8"))
    rsa_pub_key = rsa_pub_key["keys"][0]
    #print(rsa_pub_key["keys"][0])
    return rsa_pub_key
