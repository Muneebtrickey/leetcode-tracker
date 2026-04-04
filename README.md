# 🚀 Professional LeetCode Progress Tracker

A modern, high-performance web application designed for software engineers to track their algorithmic problem-solving journey. Built with **Django 6**, **Bootstrap 5**, and **Chart.js**, this platform helps users visualize progress, maintain consistency via streaks, and document technical insights.

![Dashboard Preview](https://via.placeholder.com/800x450?text=Modern+Dashboard+with+Chart.js+Visualization)

## ✨ Key Features

-   **📊 Dynamic Dashboard:** Visual representation of problem distribution (Easy/Medium/Hard) using Chart.js.
-   **🔥 Consistency Engine:** Automated streak tracking to keep you motivated and accountable.
-   **📋 Comprehensive Logging:** Track platform, difficulty, time taken, attempts, and personal notes for each problem.
-   **⭐ Portfolio-Ready:** Mark favorite problems and build a curated list of your technical accomplishments.
-   **👤 Secure Authentication:** Full user registration and login system.
-   **📱 Responsive Design:** Fully accessible on mobile, tablet, and desktop devices.

## 🛠️ Tech Stack

-   **Backend:** Python 3.12, Django 6.0
-   **Frontend:** HTML5, CSS3 (Inter Google Font), Bootstrap 5.3
-   **Icons:** FontAwesome 6.4
-   **Charts:** Chart.js 4.0
-   **Database:** SQLite (Default) / PostgreSQL (Production ready)

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/leetcode-tracker.git
cd leetcode-tracker
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```text
leetcode_tracker/    # Core project settings
tracker/             # Main application logic
├── models.py        # Database schema (Problems, Streaks, Progress)
├── views.py         # Business logic & Dashboard generation
├── forms.py         # Secure data handling
└── templates/       # UI Layer (Base, Home, Signup, etc.)
```

## 📝 Future Roadmap

-   [ ] Automated LeetCode API integration for fetching problem data.
-   [ ] Export progress as a professional PDF/Web Resume.
-   [ ] Social features to compare streaks with friends.

---
*Created by a Passionate Developer | Professional Software Engineering Portfolio*
