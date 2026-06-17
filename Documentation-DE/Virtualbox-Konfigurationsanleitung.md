Betriebssystem:
- Linux Ubuntu Server 26.04

Voraussetzungen:
- ISO -> Ubuntu Server 26.04
- Virtual Box 7.2.8

# VM Setup
Unter Virtual Box eine neue VM erstellen:

## VM Setup VBOX
### Name und Betriebssystem der Virtuellen Maschine
	VM-Name: Linux-Server
	VM-Ordner: "Auswählen des VM Ordners"
	ISO-Abbild: "ISO Datei auswählen"
	
	"Mit unbeaufsichtigter Installation fortfahren": false
	
	Betriebssystem: Linux
	Bestriebssystem-Distribution: Ubuntu
	Betriebssystem-Version: Ubuntu 25.04 (Plucky Puffin) (64-bit)
	

### Einrichtung der unbeaufsichtigten Installation des Gastbetriebssystems
Überspringen

### Virtuelle Hardware angeben
	Hauptspeicher: 4096 MB (Frei wählbar nach System)
	Anzahl der CPUs: 4 CPUs (Frei wählbar nach System)
	"EFI verwenden": false

### Virtuelle Festplatte angeben
Eine neue Festplatte erstellen:

	Plattenabbild-Ort und -Größe:
	- Ort auf der Festplatte Standard belassen
	- Größe bei 25 GB belassen
	
	Dateityp und Variante der Festplatte:
	Auf VDI belassen und Standard einstellungen beibehalten

Nun kann auf Fertigstellen geklickt werden.

## VM Starten

1. "Try or Install Ubuntu Server" auswählen
2. Warten bis der Setup Wizard beginnt.
### Setup 
	Sprache auswählen: 
		"Englisch" -> Enter
	
	Keyboard configuration:
		"German" -> Done
	
	Choose installation:
		Ubuntu Server -> Done
	
	Network configuration:
		Done
	
	Proxy configuration:
		Done
	
	Ubuntu archive mirror configuration:
		Warten auf "Mirror location passed tests" -> Done
	
	Guided storage configuration:
		Use an entire disk -> Anhaken
		Set up this disk as LVM group -> Anhaken
		Done
	
	Storage configuration:
		Done
		"Confirm destructive action" -> Continue
	
	Profile configuration:
		Your name: nils (Eigener Name)
		Your servers name: srv01
		Pick a username: nils (Eigener Name)
		Choose a password: Schule123!
		Done
	
	Upgrade to Ubuntu Pro:
		Skip for now -> Anhaken
		Continue
	
	SSH configuration:
		Install OpenSSH server -> Anhaken
		Done
	
	Featured server snaps:
		Done
	
	Installation:
		Reboot Now

## Fortfahren mit Installationsanleitung.md
