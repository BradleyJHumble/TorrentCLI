import libtorrent as lt
import time
import sys

def download_torrent(magnet_link):
    ses = lt.session()
    
    # Add torrent
    info = lt.parse_magnet_uri(magnet_link)
    h = ses.add_torrent({"ti": lt.torrent_info(info), "save_path": "./"})
    
    print("Downloading", h.name())
    
    while not h.is_seed():
        s = h.status()
        
        print(f"Seeders: {s.num_seeds}, Downloaded: {s.total_done} bytes, Progress: {s.progress:.2%}, Download rate: {s.download_rate}, ETA: {s.eta} s")
        
        time.sleep(30)

    print("Download complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python torrent_downloader.py '<magnet_link>'")
    else:
        magnet_link = sys.argv[1]
        download_torrent(magnet_link)
