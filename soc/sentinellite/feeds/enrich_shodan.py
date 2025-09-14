# feeds/enrich_shodan.py
import os, time, requests
from dotenv import load_dotenv

load_dotenv()
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
SHODAN_HOST_URL = "https://api.shodan.io/shodan/host/{ip}"

def shodan_enabled():
    return bool(SHODAN_API_KEY)

def enrich_ip_with_shodan(ip: str):
    """
    Returns a dict with selected Shodan fields or {"error": "..."} on failure.
    Rate-limit politely to avoid 429s.
    """
    if not SHODAN_API_KEY:
        return {"error": "SHODAN_API_KEY not set"}
    try:
        resp = requests.get(
            SHODAN_HOST_URL.format(ip=ip),
            params={"key": SHODAN_API_KEY},
            timeout=20,
        )
        if resp.status_code == 404:
            return {"not_found": True}
        resp.raise_for_status()
        data = resp.json()
        # normalize a few high-value fields
        return {
            "ip": data.get("ip_str") or ip,
            "org": data.get("org"),
            "isp": data.get("isp"),
            "last_update": data.get("last_update"),
            "ports": data.get("ports") or [],
            "tags": data.get("tags") or [],
            "hostnames": data.get("hostnames") or [],
            "vulns": sorted(list((data.get("vulns") or {}).keys())),
            "raw": data,  # keep raw for later pivoting
        }
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code} from Shodan"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        time.sleep(0.5)  # be polite to the API
