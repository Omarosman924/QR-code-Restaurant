# 🍽️ QR Code Restaurant Ordering System (Prototype)

This is a simplified backend prototype for a restaurant ordering system built with **Flask** and **SQLAlchemy**.

Customers can scan a QR code (currently simulated by accessing `/1`, `/2`, `/3`, etc.) to place orders. Employees can view submitted orders via a dashboard.

---

## ✅ Features

### ✅ Customer Side

- Each table is accessed via a unique route: `/1`, `/2`, `/3`, etc.
- Customers see a clean menu and choose quantities per item.
- Submitted orders are stored in the SQLite database.

### ✅ Employee Side

- Orders page displays all current orders with table number, items, quantities, and total price.
- Each order has a "Mark as Complete" button (currently non-functional — to be implemented).

---

## 🚧 In Progress

- ❌ QR Code images are **not yet generated**, but accessible manually by table number.
- 🔜 Full order status control by employees (e.g., mark order as `Completed`).
- 🔜 Admin dashboard, analytics, and real-time order updates are planned.

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **SQLAlchemy (ORM)**
- **SQLite (for now)**
- **HTML / Jinja Templates**

---

## 📝 Notes

⚠️ A future version of this project will be rebuilt using **Node.js** for more advanced backend capabilities, real-time features (like Socket.IO), and API-first structure.

---

## 📂 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/qr-code-restaurant.git
   cd qr-code-restaurant
   pip install -r requirements.txt
   python seed_data.py
   python app.py
