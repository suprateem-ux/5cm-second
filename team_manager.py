import os
import requests

# ======= CONFIGURATION =======
JOIN_TEAM_ID = "coders"        # Team to join
LEAVE_TEAM_ID = "developers"   # Team to leave
MESSAGE_TEAM_ID = "coders"     # Team to message
MESSAGE_FILE = "d.txt"         # File containing the message
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


def join_team():
    if not JOIN_TEAM_ID:
        print("⏭️ Skipping join (no JOIN_TEAM_ID set).")
        return
    print(f"➡️ Joining team: {JOIN_TEAM_ID}")
    url = f"https://lichess.org/api/team/{JOIN_TEAM_ID}/join"
    headers = {"Authorization": f"Bearer {get_token()}"}
    data = {"message": "Hello, requesting to join via automation!"}
    safe_post(url, headers, data)


def leave_team():
    if not LEAVE_TEAM_ID:
        print("⏭️ Skipping leave (no LEAVE_TEAM_ID set).")
        return
    print(f"➡️ Leaving team: {LEAVE_TEAM_ID}")
    url = f"https://lichess.org/api/team/{LEAVE_TEAM_ID}/quit"
    headers = {"Authorization": f"Bearer {get_token()}"}
    safe_post(url, headers)


def message_team():
    if not MESSAGE_TEAM_ID:
        print("⏭️ Skipping message (no MESSAGE_TEAM_ID set).")
        return
    if not os.path.exists(MESSAGE_FILE):
        print(f"⚠️ Message file '{MESSAGE_FILE}' not found, skipping message.")
        return
    with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
        message = f.read().strip()
    if not message:
        print(f"⚠️ '{MESSAGE_FILE}' is empty, skipping message.")
        return

    print(f"➡️ Sending message to all members of team: {MESSAGE_TEAM_ID}")
    url = f"https://lichess.org/api/team/{MESSAGE_TEAM_ID}/pm-all"
    headers = {"Authorization": f"Bearer {get_token()}"}
    data = {"message": message}
    safe_post(url, headers, data)


def main():
    print("=== Lichess Team Manager ===\n")
    join_team()
    leave_team()
    message_team()
    print("\n🏁 Finished all actions.")


if __name__ == "__main__":
    main()
