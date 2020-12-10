# RaspiTempLog

Dieses Paket misst einmal pro Minute die Temperatur und Luftfeuchtigkeit und zeigt das Ergebnis in einem Diagramm an. Hierzu wird ein Raspberry Pi mit einem AM2320-Sensor und Webspace mit PHP benötigt.

## Einrichtung des Raspberry Pi

Kopiere das Skript aus dem Ordner `raspi` auf deinen Raspberry Pi (im folgenden nutze ich den Ordner `/home/pi`). Bevor du das Skript ausführen kannst, musst du zuvor das Paket `adafruit-circuitpython-am2320` mit dem Befehl
```
sudo pip3 install adafruit-circuitpython-am2320
```
installieren.

Anschließend legst du mit `crontab -e` den folgenden Cronjob an (Passwort und URL ändern nicht vergessen):

```
* * * * * /home/pi/wetter.py >> /home/pi/wetter/wetter.log
* * * * * sleep 7; tail -n 720 /home/pi/wetter/wetter.log | curl -s -F 'INSERT_PASSWORD_HERE=@-' https://domain.tld/path/to/upload.php
```

## Einrichtung des Webspace

Kopiere die Inhalte des Ordners `web` auf deinen Webspace und passe dabei das Passwort in der Datei `upload.php` an. Ist der Raspberry Pi korrekt eingerichtet, sollte man nach wenigen Minuten ein Diagramm sehen können.
