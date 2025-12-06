import os
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

TOKEN = os.environ["LICHESS_TOKEN"]

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/x-www-form-urlencoded"
}


# ---------------------------------------------------
# TEAMS LIST (same as your bash script)
# ---------------------------------------------------
team_ids = [
    "world-chess-960-front", "harry-potters-07-team", "harutjunyan-g-and-friends",
    "haryana-chess-association-hca", "hoi-nhung-nguoi-thich-choi-co-vua",
    "hooshebartarchessclub", "horsey", "horsey_s", "horus-chess",
    "icff-team-effort", "icff-team-two", "icon-chess-academy-rapid-tournament",
    "im-eric-rosen-fan-club", "im-matvey-galchenko", "im-penguinim1-fan-club",
    "im-roderick-nava-chess-team", "im-satranc", "im-yoseph-and-friends",
    "indian-chess-organisation", "indian-global-chess-club", "indians-chess-army",
    "indicheck-_hu", "innovators-chess-academy", "international-academy-of-chess",
    "international-elite-chess-club", "iran", "irina_baraeva_club", "irlzs-family",
    "jaza-gaming-team", "jergs-xadrez", "k2n_chess", "ktlc-kalong-tempur-lintas-club",
    "la-communaute-de-julien-song", "lance5500-fan-club", "levitov-chess",
    "lichess-antichess", "lichess-atomic", "lichess-chess960", "lichess-crazyhouse",
    "lichess-en-espanol", "lichess-horde", "lichess-king-of-the-hill",
    "lichess-racing-kings", "lichess-three-check", "lions-of-gj5--kutch-kathiyawad",
    "livechess", "lokiy47-fans-team", "los-amigos-de-tiwinza75",
    "masthanaiah-chess-world", "mixailov_alex_team", "national-chess-blasters",
    "new-kci-bersatu", "ogca-brain-gym-online-open-chess-tournament-8374153718",
    "oni-indonesiannationalonline", "online-chess-tournamet", "online-dragons",
    "online-world-chess-lovers", "pawn-gambit", "pawn-marchers", "pawn-stars-2",
    "pawns-hurricane-2", "pca-official-tournaments", "playing", "real-humans",
    "resourchess-team", "rochade-europa-schachzeitung", "ronaldo-playing-chess",
    "royal-chess-crew", "royalpawns", "royalracer-fans", "ruchess-masters",
    "russian-chess-players", "sadistic-minions", "satranc-dunyam-youtube",
    "satranc-medya-youtube", "satranc-tv-youtube-twitch", "shiburajc",
    "sri-lanka-chess-club", "sri-lankan-chess-players", "srilankan-bulet-team",
    "success-academy-chess", "super-monster-knights", "super_chess_players",
    "syeda-faiza-elite-chess-club", "team-armagedon-esa", "team-chessable",
    "the-big-greek-aficionados", "the-chess-playing-mangoes",
    "the-house-discord-server", "the-mango-army", "thedarkknight_1234",
    "torneos-blitz-de-5--3", "trchess", "usa", "wag-sli-17", "wim-chelsie-club",
    "world-antichess-front", "world-atomic-front", "world-crazy-house-front",
    "world-king-of-the-hill-front", "world-racing-kings-front",
    "xadrez-entre-amigos-br", "xaj9uK9X", "zamboanga-oilers-team", "--chessmaster",
    "--elite-chess-players-union--", "EAtFBeZ8", "SZhfGcEe", "Xltbai79",
    "afghanistan-chess-network", "agadmators-team",
    "all-india-free-online-blitz-chess-tournament", "all-india-inter-school",
    "all_for_good123", "alleppey-team", "andhra-pradesh-chess-association",
    "antibrainrot-mango-virus", "antichess", "antichess-wc", "arab-world-team",
    "arena-catur-lipis-swiss", "austin-grandmaster-chess-academy",
    "ayaangamerz23isback3-and-friends", "bangalore-chess-club", "batchess24s-club",
    "bengal-tiger", "berserking-outlaws", "berserking_kings", "bharat-bullet-team",
    "bharat-royals", "black-dragon-chess", "brain-chess-checkmate",
    "bullet-chess-gamers", "cash-prizes-for-every-week", "central-asia",
    "central-park-chess-academy", "chess-army-og", "chess-blasters-2",
    "chess-champions-never-give-up", "chess-experts-", "chess-lover-of-ind",
    "chess-lovers-united", "chess-mango", "chess-talk-team",
    "chess-tournamentsakatsuki-team", "chess-warriors-lead", "chess4all-gens-una-sumus",
    "chess_pune", "chessburgru", "chessfns", "chesslandia", "chessmood-pro",
    "chessnetwork", "chessplayersquotes", "crestbook-chess-club", "csca-open-events",
    "cu4tG2sO", "dark-pawn-go-for-win", "darkonclassical", "darkonrapid",
    "darkonswiss-dos", "darkonteams", "dma-opg", "dmv-chess-tournaments",
    "endgame-kings", "english-chess-players", "enigma-team", "epnkeNQ3",
    "etlantis-chess-academy-dehradun-uttarakhand", "fide",
    "fide-checkmate-coronavirus", "france-deutschland-group", "francophone",
    "friendly-chess-match", "gunman-chess-community", "zhigalko_sergei-fan-club",
    "ztu46jb1"
]

TEAMS_STRING = ",".join(team_ids)


# ---------------------------------------------------
# DESCRIPTION
# ---------------------------------------------------
DESCRIPTION = (
    "Be a director of World Fronts group [APPLY HERE](https://lichess.org/forum/team-world-chess-front-official/"
    "inviting-people-for-becoming-directors-of-the-team)\n[NEXT BATTLE](coming up soon)\n\n"
    "Daniel Naroditsky, a renowned American chess grandmaster, commentator, and educator, "
    "passed away on October 19, 2025, at the age of 29.\n\n"
    "So to give a Tribute to him we are organizing Naroditsky Memorial Cup\n\n"
    "For adding your team DM [Knightzwarrior](https://lichess.org/@/KnightzWarrior)\n\n"
    "l [Hosting Team](https://lichess.org/team/world-chess-front-official) l "
    "[Official WAF Team](https://lichess.org/team/world-antichess-front) l "
    "[Next Battle](coming up soon) l "
    "[YouTube channel](https://www.youtube.com/channel/UC27N7YKrc7NBzsqw6lNWSbQ/live)  l "
    "[Give your Suggestion](https://lichess.org/forum/team-world-antichess-front)"
)


# ---------------------------------------------------
# CREATE & UPDATE
# ---------------------------------------------------
START = datetime(2025, 12, 14, tzinfo=ZoneInfo("Asia/Kolkata"))

def create_and_update(day_index):
    dt = START + timedelta(days=day_index)
    starts_at_ms = int(dt.replace(hour=19, minute=0).timestamp() * 1000)

    name = f"Naroditsky Memorial Cup Day {day_index+1}"

    # STEP A — create tournament (only host team)
    data_create = {
        "name": name,
        "clockTime": 2,
        "clockIncrement": 0,
        "minutes": 420,
        "variant": "standard",
        "rated": "true",
        "berserkable": "true",
        "streakable": "true",
        "hasChat": "true",
        "startsAt": starts_at_ms,
        "description": DESCRIPTION,
        "waitMinutes": 5,
        "conditions.accountAge": 1,

        # only ONE host team allowed:
        "teamBattleByTeam": "world-chess-front-official",
    }

    r = requests.post(
        "https://lichess.org/api/tournament",
        headers=headers,
        data=data_create
    )

    print(name, r.status_code)
    print(r.text)

    if r.status_code != 200:
        return

    tournament_id = r.json()["id"]

    # STEP B — add all teams + 15 leaders
    data_update = {
        "teams": TEAMS_STRING,
        "nbLeaders": 15
    }

    r2 = requests.post(
        f"https://lichess.org/api/tournament/team-battle/{tournament_id}",
        headers=headers,
        data=data_update
    )

    print("Update teams:", r2.status_code)
    print(r2.text)
    print("---------------")


for i in range(40):
    create_and_update(i)
