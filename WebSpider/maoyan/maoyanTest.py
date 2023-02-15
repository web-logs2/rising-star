import requests
from pyquery import PyQuery as pq
import csv


def get_one_page(url):
    headers = {
        'Cookie': '__mta=188567831.1663329996267.1663486691016.1663486742882.9; uuid_n_v=v1; uuid=02857A3035B811EDB51E079CF88BA11BA739195869E74AA29A1B92095254BAED; _csrf=65be8c3c321c252d1e1cbc58ed8112c58f320580c09109728481434d55b1f48f; _lxsdk_cuid=18346318c07c8-0905dfcfc4c87e-1a525635-1fa400-18346318c07c8; _lxsdk=02857A3035B811EDB51E079CF88BA11BA739195869E74AA29A1B92095254BAED; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1663329996; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1663487962; __mta=188567831.1663329996267.1663486742882.1663487961594.10; _lxsdk_s=1834f850294-5a0-a6e-b26%7C%7C57',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    return pq(requests.get(url, headers=headers).text)


def write_to_file(info):
    with open('result.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        for k, v in info.items():
            writer.writerow([f'影片名称: {k}'] + v)


def parse_one_page(html):
    info = {
        i.text().split('\n')[0].split(" ")[0]: [i.text().split('\n')[1],
                                                i.text().split('\n')[2],
                                                i.text().split('\n')[3]]
        for i in html('.movie-hover-info').items()}
    score = html('.channel-detail.channel-detail-orange').text().split(' ')
    img = [s.attr.src for s in html('.movie-hover-img').items()]
    src = [item.attr.href for item in html('.movie-item-title a').items()]
    for index, key in enumerate(info):
        [info[key].append('评分: ' + score[index])]
        [info[key].append('封面: ' + img[index])]
        [info[key].append('链接: ' + 'https://www.maoyan.com' + src[index])]
    return info


def main(offset):
    url = 'https://www.maoyan.com/films?offset=' + str(offset)
    html = get_one_page(url)
    info = parse_one_page(html)
    write_to_file(info)


if __name__ == '__main__':
    for i in range(3):
        main(offset=i * 30)
