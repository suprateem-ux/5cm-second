#!/usr/bin/env bash
# create_lichess_tournaments.sh
# Creates 40 Lichess team-battle tournaments (one per day), Day 1 = 2025-12-14 19:00 IST
# Requires: env var LICHESS_KEY to be set to your token

if [ -z "${LICHESS_KEY:-}" ]; then
  echo "ERROR: Please set LICHESS_KEY environment variable (your Lichess API token)."
  exit 1
fi

# Settings (from conversation)
START_DATE="2025-12-14"   # Day 1 start date (YYYY-MM-DD) at 19:00 IST
DAYS=40
CLOCK_TIME=1
CLOCK_INCREMENT=0
MINUTES_DURATION=420
RATED=true
BERSERKABLE=true
STREAKABLE=true
HASCHAT=true
BOTS_ALLOWED=false
WAIT_MINUTES=5
DESCRIPTION="Be a director of World Fronts group [APPLY HERE](https://lichess.org/forum/team-world-chess-front-official/inviting-people-for-becoming-directors-of-the-team) [NEXT BATTLE](coming up soon)\n\nDaniel Naroditsky, a renowned American chess grandmaster, commentator, and educator, passed away on October 19, 2025, at the age of 29.\n\nSo to give a Tribute to him we are organizing Naroditsky Memorial Cup\n\nFor adding your team DM [Knightzwarrior](https://lichess.org/@/KnightzWarrior)\n\nl [Hosting Team](https://lichess.org/team/world-chess-front-official) l  [Official WAF Team](https://lichess.org/team/world-antichess-front) l [Next Battle](coming up soon) l [YouTube channel](https://www.youtube.com/channel/UC27N7YKrc7NBzsqw6lNWSbQ/live)  l [Give your Suggestion](https://lichess.org/forum/team-world-antichess-front)"

# Full team list (as provided). If you want to remove or add teams, edit this array.
team_ids=(
"world-chess-960-front" "harry-potters-07-team" "harutjunyan-g-and-friends" "haryana-chess-association-hca"
"hoi-nhung-nguoi-thich-choi-co-vua" "hooshebartarchessclub" "horsey" "horsey_s" "horus-chess"
"icff-team-effort" "icff-team-two" "icon-chess-academy-rapid-tournament" "im-eric-rosen-fan-club"
"im-matvey-galchenko" "im-penguinim1-fan-club" "im-roderick-nava-chess-team" "im-satranc"
"im-yoseph-and-friends" "indian-chess-organisation" "indian-global-chess-club" "indians-chess-army"
"indicheck-_hu" "innovators-chess-academy" "international-academy-of-chess" "international-elite-chess-club"
"iran" "irina_baraeva_club" "irlzs-family" "jaza-gaming-team" "jergs-xadrez" "k2n_chess"
"ktlc-kalong-tempur-lintas-club" "la-communaute-de-julien-song" "lance5500-fan-club" "levitov-chess"
"lichess-antichess" "lichess-atomic" "lichess-chess960" "lichess-crazyhouse" "lichess-en-espanol"
"lichess-horde" "lichess-king-of-the-hill" "lichess-racing-kings" "lichess-three-check"
"lions-of-gj5--kutch-kathiyawad" "livechess" "lokiy47-fans-team" "los-amigos-de-tiwinza75"
"masthanaiah-chess-world" "mixailov_alex_team" "national-chess-blasters" "new-kci-bersatu"
"ogca-brain-gym-online-open-chess-tournament-8374153718" "oni-indonesiannationalonline" "online-chess-tournamet"
"online-dragons" "online-world-chess-lovers" "pawn-gambit" "pawn-marchers" "pawn-stars-2" "pawns-hurricane-2"
"pca-official-tournaments" "playing" "real-humans" "resourchess-team" "rochade-europa-schachzeitung"
"ronaldo-playing-chess" "royal-chess-crew" "royalpawns" "royalracer-fans" "ruchess-masters" "russian-chess-players"
"sadistic-minions" "satranc-dunyam-youtube" "satranc-medya-youtube" "satranc-tv-youtube-twitch" "shiburajc"
"sri-lanka-chess-club" "sri-lankan-chess-players" "srilankan-bulet-team" "success-academy-chess"
"super-monster-knights" "super_chess_players" "syeda-faiza-elite-chess-club" "team-armagedon-esa" "team-chessable"
"the-big-greek-aficionados" "the-chess-playing-mangoes" "the-house-discord-server" "the-mango-army" "thedarkknight_1234"
"torneos-blitz-de-5--3" "trchess" "usa" "wag-sli-17" "wim-chelsie-club" "world-antichess-front" "world-atomic-front"
"world-crazy-house-front" "world-king-of-the-hill-front" "world-racing-kings-front" "xadrez-entre-amigos-br" "xaj9uK9X"
"zamboanga-oilers-team" "--chessmaster" "--elite-chess-players-union--" "EAtFBeZ8" "SZhfGcEe" "Xltbai79"
"afghanistan-chess-network" "agadmators-team" "all-india-free-online-blitz-chess-tournament" "all-india-inter-school"
"all_for_good123" "alleppey-team" "andhra-pradesh-chess-association" "antibrainrot-mango-virus" "antichess"
"antichess-wc" "arab-world-team" "arena-catur-lipis-swiss" "austin-grandmaster-chess-academy"
"ayaangamerz23isback3-and-friends" "bangalore-chess-club" "batchess24s-club" "bengal-tiger" "berserking-outlaws"
"berserking_kings" "bharat-bullet-team" "bharat-royals" "black-dragon-chess" "brain-chess-checkmate" "bullet-chess-gamers"
"cash-prizes-for-every-week" "central-asia" "central-park-chess-academy" "chess-army-og" "chess-blasters-2"
"chess-champions-never-give-up" "chess-experts-" "chess-lover-of-ind" "chess-lovers-united" "chess-mango" "chess-talk-team"
"chess-tournamentsakatsuki-team" "chess-warriors-lead" "chess4all-gens-una-sumus" "chess_pune" "chessburgru" "chessfns"
"chesslandia" "chessmood-pro" "chessnetwork" "chessplayersquotes" "crestbook-chess-club" "csca-open-events" "cu4tG2sO"
"dark-pawn-go-for-win" "darkonclassical" "darkonrapid" "darkonswiss-dos" "darkonteams" "dma-opg" "dmv-chess-tournaments"
"endgame-kings" "english-chess-players" "enigma-team" "epnkeNQ3" "etlantis-chess-academy-dehradun-uttarakhand" "fide"
"fide-checkmate-coronavirus" "france-deutschland-group" "francophone" "friendly-chess-match" "gunman-chess-community"
"zhigalko_sergei-fan-club" "ztu46jb1"
)

# join into comma-separated list
TEAM_BATTLE_BY_TEAM=$(IFS=, ; echo "${team_ids[*]}")

# Helper: convert date YYYY-MM-DD at 19:00 IST into epoch ms (uses python for precise timezone handling)
epoch_ms_for_date() {
  PY="$1"
  python3 - <<PY
from datetime import datetime, time
from zoneinfo import ZoneInfo
d = datetime.strptime("$PY", "%Y-%m-%d")
dt = datetime.combine(d, time(19,0,0)).replace(tzinfo=ZoneInfo("Asia/Kolkata"))
print(int(dt.timestamp() * 1000))
PY
}

# create tournaments
for i in $(seq 0 $((DAYS-1))); do
  day=$((i+1))
  # compute date_for_tournament
  DATE=$(date -d "$START_DATE + $i day" +%Y-%m-%d)
  STARTS_AT_MS=$(epoch_ms_for_date "$DATE")
  NAME="DANIEL NARODITSKY MEMORIAL CUP — DAY $day"
  echo "Creating: $NAME ($DATE 19:00 IST)"
  curl https://lichess.org/api/tournament \
    --request POST \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --header "Authorization: Bearer $LICHESS_KEY" \
    --data-urlencode "name=${NAME}" \
    --data-urlencode "clockTime=${CLOCK_TIME}" \
    --data-urlencode "clockIncrement=${CLOCK_INCREMENT}" \
    --data-urlencode "minutes=${MINUTES_DURATION}" \
    --data-urlencode "startsAt=${STARTS_AT_MS}" \
    --data-urlencode "variant=standard" \
    --data-urlencode "rated=${RATED}" \
    --data-urlencode "berserkable=${BERSERKABLE}" \
    --data-urlencode "streakable=${STREAKABLE}" \
    --data-urlencode "hasChat=${HASCHAT}" \
    --data-urlencode "description=${DESCRIPTION}" \
    --data-urlencode "teamBattleByTeam=${TEAM_BATTLE_BY_TEAM}" \
    --data-urlencode "conditions.bots=${BOTS_ALLOWED}" \
    --data-urlencode "waitMinutes=${WAIT_MINUTES}" \
    --data-urlencode "conditions.accountAge=1"
done

echo "Done."
