from backend.app.auth.jwt_handler import (
    create_access_token,
    verify_access_token,
)

payload = {
    "sub": "admin@example.com"
}

token = create_access_token(payload)

print("Generated Token:\n")
print(token)

print("\nDecoded Payload:\n")
print(verify_access_token(token))