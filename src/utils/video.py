from urllib.parse import urlparse, parse_qs

def obtener_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]

    if "shorts" in url:
        return url.split("/")[-1].split("?")[0]

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if "v" in query_params:
        return query_params["v"][0]
    
    return None
