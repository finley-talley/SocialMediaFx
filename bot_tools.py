import re

social_key = {
    'twt': 'fxtwitter',
    'ig': 'www.ddinstagram',
    'tt': 'www.vxtiktok',
    'px': 'www.phixiv'
}

def find_url_index(url, str):
    return [x.start() for x in re.finditer(url, str)]

def get_urls(msg, ind):
    urls = []
    for i in ind:
        cur_link = msg[i:].split()[0]
        cl_len = len(cur_link)
        prev_char = msg[i-1]
        last_char = cur_link[cl_len-1]
        # suppress manually hidden preview links
        if not (i != 0 and prev_char == '<' and last_char == '>'):
            urls.append(cur_link)
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