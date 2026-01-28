import base64

code = "bDNhcm5fdGgzX3IwcDM1"
decoded_bytes = base64.b64decode(code)
ans = decoded_bytes.decode('utf-8')
print(ans)