from app.auth.password import (
    hash_password,
    verify_password
)

password = "Financial@123"

hashed = hash_password(password)

print("Original Password :", password)
print("Hashed Password   :", hashed)

print()

print(
    "Verification :",
    verify_password(password, hashed)
)
