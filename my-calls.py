import httpx

URL = "http://localhost:5000"  

print("=== Health Check ===")
print(httpx.get(f"{URL}/health").json())

print("\n=== Login (get token) ===")
login_data = {
    "id": "phillip.bradford@uconn.edu"
}
r = httpx.post(f"{URL}/login", json=login_data)
print(r.json())
token = r.json()["uuid_token"]

print("\n=== Verify with correct token ===")
verify_data = {
    "id": "phillip.bradford@uconn.edu",
    "uuid-token": token
}
print(httpx.post(f"{URL}/verify", json=verify_data).json())

print("\n=== Verify with WRONG token (should fail) ===")
bad_data = {
    "id": "phillip.bradford@uconn.edu",
    "uuid-token": "00000000-0000-0000-0000-000000000000"
}
print(httpx.post(f"{URL}/verify", json=bad_data).json())