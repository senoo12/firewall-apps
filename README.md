
# Firewall WLAN Application with Django

This project is a web-based firewall application built using Django, designed to enhance network security by providing access control, IP address blocking, and activity logging for devices.

Key Features:

1. Access Filtering:

- Allows administrators to define access rules based on IP addresses, IP ranges, or geolocation.

- Restricts access to certain services based on time, user agent, or custom policies.

- Monitors user activity to detect suspicious patterns.

2. Device IP Blocking:

- Enables blocking of device IPs that are deemed risky or exhibit suspicious behavior.

- Provides blacklist and whitelist management for precise access control.

- Supports temporary or permanent blocking, with full logging for security audits.

3. Activity Logging:

- Records all access attempts, blocked IPs, and administrative actions.

- Provides detailed logs for auditing and analyzing security incidents.

- Helps administrators track system usage and detect abnormal behaviors.

The application leverages Django ORM for managing IPs, firewall rules, and logs, and provides an easy-to-use web admin interface for configuration and monitoring. This system helps organizations improve network security, track activities, and mitigate risks from unauthorized or potentially harmful devices.


## Installation

Install my-project with cmd

For the first step, you need to clone this repository.
```bash
git clone https://github.com/senoo12/firewall-apps.git
cd  firewall-apps
```

Install the library (install to local). 
```python
pip install -r requirements.txt
```

You can also install with Venv. First step with Venv:
```python
// windows
python -m venv venv

// macOs/Linux
python3 -m venv venv
```

Activited your Venv.
```bash
// windows
venv\Scripts\activate

// macOs/Linux
source venv/bin/activate
```

Install the library.
```bash
pip install -r requirements.txt
```

    
## Usage/Examples

Makemigrations for migrate the models.
```python
python manage.py makemigrations
```

Migrate the models.
```python
python manage.py migrate
```

Createsuperuser for the administrator, then fill up with username & password.
```python
python manage.py createsuperuser
```

Run the server.
```python
python manage.py runserver.
```

Noted: You can test this apps with requirements minimal 2 devices. 1 for the administrator, then 2 for access the local domain.

## Screenshots
Allowed Page
![WhatsApp Image 2025-12-15 at 19 38 19](https://github.com/user-attachments/assets/6d6bcbcd-4b56-4283-985b-59a59bf760bf)

Blocked Page
<img width="1600" height="681" alt="image" src="https://github.com/user-attachments/assets/7935c4c2-009f-40d4-83bb-280fd6db1d78" />

Auth Admin Page
<img width="1600" height="679" alt="image" src="https://github.com/user-attachments/assets/c025ffe1-f84b-4cf7-8815-e67b12be06c9" />

Dashboard Page
<img width="1600" height="668" alt="image" src="https://github.com/user-attachments/assets/fc7330e8-a692-4dff-b9d9-4fd952427130" />

Dashboard Logs Page
<img width="1600" height="696" alt="image" src="https://github.com/user-attachments/assets/2caaee66-3b3b-4821-9649-4e9b55ff6503" />

Dashboard Rule Page
<img width="1600" height="619" alt="image" src="https://github.com/user-attachments/assets/d40f255c-63aa-4fac-9412-be03c7d1e236" />

Dashboard Add Rule Page


## Authors

- [@senoo12](https://www.github.com/senoo12)
- [@Justme-dev-lab](https://www.github.com/Justme-dev-lab)
- [@HaikalFrds](https://www.github.com/HaikalFrds)
- [@KrisGG31](https://www.github.com/KrisGG31)
- [@hanhendra](https://www.github.com/hanhendra)
- Ivan Maulana Pramudita
- Rafi Haritsya Fajar
