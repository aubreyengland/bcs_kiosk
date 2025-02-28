# Contact Kiosk Web App

A **Flask-based SIP contact directory** that runs inside a **Docker container**, designed to be connected to a **Cisco Desk Pro running kiosk mode**.

## Features
 **Dynamic Contact Directory** – Displays contacts grouped by category  
 **SIP Calling** – Click to call contacts using `sip:` links  
 **Dark Mode UI** – Clean and professional design  
 **Runs in Docker** – Easily deployable via **Docker Compose**  
 **Webex Desk Pro Compatible** – Can be accessed from Desk Pro's **WebEngine**  

---

## 1. Getting Started

### Prerequisites
- **Python 3.12+**
- **Docker & Docker Compose**
- **Cisco Desk Pro (Web Engine Enabled)**

### Clone the Repository
```sh
git clone https://github.com/aubreyengland/contact-kiosk.git
cd contact-kiosk