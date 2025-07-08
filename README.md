# Habit Tracker (CLI-based)

## Project Overview
The main goal of this project was to design and implement a data system for storing and managing environmental sensor data collected by a municipality. The system must reliably handle data from various sensor types, be scalable and maintainable in the long term, and support future expansion with new metrics such as CO₂ levels, fine dust, or noise. Furthermore, it should support integration with frontend applications for real-time citizen alerts.

## Features
- Analyze what data each sensor sends (e.g., timestamp, location, measurement type, value).
- Design data flow from sensor to storage.
- Decide on storage type like NoSQL.
- Define thresholds for each environmental metric.
- Create logic for real-time analysis and detection of dangerous values.
- Implement mechanisms to send warnings to frontend apps or directly to citizens.
  
## Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/IUCampus/project-data-engineering.git
cd sensor-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the sensor-app:
```bash
docker-compose up --build
```

- This will load sample data first (data-loader), and then run FastAPI.
- Visit http://localhost:8000/docs for Swagger UI.

## UML Class Diagram

![image](https://github.com/user-attachments/assets/f5d796e0-fa4d-4573-8e94-d21195d3349b)


## Project Structure

![image](https://github.com/user-attachments/assets/e582c6a2-faa0-4376-8b35-31ac2cbff482)




## Technologies Used

Python 3.7+

NoSQL for persistence

click for CLI

unittest or pytest for testing

JSON for fixture data 

Other libraries or helper tools (e.g.,datetime)


## Contacts

Email: chigozie-cyriacus.francis@iu-study.org

Website: [Chigozie Francis](https://www.franciswebapp.com/home)
