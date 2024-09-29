
# BMI Calculator

BMI Calculator è un'applicazione desktop scritta in Python utilizzando la libreria Tkinter, che consente agli utenti di calcolare il proprio **Indice di Massa Corporea** (BMI - Body Mass Index) in base alla loro altezza e peso. L'interfaccia utente è progettata per essere intuitiva e moderna, con controlli a scorrimento e visualizzazione dinamica.

## Funzionalità

- Calcolo del BMI basato su altezza (in centimetri) e peso (in chilogrammi).
- Regolazione interattiva dell'altezza e del peso tramite slider.
- Classificazione del BMI in base alle linee guida standard (sottopeso, normale, sovrappeso, obeso).
- Interfaccia grafica moderna e user-friendly con immagini e colori personalizzati.
- Visualizzazione di suggerimenti personalizzati sulla salute in base al risultato del BMI.

## Come Funziona

1. Imposta la tua altezza tramite lo slider a sinistra o inserisci manualmente il valore nel campo "Altezza".
2. Imposta il tuo peso tramite lo slider a destra o inserisci manualmente il valore nel campo "Peso".
3. Clicca sul pulsante "View Report" per calcolare il tuo BMI.
4. Il risultato sarà mostrato nella parte inferiore, insieme a una classificazione e consigli sulla salute.

## Requisiti

- **Python 3.x**
- **Tkinter** (di solito preinstallato con Python)
- **Pillow** (per la gestione delle immagini)

Per installare Pillow, puoi eseguire:

```bash
pip install Pillow
```

## Come Eseguire

1. Clona o scarica il progetto nella tua directory locale.
2. Assicurati di avere i requisiti installati.
3. Esegui il file Python principale:

```bash
python bmi_calculator.py
```

## Struttura del Progetto

- **bmi_calculator.py**: Il file principale contenente la logica dell'applicazione e l'interfaccia grafica.
- **Sprites/**: La cartella contenente tutte le immagini utilizzate nell'applicazione, come icone e sfondi.

## Esempio di Interfaccia


<p align="center">
  

![BMI Calculator Screenshot](img/im3)
![BMI Calculator Screenshot](img/im2)
![BMI Calculator Screenshot](img/im3)

<img src="img/im1.png" alt="Image 1" width="250" style="margin-right: 10px;">
  <img src="img/im2.png" alt="Image 2" width="250" style="margin-right: 10px;">
  <img src="img/im3.png" alt="Image 3" width="250">
</p>
