# test_email.py
import os
from dotenv import load_dotenv
import os
from utils.email_utils import send_magic_link
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
print(env_path)
load_dotenv(dotenv_path=env_path)

print("EMAIL_USER =", os.getenv("EMAIL_USER"))
print("EMAIL_PASS =", os.getenv("EMAIL_PASS"))
send_magic_link("your_email@gmail.com", "dummy-token-123")
