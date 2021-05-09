simple Python package to download torrent files from https://tt.animedia.tv/

```python
import animedia

ts = animedia.download_torrents('https://tt.animedia.tv/anime/vrata-shtajnera')
for name, data in ts:
    with open(name, "wb") as f:
        f.write(data)
```
