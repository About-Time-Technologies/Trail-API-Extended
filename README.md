# Bulk add to Trail Reservation Py Utility

> Written by Sam Lane 18/07/25  
> Version A.1

A simple Python utility to automate the UI process for adding multiple assets to a Trail.fi reservation, using the
Selenium web UI automation framework, written for the ROH.

## Environment Setup

Clone the repository
```cmd
git clone 
```

Create a dedicated automated user in Trail with the minimum required privileges for the task and ass their login details
to a `.env` file as below, located in the same directory as this project.

```dotenv
TRAIL_KEY_ID = trailkeyid
TRAIL_KEY_SECRET = trailsecret
TRAIL_BASIC_AUTH_API_TOKEN = trailapitoken
```