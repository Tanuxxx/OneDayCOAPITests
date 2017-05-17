import requests

LOGIN_API = "/api/authenticate"

class Session:
    def authenticate(self, url, login, pswd):
        result = requests.post(url+LOGIN_API, auth=(login, pswd))
        if result.status_code != 200:
            return None
        else:
            headers = result.headers
            self.result_headers = {}
            self.result_headers["Token"] = headers.get("Token")
            self.result_headers["TokenExpiry"] = headers.get("TokenExpiry")
            self.result_headers["Access-Control-Expose-Headers"] = headers.get("Access-Control-Expose-Headers")
            return self.result_headers
