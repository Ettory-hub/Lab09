# Lab 09 - Web Tokens

Simple Flask web-token service running on GitHub Codespaces.

### Endpoints
- GET  /health → health check
- GET  / → lists routes
- POST /login → generates and stores a UUID token for a user id
- POST /verify → verifies if the provided token matches the stored one

Tokens are stored in-memory in the TOKENS dictionary.

### How to run
```bash
pip3 install flask httpx pytest pytest-flask
python3 my_server.py         
Ports tab
python3 my-calls.py           
python3 -m pytest test_server.py -v   

