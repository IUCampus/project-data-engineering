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
git clone https://github.com/IUCampus/python-backend-project.git
cd habit-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the tracker:
```bash
python cli.py
```

## UML Class Diagram

![image](https://github.com/user-attachments/assets/5fac31e7-2926-429f-9bb2-c5a58fe7aebe)

![image](https://github.com/user-attachments/assets/26b47ce7-8d3e-4570-b1bb-6721f0f59bdb)


## Project Structure

![image](https://github.com/user-attachments/assets/2870c500-db85-4e46-98d2-d00c435b1f1f)



## Technologies Used

Python 3.7+

SQLite3 for persistence

click for CLI

unittest or pytest for testing

JSON for fixture data (optional)

Other libraries or helper tools (e.g.,datetime)


## Contacts

Email: chigozie-cyriacus.francis@iu-study.org

Website: [Chigozie Francis](https://www.franciswebapp.com/home)
