# DeskAppBiblioteca
_Progetto corso Ingegneria del Software_


## Get started!

1. Clonare la repository github (un possibile comando è riportato di seguito)

    ```shell
    git clone https://github.com/MihailBobeica/DeskAppBiblioteca.git
    ```

2. Installare le librerie python necessarie per il corretto funzionamento dell'applicazione

    ```shell
    pip install -r requirements.txt
    ```

3. Una volta avviata l'applicazione (potrebbe impiegare qualche secondo), 
è possibile effettuare il login usando le seguenti credenziali

| ruolo     | username | password  |
|-----------|----------|-----------|
| admin     | S001     | admin     |
| operatore | S002     | operatore |
| utente    | S003     | utente    |
| utente    | S004     | utente    |
| utente    | S005     | utente    |

**N.B.** Essendo una demo, per motivi di comodità, il contenuto del database viene 
ricreato tramite i seeder (presenti nel file `/database/seed.py`) a ogni avvio dell'applicazione.
Se si desidera evitare tale comportamento settare la flag `RESEED_DB` (presente nel file 
`/database/__init__.py`) a `False`, (prerequisito: aver già creato le tabelle del database, 
in questo caso semplicemente aver eseguito l'applicazione almeno una volta con la flag `RESEED_DB = True`,
che è l'opzione di default).


## Preview homepage

### Homepage Guest
![Vista homepage guest](https://github.com/MihailBobeica/DeskAppBiblioteca/blob/master/img/home_guest.png)
### Homepage Utente
![Vista homepage utente](https://github.com/MihailBobeica/DeskAppBiblioteca/blob/master/img/home_utente.png)
### Homepage Operatore
![Vista homepage operatore](https://github.com/MihailBobeica/DeskAppBiblioteca/blob/master/img/home_operatore.png)
### Homepage Admin
![vista homepage admin](https://github.com/MihailBobeica/DeskAppBiblioteca/blob/master/img/home_admin.png)

