import os
import requests

# ======= CONFIGURATION =======
JOIN_TEAM_ID = "world-chess-960-front"
LEAVE_TEAM_ID = "developers"
MESSAGE_TEAM_ID = "international-chess-talent"
MESSAGE_FILE = "d.txt"

# DM username (set it here)
DM_USERNAME = "sharanyojack"   # <- change to whoever you want to DM

# DM message file
DM_MESSAGE_FILE = "p.txt"
# ==============================


def get_token():
    token = os.getenv("LICHESS_TOKEN")
    if not token:
        raise ValueError("❌ Missing LICHESS_TOKEN environment variable")
    return token


def safe_post(url, headers, data=None):
    try:
        res = requests.post(url, headers=headers, data=data)
        if res.status_code == 200:
            print(f"✅ Success: {url}")
        else:
            print(f"❌ Failed ({res.status_code}): {url}\n{res.text}\n")
    except Exception as e:
        print(f"⚠️ Error while calling {url}: {e}\n")


# ===== DM USER DIRECT FUNCTION =====
def dm_user(username, message):
    """Send a private message to a Lichess user."""
    if not username or not message:
        print("⚠️ Username or message missing, skipping DM.")
        return

    print(f"➡️ DM’ing user: {username}")
    url = f"https://lichess.org/inbox/{username}"
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"text": message}

    safe_post(url, headers, data)
# ==================================


# ===== DM FROM p.txt =====
def dm_from_file():
    """Send a private message from p.txt."""
    if not os.path.exists(DM_MESSAGE_FILE):
        print(f"⚠️ File '{DM_MESSAGE_FILE}' not found, skipping DM.")
        return

    with open(DM_MESSAGE_FILE, "r", encoding="utf-8") as f:
        message = f.read().strip()

    if not message:
        print(f"⚠️ '{DM_MESSAGE_FILE}' is empty, skipping DM.")
        return

    print(f"➡️ DM'ing {DM_USERNAME} using message from {DM_MESSAGE_FILE}")
    dm_user(DM_USERNAME, message)
# ==========================


def join_team():
    if not JOIN_TEAM_ID:
        print("⏭️ Skipping join.")
        return

    print(f"➡️ Joining team: {JOIN_TEAM_ID}")
    url = f"https://lichess.org/team/{JOIN_TEAM_ID}/join"
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"message": "Hello, requesting to join via automation!"}
    safe_post(url, headers, data)


def leave_team():
    if not LEAVE_TEAM_ID:
        print("⏭️ Skipping leave.")
        return

    print(f"➡️ Leaving team: {LEAVE_TEAM_ID}")
    url = f"https://lichess.org/team/{LEAVE_TEAM_ID}/quit"
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    safe_post(url, headers)


def message_team():
    if not MESSAGE_TEAM_ID:
        print("⏭️ Skipping team message.")
        return

    if not os.path.exists(MESSAGE_FILE):
        print(f"⚠️ File '{MESSAGE_FILE}' not found, skipping.")
        return

    with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
        message = f.read().strip()

    if not message:
        print(f"⚠️ '{MESSAGE_FILE}' is empty, skipping.")
        return

    print(f"➡️ Messaging team: {MESSAGE_TEAM_ID}")
    url = f"https://lichess.org/team/{MESSAGE_TEAM_ID}/pm-all"
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"message": message}

    safe_post(url, headers, data)


def main():
    print("=== Lichess Team Manager ===\n")

    join_team()
    leave_team()
    message_team()

    # DM from p.txt
    dm_from_file()

    print("\n🏁 Finished all actions.")


if __name__ == "__main__":
    main()
