# LeetCode Progress Tracker

A comprehensive web application designed for software engineers to monitor and visualize their algorithmic problem-solving progress. This platform provides a structured environment to document technical insights, maintain consistency, and analyze performance metrics over time.

Built with a focus on clean architecture and performance, the tracker leverages Django for the backend, Bootstrap for a responsive user interface, and Chart.js for data visualization.

## Core Features

-   **Analytical Dashboard:** Provides a visual breakdown of solved problems by difficulty level, helping users identify areas for improvement.
-   **Consistency Tracking:** Automated streak monitoring to encourage daily practice and accountability.
-   **Detailed Problem Logging:** Capture essential data for every problem, including platform, difficulty, time spent, attempts, and personal technical notes.
-   **Curated Favorites:** Ability to bookmark significant problems for future review or portfolio highlights.
-   **Secure Authentication:** A robust user management system with secure registration and login workflows.
-   **Responsive Design:** Fully optimized for seamless use across mobile, tablet, and desktop environments.

## Technical Specifications

-   **Backend:** Python 3.12, Django 6.0
-   **Frontend:** HTML5, CSS3, Bootstrap 5.3
-   **Data Visualization:** Chart.js 4.0
-   **Icons:** FontAwesome 6.4
-   **Database:** SQLite for development, configured for PostgreSQL in production.

## Installation and Configuration

### 1. Repository Setup
```bash
git clone https://github.com/yourusername/leetcode-tracker.git
cd leetcode-tracker
```

### 2. Environment Configuration
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Dependency Management
```bash
pip install -r requirements.txt
```

### 4. Database Initialization
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Local Execution
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

## Project Organization

```text
leetcode_tracker/    # Core project configuration
tracker/             # Main application modules
├── models.py        # Database schema for problems and progress
├── views.py         # Business logic and dashboard controllers
├── forms.py         # Data validation and handling
└── templates/       # UI components and layout files
```

## Development Roadmap

-   Integration with the LeetCode API for automated data synchronization.
-   Functionality to export progress reports as professional PDF documents.
-   Collaborative features to enable shared streaks and peer benchmarking.

---
*Developed as part of a professional software engineering portfolio.*
