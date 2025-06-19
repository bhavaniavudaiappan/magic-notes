# 🪄 Magic Notes

**Magic Notes** is a magical, secure, and elegant note-taking web app that lets users log in without passwords — just using their email! Built with **FastAPI**, **MongoDB**, and **Streamlit**, it brings a beautiful UI, animated spells, and seamless note management features into your hands.

---

## 🔥 Features

- ✨ Magic Link Login — No passwords. Just check your inbox and click!
- 📥 Add Notes — Write and save instantly.
- 📝 Edit & Delete — Update or remove notes anytime.
- 🔍 Search Bar — Instantly search through all your notes.
- 🎭 UI Magic — Animated spells during login to enhance user delight.
- ☁️ MongoDB Integration — Stores notes securely in the cloud.

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: MongoDB Atlas
- **Authentication**: JWT-based magic link via Gmail SMTP
- **Deployment**: Render / Streamlit Community Cloud

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bhavaniavudaiappan/magic-notes.git
cd magic-notes
pip install -r requirements.txt
```

---

### 2. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```
EMAIL_USER=your_email_id
EMAIL_PASS=your_email_app_password
JWT_SECRET=your_super_secret_key
JWT_ALGORITHM=HS256
BASE_URL=http://localhost:8501
MONGO_URI=mongodb://localhost:27017
```

💡 Use Google App Passwords for Gmail if you have 2FA enabled.

---

### 3. Install Dependencies

**Backend**:

```bash
cd backend
uvicorn main:app --reload
```

**Frontend**:

```bash
cd ../frontend
streamlit run app.py
```

---

## 🌍 Deployment

### 🛠 On Render (Backend)

1. Push your code to GitHub.
2. Visit [Render](https://render.com).
3. Click **"New Web Service"** → Connect your repo.
4. Set **Build Command**:
   `pip install -r requirements.txt`
5. Set **Start Command**:
   `uvicorn main:app --host=0.0.0.0 --port=10000`
6. Add the required **environment variables** in the Render dashboard.

---

### ☁️ On Streamlit Community Cloud (Frontend)

1. Visit [streamlit.io/cloud](https://streamlit.io/cloud).
2. Deploy `frontend/app.py` from your GitHub repo.
3. In your code (`app.py`), make sure `API_URL` points to the deployed backend on Render.

---

## 🧙‍♂️ Creator Notes

This app is perfect for:

- Writing down thoughts on the go.
- Keeping a journal or quick todo list.
- Experiencing how authentication can feel _magical_.

---

## 🧑‍💻 Built with magic by Bhavani
