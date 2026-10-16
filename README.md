# Gym Management System

A command-line Gym Management System built with Python, featuring role-based access for Managers, Trainers, and Members.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Default Users](#default-users)
- [Modules Overview](#modules-overview)
- [Technologies](#technologies)
- [Contributors](#contributors)
- [License](#license)
- [Contact](#contact)

---

## Features

### Manager Panel
- Manage users (add, view, delete, enable/disable)
- Manage halls (add, edit, enable/disable)
- Manage classes (add, edit, view, enable/disable)
- Manage subscriptions and payments
- View reports (income, active subscriptions, etc.)

### Trainer Panel
- View assigned classes(only their own)
- View class members
- Set workout plans for members

### Member Panel
- View and manage wallet
- Buy subscriptions (Gold, Silver, Bronze)
- View workout plans
- View & Renew subscription status

### Authentication
- Role-based login for Manager, Trainer, and Member
- Password validation
- Maximum of 3 login attempts 

---

## Project Structure

```text
Gym-Management/
│
├── data/
│   ├── Bank.py                     # Simulated bank API
│   ├── initial_data.py             # Initial seed data
│   ├── subscription_catalog.py     # Subscription plans catalog
│   └── workout_storage.py          # Workout plan persistence
│
├── docs/
│   └── flowchart.jpg               # Project flowchart
│
├── models/
│   ├── __init__.py
│   ├── coach.py                    # Coach, CoachManager, CoachPanel
│   ├── exercise.py                 # Exercise model
│   ├── user.py                     # User, Manager, Trainer, Member
│   └── workout_plan.py             # WorkoutPlan model
│
├── panels/
│   ├── __init__.py
│   ├── exercise_editor.py
│   ├── exercise_input.py
│   ├── manager_panel.py            # Manager control panel
│   └── member_panel.py             # Member control panel
│
├── services/
│   ├── __init__.py
│   ├── classes_management.py       # Classes service
│   ├── enrollments.py              # Enrollment service
│   ├── halls_management.py         # Halls service
│   ├── reports.py                  # Reports service
│   ├── subscription.py             # MemberSubscription service
│   ├── transaction.py              # Transaction service
│   ├── user_management.py          # User CRUD service
│   ├── view_users.py               # Export users to file
│   ├── wallet.py                   # Wallet service
│   ├── workout_manager.py          # Workout manager
│   └── workout_service.py          # Workout service
│
├── utils/
│   ├── __init__.py
│   ├── Exceptions.py               # Custom exceptions
│   ├── storage.py                  # File storage utilities
│   └── validators.py               # Input validators
│
├── .gitignore
├── Main_menu.py                    # Main menu
├── README.md
└── main.py                         # Application entry point
```

---

## Requirements

- Python 3.10+
- No external libraries required (standard library only)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sarahghorbani13/Gym-Management.git
   cd Gym-Management
   ```

2. Run the application:

   ```bash
   python main.py
   ```

> **Note:** On some systems you may need to use `py` instead of `python`.

---

## Usage

After running the program, you will see the main menu:

```text
***** Welcome to Quera Gym! *****
--------------------------------
1: Management
2: Trainers
3: Members
4: Exit
--------------------------------
```

1. **Login:** Choose a panel (1, 2, or 3) and log in with your credentials.
2. **Navigate:** Each panel provides its own submenu. Enter the number of the option you want.
3. **Exit:** Choose option 4 from the main menu to exit.

---

## Default Users

The system comes with three default users for testing:

| Role    | Username  |  Password   |
|---------|-----------|-------------|
| Manager | `manager` | `Manager@1` |
| Trainer | `trainer` | `Trainer@1` |
| Member  | `member`  | `Member@1`  |

> **Important:** These accounts are for testing purposes only.

---

## Modules Overview

### `models/`
Data models:
- `User` (base class), `Manager`, `Trainer`, `Member`
- `Coach` (gym coach, connected to`Trainer`)
- `Exercise`
- `WorkoutPlan`

### `services/`
Business logic layer:
- User management, wallet, subscriptions, transactions
- Halls and classes management
- Report generation
- Workout services

### `panels/`
Interactive UI panels:
- `manager_panel`: Manager control panel
- `member_panel`: Member control panel
- `exercise_editor`, `exercise_input`: Workout plan editing

### `data/`
Static data and persistence:
- Subscription catalog
- Workout storage
- Bank simulation
- Initial seed data

### `utils/`
Utility modules:
- Custom exceptions
- Input validators (username, password, email)
- File storage helpers

---

## Technologies

- **Language:** Python 3.10+
- **Architecture:** Layered (models, services, panels)
- **Storage:** File-based (text files)
- **Interface:** Command-line (CLI)

---

## Contributors

- [Sarah Ghorbani]           (https://github.com/sarahghorbani13)
- [Reza Zamanizade]          (https://github.com/SRezaZZ)
- [Amirreza Qadamyari]       (https://github.com/qadamyari)
- [Sara Saadat Mehr]         (https://github.com/sara-2005codes)
- [Elham Baneshi]            (https://github.com/ebnshi1419)
- [Sadeq Sha'abani]          (https://github.com/Sadeq666)

Special thanks to our beloved mentor:
- [Amir Arsalan Khatibzadeh] (https://github.com/arsalankhz)
who guided us through this project.

---

## License

This project is for educational purposes.
Designed for Quera Bootcamp 13: Alpha Python course, Final Project.
