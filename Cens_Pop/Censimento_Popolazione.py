#---------------- importazione dei pacchetti ----------------------
import logging
import os
import asyncio
import pandas as pd
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes) 
from pathlib import Path
from datetime import datetime
import unicodedata
from sentence_transformers import SentenceTransformer, util 


# --------------------- modello per similarità semantica -------------
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
# --------------------------------------------------------------------


#-------------------- Configurazione del logging -----------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


#----------------- Token del bot telegram ------------------------
BOT_TOKEN = "7913278624:AAHYXMoqvmrZ236DzYT3DOAlsYGxpV6b5Lw"


#-----------   Dizionari per le varianti di lingua e risposte booleane (si,no,aiuto,stop) ------------
LANG_VARIANTS = {
    "it": ["italiano", "italian", "ita", "it", "IT"],
    "en": ["english", "eng", "en", "EN", "gb", "UK", "inglese"]
}
YES_VARIANTS = {
    "it": ["sì", "si", "yes", "ok", "okay", "certo", "va bene", "procedo", "iniziamo", 
           "continua", "prosegui", "certamente", "vai", "sicuro", "altroche", "altrochè", 
           "altroché", "di sicuro", "senza dubbio", "ovvio", "ovviamente"],
    "en": ["yes", "y", "ok", "okay", "sure", "go ahead", "proceed", "start", "continue", 
           "alright"]
}
NO_VARIANTS = {
    "it": ["no", "n", "no grazie", "basta", "ferma", "annulla", "stop", "fine", "non voglio"],
    "en": ["no", "n", "no thanks", "enough", "stop", "cancel", "quit", "end", "don't want", 
           "not now"]
}
HELP_VARIANTS = {
    "it": ["aiuto", "help", "spiegazione", "esempio", "come devo rispondere", "cosa devo fare"],
    "en": ["help", "aiuto", "explanation", "example", "how should I answer", "what should I do"]
}
INTENT_VOCABS = {
    "yes": YES_VARIANTS["it"] + YES_VARIANTS["en"],
    "no":  NO_VARIANTS["it"] + NO_VARIANTS["en"],
    "help": HELP_VARIANTS["it"] + HELP_VARIANTS["en"],
    "stop": ["stop", "fine", "basta", "cancel", "quit", "end"]
}

def normalize(text: str) -> str:
    """minuscole + trim + rimozione accenti"""
    text = unicodedata.normalize("NFD", text.strip().lower())
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")


#-------------------- normalizza una volta tutte le varianti per l'analisi della similarità
for d in (YES_VARIANTS, NO_VARIANTS, HELP_VARIANTS):
    for k, lst in d.items():
        d[k] = [normalize(x) for x in lst]
INTENT_VOCABS = {k: [normalize(x) for x in v] for k, v in INTENT_VOCABS.items()}

def guess_intent_semantic(user_input: str,
                          vocabularies: dict[str, list[str]],
                          threshold: float = 0.6) -> str | None:
    """Ritorna l'intent migliore (yes/no/help/stop) se la similarità supera threshold."""
    inp_emb = model.encode(user_input, convert_to_tensor=True)
    best_intent, best_score = None, 0.0
    for intent, phrases in vocabularies.items():
        for ph in phrases:
            sim = util.pytorch_cos_sim(inp_emb, model.encode(ph, convert_to_tensor=True)).item()
            if sim > best_score:
                best_intent, best_score = intent, sim
    return best_intent if best_score >= threshold else None

def update_vocab_if_similar(user_input: str,
                            vocabularies: dict[str, list[str]],
                            threshold: float = 0.6) -> str | None:
    """Aggiorna il vocabolario se la frase è simile a un intento."""
    intent = guess_intent_semantic(user_input, vocabularies, threshold)
    if intent and user_input not in vocabularies[intent]:
        vocabularies[intent].append(user_input)
        logger.info(f"Nuova espressione '{user_input}' → '{intent}' (auto‑learn)")
    return intent


#-------------------------------------- Spiegazioni per ogni domanda
HELP_EXPLANATIONS = {
    "LANG_SELECT": {
        "it": "Seleziona la lingua in cui desideri compilare il questionario. Rispondi con 'italiano' o 'english'.\nEsempio: 'italiano'",
        "en": "Select the language you prefer for the questionnaire. Reply with 'italian' or 'english'.\nExample: 'english'"
    },
    "INTRO": {
        "it": "Per iniziare il questionario ISTAT rispondi con 'si'. Questo è l'avvio della raccolta dati obbligatoria.\nEsempio: 'si'",
        "en": "To start the ISTAT questionnaire reply with 'yes'. This is the beginning of the mandatory data collection.\nExample: 'yes'"
    },
    "INFORMATIVA": {
        "it": "Ti stiamo informando che questa rilevazione è obbligatoria per legge e i tuoi dati saranno trattati in modo riservato. Rispondi 'si' per continuare.\nEsempio: 'si'",
        "en": "We inform you that this survey is mandatory by law and your data will be treated confidentially. Reply 'yes' to continue.\nExample: 'yes'"
    },
    "FAMIGLIA_LISTA": {
        "it": "Elenca tutti i componenti della tua famiglia attraverso i loro codici fiscali.",
        "en": "List all family members by their tax codes."
    },
    "CAPOFAMIGLIA": {
        "it": "Indica la persona che è il riferimento principale per la famiglia.\nEsempio: Mario Rossi",
        "en": "Indicate the person who is the main reference for the family.\nExample: John Smith"
    },
    "MORTI_TRASFERITI": {
        "it": "Segnala se ci sono persone decedute o trasferite e indica dove si sono trasferiti.\nRispondi con: 'nello stesso comune', 'in altro comune', 'all'estero' o 'non so'\nEsempio: in altro comune",
        "en": "Report if there are any deceased or moved family members and where they moved.\nReply with: 'same municipality', 'other municipality', 'abroad' or 'don't know'\nExample: other municipality"
    },
    "TIPO_ALLOGGIO": {
        "it": "Indica il tipo di alloggio scegliendo un numero da 1 a 3:\n1) abitazione normale\n2) struttura non standard (camper, baracca, ecc.)\n3) struttura collettiva (hotel, casa di riposo, ecc.)\nEsempio: 1",
        "en": "Specify the type of accommodation by choosing a number from 1 to 3:\n1) normal dwelling\n2) non-standard structure (camper, barracks, etc.)\n3) collective housing (hotel, retirement home, etc.)\nExample: 1"
    },
    "OCCUPAZIONE_ALLOGGIO": {
        "it": "Indica quanti nuclei familiari occupano l'alloggio con un numero da 1 a 5.\nEsempio: 2",
        "en": "Indicate how many households occupy the accommodation with a number from 1 to 5.\nExample: 2"
    },
    "NUMERO_FAMIGLIE_OCCUPANTI": {
        "it": "Indica il numero totale di persone che vivono nell'alloggio con un numero da 1 a 50.\nEsempio: 4",
        "en": "Indicate the total number of people living in the accommodation with a number from 1 to 50.\nExample: 4"
    },
    "TITOLO_OCCUPAZIONE": {
        "it": "Indica a che titolo occupate l'alloggio: proprietà, affitto, usufrutto o altro.\nEsempio: affitto",
        "en": "Indicate your tenure status: ownership, rent, usufruct or other.\nExample: rent"
    },
}


##### struttura domande 
#--------------------------------------- Struttura funzionamento delle domande
question_tree = [
    {
        "id": "LANG_SELECT",
        "question": {
            "it": "Seleziona la lingua del questionario (scrivi: italiano o english):",
            "en": "Select the language of the survey (type: italian or english):"
        },
        "special": "lang"
    },
    {
        "id": "INTRO",
        "question": {
            "it": "Benvenuto/a!\nRispondi alle domande scegliendo il numero dell\'opzione o digitando il testo richiesto.\nScrivi \'aiuto\' per spiegazioni, \'stop\' per interrompere.\nDigita \'si\' per iniziare.",
            "en": "Welcome!\nAnswer by typing the option number or the requested text.\nType \'help\' for explanations, \'stop\' to quit.\nType \'yes\' to begin."
        },
        "special": "intro"
    },
    {
        "id": "INFORMATIVA",
        "question": {
            "it": "Questa rilevazione è obbligatoria (art. 7 d.lgs. 322/1989). I dati sono tutelati (Reg. UE 2016/679). Procediamo? (si/no)",
            "en": "This survey is mandatory (Art. 7 Legislative Decree 322/1989). Data is protected (EU Reg. 2016/679). Shall we proceed? (yes/no)"
        },
        "special": "info"
    },


#------------------------------ Struttura  SCHEDA ALLOGGIO 
    
    {
    "id": "FAMIGLIA_LISTA",
    "question": {
        "it": "Elencami i componenti della tua famiglia attraverso i loro codici fiscali",
        "en": "List your family members by their tax codes"
    },
    "next_question_default": "CAPOFAMIGLIA"  
},
    {
        "id": "CAPOFAMIGLIA",
        "question": {
            "it": "Chi è il capofamiglia (persona di riferimento)?",
            "en": "Who is the household reference person?"
        },
        "next_question_default": "MORTI_TRASFERITI" 
    },{
        "id": "MORTI_TRASFERITI",
       "question": {
        "it": "Ci sono persone della tua famiglia che sono decedute o si sono trasferite? Dove si sono trasferiti? (nello stesso comune / in altro comune / all'estero / non so)",
        "en": "Are there any family members who have died or moved away? Where did they move? (same municipality / other municipality / abroad / don't know)"
         },
         "next_question_default": "TIPO_ALLOGGIO"
     },  
    {
        "id": "TIPO_ALLOGGIO",
        "question": {
            "it": "Indica il tipo di alloggio (scegli un numero):\n"
                  "1 Abitazione (casa, appartamento, villa)\n"
                  "2 Altro tipo di alloggio (container, baracca, roulotte, camper, ecc.)\n"
                  "3 Struttura residenziale collettiva (hotel, casa di riposo, convitto, ecc.)",
            "en": "Specify the type of accommodation (choose a number):\n"
                  "1 Dwelling (house, flat, villa)\n"
                  "2 Other type of housing (container, shack, caravan, camper, etc.)\n"
                  "3 Collective living quarters (hotel, retirement home, boarding school, etc.)"
        },
        "input_type": "number",
        "min_val": 1,
        "max_val": 3,
        "jump_rules": {
            "3": "TITOLO_OCCUPAZIONE"
        },
        "next_question_default": "OCCUPAZIONE_ALLOGGIO"
    },
     {
         "id": "OCCUPAZIONE_ALLOGGIO",
         "question": {
             "it": "L'alloggio è occupato da: Indicare il numero di famiglie",
             "en": "The housing is occupied by: Indicate the total numbers of family"
         },
         "input_type": "number",
         "min_val": 1,
         "max_val": 5,
         "next_question_default": "TITOLO_OCCUPAZIONE"
     },
     {
         "id": "TITOLO_OCCUPAZIONE",
         "question": {
             "it": "A che titolo la famiglia occupa l'alloggio? (proprietà / affitto / usufrutto / altro)",
             "en": "What is your tenure status? (ownership / rent / usufruct / other)"
         },
         "next_question_default": "END_MESSAGE"
     },
{
    "id": "END_MESSAGE",
    "action": "display_only",
    "question": {
        "it": "Questionario completato. Grazie per la collaborazione!",
        "en": "Questionnaire completed. Thank you for your cooperation!"
    },
    "next_question_default": None  # Termina esplicitamente
},
]

# --- Variabili globali ---
user_states = {}  # Memorizza lo stato dell'utente (indice domanda, lingua, risposte parziali)
user_responses = {}  # Memorizza le risposte finali per ogni utente
desktop_path = Path.home() / "Desktop" / "riepilogo_istat"
os.makedirs(desktop_path, exist_ok=True)
excel_file = desktop_path / "questionario_istat_completo.xlsx"

# --- Funzioni Principali ---
async def start_command(update: Update, context):
    user_id = update.effective_user.id
    user_states[user_id] = {
        "current_question_index": 0,
        "responses": {},
        "lang": "it"
    }
    await ask_question(update, user_id)

async def ask_question(update: Update, user_id: int):
    """Mostra la domanda corrente e – se è l'ultima – salva l'Excel."""
    state = user_states[user_id]
    current_q_def = question_tree[state["current_question_index"]]
    lang = state["lang"]

    # ────────────────────────────────────────────────────────────────
    # Caso 1: nodo solo-testo (display_only)
    # ────────────────────────────────────────────────────────────────
    if "action" in current_q_def and current_q_def["action"] == "display_only":
        await update.message.reply_text(current_q_def["question"][lang])

        # ► se non esiste una domanda successiva, significa che è l'ULTIMO nodo
        if current_q_def.get("next_question_default") is None:
            # salva risposte in Excel
            save_responses_to_excel(user_id, state["responses"])
            # copia anche in user_responses (come facevamo altrove)
            user_responses[user_id] = state["responses"].copy()
            # pulizia dello stato dell'utente
            user_states.pop(user_id, None)
        return  # fine funzione (non deve inviare altro)

    # ────────────────────────────────────────────────────────────────
    # Caso 2: domanda “normale”
    # ────────────────────────────────────────────────────────────────
    await update.message.reply_text(current_q_def["question"][lang])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text_input = update.message.text.strip()
    
    if user_id not in user_states:
        await update.message.reply_text("Per favore, usa il comando /start per iniziare.")
        return
    
    state = user_states[user_id]
    lang = get_user_lang(state)
    current_q_index = state["current_question_index"]
    current_q_def = question_tree[current_q_index]
    current_q_id = current_q_def["id"]
    
    # Gestione richieste di aiuto
    if is_help_request(text_input, lang):
        help_text = HELP_EXPLANATIONS.get(current_q_id, {}).get(lang, "Nessun aiuto disponibile per questa domanda.")
        await update.message.reply_text(help_text)
        return
    
    # Gestione comando stop
    if update_vocab_if_similar(normalize(text_input), INTENT_VOCABS, 0.6) == "stop":
        await update.message.reply_text({"it": "Questionario interrotto.", "en": "Survey stopped."}[lang])
        if user_id in user_states:
            del user_states[user_id]
        return
    
    # Gestione input
    if current_q_def.get("special") == "lang":
        if text_input.lower() in ["italiano", "english"]:
            state["lang"] = "it" if text_input.lower() == "italiano" else "en"
            state["current_question_index"] += 1
            await ask_question(update, user_id)
        else:
            await update.message.reply_text(current_q_def["question"]["it"] + " - " + current_q_def["question"]["en"])
        return
    
    if current_q_def.get("special") in ["intro", "info"]:
        if interpret_yes_no(text_input, lang) != "yes":
            await update.message.reply_text({"it": "Per favore, digita 'sì' per procedere.", "en": "Please type 'yes' to proceed."}[lang])
            return
        state["responses"][current_q_id] = text_input
        state["current_question_index"] += 1
        await ask_question(update, user_id)
        return
    
    # Validazione input numerico
    if "input_type" in current_q_def and current_q_def["input_type"] == "number":
        try:
            value = int(text_input)
            min_val = current_q_def.get("min_val")
            max_val = current_q_def.get("max_val")
            if min_val is not None and value < min_val:
                await update.message.reply_text(f"Per favore, inserisci un numero >= {min_val}.")
                return
            if max_val is not None and value > max_val:
                await update.message.reply_text(f"Per favore, inserisci un numero <= {max_val}.")
                return
        except ValueError:
            await update.message.reply_text("Per favore, inserisci un numero valido.")
            return
    
    # Salva la risposta
    state["responses"][current_q_id] = text_input
    
    # Calcolo prossima domanda
    next_q_id = get_next_question_id(current_q_id, text_input, user_id)
    
    if next_q_id is None:
        await update.message.reply_text({"it": "Questionario completato. Grazie!", "en": "Survey completed. Thank you!"}[lang])
        # Salva le risposte finali
        user_responses[user_id] = state["responses"].copy()
        save_responses_to_excel(user_id, state["responses"])
        del user_states[user_id]
        return
    
    # Trova l'indice della prossima domanda
    next_q_index = next((i for i, q in enumerate(question_tree) if q["id"] == next_q_id), None)
    if next_q_index is not None:
        state["current_question_index"] = next_q_index
        await ask_question(update, user_id)
    else:
        await update.message.reply_text({"it": "Errore nel questionario.", "en": "Survey error."}[lang])

def get_next_question_id(current_id, last_input=None, user_id=None):
    current_q_def = next((q for q in question_tree if q["id"] == current_id), None)
    if current_q_def is None:
        return None
    
    # Controlla le regole di salto
    if "jump_rules" in current_q_def and last_input:
        cleaned = last_input.strip()
        if cleaned in current_q_def["jump_rules"]:
            return current_q_def["jump_rules"][cleaned]
    
    # Ritorna la prossima domanda di default
    return current_q_def.get("next_question_default")

def get_user_lang(state):
    return state.get("lang", "it")

def interpret_yes_no(text: str, lang: str) -> str | None:
    txt = normalize(text)
    if txt in YES_VARIANTS[lang]:
        return "yes"
    elif txt in NO_VARIANTS[lang]:
        return "no"
    return update_vocab_if_similar(txt, INTENT_VOCABS, 0.6)

def is_help_request(text, lang):
    text_lower = text.strip().lower()
    return any(text_lower == variant.lower() for variant in HELP_VARIANTS[lang])
# --- mapping fisso ID domanda -> testo (italiano) -----------------
def _build_question_text_map():
    mapping = {}
    for q in question_tree:
        # usa il testo italiano come "chiave" stabile in excel
        testo = q["question"]["it"] if "question" in q else ""
        # per i nodi display_only, teniamo comunque il testo
        mapping[q["id"]] = testo.splitlines()[0]  # prima riga pulita
    return mapping

QUESTION_TEXT = _build_question_text_map()

def save_responses_to_excel(user_id, responses):
    """
    Salva/aggiorna un file Excel a matrice:
        • indice  = ID domanda
        • col_0   = Testo domanda
        • col_*>1 = risposte dei vari utenti (nome colonna = user_id Telegram)
    """
    try:
        # 1. DataFrame utente corrente  ------------------------------
        #    index = ID domanda • colonna = ID utente
        df_user = pd.DataFrame.from_dict(
            responses, orient="index", columns=[str(user_id)]
        )

        # 2. Aggiungi colonna fissa con i testi delle domande --------
        df_user.insert(0, "Testo domanda", df_user.index.map(QUESTION_TEXT))

        # 3. Se esiste già il file, caricalo e fai outer-join ----------
        if excel_file.exists():
            df_existing = pd.read_excel(excel_file, index_col=0)  # 0 = indice (ID domanda)
            # union sull’indice, poi concat sulle colonne (outer join)
            df_final = df_existing.join(df_user, how="outer")
        else:
            df_final = df_user.copy()

        # 4. Ordina l’indice nell’ordine definito in question_tree ----
        order = [q["id"] for q in question_tree]
        df_final = df_final.reindex(order)

        # 5. Salva -----------------------------------------------------
        df_final.to_excel(excel_file, index=True)
        logger.info(f"Excel aggiornato: {excel_file}")

    except Exception as e:
        logger.error(f"Errore nel salvare le risposte: {e}", exc_info=True)

# --- Main ---
if __name__ == "__main__":
    if not BOT_TOKEN:
        print("ERRORE: Il BOT_TOKEN non è stato impostato.")
    else:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        print("Avvio del bot Telegram...")
        app.run_polling()