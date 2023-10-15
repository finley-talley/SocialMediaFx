import re

social_key = {
    'twt': 'vxtwitter',
    'ig': 'www.ddinstagram',
    'tt': 'www.vxtiktok'
}

def find_url_index(url, str):
    return [x.start() for x in re.finditer(url, str)]

def get_urls(msg, ind):
    urls = []
    for i in ind:
        urls.append(msg[i:].split()[0])
    return urls

def change_to_vx(domain, urls, social):
    social = social_key[social]
    for i, url in enumerate(urls):
        urls[i] = url.replace(domain, f'https://{social}.com')
    print(f'urls:\t{urls}')
    return urls