# excel_handler.py

import pandas as pd
import os
import logging
from datetime import datetime
from pathlib import Path

# IMPORTIAMO GLI ALBERI DELLE DOMANDE PER POTER COSTRUIRE L'ELENCO COMPLETO DELLE COLONNE
from Questionario import question_tree_10_plus, question_tree_3_9, preliminary_questions

# =============================================================================
# GESTORE PER IL SALVATAGGIO DELLE RISPOSTE SU FILE EXCEL
# QUESTA VERSIONE È COMPLETA E FUNZIONANTE
# =============================================================================

logger = logging.getLogger(__name__)

# DEFINIAMO IL PERCORSO DEL FILE EXCEL SUL DESKTOP
# CREA UNA CARTELLA "report_istat" SUL DESKTOP SE NON ESISTE
DESKTOP_PATH = Path.home() / "Desktop" / "report_istat"
os.makedirs(DESKTOP_PATH, exist_ok=True)
EXCEL_FILE_PATH = DESKTOP_PATH / "report_questionario_imprese.xlsx"


def get_all_question_ids():
    """
    CREA UNA LISTA ORDINATA DI TUTTI GLI ID DI DOMANDA POSSIBILI
    DA ENTRAMBI I QUESTIONARI, PER GARANTIRE CHE LE COLONNE IN EXCEL
    SIANO SEMPRE NELLO STESSO ORDINE.
    """
    # ESTRAE GLI ID DALLE DOMANDE PRELIMINARI E DAI DUE ALBERI
    preliminary_ids = [q['id'] for q in preliminary_questions]
    ids_10_plus = [q['id'] for q in question_tree_10_plus]
    ids_3_9 = [q['id'] for q in question_tree_3_9]
    
    # UNISCE TUTTI GLI ID E RIMUOVE I DUPLICATI MANTENENDO L'ORDINE
    all_ids = list(dict.fromkeys(preliminary_ids + ids_10_plus + ids_3_9))
    
    return all_ids


# LISTA COMPLETA E ORDINATA DELLE COLONNE PER IL NOSTRO FILE EXCEL
ALL_COLUMN_HEADERS = get_all_question_ids()


def save_user_responses(user_id, state):
    """
    SALVA LE RISPOSTE DI UN UTENTE IN UN FILE EXCEL.
    - Se il file non esiste, lo crea.
    - Se il file esiste, aggiunge una nuova riga o aggiorna quella esistente.
    """
    try:
        logger.info(f"Avvio salvataggio risposte per l'utente {user_id} su file Excel.")
        
        # 1. PREPARA LA NUOVA RIGA CON I DATI DELL'UTENTE
        #    Il dizionario 'user_data' conterrà le intestazioni di colonna e i valori.
        user_data = {
            "UserID": user_id,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Lingua": state.get("lang", "N/D"),
            "TipoQuestionario": state.get("questionnaire_type", "N/D"),
        }
        
        # Aggiunge le risposte dell'utente al dizionario
        user_data.update(state.get("responses", {}))

        # Crea un DataFrame pandas con i dati dell'utente (sarà una singola riga)
        new_row_df = pd.DataFrame([user_data])
        new_row_df.set_index("UserID", inplace=True)

        # 2. LEGGI IL FILE EXCEL ESISTENTE O CREANE UNO NUOVO
        if EXCEL_FILE_PATH.exists():
            # Legge il file esistente, usando 'UserID' come indice delle righe
            df_existing = pd.read_excel(EXCEL_FILE_PATH, index_col="UserID")
            
            # Se l'utente ha già compilato il questionario, rimuoviamo la sua vecchia riga
            if user_id in df_existing.index:
                df_existing.drop(user_id, inplace=True)
                logger.info(f"Utente {user_id} già presente. La sua vecchia riga verrà sovrascritta.")
            
            # Unisce il vecchio DataFrame con la nuova riga
            df_final = pd.concat([df_existing, new_row_df])
        else:
            # Se il file non esiste, il nostro DataFrame finale è semplicemente la nuova riga
            df_final = new_row_df
            logger.info(f"File Excel non trovato. Verrà creato un nuovo file: {EXCEL_FILE_PATH}")

        # 3. ORDINA E FORMATTA LE COLONNE
        #    Garantisce che le colonne siano sempre nello stesso ordine, anche se un utente
        #    non ha risposto a tutte le domande.
        
        # Crea una lista di colonne di base più tutte le possibili domande
        final_columns_order = ["Timestamp", "Lingua", "TipoQuestionario"] + ALL_COLUMN_HEADERS
        
        # Riordina il DataFrame. Le colonne mancanti verranno create e riempite con NaN (vuoto).
        df_final = df_final.reindex(columns=final_columns_order)
        
        # 4. SALVA IL DATAFRAME SU FILE EXCEL
        #    'index=True' salva la colonna 'UserID'
        df_final.to_excel(EXCEL_FILE_PATH, index=True)
        
        logger.info(f"Risposte per l'utente {user_id} salvate con successo in {EXCEL_FILE_PATH}")

    except Exception as e:
        logger.error(f"ERRORE CRITICO durante il salvataggio su Excel per l'utente {user_id}: {e}", exc_info=True)