# Smart Agriculture - AI-Powered Farming Recommendations

A web-based intelligent agriculture system that provides personalized farming recommendations using AI technology and environmental data analysis.

## 📋 Project Description

Smart Agriculture is a Flask-based web application that leverages Google's Gemini AI to provide intelligent farming recommendations. Farmers can input their soil type, weather conditions, rainfall, temperature, and location to receive AI-powered insights and recommendations for optimal crop cultivation and farm management.

**Key Features:**
- 🔐 User Authentication (Login/Register)
- 🌾 AI-Powered Farming Recommendations using Google Gemini
- 📊 Dashboard with user-specific data
- 📜 History tracking of previous recommendations
- 🎯 Results display with detailed agricultural insights
- 💾 MySQL database for persistent data storage
- 📱 Responsive web interface

## 👥 Group Members

1. Ridwan Abdi Jibriil
2. Cabdimalik Mahamed Ismail
3. Suhayb Mahamed Saleeban
4. Khaalid Mahamuud Cabdilahi
5. Ahmed Hasan Muxumed
6. Osame Ismail Ahmed
7. Nagiib Husain Ibraahim
8. Marwaan Cabdilaahi Xuseen

## 🛠️ Technologies Used

- **Backend:** Python Flask
- **AI/ML:** Google Gemini AI (Flash Lite Model)
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:** 
  - Flask (Web Framework)
  - google-genai (AI Integration)
  - mysql-connector-python (Database Connection)
  - tenacity (Retry Logic for API calls)
  - markdown (Text Processing)

## 📦 Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/smart_agriculture.git
cd smart_agriculture
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

**Activate virtual environment:**
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Database

1. Open MySQL and create the database:
```sql
CREATE DATABASE smart_agriculture;
USE smart_agriculture;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    soil VARCHAR(100),
    weather VARCHAR(100),
    rainfall VARCHAR(100),
    temperature VARCHAR(100),
    location VARCHAR(255),
    recommendation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Step 5: Configure Environment
Update the following in `app.py`:
- MySQL credentials (host, user, password)
- Ensure MySQL server is running
- API key for Google Gemini (already configured in app.py)

## 🚀 How to Run

1. **Ensure MySQL is running**
   ```bash
   mysql -u root -p
   ```

2. **Activate virtual environment** (if not already activated)
   ```bash
   venv\Scripts\activate
   ```

3. **Run the Flask application**
   ```bash
   python app.py
   ```

4. **Open your browser and navigate to**
   ```
   http://localhost:5000
   ```

5. **First-time users:**
   - Click on "Register" to create an account
   - Enter your details and create a password
   - Login with your credentials

6. **Get Recommendations:**
   - Fill in the form with your farm details:
     - Soil Type
     - Weather Conditions
     - Rainfall
     - Temperature
     - Location
   - Click "Get Recommendations"
   - View AI-generated farming insights

## 📂 Project Structure

```
smart_agriculture/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/
│   ├── style.css         # Stylesheet
│   └── app.js            # Frontend JavaScript
└── templates/
    ├── index.html        # Home/Dashboard page
    ├── login.html        # Login page
    ├── register.html     # Registration page
    ├── dashboard.html    # User dashboard
    ├── history.html      # Recommendation history
    └── result.html       # Recommendation results
```

## 🔒 Security Notes

⚠️ **Important:** Before pushing to production or public repository:
1. Remove or regenerate the API key in app.py
2. Use environment variables for sensitive data (database credentials, API keys)
3. Implement proper password hashing (bcrypt instead of plain text)
4. Add HTTPS security

## 🐛 Troubleshooting

**Issue:** "Cannot connect to MySQL"
- **Solution:** Ensure MySQL server is running and credentials in app.py are correct

**Issue:** "Gemini API error"
- **Solution:** Check API key validity and ensure you have internet connection

**Issue:** "Module not found"
- **Solution:** Run `pip install -r requirements.txt` and ensure virtual environment is activated

## 📸 Screenshots

[Add screenshots of your application here showing:]
- Login page
- Dashboard
- Recommendation form
- Results page
- History page

## 🎥 Demo Video

[Link to demo video if available]

## 📝 License

This project is created for educational purposes.

## 📞 Contact & Support

For questions or issues, contact the project group members.

---

**Last Updated:** May 18, 2026  
**Deadline:** May 19, 2026
