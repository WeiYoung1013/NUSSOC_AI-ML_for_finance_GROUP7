import requests

def register_user(base_url, user_name, password, password_confirm):
    url = f"{base_url}/auth/register"
    payload = {
        "user_name": user_name,
        "password": password,
        "password_confirm": password_confirm
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    
    if response.status_code == 201:
        print("Registration successful!")
    else:
        print(f"Failed to register. Status code: {response.status_code}")
        try:
            print("Response JSON:", response.json())
        except requests.exceptions.JSONDecodeError:
            print("Response is not in JSON format.")

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # 替换为您的服务器地址
    user_name = "example_user"
    password = "example_password"
    password_confirm = "example_password"
    
    register_user(base_url, user_name, password, password_confirm)
