# Spotify Ads Silencer

### Demo Image
![](https://github.com/stevenbuttifint/spotify-ads-silencer/blob/main/demo/window.JPG?raw=true)

---

### Table of Contents
- [Description](#description)
- [How It Works](#how-it-works)
- [What I Learned](#what-i-learned)

---

### Description

This project has been designed to improve the quality of life for people like myself using Free Spotify. It automatically mutes the Spotify application when advertisements are playing, providing a more peaceful environment.

---

### How It Works
This project has been created using Python. The Tkinter GUI toolkit has been used to create a clean front-end for the user. Here they can see the current audio state of spotify be it silenced or audible in addition to the amount of advertisements that have been silences in the current session. The back-end consists of Python Core Audio Windows Library (pycaw), and a foreign function library called "ctypes". Pycaw was used to manage the Spotify session sound while ctypes allows for windows dlls to be called.

---

### What I Learned
- How to get the current application sessions active on a Windows environment through Python.
- How to change the volume of application sessions on Windows using python.
- How to display images with transparent backgrounds in Tkinter using canvases.

[Back To The Top](#spotify-ads-silencer)
 
