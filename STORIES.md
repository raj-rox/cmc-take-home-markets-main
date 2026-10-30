# Stories: classifying a change everywhere a product is licensed

## The journey today

Today an impact assessment is a position no system holds. It runs on documents, spreadsheets and institutional memory. To answer "what does this change mean everywhere we're licensed?", the regulatory lead interviews the villages: the registration spreadsheet, the country matrix, the affiliate who remembers how Brazil treats biologics.

**Who is involved**
- **Change owner:** QA or manufacturing at the site.
- **RA CMC lead:** owns the assessment.
- **Regional RA:** knows a market's rules and confirms its classification.
- **RA operations:** keeps the record of where products are licensed.

| # | Step | Who | Today it lives in… | Where it goes wrong |
|---|---|---|---|---|
| 1 | A change is raised: new supplier, new site, tighter spec. RA is asked for its regulatory impact. | Change owner → RA CMC lead | A change request in the quality system | *Trigger only; out of scope.* |
| 2 | Find the products the change touches. | RA CMC lead | Product and manufacturing data | A product is missed because the link lives in someone's head. Already covered by `Change → Product` in the worked example. |
| 3 | Find where each product is licensed, and which markets each licence covers. | RA CMC lead with RA operations | A registration spreadsheet | The spreadsheet doesn't know what a licence is. One EU centralised licence covers every EU and EEA market: Norway gets dropped, or Germany is counted twice. Whether the product is synthetic or biological, which decides Brazil's rules, isn't recorded. |
| 4 | Find whose rules apply to each licence. | RA CMC lead with regional RA | A country matrix and the memory of whoever was in the room | Assumptions harden into fact. "Cambodia follows ASEAN" is assumed, though the primary sources don't establish it. "UK = EU" is assumed, though the UK still runs the pre-2024 EU rules. US drug categories get used for a biologic. |
| 5 | Classify the change for each product in each market, and say why. The US and EU are usually done first, then other markets follow. | RA CMC lead drafts; regional RA confirms | A spreadsheet cell and an email thread | Same label, different rules: the EU's "IB" is copied to Switzerland or South Africa. Codes are made up where no list exists. The reasoning lives in an inbox. |
| 6 | Review the impact as a whole: which markets need prior approval, which only need notifying, which need nothing. | RA CMC lead → change board | The finished spreadsheet | A blank cell reads as "no impact". Nobody can see at a glance which markets need prior approval. |

Everything after step 6, planning and preparing the filings, is out of scope.

**What the system must defend.** The assessment becomes an object the system holds the meaning of. It knows:
- what each licence covers;
- whose rules apply to it;
- which categories those rules allow.

It refuses a category from the wrong rules, and it never lets an unknown read as "no impact".

*Source: the failure modes in steps 3–5 come from the evidence (E2–E5). The roles and the order of work are general industry practice, to be validated with RA users (see MEMO.md, open questions).*

## Terms

These words name the concepts in the model and are used with one meaning throughout.

- **Market:** a country where a product can be licensed (Germany, Norway, Singapore).
- **Regulator:** the body that grants licences and receives filings. A regulator acts for one or more markets: BfArM for Germany; the European Commission for every EU and EEA market.
- **Licence:** a product's authorisation from one regulator, covering one or more markets.
- **Rule set:** a published scheme of reporting categories, such as EU Regulation 1234/2008 or Brazil RDC 73/2016. It applies in given markets to a given type of product (synthetic or biological).
- **Reporting category:** one category within one rule set (EU `IB`, UK `IB`, Singapore `MIV-1`). It has a **filing route**: what the category requires.
- **Filing route:** one of these:
  - prior approval
  - notify then wait
  - notify at implementation
  - do and document
  - no filing
  - new application
- **Classification:** what the user records for one product in one market on one change.

## Stories

### S1. Record what a licence covers
*As RA operations, I record each licence a product holds: which regulator granted it and which markets it covers. Every assessment then starts from the real footprint.*

- **AC1.1** A licence names one product, one regulator and at least one market.
- **AC1.2** A licence can only cover markets its regulator acts for. A European Commission licence can cover Germany, France and Norway. An MHRA licence cannot cover Germany.
- **AC1.3** A product has at most one licence covering any one market. Recording a German national licence for a product that already has an EU centralised licence is rejected.
- **AC1.4** A centralised licence is one record covering many markets, not one record per market.

### S2. See whose rules apply to a licence
*As the RA CMC lead, for each licence I see the rule set that applies in each market it covers. I never classify against the wrong rules.*

- **AC2.1** The rule set is worked out from the market and whether the product is synthetic or biological. The user never chooses it.
- **AC2.2** In Brazil, a synthetic product gets RDC 73/2016 and a biological product gets RDC 913/2024.
- **AC2.3** A UK licence gets the MHRA rule set. A Swiss licence gets the Swissmedic rule set. Neither gets the EU rule set.
- **AC2.4** A German national licence and an EU centralised licence covering Germany get the same EU rule set.
- **AC2.5** Where no rule set is established, the system shows "rule set unknown" and does not fall back to the ASEAN guideline. These markets are Cambodia, Lao PDR, Myanmar and Timor-Leste, and US or Argentine biologics.

### S3. See the categories a rule set allows
*As the RA CMC lead, I see every reporting category in the applicable rule set, with its filing route and the document it comes from. I pick from the real list, not from memory.*

- **AC3.1** Each reporting category belongs to exactly one rule set. UK `IB` and EU `IB` are separate categories, even though their codes match.
- **AC3.2** Each reporting category has exactly one filing route.
- **AC3.3** Tools that are not categories are not offered as categories: comparability protocols, PACMPs, EU Article 5 requests, South Africa's Z-code and reliance codes.
- **AC3.4** Each rule set shows its governing document and edition. For example, the UK shows the 2013 EU classification guideline and the EU shows Guideline C/2025/5045.

### S4. Get the full list of lines to classify
*As the RA CMC lead, when I open a change I get one line for every market where each affected product is licensed. Nothing is missed and nothing is counted twice.*

- **AC4.1** Take a change touching one product licensed by the FDA and by the European Commission (centralised). It has lines for the United States, Germany, France and Norway, each exactly once.
- **AC4.2** An affected product with no licence recorded is flagged on the change. It is not silently left out.
- **AC4.3** If a licence is added after classification started, its new markets appear as lines still to classify.

### S5. Classify a line
*As the RA CMC lead, I record a reporting category and my reasoning for a product in a market. As regional RA, I can review that reasoning.*

- **AC5.1** The category must belong to the rule set that applies to that line. Recording EU `IB` on a Swiss line is rejected.
- **AC5.2** The reasoning is required, for example the guideline condition met.
- **AC5.3** The line's filing route is the category's filing route, shown, not re-entered.
- **AC5.4** Under a licence covering several markets, every market gets the same category. Germany and France under one centralised licence cannot be classified differently.

### S6. Say why a line has no category
*As the RA CMC lead, when a line can't be classified or the change doesn't touch that licence, I record that explicitly with a reason. A blank never means "no impact".*

- **AC6.1** A line is in one of three states:
  - **not yet classified** (the default)
  - **classified** (has a category)
  - **not affected** (the change doesn't touch what this licence registers; a reason is required)
- **AC6.2** A line whose rule set is unknown cannot be classified. It stays visible as not yet classified, showing "rule set unknown".
- **AC6.3** "Not affected" is different from a "no filing" category. Singapore's `NO-NOTIFICATION` is a classification. "This site isn't registered in Mexico" is "not affected".

### S7. Review the impact as a whole
*As the RA CMC lead presenting to the change board, I see every product and market on the change with its category and filing route. I can show which markets need prior approval and that nothing has been left out.*

- **AC7.1** The view shows product, market, regulator, category and filing route for every line.
- **AC7.2** The assessment counts as complete only when no line is still not yet classified. The number still open is shown.
- **AC7.3** The view can be filtered to the lines whose filing route is prior approval.
