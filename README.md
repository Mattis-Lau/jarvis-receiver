# JARVIS Cast Receiver

Application ID: `8B0C0E45`  
Receiver URL: `https://mattis-lau.github.io/jarvis-receiver/`  
Custom Namespace: `urn:x-cast:com.jarvis.receiver`

## GitHub Pages

1. `index.html` in das Repository `Mattis-Lau/jarvis-receiver` hochladen.
2. GitHub → **Settings → Pages**
3. Source: **Deploy from a branch**
4. Branch: **main**
5. Folder: **/(root)**
6. Save
7. Danach prüfen, ob diese URL im Browser funktioniert:

   https://mattis-lau.github.io/jarvis-receiver/

## Google Cast Developer Console

Receiver Application URL:

https://mattis-lau.github.io/jarvis-receiver/

Application ID:

8B0C0E45

## Test

Nach Veröffentlichung/Registrierung des Test-Chromecasts:

```powershell
python receiver_test.py
```

Der Fernseher sollte eine JARVIS-Rezeptauswahl mit vier Karten anzeigen.
