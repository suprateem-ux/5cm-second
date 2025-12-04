import os
import requests

DM_USERNAME = "Unstoppable_2011""       # <- change this
DM_MESSAGE_FILE = "p.txt"        # message stored here


def get_token():
    token = os.getenv("LICHESS_TOKEN")
    if not token:
        raise ValueError("Missing LICHESS_TOKEN environment variable")
    return token


def dm_user(username, message):
    url = f"https://lichess.org/inbox/{username}"
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"text": message}

    res = requests.post(url, headers=headers, data=data)
    if res.status_code == 200:
        print("DM sent successfully")
    else:
        print(f"Failed ({res.status_code}): {res.text}")


def main():
    if not os.path.exists(DM_MESSAGE_FILE):
        print(f"{DM_MESSAGE_FILE} not found.")
        return

    with open(DM_MESSAGE_FILE, "r", encoding="utf-8") as f:
        message = f.read().strip()

    if not message:
        print("Message file empty.")
        return

    print(f"Sending DM to {DM_USERNAME}…")
    dm_user(DM_USERNAME, message)


if __name__ == "__main__":
    main()
