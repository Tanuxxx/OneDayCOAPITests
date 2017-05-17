import requests

LOGIN_API = "/api/authenticate"

class Session:
    def authenticate(url, login, pswd):
        result = requests.post(url+LOGIN_API, auth=(login, pswd))
        if result.status_code != 200:
            return None
        else:
            headers = result.headers
            result_headers = {}
            result_headers["Token"] = headers.get("Token")
            result_headers["TokenExpiry"] = headers.get("TokenExpiry")
            result_headers["Access-Control-Expose-Headers"] = headers.get("Access-Control-Expose-Headers")
            return result_headers
