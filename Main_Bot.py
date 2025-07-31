# bot.py

import logging
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# IMPORTA I DATI DAI NOSTRI FILE
from Questionario import (
    preliminary_questions, question_tree_10_plus, question_tree_3_9,
    LANG_VARIANTS, YES_VARIANTS, NO_VARIANTS, HELP_VARIANTS, HELP_TEXTS,STOP_COMMANDS
)
from Salvataggio_Excel import save_user_responses

# ==============================================================================
# DIZIONARIO PER I TITOLI DELLE SEZIONI
# ==============================================================================
SECTION_TITLES = {
    "it": {
        "1": "SEZIONE 1: PROPRIETÀ, CONTROLLO E GESTIONE",
        "2": "SEZIONE 2: RISORSE UMANE",
        "3": "SEZIONE 3: RELAZIONI PRODUTTIVE E FILIERE"
    },
    "en": {
        "1": "SECTION 1: OWNERSHIP, CONTROL AND MANAGEMENT",
        "2": "SECTION 2: HUMAN RESOURCES",
        "3": "SECTION 3: PRODUCTION RELATIONSHIPS AND SUPPLY CHAINS"
    }
}


# ==============================================================================
# FILE PRINCIPALE DEL BOT (VERSIONE FINALE)
# ==============================================================================


# ------------------------------------------------------------------------------
# CONFIGURAZIONE INIZIALE
# ------------------------------------------------------------------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = "7913278624:AAHYXMoqvmrZ236DzYT3DOAlsYGxpV6b5Lw"
user_states = {} # DIZIONARIO PER MEMORIZZARE LO STATO DI OGNI UTENTE

# DEFINIAMO GLI STATI PER LA CONVERSATIONHANDLER
SELECTING_ACTION, TYPING_RESPONSE = range(2)

# ------------------------------------------------------------------------------
# FUNZIONI DI UTILITY
# ------------------------------------------------------------------------------

def get_current_question_tree(state):
    """RESTITUISCE L'ALBERO DELLE DOMANDE CORRETTO IN BASE ALLO STATO."""
    return question_tree_10_plus if state.get("questionnaire_type") == "10+" else question_tree_3_9

def find_question_by_id(question_id, tree):
    """TROVA UNA DOMANDA NELL'ALBERO DATO IL SUO ID."""
    if not tree: return None, -1
    for i, q_def in enumerate(tree):
        if q_def["id"] == question_id:
            return q_def, i
    return None, -1

# ------------------------------------------------------------------------------
# GESTORI DEI COMANDI E MESSAGGI TELEGRAM
# ------------------------------------------------------------------------------

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """ESEGUITO CON /start. INIZIALIZZA LO STATO E PONE LA PRIMA DOMANDA."""
    user_id = update.effective_user.id
    logger.info(f"UTENTE {user_id} HA AVVIATO IL BOT CON /start.")

    user_states[user_id] = {
        "user_id": user_id, "lang": "it", "questionnaire_type": None,
        "current_question_id": preliminary_questions[0]["id"], "is_preliminary": True,
        "responses": {}, "yes_no_table_state": {}
    }
    await ask_question(update, context)
    return TYPING_RESPONSE

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """GESTISCE OGNI MESSAGGIO DI TESTO. È IL MOTORE PRINCIPALE."""
    user_id = update.effective_user.id
    text_input = update.message.text.strip()

    if user_id not in user_states:
        await update.message.reply_text("Per favore, usa /start per iniziare.\nPlease use /start command to begin.")
        return ConversationHandler.END

    state = user_states[user_id]
    lang = state["lang"]
    
    # NORMALIZZA L'INPUT PER I CONTROLLI
    normalized_input = text_input.lower()

    # GESTIONE COMANDI DI STOP ESPLICITI
    if normalized_input in STOP_COMMANDS['it'] + STOP_COMMANDS['en']:
        await update.message.reply_text({"it": "Questionario interrotto come richiesto.", "en": "Survey stopped as requested."}[lang])
        if user_id in user_states: del user_states[user_id] # Pulisce lo stato
        return ConversationHandler.END

    # GESTIONE COMANDI DI AIUTO
    if normalized_input in HELP_VARIANTS['it'] + HELP_VARIANTS['en']:
        q_id = state.get("current_question_id", "DEFAULT")
        
        # TROVA LA DEFINIZIONE DELLA DOMANDA CORRENTE
        q_def = None
        if state.get("is_preliminary"):
            q_def, _ = find_question_by_id(q_id, preliminary_questions)
        else:
            tree = get_current_question_tree(state)
            if tree: q_def, _ = find_question_by_id(q_id, tree)
        
        # RECUPERA IL TESTO DI AIUTO DI BASE
        help_message = HELP_TEXTS[lang].get(q_id, HELP_TEXTS[lang]["DEFAULT"])
        
        # AGGIUNGE LE ISTRUZIONI DI RISPOSTA IN BASE AL TIPO DI DOMANDA
        instruction_text = ""
        if q_def:
            q_type = q_def.get("question_type")
            if q_type == "single_choice":
                instruction_text = {"it": "\n\n*Come rispondere:* Digita il *numero* dell'opzione che vuoi scegliere (es. `1`).", 
                                    "en": "\n\n*How to answer:* Type the *number* of the option you want to choose (e.g., `1`)."}[lang]
            elif q_type == "yes_no_table":
                instruction_text = {"it": "\n\n*Come rispondere:* Digita `sì` o `no`.", "en": "\n\n*How to answer:* Type `yes` or `no`."}[lang]
            elif "multiple_choice" in q_type:
                instruction_text = {"it": "\n\n*Come rispondere:* Digita i *numeri* delle opzioni che vuoi scegliere, separati da una virgola (es. `1, 3`).", 
                                    "en": "\n\n*How to answer:* Type the *numbers* of the options you want to choose, separated by a comma (e.g., `1, 3`)."}[lang]
            elif q_type == "percentage":
                instruction_text = {"it": "\n\n*Come rispondere:* Inserisci un valore numerico per la percentuale (es. `25`).", 
                                    "en": "\n\n*How to answer:* Enter a numeric value for the percentage (e.g., `25`)."}[lang]
            elif q_type == "text":
                 instruction_text = {"it": "\n\n*Come rispondere:* Scrivi la tua risposta come testo libero.", 
                                    "en": "\n\n*How to answer:* Write your answer as free text."}[lang]

        # COMBINA IL MESSAGGIO FINALE
        final_help_message = f"💡 *Aiuto per la domanda '{q_id}'*:\n\n_{help_message}_{instruction_text}"
        await update.message.reply_text(final_help_message, parse_mode='Markdown')
        
        return TYPING_RESPONSE

    # SE NON È UN COMANDO, PROCESSA LA RISPOSTA
    await process_user_response(update, context)
    return TYPING_RESPONSE

# ------------------------------------------------------------------------------
# MOTORE DEL QUESTIONARIO
# ------------------------------------------------------------------------------

async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE, question_id=None):
    """
    TROVA E INVIA ALL'UTENTE LA DOMANDA CORRENTE.
    GESTISCE AUTOMATICAMENTE I NODI 'display_only' E LE TABELLE.
    SE IL QUESTIONARIO È FINITO, SALVA I DATI.
    """
    user_id = update.effective_user.id
    if user_id not in user_states: return
    state = user_states[user_id]
    
    q_id_to_ask = question_id if question_id else state["current_question_id"]
    
    # CASO 1: FINE DEL QUESTIONARIO
    if q_id_to_ask is None or q_id_to_ask == "END_SURVEY":
        lang = state["lang"]
        final_message = "Grazie per la collaborazione!"
        
        tree = get_current_question_tree(state)
        if tree:
            q_def, _ = find_question_by_id("END_SURVEY", tree)
            if q_def and "question" in q_def: final_message = q_def["question"][lang]
            
        await update.message.reply_text(f"✅ {final_message}")
        logger.info(f"QUESTIONARIO COMPLETATO PER L'UTENTE {user_id}.")
        save_user_responses(user_id, state)
        if user_id in user_states: del user_states[user_id]
        return

    # TROVA LA DEFINIZIONE DELLA DOMANDA
    q_def, q_index = (find_question_by_id(q_id_to_ask, preliminary_questions) if state["is_preliminary"] 
                      else find_question_by_id(q_id_to_ask, get_current_question_tree(state)))
    
    if not q_def:
        logger.error(f"ERRORE: ID domanda '{q_id_to_ask}' non trovato.")
        await update.message.reply_text("Si è verificato un errore interno.")
        return

    # Aggiorna lo stato con la domanda corrente che stiamo processando
    state["current_question_id"] = q_id_to_ask
    lang = state["lang"]
    
    # ANNUNCIO DELLA SEZIONE (SE CAMBIA)
    # Questo controllo viene fatto qui, prima di decidere il tipo di domanda,
    # per funzionare anche se la prima domanda di una sezione è 'display_only'.
    current_section = q_def.get("section")
    last_section = state.get("last_section_announced")
    if current_section and current_section != last_section:
        section_title = SECTION_TITLES[lang].get(current_section)
        if section_title:
            await update.message.reply_text(f"--- *{section_title}* ---", parse_mode='Markdown')
            state["last_section_announced"] = current_section

    # GESTIONE DEI DIVERSI TIPI DI DOMANDA
    q_type = q_def.get("question_type")

    if q_type == "display_only":
        message_text = q_def["question"].get(lang, q_def["question"]["it"])
        await update.message.reply_text(f"ℹ️ {message_text}")
        
        next_q_id = get_next_question_id(q_def, state)
        state["current_question_id"] = next_q_id
        await ask_question(update, context) # Avanza automaticamente
        return

    if q_type == "yes_no_table":
        await handle_yes_no_table(update, context, q_def)
        return

    # DOMANDA NORMALE (che richiede una risposta)
    message_text = q_def["question"].get(lang, q_def["question"]["it"])
    if "options" in q_def: message_text += f"\n\n" + "\n".join(q_def["options"])
    if "notes" in q_def: message_text += f"\n\n_{q_def['notes'].get(lang, q_def['notes']['it'])}_"
        
    await update.message.reply_text(message_text, parse_mode='Markdown')

async def process_user_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    VALIDA LA RISPOSTA, LA SALVA E DETERMINA LA PROSSIMA DOMANDA.
    """
    user_id = update.effective_user.id
    state = user_states[user_id]
    text_input = update.message.text.strip()
    
    # TROVA LA DEFINIZIONE DELLA DOMANDA CORRENTE
    q_id = state["current_question_id"]
    q_def, _ = (find_question_by_id(q_id, preliminary_questions) if state["is_preliminary"]
                else find_question_by_id(q_id, get_current_question_tree(state)))

    # SE STIAMO GESTENDO UNA TABELLA YES/NO, USA IL SUO GESTORE SPECIFICO
    if q_def.get("question_type") == "yes_no_table":
        await handle_yes_no_table(update, context, q_def, text_input)
        return

    # VALIDAZIONE E SALVATAGGIO PER DOMANDE NORMALI
    is_valid, error_message, processed_response = validate_response(text_input, q_def, state)
    if not is_valid:
        await update.message.reply_text(error_message)
        return

    state["responses"][q_id] = processed_response
    
    # DETERMINA LA PROSSIMA DOMANDA
    next_q_id = get_next_question_id(q_def, state)
    
    # GESTIONE SALTI CONDIZIONALI
    tree = get_current_question_tree(state)
    while tree and next_q_id and next_q_id != "END_SURVEY":
        next_q_def, _ = find_question_by_id(next_q_id, tree)
        if not next_q_def: break

        if "depends_on" in next_q_def:
            dep_id, dep_option_idx = next_q_def["depends_on"]["id"], next_q_def["depends_on"]["option_index"]
            dep_option_num = str(dep_option_idx + 1)
            
            if dep_id not in state["responses"] or dep_option_num not in state["responses"].get(dep_id, ''):
                logger.info(f"UTENTE {user_id}: Salto domanda '{next_q_id}' per dipendenza non soddisfatta.")
                next_q_id = next_q_def.get("next_question_default")
                continue
        break
        
    state["current_question_id"] = next_q_id
    await ask_question(update, context)

async def handle_yes_no_table(update: Update, context: ContextTypes.DEFAULT_TYPE, q_def, response=None):
    """
    GESTORE SPECIFICO PER DOMANDE DI TIPO 'yes_no_table'.
    PONE UNA DOMANDA 'Sì/No' PER OGNI OPZIONE NELLA LISTA, UNA ALLA VOLTA.
    """
    user_id = update.effective_user.id
    if user_id not in user_states: return
    state = user_states[user_id]
    q_id = q_def["id"]
    lang = state["lang"]

    # INIZIALIZZA LO STATO DELLA TABELLA SE È LA PRIMA VOLTA CHE ENTRIAMO
    if q_id not in state.get("yes_no_table_state", {}):
        state["yes_no_table_state"] = {q_id: {"current_option_index": 0, "answers": []}}
    
    table_state = state["yes_no_table_state"][q_id]
    
    # SE 'response' NON È None, SIGNIFICA CHE L'UTENTE HA APPENA RISPOSTO A UNA SOTTO-DOMANDA
    if response is not None:
        # Registra la risposta 'Sì' (1) o 'No' (2)
        choice = "1" if response.lower() in YES_VARIANTS[lang] else "2"
        table_state["answers"].append(choice)
        # Avanza all'indice della prossima opzione
        table_state["current_option_index"] += 1

    current_option_index = table_state["current_option_index"]

    # CONTROLLA SE ABBIAMO FINITO TUTTE LE OPZIONI DELLA TABELLA
    if current_option_index >= len(q_def["options"]):
        # Abbiamo finito la tabella.
        # 1. Aggrega le risposte "Sì" (quelle con valore "1")
        final_answers = [str(i + 1) for i, ans in enumerate(table_state["answers"]) if ans == "1"]
        state["responses"][q_id] = ", ".join(final_answers) if final_answers else "Nessuna"
        
        # Pulisci lo stato temporaneo della tabella
        del state["yes_no_table_state"][q_id]

        # 2. Determina la prossima domanda
        next_q_id = None
        # Controlla la regola 'jump_if_all_no'
        if not final_answers and "jump_if_all_no" in q_def:
            next_q_id = q_def["jump_if_all_no"]
        else:
            next_q_id = q_def.get("next_question_default")
        
        # 3. Procedi alla prossima domanda
        state["current_question_id"] = next_q_id
        await ask_question(update, context)
    else:
        # NON ABBIAMO FINITO: PONI LA DOMANDA PER L'OPZIONE CORRENTE
        option_text = q_def["options"][current_option_index]
        
        # Costruisce il testo della domanda per la riga corrente della tabella
        # Usa il testo principale come titolo
        main_question_text = q_def["question"].get(lang, q_def["question"]["it"])
        prompt = f"{main_question_text}\n\n➡️ *{option_text}*\n\nRispondi con `sì` o `no`."
        
        await update.message.reply_text(prompt, parse_mode='Markdown')


def validate_response(text_input, q_def, state):
    """
    VALIDA LA RISPOSTA DELL'UTENTE.
    """
    # SE q_def è None (improbabile ma sicuro), non fare nulla
    if not q_def:
        return False, "Errore interno.", None

    q_type = q_def.get("question_type", "text")
    lang = state.get("lang", "it") # Usa .get per sicurezza

    # GESTIONE SPECIALE PER LA PRIMA DOMANDA (LINGUA)
    if q_type == "language_selection":
        if text_input.lower() in LANG_VARIANTS["it"]:
            state["lang"] = "it"
            return True, None, "it"
        if text_input.lower() in LANG_VARIANTS["en"]:
            state["lang"] = "en"
            return True, None, "en"
        return False, "Lingua non valida. Scrivi 'italiano' o 'english'.", None

    # ORA 'lang' È SICURAMENTE DEFINITO
    
    if q_type == "company_size_selection":
        # Controlla direttamente l'input dell'utente
        if text_input.strip() == "1":
            state["questionnaire_type"] = "3-9"
            return True, None, "3-9"
        elif text_input.strip() == "2":
            state["questionnaire_type"] = "10+"
            return True, None, "10+"
        else:
            return False, {"it": "Risposta non valida. Per favore, digita `1` o `2`.", "en": "Invalid answer. Please type `1` or `2`."}[lang], None

    if q_type == "confirmation":
        return (True, None, "yes") if text_input.lower() in YES_VARIANTS[lang] else (False, {"it": "Digita 'sì' per procedere.", "en": "Type 'yes' to proceed."}[lang], None)

    # GESTIONE DOMANDE CON OPZIONI
    # Controlla prima se 'options' esiste per evitare KeyError
    if "options" not in q_def:
        # Se non ci sono opzioni, la consideriamo una risposta testuale valida
        return True, None, text_input

    valid_choices_nums = {str(i + 1) for i in range(len(q_def["options"]))}

    if q_type == "single_choice":
        user_choice = text_input.split('.')[0].strip()
        return (True, None, user_choice) if user_choice in valid_choices_nums else (False, {"it": "Opzione non valida. Scegli un numero dalla lista.", "en": "Invalid option. Choose a number from the list."}[lang], None)

    if "multiple_choice" in q_type:
        choices = set(c.strip() for c in re.split(r'[,\s]+', text_input) if c)
        if not choices.issubset(valid_choices_nums):
            return False, {"it": "Una o più opzioni non sono valide. Controlla i numeri inseriti.", "en": "One or more options are invalid. Please check the numbers you entered."}[lang], None

        max_opts = {"multiple_choice_max_3": 3, "multiple_choice_max_4": 4}.get(q_type)
        if max_opts and len(choices) > max_opts:
            return False, {"it": f"Puoi scegliere al massimo {max_opts} opzioni.", "en": f"You can choose up to {max_opts} options."}[lang], None

        return True, None, ", ".join(sorted(list(choices)))

    if q_type == "percentage":
        try:
            val = float(text_input.replace('%', '').strip())
            return (True, None, f"{val}%") if 0 <= val <= 100 else (False, {"it": "Inserisci una percentuale tra 0 e 100.", "en": "Enter a percentage between 0 and 100."}[lang], None)
        except ValueError:
            return False, {"it": "Formato non valido. Inserisci un numero.", "en": "Invalid format."}[lang], None

    # Fallback per qualsiasi altro tipo non gestito esplicitamente (es. 'text')
    return True, None, text_input


def get_next_question_id(q_def, state):
    """DETERMINA L'ID DELLA PROSSIMA DOMANDA."""
    # PRIMA OTTENIAMO L'ID DELLA DOMANDA CORRENTE
    q_id = q_def["id"]
    # POI USIAMO L'ID PER RECUPERARE LA RISPOSTA
    response = state["responses"].get(q_id)
    
    # Controlla le regole di salto
    if "jump_rules" in q_def and response in q_def["jump_rules"]:
        return q_def["jump_rules"][response]

    # Controlla il salto per 'tutto no' nella tabella yes_no
    # Questa logica è ora gestita in handle_yes_no_table, quindi qui non serve più.

    # Se non ci sono salti, vai alla domanda di default
    # Gestione speciale per le domande preliminari
    if state["is_preliminary"]:
        # Troviamo l'indice della domanda corrente nella lista delle preliminari
        current_idx = -1
        for i, q in enumerate(preliminary_questions):
            if q["id"] == q_id:
                current_idx = i
                break
        
        # Se non è l'ultima, passiamo alla successiva
        if current_idx != -1 and current_idx + 1 < len(preliminary_questions):
            return preliminary_questions[current_idx + 1]["id"]
        else: 
            # Fine domande preliminari: passa al questionario reale
            state["is_preliminary"] = False
            tree = get_current_question_tree(state)
            return tree[0]["id"] if tree else None

    # Se siamo nel questionario principale, restituisci semplicemente il default
    return q_def.get("next_question_default")
# ------------------------------------------------------------------------------
# BLOCCO PRINCIPALE
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    if BOT_TOKEN == "I7913278624:AAHYXMoqvmrZ236DzYT3DOAlsYGxpV6b5Lw":
        print("ERRORE: DEVI INSERIRE IL TUO TOKEN DEL BOT IN bot.py")
    else:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        
        # USA CONVERSATIONHANDLER PER UNA GESTIONE PIÙ ROBUSTA DELLO STATO
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start_command)],
            states={
                TYPING_RESPONSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)]
            },
            fallbacks=[CommandHandler("start", start_command)], # Permette di riavviare in qualsiasi momento
        )
        
        app.add_handler(conv_handler)
        
        print("BOT IN AVVIO...")
        app.run_polling()