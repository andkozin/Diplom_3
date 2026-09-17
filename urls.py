# urls.py

BASE_URL = "https://stellarburgers.education-services.ru"

LOGIN_URL = f"{BASE_URL}/login"
REGISTER_URL = f"{BASE_URL}/register"
FEED_URL = f"{BASE_URL}/feed"
CONSTRUCTOR_URL = f"{BASE_URL}"

AUTH = {
    "user": f"{BASE_URL}/api/auth/user"
}
