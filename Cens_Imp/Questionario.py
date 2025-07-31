# question_data.py

# ==============================================================================
# FILE PER I DATI STATICI DEL QUESTIONARIO
# CONTIENE:
# 1. VOCABOLARI PER L'INTERPRETAZIONE DELLE RISPOSTE (SÌ/NO/AIUTO)
# 2. STRUTTURE DATI (ALBERI) CON LE DOMANDE E LE REGOLE DI SALTO
# ==============================================================================

# ------------------------------------------------------------------------------
# VOCABOLARI PER LA SCELTA DELLA LINGUA E PER LE RISPOSTE SÌ/NO/AIUTO
# ------------------------------------------------------------------------------
LANG_VARIANTS = {
    "it": ["italiano", "italian", "ita", "it"],
    "en": ["english", "eng", "en", "inglese"]
}

YES_VARIANTS = {
    "it": ["sì", "si", "yes", "ok", "certo", "procedo", "iniziamo", "continua", "va bene"],
    "en": ["yes", "y", "ok", "okay", "sure", "go ahead", "proceed", "start", "continue"]
}

NO_VARIANTS = {
    "it": ["no", "n"],
    "en": ["no", "n"]
}

STOP_COMMANDS = {
    "it": ["stop", "basta", "annulla", "fine", "esci", "interrompi"],
    "en": ["stop", "end", "quit", "cancel", "exit"]
}

HELP_VARIANTS = {
    "it": ["aiuto", "help", "spiegazione", "esempio"],
    "en": ["help", "aiuto", "explanation", "example"]
}


# ------------------------------------------------------------------------------
# TESTI DI AIUTO DETTAGLIATI PER OGNI DOMANDA (ITALIANO E INGLESE)
# ------------------------------------------------------------------------------
HELP_TEXTS = {
    "it": {
        "DEFAULT": "Per favore, rispondi alla domanda scegliendo una delle opzioni numeriche o inserendo il testo richiesto. Scrivi 'stop' per uscire.",
        
        # --- SEZIONE 1: 10+ e 3-9 ADDETTI ---
        "1.1": "Indica se la proprietà e il controllo effettivo dell'azienda sono riconducibili a una persona o a un gruppo di persone legate da vincoli familiari.\n\n*Nota: Il controllo si sostanzia nella capacità di stabilire le politiche operative, finanziarie e produttive.*",
        "1.2": "Specifica chi ha la responsabilità finale delle decisioni operative e strategiche. Può essere l'imprenditore stesso, un familiare, o un manager esterno.\n\n*Nota: Per 'famiglia controllante' si intende una famiglia in possesso di una quota del capitale d'impresa superiore al 50%.*",
        "1.5": "Un'impresa appartiene a un gruppo se è controllata da un'altra società (capogruppo) o se controlla altre società (controllate).",
        "1.8": "Un 'passaggio generazionale' si verifica quando la gestione o la proprietà dell'impresa viene trasferita tra soggetti legati da vincolo di parentela (es. da padre a figlio). Indica l'ultimo passaggio avvenuto.",
        "1.9": "Descrivi l'effetto che il passaggio generazionale ha avuto sulla composizione della proprietà. Ad esempio, se ha portato all'ingresso di nuovi soci esterni alla famiglia.",
        "S1.3": "Indica chi partecipa al processo decisionale strategico. Se le decisioni sono prese in modo collaborativo (es. l'imprenditore ne discute con i dipendenti), puoi selezionare più opzioni separandole con una virgola.",

        # --- SEZIONE 1: SOLO 10+ ADDETTI ---
        "X1.4_intro": "Per 'centralizzate' si intende se le decisioni strategiche più importanti per una funzione vengono prese principalmente dalla direzione centrale (es. imprenditore, CDA) o se sono delegate ai responsabili di funzione. Scegli un'opzione da 1 a 4 per ogni funzione aziendale.",
        "X1.6_intro": "Pensa agli obiettivi principali che l'azienda si è posta negli ultimi due anni. Per ciascuno, indica prima se è stato un obiettivo (Sì/No) e, in caso affermativo, con quale grado di successo è stato raggiunto.",
        "X1.7": "Indica quali saranno le principali direzioni strategiche dell'impresa per il prossimo futuro. Puoi scegliere più opzioni separandole con una virgola (es. 1, 4, 10).",

        # --- SEZIONE 2: 10+ e 3-9 ADDETTI ---
        "2.1": "Considera qualsiasi forma di nuovo personale entrato in azienda nel biennio 2021-2022, inclusi dipendenti, collaboratori a partita IVA e lavoratori in somministrazione (interinali). Non contare chi ha solo cambiato tipo di contratto (es. da determinato a indeterminato).",
        "2.2": "Specifica il tipo di contratto o rapporto di lavoro delle nuove risorse umane. Puoi scegliere più opzioni.",
        "2.4": "Le competenze trasversali (o 'soft skills') sono capacità non tecniche, come la capacità di lavorare in team, la comunicazione efficace o la risoluzione di problemi. Indica fino a tre delle più importanti che avete ricercato.",
        "2.5": "Se l'azienda ha avuto difficoltà a trovare nuovo personale, indica quali sono stati i principali ostacoli. Puoi scegliere fino a tre fattori.",
        "2.7": "Lo smart working o telelavoro è una modalità di lavoro svolta al di fuori dei locali aziendali, utilizzando strumenti digitali. Indica la percentuale di personale che svolge mansioni compatibili con questa modalità.",
        "2.8": "Indica la percentuale effettiva di personale che ha lavorato da remoto almeno un giorno a settimana nel periodo indicato. Rispondi con un numero (es. 15).",
        "2.9": "Indica quali sono i principali motivi che impediscono o limitano l'adozione del lavoro da remoto nella tua azienda. Puoi scegliere fino a quattro fattori.",
        "2.12": "Indica se l'azienda ha organizzato o finanziato corsi di formazione per il personale, escludendo quelli obbligatori per legge (es. sicurezza sul lavoro, D.Lgs 81/2008).",

        # --- SEZIONE 2: SOLO 10+ ADDETTI ---
        "X2.3": "Indica quali canali avete usato per trovare e assumere nuovo personale. Puoi scegliere più opzioni.",
        "X2.6": "Descrivi le pratiche messe in atto per rendere l'azienda attrattiva per i talenti e per trattenere il personale qualificato già presente. Puoi selezionare più opzioni.",
        "X2.10_intro": "Per le seguenti competenze digitali, valuta prima se sono importanti per la tua attività (Sì/No) e poi se il tuo personale le possiede a un livello adeguato.",
        "X2.11": "Indica quali strumenti di gestione del personale sono stati utilizzati, come incentivi basati sulla performance o sistemi di valutazione periodica. Puoi scegliere più opzioni.",
        "X2.13": "Se hai svolto formazione non obbligatoria, specifica di che tipo. Rispondi 'sì' o 'no' per ogni opzione.",
        "X2.14": "Indica la fascia percentuale di dipendenti che ha partecipato ad almeno un corso di formazione non obbligatoria nel 2022.",

        # --- SEZIONE 3: 10+ e 3-9 ADDETTI ---
        "3.1": "Indica se l'azienda ha avuto rapporti di collaborazione o scambio con altre entità esterne, sia come cliente (commessa) che come fornitore (fornitura/appalto). Rispondi 'sì' o 'no' per ogni tipo di relazione.",
        "3.4_1": "Indica i motivi principali che hanno spinto l'azienda a ordinare beni/servizi da terzi. Puoi scegliere fino a tre opzioni.",
        "3.4_2": "Indica i motivi principali che hanno spinto l'azienda a fornire beni/servizi ad altri. Puoi scegliere fino a tre opzioni.",
        "3.6": "Descrivi le difficoltà principali incontrate quando si è cercato di stabilire nuove collaborazioni con altre aziende. Puoi scegliere fino a tre opzioni.",
        "3.7": "Una filiera produttiva è l'insieme di attività che portano un prodotto al consumatore finale. Indica i 'macro-settori' in cui opera la tua azienda. Puoi scegliere più opzioni.",

        # --- SEZIONE 3: SOLO 10+ ADDETTI ---
        "3.2_1": "Per le commesse (acquisti), indica con chi avete avuto rapporti (es. altre aziende del gruppo, università, etc.). Puoi scegliere più opzioni.",
        "X3.3_1": "Indica per quali funzioni aziendali avete fatto ricorso a commesse esterne. Puoi scegliere più opzioni.",
        "X3.5_1": "Indica il numero di soggetti da cui avete acquistato beni/servizi in regime di commessa.",
        "3.8_intro": "Pensa al bene o servizio che rappresenta il costo di acquisto più alto per la tua azienda. Valuta quanto la tua azienda può influenzarne prezzo, qualità e quantità.",
        "3.9_intro": "Pensa al bene o servizio che genera il maggior ricavo per la tua azienda. Valuta quanto la tua azienda può influenzarne prezzo, qualità e quantità."
    },
    "en": {
        "DEFAULT": "Please answer the question by choosing one of the numbered options or by entering the requested text. Type 'stop' to exit.",

        # --- SECTION 1: 10+ and 3-9 EMPLOYEES ---
        "1.1": "Indicate if the ownership and effective control of the company are attributable to a person or a group of people linked by family ties.\n\n*Note: Control takes the form of the ability to establish operational, financial, and production policies.*",
        "1.2": "Specify who has the final responsibility for operational and strategic decisions. It can be the entrepreneur, a family member, or an external manager.\n\n*Note: 'Controlling family' means a family holding more than 50% of the company's share capital.*",
        "1.5": "A company belongs to a group if it is controlled by another company (parent company) or if it controls other companies (subsidiaries).",
        "1.8": "A 'generational change' occurs when the management or ownership of the company is transferred between subjects linked by blood relations (e.g., from parent to child). Indicate the most recent change.",
        "1.9": "Describe the effect the generational change had on the ownership structure. For example, if it led to the entry of new shareholders from outside the family.",
        "S1.3": "Indicate who participates in the strategic decision-making process. If decisions are made collaboratively (e.g., the entrepreneur discusses them with employees), you can select multiple options separated by a comma.",

        # --- SECTION 1: ONLY 10+ EMPLOYEES ---
        "X1.4_intro": "'Centralised' means whether the most important strategic decisions for a function are made mainly by the central management (e.g., entrepreneur, Board of Directors) or are delegated to function managers. Choose an option from 1 to 4 for each business function.",
        "X1.6_intro": "Think about the main objectives the company set for itself in the last two years. For each, first indicate if it was an objective (Yes/No), and if so, with what degree of success it was achieved.",
        "X1.7": "Indicate what the main strategic directions of the company will be for the near future. You can choose multiple options separated by a comma (e.g., 1, 4, 10).",

        # --- SECTION 2: 10+ and 3-9 EMPLOYEES ---
        "2.1": "Consider any form of new personnel who joined the company in the 2021-2022 period, including employees, VAT-registered collaborators, and temporary agency workers. Do not count those who only changed their contract type (e.g., from fixed-term to permanent).",
        "2.2": "Specify the type of contract or employment relationship of the new human resources. You can choose more than one option.",
        "2.4": "Transversal skills (or 'soft skills') are non-technical abilities, such as teamwork, effective communication, or problem-solving. Indicate up to three of the most important ones you looked for.",
        "2.5": "If the company had difficulty finding new personnel, indicate what the main obstacles were. You can choose up to three factors.",
        "2.7": "Smart working or teleworking is a mode of work performed outside the company's premises using digital tools. Indicate the percentage of staff who perform tasks compatible with this mode.",
        "2.8": "Indicate the actual percentage of staff who worked remotely at least one day a week in the specified period. Answer with a number (e.g., 15).",
        "2.9": "Indicate the main reasons that prevent or limit the use of remote work in your company. You can choose up to four factors.",
        "2.12": "Indicate if the company has organized or financed training courses for staff, excluding those mandatory by law (e.g., workplace safety).",

        # --- SECTION 2: ONLY 10+ EMPLOYEES ---
        "X2.3": "Indicate which channels you used to find and hire new personnel. You can choose more than one option.",
        "X2.6": "Describe the practices implemented to make the company attractive to talent and to retain qualified staff already present. You can select multiple options.",
        "X2.10_intro": "For the following digital skills, first evaluate if they are important for your business (Yes/No) and then if your staff possesses them at an adequate level.",
        "X2.11": "Indicate which personnel management tools were used, such as performance-based incentives or periodic evaluation systems. You can choose more than one option.",
        "X2.13": "If you have conducted non-compulsory training, specify what type. Answer 'yes' or 'no' for each option.",
        "X2.14": "Indicate the percentage range of employees who participated in at least one non-compulsory training course in 2022.",

        # --- SECTION 3: 10+ and 3-9 EMPLOYEES ---
        "3.1": "Indicate if the company has had collaboration or exchange relationships with other external entities, either as a customer (job order) or as a supplier (supply/contracting). Answer 'yes' or 'no' for each type of relationship.",
        "3.4_1": "Indicate the main reasons that led the company to order goods/services from third parties. You can choose up to three options.",
        "3.4_2": "Indicate the main reasons that led the company to supply goods/services to others. You can choose up to three options.",
        "3.6": "Describe the main difficulties encountered when trying to establish new collaborations with other companies. You can choose up to three options.",
        "3.7": "A supply chain is the set of activities that bring a product to the final consumer. Indicate the 'macro-sectors' in which your company operates. You can choose multiple options.",

        # --- SECTION 3: ONLY 10+ EMPLOYEES ---
        "3.2_1": "For job orders (purchases), indicate with whom you had relationships (e.g., other group companies, universities, etc.). You can choose more than one option.",
        "X3.3_1": "Indicate for which business functions you used external job orders. You can choose more than one option.",
        "X3.5_1": "Indicate the number of subjects from whom you purchased goods/services under a job order.",
        "3.8_intro": "Think about the good or service that represents the highest purchase cost for your company. Evaluate how much your company can influence its price, quality, and quantity.",
        "3.9_intro": "Think about the good or service that generates the most revenue for your company. Evaluate how much your company can influence its price, quality, and quantity."
    }
}


# ------------------------------------------------------------------------------
# STRUTTURA PER LE DOMANDE PRELIMINARI (LINGUA E DIMENSIONE AZIENDA)
# QUESTE VENGONO POSTE PRIMA DI INIZIARE IL QUESTIONARIO VERO E PROPRIO
# ------------------------------------------------------------------------------
preliminary_questions = [
    {
        "id": "LANG_SELECT",
        "question": {
            "it": "Benvenuto / Welcome\n\n"
                  "Seleziona la lingua / Select the language\n"
                  "*(scrivi 'italiano' o 'english')*",
            "en": "Benvenuto / Welcome\n\n"
                  "Seleziona la lingua / Select the language\n"
                  "*(type 'italiano' or 'english')*"
        },
        "question_type": "language_selection",
        "next_question_default": "WELCOME_MESSAGE" # Punta al nuovo messaggio di benvenuto
    },
     {
        "id": "WELCOME_MESSAGE",
        "question": {
            "it": "🇮🇹 *Benvenuto nel questionario ISTAT per il Censimento Permanente delle Imprese.*\n\n"
                  "Questo bot ti guiderà nella compilazione.\n\n"
                  "➡️ Per rispondere, digita il *numero* dell'opzione che vuoi selezionare.\n"
                  "➡️ Per interrompere in qualsiasi momento, scrivi `stop`.\n"
                  "➡️ Se hai bisogno di aiuto su una domanda, scrivi `aiuto`.\n\n"
                  "Quando sei pronto, digita `sì` o `procedi` per continuare.",
            "en": "🇬🇧 *Welcome to the ISTAT questionnaire for the Permanent Census of Economic Units.*\n\n"
                  "This bot will guide you through the compilation.\n\n"
                  "➡️ To answer, type the *number* of the option you want to select.\n"
                  "➡️ To stop at any time, type `stop`.\n"
                  "➡️ If you need help with a question, type `help`.\n\n"
                  "When you are ready, type `yes` or `proceed` to continue."
        },
        "question_type": "confirmation",
        "next_question_default": "COMPANY_SIZE_SELECT"
    },
    {
        "id": "COMPANY_SIZE_SELECT",
        "question": {
            "it": "Per continuare, indica la dimensione della tua impresa:\n\n"
                  "1. Da 3 a 9 addetti\n"
                  "2. 10 o più addetti\n\n"
                  "Digita `1` o `2`.",
            "en": "To continue, please indicate your company's size:\n\n"
                  "1. From 3 to 9 employees\n"
                  "2. 10 or more employees\n\n"
                  "Type `1` or `2`."
        },
        "question_type": "company_size_selection",
        "next_question_default": "INTRO" # Il resto del flusso rimane invariato
    },
    {
        "id": "INTRO",
        "question": {
            "it": "Perfetto. Il questionario sta per iniziare.\n\nDigita 'sì' per confermare e procedere.",
            "en": "Perfect. The questionnaire is about to begin.\n\nType 'yes' to confirm and proceed."
        },
        "question_type": "confirmation",
        # 'next_question_default' sarà il primo ID del questionario scelto
        # che il motore del bot gestirà dinamicamente
    }
]


# ------------------------------------------------------------------------------
# DEFINIZIONE DEGLI ALBERI DELLE DOMANDE (PER ORA VUOTI)
# QUI VERRANNO INSERITE LE DOMANDE DELLE SEZIONI 1-3 NELLE PROSSIME PARTI
# ------------------------------------------------------------------------------

# QUESTIONARIO PER AZIENDE CON 10+ ADDETTI
question_tree_10_plus = [
    # ------------------- SEZIONE 1 – PROPRIETÀ, CONTROLLO E GESTIONE -------------------
    {
        "id": "1.1",
        "section": "1",
        "question": {
            "it": "1.1 Ad oggi l'impresa è, direttamente o indirettamente, controllata da una persona fisica o una famiglia?",
            "en": "1.1 As of this date, is the company directly or indirectly controlled by a natural person or a family?"
        },
        "notes": {
            "it": "Nota: Il controllo si sostanzia nella capacità di stabilire le politiche operative, finanziarie e produttive.",
            "en": "Note: The control take the form of the ability to establish operational, financial and production policies."
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "X1.4_intro"}, # Salta alla domanda X1.4 se la risposta è "No"
        "next_question_default": "1.2"
    },
    {
        "id": "1.2",
        "section": "1",
        "question": {
            "it": "1.2 Chi ha la responsabilità della gestione dell'impresa?",
            "en": "1.2 Who is in charge of managing the company?"
        },
        "notes": {
            "it": "Nota: Per 'famiglia controllante' si intende una famiglia in possesso di una quota del capitale d'impresa superiore al 50% che ne permette il controllo dell'attività.",
            "en": "Note: 'Controlling family' means a family holding more than 50% of the company's share capital granting it control of the activity."
        },
        "question_type": "single_choice",
        "options": [
            "1. L'imprenditore o il socio principale o unico",
            "2. Un membro della famiglia proprietaria o controllante",
            "3. Un manager selezionato all'interno dell'impresa",
            "4. Un manager assunto all'esterno dell'impresa",
            "5. Altro soggetto"
        ],
        "next_question_default": "X1.4_intro" # Procede comunque a X1.4
    },
    # DOMANDA 1.3 ESCLUSA COME DA PDF
    
    # GESTIONE DELLA TABELLA X1.4
    # La trasformiamo in un'introduzione seguita da una serie di domande.
    {
        "id": "X1.4_intro",
        "section": "1",
        "question": {
            "it": "Le prossime domande riguardano il livello di *centralizzazione* delle decisioni strategiche.\n\nPer ogni funzione aziendale che elencherò, indica se le decisioni sono prese in modo:\n\n1. Molto centralizzato\n2. Abbastanza centralizzato\n3. Poco centralizzato\n4. Per nulla centralizzato",
            "en": "The next questions are about the level of *centralization* of strategic decisions.\n\nFor each business function I will list, please indicate if decisions are made in a way that is:\n\n1. A lot centralized\n2. Enough centralized\n3. A little centralized\n4. Not at all centralized"
        },
        "question_type": "display_only",
        "next_question_default": "X1.4_a"
    },
    {
        "id": "X1.4_a",
        "section": "1",
        "question": {
            "it": "X1.4 a. Attività principale",
            "en": "X1.4 a. Main activity"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_b"
    },
    {
        "id": "X1.4_b",
        "section": "1",
        "question": {
            "it": "X1.4 b. Funzioni di supporto",
            "en": "X1.4 b. Support functions"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_c"
    },
    {
        "id": "X1.4_c",
        "section": "1",
        "question": {
            "it": "X1.4 c. Approvvigionamento",
            "en": "X1.4 c. Procurement"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_d"
    },
    {
        "id": "X1.4_d",
        "section": "1",
        "question": {
            "it": "X1.4 d. Marketing, vendita e servizi post-vendita",
            "en": "X1.4 d. Marketing, sales and after-sales services"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_e"
    },
    {
        "id": "X1.4_e",
        "section": "1",
        "question": {
            "it": "X1.4 e. Distribuzione, trasporto e magazzinaggio",
            "en": "X1.4 e. Distribution, transport and warehousing"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_f"
    },
    {
        "id": "X1.4_f",
        "section": "1",
        "question": {
            "it": "X1.4 f. Amministrazione/finanza",
            "en": "X1.4 f. Administration/finances"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_g"
    },
    {
        "id": "X1.4_g",
        "section": "1",
        "question": {
            "it": "X1.4 g. Ricerca e sviluppo, innovazione, progettazione",
            "en": "X1.4 g. Research and development, innovation, design"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_h"
    },
    {
        "id": "X1.4_h",
        "section": "1",
        "question": {
            "it": "X1.4 h. Tecnologie informatiche (ICT)",
            "en": "X1.4 h. ICT"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "X1.4_i"
    },
    {
        "id": "X1.4_i",
        "section": "1",
        "question": {
            "it": "X1.4 i. Gestione e formazione delle risorse umane",
            "en": "X1.4 i. Human resources management and training"
        },
        "question_type": "single_choice",
        "options": ["1. Molto", "2. Abbastanza", "3. Poco", "4. Per nulla"],
        "next_question_default": "1.5"
    },
    {
        "id": "1.5",
        "section": "1",
        "question": {
            "it": "1.5 L'impresa appartiene a un gruppo?",
            "en": "1.5 Does the company belong to a group?"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "next_question_default": "X1.6_intro"
    },
    # GESTIONE TABELLA X1.6 e X1.6.1
    # Verrà gestita come una serie di domande a due parti.
    # Prima si chiede se l'obiettivo è stato perseguito (Sì/No).
    # Se Sì, si chiede l'esito.
    {
        "id": "X1.6_intro",
        "section": "1",
        "question": {
            "it": "Ora ti farò una serie di domande sugli obiettivi strategici perseguiti nel biennio 2021-2022. Per ogni obiettivo, prima indica se è stato perseguito (Sì/No), e in caso affermativo, quale è stato l'esito.",
            "en": "Now I will ask a series of questions about the strategic objectives pursued in the 2021-2022 period. For each objective, first indicate if it was pursued (Yes/No), and if so, what the outcome was."
        },
        "question_type": "display_only",
        "next_question_default": "X1.6_1"
    },
    {
        "id": "X1.6_1",
        "section": "1",
        "question": {
            "it": "X1.6 Obiettivo 1: Difendere la propria posizione competitiva. È stato perseguito? (Sì/No)",
            "en": "X1.6 Objective 1: Defending its competitive position. Was it pursued? (Yes/No)"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "X1.6_2"}, # Se No, salta al prossimo obiettivo
        "next_question_default": "X1.6.1_1" # Se Sì, chiedi l'esito
    },
    {
        "id": "X1.6.1_1",
        "section": "1",
        "question": {
            "it": "X1.6.1 Esito per 'Difendere la propria posizione competitiva':",
            "en": "X1.6.1 Outcome for 'Defending its competitive position':"
        },
        "question_type": "single_choice",
        "options": [
            "1. Obiettivo pienamente raggiunto",
            "2. Obiettivo in parte raggiunto",
            "3. Obiettivo non raggiunto"
        ],
        "next_question_default": "X1.6_2"
    },
    # E così via per tutti gli obiettivi da 2 a 12...
    # Per brevità, qui mostro solo l'obiettivo 2 e 12 per illustrare lo schema ripetitivo.
    # Il codice completo includerà tutti gli obiettivi.
    {
        "id": "X1.6_2",
        "section": "1",
        "question": {
            "it": "X1.6 Obiettivo 2: Ampliare la gamma di beni e/o servizi offerti. È stato perseguito? (Sì/No)",
            "en": "X1.6 Objective 2: Expanding the range of goods and/or services offered. Was it pursued? (Yes/No)"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "X1.6_3"},
        "next_question_default": "X1.6.1_2"
    },
    {
        "id": "X1.6.1_2",
        "section": "1",
        "question": {
            "it": "X1.6.1 Esito per 'Ampliare la gamma di beni e/o servizi offerti':",
            "en": "X1.6.1 Outcome for 'Expanding the range of goods and/or services offered':"
        },
        "question_type": "single_choice",
        "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"],
        "next_question_default": "X1.6_3"
    },
    
    # CODICE DA INSERIRE AL POSTO DEI PLACEHOLDER PER X1.6
    {
        "id": "X1.6_3",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 3: Accedere a nuovi segmenti di mercato. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 3: Gaining access to new market segments. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_4"}, "next_question_default": "X1.6.1_3"
    },
    {
        "id": "X1.6.1_3",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Accedere a nuovi segmenti di mercato':", "en": "X1.6.1 Outcome for 'Gaining access to new market segments':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_4"
    },
    {
        "id": "X1.6_4",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 4: Aumentare l'attività all'estero. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 4: Increasing activity abroad. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_5"}, "next_question_default": "X1.6.1_4"
    },
    {
        "id": "X1.6.1_4",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Aumentare l'attività all'estero':", "en": "X1.6.1 Outcome for 'Increasing activity abroad':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_5"
    },
    {
        "id": "X1.6_5",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 5: Aumentare l'attività in Italia. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 5: Increasing activity in Italy. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_6"}, "next_question_default": "X1.6.1_5"
    },
    {
        "id": "X1.6.1_5",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Aumentare l'attività in Italia':", "en": "X1.6.1 Outcome for 'Increasing activity in Italy':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_6"
    },
    {
        "id": "X1.6_6",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 6: Riportare all'interno dell'impresa attività precedentemente esternalizzate. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 6: Bringing previously outsourced activities back into the company. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_7"}, "next_question_default": "X1.6.1_6"
    },
    {
        "id": "X1.6.1_6",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Riportare attività esternalizzate':", "en": "X1.6.1 Outcome for 'Bringing previously outsourced activities back':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_7"
    },
    {
        "id": "X1.6_7",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 7: Ridimensionare l'attività all'estero (downsizing). È stato perseguito? (Sì/No)", "en": "X1.6 Objective 7: Downsizing activity abroad. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_8"}, "next_question_default": "X1.6.1_7"
    },
    {
        "id": "X1.6.1_7",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Ridimensionare l'attività all'estero':", "en": "X1.6.1 Outcome for 'Downsizing activity abroad':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_8"
    },
    {
        "id": "X1.6_8",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 8: Ridimensionare l'attività in Italia. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 8: Downsizing activity in Italy. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_9"}, "next_question_default": "X1.6.1_8"
    },
    {
        "id": "X1.6.1_8",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Ridimensionare l'attività in Italia':", "en": "X1.6.1 Outcome for 'Downsizing activity in Italy':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_9"
    },
    {
        "id": "X1.6_9",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 9: Attivare o incrementare le collaborazioni con altre imprese. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 9: Activating or increasing collaborations with other companies. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_10"}, "next_question_default": "X1.6.1_9"
    },
    {
        "id": "X1.6.1_9",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Attivare/incrementare collaborazioni':", "en": "X1.6.1 Outcome for 'Activating/increasing collaborations':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_10"
    },
    {
        "id": "X1.6_10",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 10: Aumentare gli investimenti in nuove tecnologie. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 10: Increasing investments in new technologies. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_11"}, "next_question_default": "X1.6.1_10"
    },
    {
        "id": "X1.6.1_10",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Aumentare investimenti in nuove tecnologie':", "en": "X1.6.1 Outcome for 'Increasing investments in new technologies':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_11"
    },
    {
        "id": "X1.6_11",
        "section": "1",
        "question": {"it": "X1.6 Obiettivo 11: Attivare/incrementare misure per la responsabilità sociale e ambientale. È stato perseguito? (Sì/No)", "en": "X1.6 Objective 11: Activating/increasing measures for social and environmental responsibility. Was it pursued? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X1.6_12"}, "next_question_default": "X1.6.1_11"
    },
    {
        "id": "X1.6.1_11",
        "section": "1",
        "question": {"it": "X1.6.1 Esito per 'Misure di responsabilità sociale e ambientale':", "en": "X1.6.1 Outcome for 'Measures for social and environmental responsibility':"},
        "question_type": "single_choice", "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"], "next_question_default": "X1.6_12"
    },

    {
        "id": "X1.6_12",
        "section": "1",
        "question": {
            "it": "X1.6 Obiettivo 12: Altri obiettivi strategici. È stato perseguito? (Sì/No)",
            "en": "X1.6 Objective 12: Other strategic objectives. Was it pursued? (Yes/No)"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "X1.7"},
        "next_question_default": "X1.6.1_12"
    },
    {
        "id": "X1.6.1_12",
        "section": "1",
        "question": {
            "it": "X1.6.1 Esito per 'Altri obiettivi strategici':",
            "en": "X1.6.1 Outcome for 'Other strategic objectives':"
        },
        "question_type": "single_choice",
        "options": ["1. Obiettivo pienamente raggiunto", "2. Obiettivo in parte raggiunto", "3. Obiettivo non raggiunto"],
        "next_question_default": "X1.7"
    },
    
    {
        "id": "X1.7",
        "section": "1",
        "question": {
            "it": "X1.7 Verso quali obiettivi saranno prevalentemente orientate le strategie dell'impresa durante il triennio 2023-2025? (Scegli una o più opzioni, separandole con una virgola. Es: 1, 4, 11)",
            "en": "X1.7 Towards which objectives will the company's strategies be mainly oriented during the 2023-2025 three-year period? (Choose one or more options, separated by a comma. E.g: 1, 4, 11)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Difendere la propria posizione competitiva",
            "2. Ampliare la gamma di beni e/o servizi offerti",
            "3. Accedere a nuovi segmenti di mercato",
            "4. Aumentare l'attività all'estero",
            "5. Aumentare l'attività in Italia",
            "6. Riportare all'interno dell'impresa attività precedentemente esternalizzate",
            "7. Ridimensionare l'attività all'estero (downsizing)",
            "8. Ridimensionare l'attività in Italia",
            "9. Attivare o incrementare le collaborazioni con altre imprese",
            "10. Aumentare gli investimenti in nuove tecnologie",
            "11. Attivare o incrementare misure finalizzate alla responsabilità sociale ed ambientale",
            "12. Altri obiettivi strategici"
        ],
        "next_question_default": "1.8"
    },
    
    # Le domande 1.8 e 1.9 sono condizionate dalla risposta a 1.1.
    # Il motore del questionario dovrà gestire questo salto.
    # Se l'utente ha risposto No a 1.1, queste domande non vengono poste.
    # La logica di salto in 1.1 ("2": "X1.4_intro") non va direttamente a 1.8.
    # Per ora, la sequenza lineare è questa, la logica di salto la gestirà il motore.
    {
        "id": "1.8",
        "section": "1",
        "question": {
            "it": "1.8 Dal 2016 ad oggi l'impresa ha affrontato almeno un passaggio generazionale? (Questa domanda è mostrata solo se l'impresa è controllata da una persona fisica o famiglia)",
            "en": "1.8 Did the company face at least one generational change from 2016 to date? (This question is only shown if the company is controlled by a natural person or family)"
        },
        "question_type": "single_choice",
        "options": [
            "1. Sì, tra il 2016 e il 2018",
            "2. Sì, tra il 2019 e il 2021",
            "3. Sì, nel 2022",
            "4. No, ma potrebbe affrontarlo entro il 2025",
            "5. No"
        ],
        "jump_rules": {
            "4": "2.1", # Salto alla Sezione 2
            "5": "2.1"  # Salto alla Sezione 2
        },
        "next_question_default": "1.9"
    },
    {
        "id": "1.9",
        "section": "1",
        "question": {
            "it": "1.9 Quali conseguenze ha avuto il passaggio generazionale sul ruolo della famiglia proprietaria o controllante?",
            "en": "1.9 What were the consequences of the generational change on the role of the owning or controlling family?"
        },
        "question_type": "single_choice",
        "options": [
            "1. Rafforzamento del ruolo della famiglia",
            "2. Mantenimento del ruolo della famiglia",
            "3. Riduzione del ruolo della famiglia",
            "4. Perdita del controllo da parte della famiglia"
        ],
        "next_question_default": "2.1" # Fine della Sezione 1
    },
    
    # ------------------- SEZIONE 2 – RISORSE UMANE -------------------
    {
        "id": "2.1",
        "section": "2",
        "question": {
            "it": "2.1 Nel biennio 2021-2022 l'impresa ha acquisito risorse umane?\n(Includere collaboratori esterni con partita IVA. Non considerare i lavoratori che hanno solo modificato la tipologia contrattuale).",
            "en": "2.1 Did the company acquire human resources in the 2021-2022 two-year period?\n(Includes external collaborators with VAT registration number. Do not consider workers who only changed contractual form)."
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "2.5"},
        "next_question_default": "2.2"
    },
    {
        "id": "2.2",
        "section": "2",
        "question": {
            "it": "2.2 Quali tipologie di risorse umane sono state acquisite? (Scegli una o più opzioni, separate da virgola)",
            "en": "2.2 Which types of human resources have been acquired? (Choose one or more options, separated by comma)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Dipendenti con contratto a tempo indeterminato",
            "2. Dipendenti con contratto a tempo determinato",
            "3. Lavoratori con contratto di somministrazione",
            "4. Lavoratori con rapporto di collaborazione (inclusi esterni con P.IVA)"
        ],
        "next_question_default": "X2.3"
    },
    {
        "id": "X2.3",
        "section": "2",
        "question": {
            "it": "X.2.3 Quali modalità ha utilizzato l'impresa per individuare e selezionare le risorse umane acquisite nel 2021-2022? (Scegli una o più opzioni)",
            "en": "X.2.3 Which methods did the company use to identify and select the human resources acquired in the 2021-2022? (Choose one or more options)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Canali informali (conoscenza personale, etc.)",
            "2. Utilizzo di informazioni già disponibili in azienda (CV inviati, etc.)",
            "3. Collaborazione con soggetti autorizzati all'intermediazione (enti bilaterali, scuole, etc.)",
            "4. Ricerca attiva di candidati (annunci su media, sito web, etc.)",
            "5. Agenzie per il lavoro private",
            "6. Agenzie per il lavoro pubbliche (Centri per l'Impiego)",
            "7. Altre modalità"
        ],
        "next_question_default": "2.4"
    },
    {
        "id": "2.4",
        "section": "2",
        "question": {
            "it": "2.4 Nel 2021-2022, quali competenze trasversali l'impresa ha ritenuto più importanti nella selezione? (Indica fino a tre opzioni)",
            "en": "2.4 In the 2021-2022, which transversal skills did the company consider most important in the selection? (Indicate up to three options)"
        },
        "question_type": "multiple_choice_max_3",
        "options": [
            "1. Capacità di anticipare scenari futuri",
            "2. Capacità di risolvere problemi e situazioni critiche",
            "3. Capacità di adattarsi a nuovi contesti e ruoli",
            "4. Capacità di lavorare in gruppo",
            "5. Capacità di comunicare e interagire efficacemente",
            "6. Capacità di elaborare idee innovative e originali",
            "7. Altre competenze trasversali",
            "8. Nessuna competenza trasversale"
        ],
        "next_question_default": "2.5"
    },
    {
        "id": "2.5",
        "section": "2",
        "question": {
            "it": "2.5 Nel 2021-2022, quali sono stati i fattori principali che hanno ostacolato l'acquisizione di risorse umane? (Indica fino a tre fattori)",
            "en": "2.5 In the 2021-2022, what were the main factors that hindered the acquisition of human resources? (Indicate up to three factors)"
        },
        "question_type": "multiple_choice_max_3",
        "options": [
            "1. L'impresa non ha considerato la possibilità di acquisire risorse",
            "2. Incertezza sulla sostenibilità dei costi futuri",
            "3. Difficoltà finanziarie dell'impresa",
            "4. Oneri fiscali e contributivi troppo elevati",
            "5. Mancanza di spazio o problemi logistici",
            "6. Difficoltà nel reperire personale con le competenze trasversali richieste",
            "7. Difficoltà nel reperire personale con le competenze tecniche richieste",
            "8. Difficoltà di accesso a fondi pubblici/incentivi",
            "9. Altri ostacoli",
            "10. Nessun ostacolo"
        ],
        "next_question_default": "X2.6"
    },
    {
        "id": "X2.6",
        "section": "2",
        "question": {
            "it": "X.2.6 Nel 2021-2022, quali pratiche ha utilizzato l'impresa per attrarre e/o trattenere personale qualificato? (Scegli una o più opzioni)",
            "en": "X.2.6 In the 2021-2022, which practices have been used by the company to attract and/or retain qualified staff? (Choose one or more options)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Definizione e negoziazione di percorsi di carriera accelerati",
            "2. Possibilità di incremento salariale",
            "3. Incentivi per auto-formazione e crescita professionale",
            "4. Flessibilità negli orari di lavoro",
            "5. Accesso a benefit aziendali",
            "6. Riconoscimento formale del lavoro svolto",
            "7. Gradi crescenti di autonomia sul lavoro",
            "8. Coinvolgimento nelle decisioni aziendali",
            "9. Cessione di quote societarie, partnership, etc.",
            "10. Altre pratiche",
            "11. Nessuna pratica"
        ],
        "next_question_default": "2.7"
    },
    {
        "id": "2.7",
        "section": "2",
        "question": {
            "it": "2.7 Tra settembre e dicembre 2022, quale percentuale del personale ha svolto un lavoro che poteva essere effettuato anche a distanza (smart working/telelavoro)?",
            "en": "2.7 Between September and December 2022, what percentage of company staff performed a work capable of being undertaken also from remote (smart working/teleworking)?"
        },
        "question_type": "single_choice",
        "options": [
            "1. Nessuno o quasi nessuno, il lavoro svolto necessita della presenza",
            "2. Meno del 15%",
            "3. Tra il 15% e il 30%",
            "4. Tra il 31% e il 50%",
            "5. Oltre il 50%"
        ],
        "jump_rules": {"1": "X2.10_intro"},
        "next_question_default": "2.8"
    },
    {
        "id": "2.8",
        "section": "2",
        "question": {
            "it": "2.8 Tra settembre e dicembre 2022, quale è stata la percentuale del personale che ha lavorato a distanza (smart working/telelavoro) sul totale del personale? (Indica una stima in %)",
            "en": "2.8 Between September and December 2022, what was the percentage of company staff who worked from remote (smart working/teleworking) out of the total staff complement? (Indicate an estimate in %)"
        },
        "question_type": "percentage",
        "next_question_default": "2.9"
    },
    {
        "id": "2.9",
        "section": "2",
        "question": {
            "it": "2.9 Quali fattori impediscono o limitano l'uso del lavoro a distanza? (Indica fino a quattro fattori)",
            "en": "2.9 Which factors prevent or limit the use of work from remote? (Indicate up to four factors)"
        },
        "question_type": "multiple_choice_max_4",
        "options": [
            "1. Assenza di una infrastruttura ICT adeguata nell'impresa",
            "2. Assenza di una connessione affidabile e veloce sul territorio",
            "3. Costi troppo elevati",
            "4. Necessità di rilevanti cambiamenti organizzativi",
            "5. Assenza di normative adeguate",
            "6. Difficoltà nel monitoraggio e valutazione dei risultati",
            "7. Mancanza di competenze digitali tra i lavoratori",
            "8. Preoccupazione per l'impatto negativo sull'efficienza",
            "9. Altri fattori",
            "10. Nessun fattore"
        ],
        "next_question_default": "X2.10_intro"
    },
    # GESTIONE TABELLA X2.10
    {
        "id": "X2.10_intro",
        "section": "2",
        "question": {
            "it": "Ora, per le seguenti competenze digitali, indica se sono state rilevanti per l'attività aziendale nel 2021-2022 e, in caso affermativo, se erano possedute in modo adeguato dal personale.",
            "en": "Now, for the following digital skills, please indicate if they were significant for the company's activities in 2021-2022 and, if so, whether they were adequately possessed by the staff."
        },
        "question_type": "display_only",
        "next_question_default": "X2.10_1"
    },
    {
        "id": "X2.10_1",
        "section": "2",
        "question": {
            "it": "X.2.10 Competenza 1: Ricercare, modificare ed elaborare documenti o dati in formato digitale. Era rilevante? (Sì/No)",
            "en": "X.2.10 Skill 1: Researching, modifying and elaborating documents or data in digital format. Was it significant? (Yes/No)"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "X2.10_2"},
        "next_question_default": "X2.10.1_1"
    },
    {
        "id": "X2.10.1_1",
        "section": "2",
        "question": {
            "it": "X.2.10.1 La competenza 'Ricercare dati' era posseduta in modo adeguato dal personale?",
            "en": "X.2.10.1 Was the 'Researching data' skill adequately possessed by staff?"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "next_question_default": "X2.10_2"
    },
    # ... (Schema da ripetere per le competenze 2, 3, 4) ...
    {
        "id": "X2.10_2",
        "section": "2",
        "question": {
            "it": "X.2.10 Competenza 2: Comunicare via e-mail, collaborare o condividere informazioni. Era rilevante? (Sì/No)",
            "en": "X.2.10 Skill 2: Communicating via e-mail, collaborating or sharing information. Was it significant? (Yes/No)"
        },
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X2.10_3"}, "next_question_default": "X2.10.1_2"
    },
    {
        "id": "X2.10.1_2",
        "section": "2",
        "question": {"it": "X.2.10.1 La competenza 'Comunicare' era posseduta in modo adeguato?", "en": "X.2.10.1 Was the 'Communicating' skill adequately possessed?"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "next_question_default": "X2.10_3"
    },
    {
        "id": "X2.10_3",
        "section": "2",
        "question": {"it": "X.2.10 Competenza 3: Proteggere dati personali e dispositivi. Era rilevante? (Sì/No)", "en": "X.2.10 Skill 3: Protecting personal data and devices. Was it significant? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X2.10_4"}, "next_question_default": "X2.10.1_3"
    },
    {
        "id": "X2.10.1_3",
        "section": "2",
        "question": {"it": "X.2.10.1 La competenza 'Proteggere dati' era posseduta in modo adeguato?", "en": "X.2.10.1 Was the 'Protecting data' skill adequately possessed?"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "next_question_default": "X2.10_4"
    },
    {
        "id": "X2.10_4",
        "section": "2",
        "question": {"it": "X.2.10 Competenza 4: Risolvere problemi tecnico-informatici. Era rilevante? (Sì/No)", "en": "X.2.10 Skill 4: Solving technical-IT problems. Was it significant? (Yes/No)"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "jump_rules": {"2": "X2.11"}, "next_question_default": "X2.10.1_4"
    },
    {
        "id": "X2.10.1_4",
        "section": "2",
        "question": {"it": "X.2.10.1 La competenza 'Risolvere problemi IT' era posseduta in modo adeguato?", "en": "X.2.10.1 Was the 'Solving IT problems' skill adequately possessed?"},
        "question_type": "single_choice", "options": ["1. Sì", "2. No"], "next_question_default": "X2.11"
    },
    {
        "id": "X2.11",
        "section": "2",
        "question": {
            "it": "X.2.11 Quali politiche di retribuzione, gestione e valutazione del personale sono state utilizzate nel 2021-2022? (Scegli una o più opzioni)",
            "en": "X.2.11 Which staff remuneration, management and appraisal policies were resorted to by the company in 2021-2022? (Choose one or more options)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Incentivi basati sui risultati individuali",
            "2. Incentivi basati sui risultati di team/stabilimento",
            "3. Incentivi basati sui risultati complessivi dell'impresa",
            "4. Valutazione periodica delle competenze",
            "5. Mobilità tra funzioni e rotazione delle mansioni",
            "6. Flessibilità dell'orario di lavoro",
            "7. Comunicazione tra lavoratori e proprietà/management",
            "8. Raccolta sistematica di opinioni sui processi produttivi",
            "9. Attività per ridurre il gender gap",
            "10. Altre politiche",
            "11. Nessuna politica specifica"
        ],
        "next_question_default": "2.12"
    },
    {
        "id": "2.12",
        "section": "2",
        "question": {
            "it": "2.12 Nel 2022, l'impresa ha svolto attività di formazione aziendale diversa da quella obbligatoria?",
            "en": "2.12 In 2022, did the company undertake training activity other than the compulsory one?"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "3.1"}, # Salto alla Sezione 3
        "next_question_default": "X2.13"
    },
    {
        "id": "X2.13",
        "section": "2",
        "question": {
            "it": "X.2.13 Nel 2022, quali attività di formazione (diverse da quella obbligatoria) sono state svolte? (Scegli Sì/No per ogni opzione)",
            "en": "X.2.13 In 2022, which training activities (other than compulsory) were carried out by the company? (Choose Yes/No for each option)"
        },
        "question_type": "yes_no_table", # Tipo speciale per gestire questa tabella
        "options": [
            "1. Formazione per neo-assunti",
            "2. Formazione continua del personale",
            "3. Riqualificazione del personale per nuove mansioni",
            "4. Training on the job",
            "5. Altre attività di formazione non obbligatoria"
        ],
        "next_question_default": "X2.14"
    },
    {
        "id": "X2.14",
        "section": "2",
        "question": {
            "it": "X.2.14 Nel 2022, quale percentuale del personale ha partecipato ad almeno un'attività di formazione aziendale (diversa da quella obbligatoria)?",
            "en": "X.2.14 In 2022, what was the staff percentage that took part in at least one company training activity (other than compulsory)?"
        },
        "question_type": "single_choice",
        "options": [
            "1. Meno del 5%",
            "2. Tra il 5% e il 14%",
            "3. Tra il 15% e il 29%",
            "4. Tra il 30% e il 49%",
            "5. 50% e oltre"
        ],
        "next_question_default": "3.1" # Fine Sezione 2
    },

   # ------------------- SEZIONE 3 – RELAZIONI PRODUTTIVE E FILIERE -------------------
    {
        "id": "3.1",
        "section": "3",
        "question": {
            "it": "3.1 Nel 2022 l'impresa ha intrattenuto le seguenti relazioni con altre imprese o enti? (Scegli Sì/No per ogni opzione)",
            "en": "3.1 Did the company entertain relationships with other companies or entities in 2022? (Choose Yes/No for each option)"
        },
        "question_type": "yes_no_table",
        "options": [
            "1. Commessa (l'impresa ha ordinato/acquistato beni o servizi)",
            "2. Fornitura/subfornitura/appalto (l'impresa ha fornito beni o servizi)",
            "3. Accordi formali (consorzio, contratti di rete, etc.)",
            "4. Accordi informali"
        ],
        "jump_if_all_no": "3.6", # Se l'utente risponde 'No' a tutto, salta a 3.6
        "next_question_default": "3.2_intro"
    },
    
    # GESTIONE DELLA TABELLA 3.2, X3.3, 3.4, 3.5
    # Queste domande sono interconnesse e dipendono dalle risposte date in 3.1.
    # Il motore del bot le porrà solo per le relazioni che l'utente ha indicato di avere.
    {
        "id": "3.2_intro",
        "section": "3",
        "question": {
            "it": "Perfetto. Ora approfondiamo le relazioni che hai selezionato.",
            "en": "Perfect. Now let's dive deeper into the relationships you selected."
        },
        "question_type": "display_only",
        "next_question_default": "3.2_1"
    },

    # --- CICLO PER RELAZIONE 1: COMMESSA ---
    # Queste domande verranno poste solo se l'utente ha risposto 'Sì' a 'Commessa' nella 3.1
    {
        "id": "3.2_1",
        "section": "3",
        "question": {
            "it": "Riguardo alla relazione di COMMESSA, con quali soggetti è stata intrattenuta? (Scegli una o più opzioni)",
            "en": "Regarding the JOB ORDER relationship, with which subjects was it entertained? (Choose one or more options)"
        },
        "depends_on": {"id": "3.1", "option_index": 0}, # Dipende dalla prima opzione di 3.1
        "question_type": "multiple_choice",
        "options": [
            "1. Imprese del gruppo in Italia", "2. Imprese del gruppo all'estero",
            "3. Altre imprese in Italia", "4. Altre imprese all'estero",
            "5. Università o centri di ricerca", "6. Pubblica amministrazione", "7. Altri soggetti"
        ],
        "next_question_default": "X3.3_1"
    },
    {
        "id": "X3.3_1",
        "section": "3",
        "question": {
            "it": "Per quali funzioni è stata usata la COMMESSA? (Scegli una o più opzioni)",
            "en": "For which functions was the JOB ORDER used? (Choose one or more options)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Attività principale", "2. R&S, innovazione, design", "3. ICT",
            "4. Approvvigionamento", "5. Distribuzione, trasporto",
            "6. Marketing, vendite", "7. Servizi legali/finanziari", "8. Altra funzione"
        ],
        "next_question_default": "3.4_1"
    },
    {
        "id": "3.4_1",
        "section": "3",
        "question": {
            "it": "Quali sono i motivi principali per la relazione di COMMESSA? (Scegli fino a tre opzioni)",
            "en": "What are the main reasons for the JOB ORDER relationship? (Choose up to three options)"
        },
        "question_type": "multiple_choice_max_3",
        "options": [
            "1. Riduzione dei costi", "2. Sviluppo di nuovi prodotti/processi",
            "3. Accesso a nuove competenze/tecnologie", "4. Maggiore flessibilità organizzativa",
            "5. Accesso a nuovi mercati/clienti", "6. Internazionalizzazione", "7. Altri motivi"
        ],
        "next_question_default": "X3.5_1"
    },
    {
        "id": "X3.5_1",
        "section": "3",
        "question": {
            "it": "Con quanti soggetti è stata intrattenuta la relazione di COMMESSA?",
            "en": "With how many subjects was the JOB ORDER relationship entertained?"
        },
        "question_type": "single_choice",
        "options": ["1. 1", "2. Da 2 a 4", "3. Da 5 a 9", "4. 10 e oltre"],
        "next_question_default": "3.2_2" # Passa al prossimo ciclo di relazione
    },
    
    # --- CICLO PER RELAZIONE 2: FORNITURA/SUBFORNITURA ---
    {
        "id": "3.2_2",
        "section": "3",
        "question": { "it": "Riguardo alla FORNITURA/SUBFORNITURA, con quali soggetti? (Scegli una o più opzioni)", "en": "Regarding SUPPLY/SUBCONTRACTING, with which subjects? (Choose one or more options)" },
        "depends_on": {"id": "3.1", "option_index": 1},
        "question_type": "multiple_choice",
        "options": [
            "1. Imprese del gruppo in Italia", "2. Imprese del gruppo all'estero",
            "3. Altre imprese in Italia", "4. Altre imprese all'estero",
            "5. Università o centri di ricerca", "6. Pubblica amministrazione", "7. Altri soggetti"
        ],
        "next_question_default": "X3.3_2"
    },
    {
        "id": "X3.3_2",
        "section": "3",
        "question": { "it": "Per quali funzioni è stata usata la FORNITURA/SUBFORNITURA?", "en": "For which functions was SUPPLY/SUBCONTRACTING used?" },
        "question_type": "multiple_choice",
        "options": ["1. Attività principale", "2. R&S, innovazione, design", "3. ICT", "4. Approvvigionamento", "5. Distribuzione, trasporto", "6. Marketing, vendite", "7. Servizi legali/finanziari", "8. Altra funzione"],
        "next_question_default": "3.4_2"
    },
    {
        "id": "3.4_2",
        "section": "3",
        "question": { "it": "Quali sono i motivi principali per la FORNITURA/SUBFORNITURA? (Scegli fino a tre opzioni)", "en": "What are the main reasons for SUPPLY/SUBCONTRACTING? (Choose up to three options)" },
        "question_type": "multiple_choice_max_3",
        "options": ["1. Riduzione dei costi", "2. Sviluppo di nuovi prodotti/processi", "3. Accesso a nuove competenze/tecnologie", "4. Maggiore flessibilità organizzativa", "5. Accesso a nuovi mercati/clienti", "6. Internazionalizzazione", "7. Altri motivi"],
        "next_question_default": "X3.5_2"
    },
    {
        "id": "X3.5_2",
        "section": "3",
        "question": { "it": "Con quanti soggetti è stata intrattenuta la relazione di FORNITURA/SUBFORNITURA?", "en": "With how many subjects was the SUPPLY/SUBCONTRACTING relationship entertained?" },
        "question_type": "single_choice",
        "options": ["1. 1", "2. Da 2 a 4", "3. Da 5 a 9", "4. 10 e oltre"],
        "next_question_default": "3.2_3"
    },
    
    # --- CICLO PER RELAZIONE 3: ACCORDI FORMALI ---
    # ... segue lo stesso schema ...
    {
        "id": "3.2_3",
        "section": "3",
        "question": { "it": "Riguardo agli ACCORDI FORMALI, con quali soggetti?", "en": "Regarding FORMAL AGREEMENTS, with which subjects?" },
        "depends_on": {"id": "3.1", "option_index": 2},
        "question_type": "multiple_choice", "options": ["1. Imprese del gruppo in Italia", "2. Imprese del gruppo all'estero", "3. Altre imprese in Italia", "4. Altre imprese all'estero", "5. Università o centri di ricerca", "6. Pubblica amministrazione", "7. Altri soggetti"],
        "next_question_default": "X3.3_3"
    },
    {
        "id": "X3.3_3", "section": "3", "question": { "it": "Per quali funzioni sono stati usati gli ACCORDI FORMALI?", "en": "For which functions were FORMAL AGREEMENTS used?" }, "question_type": "multiple_choice", "options": ["1. Attività principale", "2. R&S, innovazione, design", "3. ICT", "4. Approvvigionamento", "5. Distribuzione, trasporto", "6. Marketing, vendite", "7. Servizi legali/finanziari", "8. Altra funzione"], "next_question_default": "3.4_3"
    },
    {
        "id": "3.4_3", "section": "3", "question": { "it": "Quali sono i motivi principali per gli ACCORDI FORMALI? (Scegli fino a tre opzioni)", "en": "What are the main reasons for FORMAL AGREEMENTS? (Choose up to three options)" }, "question_type": "multiple_choice_max_3", "options": ["1. Riduzione dei costi", "2. Sviluppo di nuovi prodotti/processi", "3. Accesso a nuove competenze/tecnologie", "4. Maggiore flessibilità organizzativa", "5. Accesso a nuovi mercati/clienti", "6. Internazionalizzazione", "7. Altri motivi"], "next_question_default": "X3.5_3"
    },
    {
        "id": "X3.5_3", "section": "3", "question": { "it": "Con quanti soggetti sono stati intrattenuti ACCORDI FORMALI?", "en": "With how many subjects were FORMAL AGREEMENTS entertained?" }, "question_type": "single_choice", "options": ["1. 1", "2. Da 2 a 4", "3. Da 5 a 9", "4. 10 e oltre"], "next_question_default": "3.2_4"
    },
    
    # --- CICLO PER RELAZIONE 4: ACCORDI INFORMALI ---
    # ... segue lo stesso schema ...
    {
        "id": "3.2_4",
        "section": "3",
        "question": { "it": "Riguardo agli ACCORDI INFORMALI, con quali soggetti?", "en": "Regarding INFORMAL AGREEMENTS, with which subjects?" },
        "depends_on": {"id": "3.1", "option_index": 3},
        "question_type": "multiple_choice", "options": ["1. Imprese del gruppo in Italia", "2. Imprese del gruppo all'estero", "3. Altre imprese in Italia", "4. Altre imprese all'estero", "5. Università o centri di ricerca", "6. Pubblica amministrazione", "7. Altri soggetti"],
        "next_question_default": "X3.3_4"
    },
    {
        "id": "X3.3_4", "section": "3", "question": { "it": "Per quali funzioni sono stati usati gli ACCORDI INFORMALI?", "en": "For which functions were INFORMAL AGREEMENTS used?" }, "question_type": "multiple_choice", "options": ["1. Attività principale", "2. R&S, innovazione, design", "3. ICT", "4. Approvvigionamento", "5. Distribuzione, trasporto", "6. Marketing, vendite", "7. Servizi legali/finanziari", "8. Altra funzione"], "next_question_default": "3.4_4"
    },
    {
        "id": "3.4_4", "section": "3", "question": { "it": "Quali sono i motivi principali per gli ACCORDI INFORMALI? (Scegli fino a tre opzioni)", "en": "What are the main reasons for INFORMAL AGREEMENTS? (Choose up to three options)" }, "question_type": "multiple_choice_max_3", "options": ["1. Riduzione dei costi", "2. Sviluppo di nuovi prodotti/processi", "3. Accesso a nuove competenze/tecnologie", "4. Maggiore flessibilità organizzativa", "5. Accesso a nuovi mercati/clienti", "6. Internazionalizzazione", "7. Altri motivi"], "next_question_default": "X3.5_4"
    },
    {
        "id": "X3.5_4", "section": "3", "question": { "it": "Con quanti soggetti sono stati intrattenuti ACCORDI INFORMALI?", "en": "With how many subjects were INFORMAL AGREEMENTS entertained?" }, "question_type": "single_choice", "options": ["1. 1", "2. Da 2 a 4", "3. Da 5 a 9", "4. 10 e oltre"],
        "next_question_default": "3.6" # Fine del ciclo delle relazioni
    },
    
    # --- DOMANDE SUCCESSIVE DELLA SEZIONE 3 ---
    {
        "id": "3.6",
        "section": "3",
        "question": {
            "it": "3.6 Quali sono state le principali difficoltà incontrate nell'avviare relazioni con altre imprese o enti? (Scegli fino a tre opzioni)",
            "en": "3.6 What were the main difficulties encountered by the company in initiating relationships with other companies or entities? (Choose up to three options)"
        },
        "question_type": "multiple_choice_max_3",
        "options": [
            "1. Nessuna difficoltà o non interessata",
            "2. Difficoltà associate alla localizzazione",
            "3. Dimensioni aziendali limitate",
            "4. Scarsa disponibilità di partner con i requisiti necessari",
            "5. Barriere legali/regolatorie o oneri burocratici",
            "6. Timore di perdere autonomia decisionale",
            "7. Altre difficoltà"
        ],
        "next_question_default": "3.7_intro"
    },
    {
        "id": "3.7_intro",
        "section": "3",
        "question": {
            "it": "Ora le chiedo di indicare tutte le filiere a cui ritiene che la sua impresa contribuisca maggiormente. Potrà scegliere una o più opzioni dalla lista che segue, separandole con una virgola.",
            "en": "Now, please indicate all the supply chains to which you believe your company contributes the most. You can choose one or more options from the following list, separated by a comma."
        },
        "question_type": "display_only",
        "next_question_default": "3.7"
    },
    {
        "id": "3.7",
        "section": "3",
        "question": {
            "it": "3.7 Indicare le filiere di contribuzione:",
            "en": "3.7 Indicate the supply chains of contribution:"
        },
        "question_type": "multiple_choice_long_list", # Tipo speciale per lista lunga
        "options": [
            "1. Agroalimentare", "2. Arredamento", "3. Abbigliamento/calzature",
            "4. Editoria", "5. Farmaceutica/cura persona", "6. Sanità e assistenza sociale",
            "7. Mezzi di trasporto su gomma", "8. Infrastrutture trasporti su gomma",
            "9. Mezzi di trasporto su acqua", "10. Infrastrutture trasporti su acqua",
            "11. Mezzi di trasporto su rotaia", "12. Infrastrutture trasporti su rotaia",
            "13. Aero-spazio e difesa", "14. Infrastrutture aero-spaziali e difesa",
            "15. App. elettriche/elettroniche uso domestico", "16. App. elettriche industriali/macchine non dedicate",
            "17. Utensileria e minuteria non elettrica", "18. Preziosi", "19. Energia",
            "20. Economia circolare e gestione rifiuti", "21. Servizio idrico", "22. Edilizia",
            "23. Finanza", "24. Turismo e tempo libero", "25. Contenuti audio e audiovisivi",
            "26. Infrastrutture e servizi telecomunicazioni", "27. Istruzione e formazione professionale", "28. Altra filiera"
        ],
        "next_question_default": "3.7.1_intro"
    },
    
    # GESTIONE DOMANDE 3.7.1, 3.8 e 3.9
    # Queste dipendono dalle filiere scelte in 3.7
    {
        "id": "3.7.1_intro",
        "section": "3",
        "question": {
            "it": "Per le prime 4 filiere che ha indicato, fornisca la percentuale di fatturato relativa.",
            "en": "For the first 4 supply chains you indicated, please provide the related turnover percentage."
        },
        "question_type": "display_only",
        "next_question_default": "3.7.1"
    },
    {
        "id": "3.7.1",
        "section": "3",
        "question": {
            "it": "3.7.1 Inserire le percentuali di fatturato per le filiere scelte (es: 'Filiera 1: 50%, Filiera 2: 30%').",
            "en": "3.7.1 Enter the turnover percentages for the chosen supply chains (e.g., 'Supply chain 1: 50%, Supply chain 2: 30%')."
        },
        "question_type": "text", # L'utente scrive testo libero
        "next_question_default": "3.8_intro"
    },
    {
        "id": "3.8_intro",
        "section": "3",
        "question": {
            "it": "Ora, per la filiera con il COSTO più elevato, indichi se è d'accordo o in disaccordo con le seguenti affermazioni.",
            "en": "Now, for the supply chain with the highest COST, please indicate whether you agree or disagree with the following statements."
        },
        "question_type": "display_only",
        "next_question_default": "3.8_A"
    },
    {
        "id": "3.8_A",
        "section": "3",
        "question": {"it": "A. La nostra impresa ha la capacità di influenzare il PREZZO dell'asset acquistato.", "en": "A. Our company has the ability to significantly influence the PRICE of the purchased asset."},
        "question_type": "single_choice", "options": ["1. D'accordo", "2. In disaccordo", "3. Non so"],
        "next_question_default": "3.8_B"
    },
    {
        "id": "3.8_B",
        "section": "3",
        "question": {"it": "B. La nostra impresa ha la capacità di influenzare la QUALITÀ dell'asset acquistato.", "en": "B. Our company has the ability to significantly influence the QUALITY of the purchased asset."},
        "question_type": "single_choice", "options": ["1. D'accordo", "2. In disaccordo", "3. Non so"],
        "next_question_default": "3.8_C"
    },
    {
        "id": "3.8_C",
        "section": "3",
        "question": {"it": "C. La nostra impresa ha la capacità di influenzare la QUANTITÀ dell'asset acquistato.", "en": "C. Our company has the ability to significantly influence the QUANTITY of the purchased asset."},
        "question_type": "single_choice", "options": ["1. D'accordo", "2. In disaccordo", "3. Non so"],
        "next_question_default": "3.9_intro"
    },
    {
        "id": "3.9_intro",
        "section": "3",
        "question": {
            "it": "Infine, per la filiera con il RICAVO più elevato, indichi se è d'accordo o in disaccordo con le seguenti affermazioni.",
            "en": "Finally, for the supply chain with the highest REVENUE, please indicate whether you agree or disagree with the following statements."
        },
        "question_type": "display_only",
        "next_question_default": "3.9_A"
    },
    {
        "id": "3.9_A",
        "section": "3",
        "question": {"it": "A. La nostra impresa ha la capacità di influenzare il PREZZO dell'asset venduto.", "en": "A. Our company has the ability to significantly influence the PRICE of the sold asset."},
        "question_type": "single_choice", "options": ["1. D'accordo", "2. In disaccordo", "3. Non so"],
        "next_question_default": "3.9_B"
    },
    {
        "id": "3.9_B",
        "section": "3",
        "question": {"it": "B. La nostra impresa ha la capacità di influenzare la QUALITÀ dell'asset venduto.", "en": "B. Our company has the ability to significantly influence the QUALITY of the sold asset."},
        "question_type": "single_choice", "options": ["1. D'accordo", "2. In disaccordo", "3. Non so"],
        "next_question_default": "3.9_C"
    },
    {
        "id": "3.9_C",
        "section": "3",
        "question": {"it": "C. La nostra impresa ha la capacità di influenzare la QUANTITÀ dell'asset venduto.", "en": "C. Our company has the ability to significantly influence the QUANTITY of the sold asset."},
        "question_type": "single_choice", "options": ["1. D'accordo", "2. In disaccordo", "3. Non so"],
        "next_question_default": "END_SURVEY" # Fine del questionario per noi
    },
    
    # NODO FINALE
    {
        "id": "END_SURVEY",
        "section": "end",
        "question": {
            "it": "Le sezioni 1, 2 e 3 del questionario sono state completate. Grazie mille per la sua collaborazione!",
            "en": "Sections 1, 2 and 3 of the questionnaire are now complete. Thank you very much for your cooperation!"
        },
        "question_type": "display_only",
        "next_question_default": None # Termina esplicitamente il flusso
    }    
    ]



# QUESTIONARIO PER AZIENDE CON 3-9 ADDETTI
question_tree_3_9 = [
    # ------------------- SEZIONE 1 – PROPRIETÀ, CONTROLLO E GESTIONE -------------------
    {
        "id": "1.1",
        "section": "1",
        "question": {
            "it": "1.1 Ad oggi l'impresa è, direttamente o indirettamente, controllata da una persona fisica o una famiglia?",
            "en": "1.1 As of this date, is the company directly or indirectly controlled by a natural person or a family?"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "1.5"},
        "next_question_default": "1.2"
    },
    {
        "id": "1.2",
        "section": "1",
        "question": {
            "it": "1.2 Chi ha la responsabilità della gestione dell'impresa?",
            "en": "1.2 Who is in charge of managing the company?"
        },
        "question_type": "single_choice",
        "options": [
            "1. L'imprenditore o il socio principale o unico",
            "2. Un membro della famiglia proprietaria o controllante",
            "3. Un manager selezionato all'interno dell'impresa",
            "4. Un manager assunto all'esterno dell'impresa",
            "5. Altro soggetto"
        ],
        "next_question_default": "S1.3"
    },
    {
        "id": "S1.3",
        "section": "1",
        "question": {
            "it": "S1.3 Da chi vengono prese le decisioni strategiche all'interno dell'impresa? (Scegli una o più opzioni)",
            "en": "S1.3 By whom are strategic decisions taken within the company? (Choose one or more of the following options)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Esclusivamente dall'imprenditore",
            "2. Dall'imprenditore di concerto con dirigenti/manager",
            "3. Dall'imprenditore di concerto con i familiari",
            "4. Dall'imprenditore dopo averne discusso con i dipendenti",
            "5. Altro"
        ],
        "next_question_default": "1.5"
    },
    {
        "id": "1.5",
        "section": "1",
        "question": {
            "it": "1.5 L'impresa appartiene a un gruppo?",
            "en": "1.5 Does the company belong to a group?"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "next_question_default": "1.8" # Le domande X1.6 e X1.7 sono assenti in questa versione
    },
    {
        "id": "1.8",
        "section": "1",
        "question": {
            "it": "1.8 Dal 2016 ad oggi l'impresa ha affrontato almeno un passaggio generazionale? (Mostrata solo se controllata da persona fisica/famiglia)",
            "en": "1.8 Did the company face at least one generational change from 2016 to date? (Only shown if controlled by a natural person/family)"
        },
        "depends_on": {"id": "1.1", "option_index": 0}, # Dipende dalla risposta 'Sì' (opzione 1) a 1.1
        "question_type": "single_choice",
        "options": [
            "1. Sì, tra il 2016 e il 2018", "2. Sì, tra il 2019 e il 2021", "3. Sì, nel 2022",
            "4. No, ma potrebbe affrontarlo entro il 2025", "5. No"
        ],
        "jump_rules": {"4": "2.1", "5": "2.1"},
        "next_question_default": "1.9"
    },
    {
        "id": "1.9",
        "section": "1",
        "question": {
            "it": "1.9 Quali conseguenze ha avuto il passaggio generazionale sul ruolo della famiglia proprietaria o controllante?",
            "en": "1.9 What were the consequences of the generational change on the role of the owning or controlling family?"
        },
        "depends_on": {"id": "1.1", "option_index": 0}, # Anche questa dipende da 1.1
        "question_type": "single_choice",
        "options": [
            "1. Rafforzamento del ruolo della famiglia", "2. Mantenimento del ruolo della famiglia",
            "3. Riduzione del ruolo della famiglia", "4. Perdita del controllo da parte della famiglia"
        ],
        "next_question_default": "2.1"
    },
    
    # ------------------- SEZIONE 2 – RISORSE UMANE -------------------
    # La sezione 2 per 3-9 addetti è quasi identica, ma mancano alcune domande X
    {
        "id": "2.1",
        "section": "2",
        "question": {
            "it": "2.1 Nel biennio 2021-2022 l'impresa ha acquisito risorse umane?",
            "en": "2.1 Did the company acquire human resources in the 2021-2022 two-year period?"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "jump_rules": {"2": "2.5"},
        "next_question_default": "2.2"
    },
    {
        "id": "2.2",
        "section": "2",
        "question": {
            "it": "2.2 Quali tipologie di risorse umane sono state acquisite? (Scegli una o più opzioni)",
            "en": "2.2 Which types of human resources have been acquired? (Choose one or more options)"
        },
        "question_type": "multiple_choice",
        "options": [
            "1. Dipendenti con contratto a tempo indeterminato", "2. Dipendenti con contratto a tempo determinato",
            "3. Lavoratori con contratto di somministrazione", "4. Lavoratori con rapporto di collaborazione"
        ],
        "next_question_default": "2.4" # Salta la X2.3
    },
    {
        "id": "2.4",
        "section": "2",
        "question": {
            "it": "2.4 Nel 2021-2022, quali competenze trasversali ha ritenuto più importanti? (Indica fino a tre opzioni)",
            "en": "2.4 In 2021-2022, which transversal skills did the company consider most important? (Indicate up to three options)"
        },
        "question_type": "multiple_choice_max_3",
        "options": [
            "1. Capacità di anticipare scenari futuri", "2. Capacità di risolvere problemi",
            "3. Capacità di adattarsi", "4. Capacità di lavorare in gruppo",
            "5. Capacità di comunicare", "6. Capacità di elaborare idee innovative",
            "7. Altre competenze trasversali", "8. Nessuna competenza trasversale"
        ],
        "next_question_default": "2.5"
    },
    {
        "id": "2.5",
        "section": "2",
        "question": {
            "it": "2.5 Quali sono stati i fattori principali che hanno ostacolato l'acquisizione di risorse umane? (Indica fino a tre fattori)",
            "en": "2.5 What were the main factors that hindered the acquisition of human resources? (Indicate up to three factors)"
        },
        "question_type": "multiple_choice_max_3",
        "options": [
            "1. Non considerata la possibilità", "2. Incertezza sui costi futuri",
            "3. Difficoltà finanziarie", "4. Oneri fiscali/contributivi elevati",
            "5. Mancanza di spazio/problemi logistici", "6. Difficoltà a reperire skill trasversali",
            "7. Difficoltà a reperire skill tecniche", "8. Difficoltà accesso a fondi pubblici",
            "9. Altri ostacoli", "10. Nessun ostacolo"
        ],
        "next_question_default": "2.7" # Salta la X2.6
    },
    {
        "id": "2.7",
        "section": "2",
        "question": {
            "it": "2.7 Tra settembre e dicembre 2022, quale percentuale del personale ha svolto un lavoro che poteva essere effettuato anche a distanza?",
            "en": "2.7 Between September and December 2022, what percentage of company staff performed a work capable of being undertaken also from remote?"
        },
        "question_type": "single_choice",
        "options": [
            "1. Nessuno o quasi nessuno", "2. Meno del 15%", "3. Tra il 15% e il 30%",
            "4. Tra il 31% e il 50%", "5. Oltre il 50%"
        ],
        "jump_rules": {"1": "2.12"},
        "next_question_default": "2.8"
    },
    {
        "id": "2.8",
        "section": "2",
        "question": {
            "it": "2.8 Quale è stata la percentuale del personale che ha lavorato a distanza sul totale? (Indica una stima in %)",
            "en": "2.8 What was the percentage of company staff who worked from remote out of the total staff? (Indicate an estimate in %)"
        },
        "question_type": "percentage",
        "next_question_default": "2.9"
    },
    {
        "id": "2.9",
        "section": "2",
        "question": {
            "it": "2.9 Quali fattori impediscono o limitano l'uso del lavoro a distanza? (Indica fino a quattro fattori)",
            "en": "2.9 Which factors prevent or limit the use of work from remote? (Indicate up to four factors)"
        },
        "question_type": "multiple_choice_max_4",
        "options": [
            "1. Assenza infrastruttura ICT", "2. Assenza connessione veloce", "3. Costi troppo elevati",
            "4. Necessità cambiamenti organizzativi", "5. Obblighi onerosi",
            "6. Difficoltà nel monitoraggio", "7. Mancanza competenze digitali",
            "8. Preoccupazione per impatto negativo", "9. Altri fattori", "10. Nessun fattore"
        ],
        "next_question_default": "2.12" # Salta le domande X2.10 e X2.11
    },
    {
        "id": "2.12",
        "section": "2",
        "question": {
            "it": "2.12 Nel 2022, l'impresa ha svolto attività di formazione aziendale diversa da quella obbligatoria?",
            "en": "2.12 In 2022, did the company undertake training activity other than the compulsory one?"
        },
        "question_type": "single_choice",
        "options": ["1. Sì", "2. No"],
        "next_question_default": "3.1" # In questa versione non ci sono le domande X2.13 e X2.14
    },
    
    # ------------------- SEZIONE 3 – RELAZIONI PRODUTTIVE E FILIERE -------------------
    # La sezione 3 è identica nelle domande presenti, quindi riutilizziamo la stessa struttura del 10+
    # ma la copiamo qui per mantenere i due questionari separati e modificabili indipendentemente.
    {
        "id": "3.1",
        "section": "3",
        "question": {"it": "3.1 Nel 2022 l'impresa ha intrattenuto relazioni con altre imprese o enti? (Sì/No per opzione)", "en": "3.1 Did the company entertain relationships with other companies or entities in 2022? (Yes/No per option)"},
        "question_type": "yes_no_table",
        "options": ["1. Commessa", "2. Fornitura/subfornitura", "3. Accordi formali", "4. Accordi informali"],
        "jump_if_all_no": "3.6",
        "next_question_default": "3.2_intro"
    },
    {
        "id": "3.2_intro",
        "section": "3",
        "question": {"it": "Ora, per le relazioni indicate, risponda alle seguenti domande.", "en": "Now, for the indicated relationships, please answer the following questions."},
        "question_type": "display_only",
        "next_question_default": "3.4_1" # La versione 3-9 non ha le domande 3.2, X3.3. Salta direttamente alla 3.4
    },
    # --- CICLO PER RELAZIONE 1: COMMESSA (versione 3-9) ---
    {
        "id": "3.4_1",
        "section": "3",
        "question": {"it": "Quali sono i motivi principali per la COMMESSA? (Scegli fino a tre)", "en": "What are the main reasons for the JOB ORDER? (Choose up to three)"},
        "depends_on": {"id": "3.1", "option_index": 0},
        "question_type": "multiple_choice_max_3",
        "options": ["1. Riduzione costi", "2. Sviluppo nuovi prodotti", "3. Accesso nuove competenze", "4. Flessibilità organizzativa", "5. Accesso nuovi mercati", "6. Internazionalizzazione", "7. Altri motivi"],
        "next_question_default": "3.4_2"
    },
    # --- CICLO PER RELAZIONE 2: FORNITURA (versione 3-9) ---
    {
        "id": "3.4_2",
        "section": "3",
        "question": {"it": "Quali sono i motivi principali per la FORNITURA/SUBFORNITURA? (Scegli fino a tre)", "en": "What are the main reasons for SUPPLY/SUBCONTRACTING? (Choose up to three)"},
        "depends_on": {"id": "3.1", "option_index": 1},
        "question_type": "multiple_choice_max_3",
        "options": ["1. Riduzione costi", "2. Sviluppo nuovi prodotti", "3. Accesso nuove competenze", "4. Flessibilità organizzativa", "5. Accesso nuovi mercati", "6. Internazionalizzazione", "7. Altri motivi"],
        "next_question_default": "3.4_3"
    },
    # --- CICLO PER RELAZIONE 3: ACCORDI FORMALI (versione 3-9) ---
    {
        "id": "3.4_3",
        "section": "3",
        "question": {"it": "Quali sono i motivi principali per gli ACCORDI FORMALI? (Scegli fino a tre)", "en": "What are the main reasons for FORMAL AGREEMENTS? (Choose up to three)"},
        "depends_on": {"id": "3.1", "option_index": 2},
        "question_type": "multiple_choice_max_3",
        "options": ["1. Riduzione costi", "2. Sviluppo nuovi prodotti", "3. Accesso nuove competenze", "4. Flessibilità organizzativa", "5. Accesso nuovi mercati", "6. Internazionalizzazione", "7. Altri motivi"],
        "next_question_default": "3.4_4"
    },
    # --- CICLO PER RELAZIONE 4: ACCORDI INFORMALI (versione 3-9) ---
    {
        "id": "3.4_4",
        "section": "3",
        "question": {"it": "Quali sono i motivi principali per gli ACCORDI INFORMALI? (Scegli fino a tre)", "en": "What are the main reasons for INFORMAL AGREEMENTS? (Choose up to three)"},
        "depends_on": {"id": "3.1", "option_index": 3},
        "question_type": "multiple_choice_max_3",
        "options": ["1. Riduzione costi", "2. Sviluppo nuovi prodotti", "3. Accesso nuove competenze", "4. Flessibilità organizzativa", "5. Accesso nuovi mercati", "6. Internazionalizzazione", "7. Altri motivi"],
        "next_question_default": "3.6"
    },
    {
        "id": "3.6",
        "section": "3",
        "question": {"it": "3.6 Quali sono state le principali difficoltà nell'avviare relazioni? (Scegli fino a tre)", "en": "3.6 What were the main difficulties in initiating relationships? (Choose up to three)"},
        "question_type": "multiple_choice_max_3",
        "options": ["1. Nessuna difficoltà/non interessata", "2. Difficoltà localizzazione", "3. Dimensioni limitate", "4. Scarsità partner", "5. Barriere legali/burocratiche", "6. Timore perdita autonomia", "7. Altre difficoltà"],
        "next_question_default": "3.7_intro"
    },
    {
        "id": "3.7_intro",
        "section": "3",
        "question": {"it": "Indichi le filiere a cui contribuisce.", "en": "Indicate the supply chains you contribute to."},
        "question_type": "display_only",
        "next_question_default": "3.7"
    },
    {
        "id": "3.7",
        "section": "3",
        "question": {"it": "3.7 Indicare le filiere di contribuzione (una o più opzioni):", "en": "3.7 Indicate the supply chains (one or more options):"},
        "question_type": "multiple_choice_long_list",
        "options": ["1. Agroalimentare", "2. Arredamento", "3. Abbigliamento/calzature", "4. Editoria", "5. Farmaceutica/cura persona", "6. Sanità e assistenza sociale", "7. Mezzi trasporto gomma", "8. Infrastrutture trasporti gomma", "9. Mezzi trasporto acqua", "10. Infrastrutture trasporti acqua", "11. Mezzi trasporto rotaia", "12. Infrastrutture trasporti rotaia", "13. Aero-spazio e difesa", "14. Infrastrutture aero-spaziali", "15. App. elettriche/elettroniche", "16. App. elettriche industriali", "17. Utensileria non elettrica", "18. Preziosi", "19. Energia", "20. Economia circolare/rifiuti", "21. Servizio idrico", "22. Edilizia", "23. Finanza", "24. Turismo e tempo libero", "25. Contenuti audio/video", "26. Telecomunicazioni", "27. Istruzione/formazione", "28. Altra filiera"],
        "next_question_default": "END_SURVEY" # Le domande 3.7.1, 3.8, 3.9 non sono presenti nella versione 3-9
    },
    # NODO FINALE PER 3-9
    {
        "id": "END_SURVEY",
        "section": "end",
        "question": {"it": "Le sezioni 1, 2 e 3 sono state completate. Grazie per la collaborazione!", "en": "Sections 1, 2 and 3 are complete. Thank you for your cooperation!"},
        "question_type": "display_only",
        "next_question_default": None
    }
]
