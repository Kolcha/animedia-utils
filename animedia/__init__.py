import cgi
import lxml.html
import re
import requests

_link_re = re.compile(r"^https?:\/\/tt\.animedia\.tv\/anime\/[\w-]+\/?$")


def match_link(link: str) -> bool:
    return _link_re.match(link) is not None


def _get_torrent_links(content: bytes) -> list[str]:
    tree = lxml.html.fromstring(content)
    nodes = tree.xpath('//div[@class="download_tracker"]/a')
    nodes.extend(tree.xpath('//a[@class="download_tracker_btn_input"]'))
    return [n.get('href') for n in nodes if n.get('href').startswith('http')]


def _get_torrent_file_name(headers: dict[str, str]) -> str:
    _, params = cgi.parse_header(headers['Content-Disposition'])
    return params['filename'].encode('latin1').decode('utf-8')


def _download_torrent_file(link: str, session: requests.Session) -> tuple[str, bytes]:
    r = session.get(link)
    filename = _get_torrent_file_name(r.headers)
    return (filename, r.content)


def download_torrents(link: str, session: requests.Session = None) -> list[tuple[str, bytes]]:
    if not session:
        session = requests.Session()
    r = session.get(link)
    if r.status_code != 200:
        return []
    torrent_links = _get_torrent_links(r.content)
    return [_download_torrent_file(t, session) for t in torrent_links]
