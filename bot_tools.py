import re

social_key = {
    'twt': 'vxtwitter',
    'ig': 'www.ddinstagram',
    'tt': 'www.vxtiktok',
    'px': 'www.phixiv'
}

def find_url_index(url, str):
    return [x.start() for x in re.finditer(url, str)]

def get_urls(msg, ind):
    urls = []
    for i in ind:
        urls.append(msg[i:].split()[0])
    return urls

def change_to_vx(domain, urls, social):
    if social == 'px': tld = 'net'
    else: tld = 'com'
        
    social = social_key[social]

    for i, url in enumerate(urls):
        urls[i] = url.replace(domain, f'https://{social}.{tld}')
    return urls

def join_urls(urls):
    link_start = '[(link)]('
    link_join = ') [(link)]('
    link_end = ')'
    final_link = link_start + link_join.join(urls) + link_end
    return final_link