# E-commerce Admin API

## Features
- Product registration
- Inventory tracking (with low stock alert)
- Sales management
- Revenue reports and comparison

## Tech Stack
- FastAPI
- SQLAlchemy
- MySQL

## Setup
1. Clone the repo `git clone https://github.com/Sufyan-00/E-commerce_Admin_API.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a database in MySQL named ecommerce_admin using XAMPP(prefered)
4. Run `python demo_data.py` to populate fake data
5. Launch: `uvicorn app.main:app --reload` | `python -m uvicorn app.main:app --reload`
6. Open docs at: `http://localhost:8000/docs`
