**Sollte noch kein Server über eine VM bestehen gibt es z.B. eine Konfigurationsanleitung für Virtualbox unter ./Virtualbox-Konfigurationsanleitung.md**

# Installationsanleitung

## Netzwerk konfiguration
    sudo nano /etc/netplan/00-installer-config.yaml

Die Datei sollte folgende Basis konfiguration beinhalten:
```
network:
    version: 2
    ethernets:
        YOUR_INTERFACE_NAME:
            dhcp4: no
            dhcp6: no
            addresses:
                - 192.168.178.100/24
            routes:
                - to: default
                  via: 192.168.178.1
            nameservers:
                addresses:
                    - 192.168.178.1  
```

**Bei der IP Adresse vorher schauen, ob diese bereits vergeben ist. Wenn ja eine andere Freie verwenden.**

Mit folgenden befehl dann die Konfiguration anwenden:
    sudo netplan apply

Mit `ip a` kann man die Konfiguration überprüfen.
Mit `ping 8.8.8.8` kann man die erreichbarkeit ins "Internet" / google DNS testen.

## Neuen Benutzer anlegen

Benutzer ohne Sudo-Rechten anlegen:
```
sudo adduser willi
    passwort: Schule123!
    Alles andere Optional im Dialog
```

Benutzer mit Sudo-Rechten anlegen:
```
sudo adduser fernzugriff
    passwort: Schule123!
    Alles andere Optional im Dialog
sudo usermod -aG sudo fernzugriff
```

## SSH Konfiguration
SSH Server wurde bereits mit der Server installation installiert.

Folgenden Befehl ausführen:
`sudo nano /etc/ssh/sshd_config`

Einstellungen in der Datei:
```
    #PermitRootLogin prohibit-password -> PermitRootLogin no
    #PasswordAuthentication yes -> PasswordAuthentication yes
    AllowUsers fernzugriff
```

Das AllowUsers muss hinzugefügt werden, dass man sich nur über den fernzugriff user per ssh anmelden kann.

Nun kann man sich mit dem fernzugriff User über SSH verbinden.
Hierzu einfach in der CMD `ssh fernzugriff@ipadresse` eingeben, dann nur noch das Passwort und man ist mit dem User fernzugriff auf dem Server eingeloggt.

## Docker Installieren
Docker mit folgenden befehl installieren:
`sudo apt install docker.io`

Docker als Service mit folgenden befehl starten:
`sudo systemctl start docker.service`

Docker auf funktion testen mit folgenden Befehl:
`sudo docker run hello-world`

## Setup
Programm auf den Server laden:
`git clone https://github.com/VenusKomet/YATLAPPP.git`

In den Ordner wechseln
`cd YATLAPPP/backend/`

Docker Image für einen Container erstellen: `sudo docker image build -t webapi .`
Docker Container starten: `sudo docker run -p 5000:5000 -d webapi`

Testen ob der Docker Container läuft:
`sudo docker ps`

Aufrufen der URL: `http://<serverip>:5000/todo-list`