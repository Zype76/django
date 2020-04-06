import requests


def run_query(request):
    # Create our results list which we'll populate.
    url = 'https://api.jikan.moe/v3/search/anime?q={}&limit=16'.format(request)

    r = requests.get(url)
    #Needs a dictionary
    json_response = r.json()
    results = json_response['results'] 
    return results
