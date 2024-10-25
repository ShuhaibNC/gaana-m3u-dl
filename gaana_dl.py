#!/usr/bin/env python
# coding: utf-8

import requests
import m3u8

url = input("Paste master.m3u8 file link: ")
print("[*] Downloading m3u8 file...")
r = requests.get(url)
print("[#] Done.")

m3u8_master = m3u8.loads(r.text)
playlist_url = m3u8_master.data["playlists"][0]["uri"]
print("[!] Capturing playlist link...")
r = requests.get(playlist_url)


playlist = m3u8.loads(r.text)
video = playlist.data["segments"][0]["uri"]
print("[#] Done.")

file_name = input("[?] Enter Music File name: ")
print("\nDownloading",file_name+"...")
with open(file_name, "wb") as f:
    for segment in playlist.data["segments"]:
        url = segment["uri"]
        r = requests.get(url)
        f.write(r.content)
print("\n"+file_name,"Downloaded Successfully.")