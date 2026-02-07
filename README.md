# Bulk add to Trail Reservation Py Utility

> Written by Sam Lane 18/07/25  
> Version A.1

A simple Python utility to automate the bulk modification of assets in a Trail.fi database

## Environment Setup

Clone the repository
```cmd
git clone https://github.com/About-Time-Technologies/Trail-API-Extended
```

Create a api key in Trail with the minimum required privileges for the task and copy the details of the key
to a `.env` file as below, located in the same directory as this project.

```dotenv
TRAIL_KEY_ID = trailkeyid
TRAIL_KEY_SECRET = trailsecret
TRAIL_BASIC_AUTH_API_TOKEN = trailapitoken
```

## Using the utility

- Install all required modules:

```cmd
pip install -r requirements.txt 
```

- Define a list of asset ids in a `.CSV` file that you want to add to the reservation


- Run the script

## Commands

- all commands make use of `-target` to define the asset id (or CSV file containing asset ids)
- add `-h` to a command to access the help

### Change Department

Change the department of one or more assets.

```cmd
python trail-api-extended.py change-department -target sample.csv --department "Warehouse"
```

Or for a single asset:

```cmd
python trail-api-extended.py change-department -target I100115 --department "Sound Department"
```

#### Command Line Switches

- `--department` (Required) Target department name. Always enclose in "" if the department name contains spaces.

### Delete

  ```cmd
  python trail-api-extended.py delete -target sample.csv --reason redundant --description "Removed from FOH"
  ```

#### Command Line Switches

- `--reason` Reason for deletion e.g.; redundant
- `--description` The reason for the deletion. Always enclose in "" e.g.; "Removed from stores"
- `--force` If this switch is used then the utility will not ask the user to confirm the item before deletion.
- `--permanent` Permanently deletes the item. Use with caution.