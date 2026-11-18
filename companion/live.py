"""Read the newest Strava activity, keeping rotated refresh tokens on the host."""
import json, os, time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from serve import page

def reading(o, memory):
    token_file = Path(o["token_file"]).expanduser()
    token = json.loads(token_file.read_text())
    if token.get("expires_at", 0) < time.time() + 90:
        body = urlencode(dict(client_id=os.environ["STRAVA_CLIENT_ID"],
            client_secret=os.environ["STRAVA_CLIENT_SECRET"], grant_type="refresh_token",
            refresh_token=token["refresh_token"])).encode()
        with urlopen(Request("https://www.strava.com/oauth/token", data=body), timeout=12) as r:
            rotated = json.load(r)
        temp = token_file.with_suffix(".rotating")
        with os.fdopen(os.open(temp, os.O_CREAT|os.O_TRUNC|os.O_WRONLY, 0o600), "w") as out:
            json.dump(rotated, out)
        temp.replace(token_file)
        token = rotated
    request = Request("https://www.strava.com/api/v3/athlete/activities?per_page=1",
                      headers={"Authorization":"Bearer "+token["access_token"]})
    with urlopen(request, timeout=12) as r:
        rows = json.load(r)
    if not rows:
        return dict(state="No visible activities",key="empty",pages=[page("KUDOS","No activity","Check activity read access")])
    a=rows[0]; count=int(a["kudos_count"])
    return dict(state="Latest Strava activity",key=f'{a["id"]}/{count}',pages=[
        page("KUDOS",count,a["name"],a["sport_type"],a["start_date_local"][:10]),
        page("ACTIVITY",a["sport_type"],a["name"],f'{a.get("distance",0)/1000:.2f} km')])
