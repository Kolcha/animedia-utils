# -*- coding: utf-8 -*-

import cgi
import lxml.html
import requests


def _get_torrent_links(content):
    tree = lxml.html.fromstring(content)
    nodes = tree.xpath('//div[@class="download_tracker"]/a')
    nodes.extend(tree.xpath('//a[@class="download_tracker_btn_input"]'))
    return [n.get('href') for n in nodes if n.get('href').startswith('http')]


def _get_torrent_file_name(headers):
    value, params = cgi.parse_header(headers['Content-Disposition'])
    return params['filename']


def _download_torrent_file(link, session):
    r = session.get(link)
    filename = _get_torrent_file_name(r.headers)
    return (filename, r.content)


def download_torrents(link, session=None):
    if not session:
        session = requests.Session()
    r = session.get(link)
    if r.status_code != 200:
        return []
    torrent_links = _get_torrent_links(r.content)
    return [_download_torrent_file(t, session) for t in torrent_links]


if __name__ == '__main__':
    ts = download_torrents('https://tt.animedia.tv/anime/vrata-shtajnera')
    for t in ts:
        with open(t[0], "wb") as f:
            f.write(t[1])
