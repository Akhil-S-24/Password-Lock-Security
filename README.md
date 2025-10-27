# Password-Lock-Security
Unlock Security Alert is a desktop Flask app that protects accounts by tracking login attempts. After three failed tries it captures a webcam photo, emails the owner with the image, and logs the event in MongoDB. Easy setup with user management and secure alerting. Ideal for personal &amp; small teams.!

🔐 Unlock Security Alert

Unlock Security Alert is a desktop-based security application built using Flask, Python, HTML, CSS, and MongoDB.
It helps protect your system by monitoring login attempts and alerting the owner of unauthorized access.

🚨 Features

Tracks login attempts securely

Captures intruder photo after 3 failed password entries

Sends captured photo automatically via Gmail

Stores user data and alerts in MongoDB

Simple and clean web-based interface

⚙️ Tech Stack

Frontend: HTML, CSS

Backend: Python (Flask)

Database: MongoDB

Camera & Email: OpenCV, smtplib

🛠️ How It Works

User sets up their email and password.

On each login, the app verifies the credentials.

If the password is entered incorrectly more than 3 times:

A webcam photo is captured.

The photo is emailed to the registered address.

The attempt is logged in MongoDB.

💡 Purpose

This project enhances personal system security by instantly notifying the owner of unauthorized login attempts — useful for laptops and personal PCs.
