"""Exchange a Strava authorization code for a personal activity token file."""
import argparse,getpass,json,os
from urllib.parse import urlencode,parse_qs,urlsplit
from urllib.request import Request,urlopen
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("--output",default="tokens.json");p.add_argument("--private-activities",action="store_true")
def main():
    args=p.parse_args()
    scope="activity:read_all" if args.private_activities else "activity:read"
    print("Open this link while signed into Strava:")
    print("https://www.strava.com/oauth/authorize?"+urlencode(dict(client_id=os.environ["STRAVA_CLIENT_ID"],response_type="code",redirect_uri="http://localhost",approval_prompt="force",scope=scope)))
    redirect=getpass.getpass("Paste the localhost redirect URL (hidden): ")
    code=parse_qs(urlsplit(redirect).query)["code"][0]
    body=urlencode(dict(client_id=os.environ["STRAVA_CLIENT_ID"],client_secret=os.environ["STRAVA_CLIENT_SECRET"],code=code,grant_type="authorization_code")).encode()
    with urlopen(Request("https://www.strava.com/oauth/token",data=body),timeout=12) as r:token=json.load(r)
    with os.fdopen(os.open(args.output,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600),"w") as out:json.dump({k:token[k] for k in ["access_token","refresh_token","expires_at"]},out)
    print("Saved the activity token file.")
if __name__=="__main__":main()
