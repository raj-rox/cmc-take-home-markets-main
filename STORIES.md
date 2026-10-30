# Stories: classifying a change everywhere a product is licensed

## The journey today

Today an impact assessment is a position no system holds. It runs on documents, spreadsheets and institutional memory. To answer "what does this change mean everywhere we're licensed?", the regulatory lead pieces it together from scattered sources: the registration spreadsheet, the country matrix, the affiliate who remembers how Brazil treats biologics.

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

*Source: the failure modes in steps 3–5 come from the evidence (E2–E5). The roles and the order of work are general industry practice.*

## Terms

These words name the concepts in the model and are used with one meaning throughout.

- **Market:** a country where a product can be licensed (Germany, Norway, Singapore).
- **Regulator:** the body that grants licences and receives filings. A regulator acts for one or more markets: BfArM for Germany; the European Commission for every EU and EEA market.
- **Licence:** a product's authorisation from one regulator, covering one or more markets.
- **Rule set:** a published scheme of reporting categories, such as EU Regulation 1234/2008 or Brazil RDC 73/2016. It applies in one or more markets, to one or more product types.
- **Product type:** the kind of product a rule set is written for. It comes from a seeded list, currently synthetic and biological.
- **Reporting category:** one category within one rule set (EU `IB`, UK `IB`, Singapore `MIV-1`). It has a **filing route**: what the category requires.
- **Filing route:** what a category requires, defined by when the change may be implemented relative to telling the regulator. One of these:

  | Route | Definition | Examples |
  |---|---|---|
  | Prior approval | File first; implement only once the regulator approves. | US `PAS`, EU `II` |
  | Notify then wait | File first; implement after a set standstill unless the regulator objects. | US `CBE-30`, EU `IB`, Singapore `MIV-2-NOTIFICATION` |
  | Notify at implementation | Implement, then file an individual notification at once or within a set window. | US `CBE-0`, EU `IA_IN`, Singapore `MIV-2-DO-AND-TELL` |
  | Do and document | Implement and record it; report only in a periodic, bundled filing or in the company's own change history. | US `AR` (annual report), EU `IA` (annual update), Brazil `SYN-HMP` |
  | No filing | Never reported to the regulator. | US `PQS-NOFILE`, Singapore `NO-NOTIFICATION` |
  | New application | Can't be filed as a variation at all; needs an extension or new licence application. | EU `EXT`, Saudi `NEW-APP` |

  The test that separates the two "implement first" routes: an individual filing for this change means notify at implementation; a periodic bundle means do and document.
- **Classification:** what the user records for one licence on one change. A licence belongs to one product, so this is per product × licence. It is shown once for each market the licence covers.

## Stories

### S1. Record what a licence covers
*As RA operations, I record each licence a product holds: which regulator granted it and which markets it covers. Every assessment then starts from the real footprint.*

- **AC1.1** A licence names one product, one regulator and at least one market.
- **AC1.2** A licence can only cover markets its regulator acts for. A European Commission licence can cover Germany, France and Norway. An MHRA licence cannot cover Germany.
- **AC1.3** A product has at most one licence covering any one market. Recording a German national licence for a product that already has an EU centralised licence is rejected.
- **AC1.4** Recording one EU centralised licence shows the product as licensed in Germany, France and Norway. Withdrawing that licence removes all three together.
- **AC1.5** All markets a licence covers must share one rule set for that product; otherwise the licence is rejected. An EU centralised licence covering Germany, France and Norway passes, because all three use the EU rule set.

### S2. See whose rules apply to a licence
*As the RA CMC lead, for each licence I see the one rule set that applies to it. I never classify against the wrong rules.*

- **AC2.1** The rule set is worked out from the market and the product's product type. The user never chooses it.
- **AC2.2** In Brazil, a synthetic product gets RDC 73/2016 and a biological product gets RDC 913/2024.
- **AC2.3** A UK licence gets the MHRA rule set. A Swiss licence gets the Swissmedic rule set. Neither gets the EU rule set.
- **AC2.4** A German national licence and an EU centralised licence covering Germany get the same EU rule set.
- **AC2.5** Where no rule set is recorded for a market and product type, the system shows "rule set unknown" and does not fall back to another rule set (such as the ASEAN guideline). Currently: Brunei, Cambodia, Lao PDR, Myanmar, Thailand and Timor-Leste for all products; biologics in Argentina, Singapore, Malaysia, the Philippines, Indonesia and VietNam.
- **AC2.6** No market gets the ASEAN Variation Guideline (AVG) as its rule set unless a primary source shows that market adopts it. Nobody files under the AVG itself; every ASEAN member applies its own scheme.
  - Malaysia gets its own rule set, the Malaysian Variation Guideline (2nd ed., July 2022). It is based on AVG Rev 2, but its `MaV`, `MiV-PA` and `MiV-N` are Malaysia's own categories.
  - The Philippines gets its own rule set, the Philippine Variation Guidelines (V1.0, 2020). Its `MaV`, `MiV-PA` and `MiV-N` are the Philippines' own categories, though they share the AVG's labels. The national `MaV-PH`, `MiV-PH` and `MiV-PH-N` codes it prints are change types within those categories, not extra categories.
  - Singapore, Indonesia and Viet Nam each get their own national rule set (HSA's categories, PerBPOM 24/2017 as amended, Circular 12/2025/TT-BYT).
  - Brunei shows "rule set unknown". The primary source shows only that BDMCA publishes MaV/MiV submission procedures, not that it adopts the AVG or what its full category list is.
  - Thailand shows "rule set unknown" until checked. The Thai FDA cites the AVG "alongside other frameworks", which doesn't establish which categories apply.
- **AC2.7** A product can't be recorded without a product type (synthetic or biological).

### S3. See the categories a rule set allows
*As the RA CMC lead, I see every reporting category in the applicable rule set, with its filing route and the document it comes from. I pick from the real list, not from memory.*

- **AC3.1** Each reporting category belongs to exactly one rule set. UK `IB` and EU `IB` are separate categories, even though their codes match.
- **AC3.2** Each reporting category has exactly one filing route.
- **AC3.3** Tools that are not categories are not offered as categories: comparability protocols, PACMPs, EU Article 5 requests, South Africa's Z-code and reliance codes.
- **AC3.4** Each rule set shows its governing document and edition. For example, the UK shows the 2013 EU classification guideline and the EU shows Guideline C/2025/5045. Each rule set holds only its current edition, with no history. When an edition is replaced, the rule set is updated in place.

### S4. Get the full list of licences to classify
*As the RA CMC lead, when I open a change I get every licence held by each affected product, shown against every market it covers. Nothing is missed and nothing is counted twice.*

- **AC4.1** Take a change touching one product licensed by the FDA and by the European Commission (centralised). It needs two classifications, one per licence, shown as four market rows: United States, Germany, France and Norway, each exactly once.
- **AC4.2** An affected product with no licence recorded is flagged on the change. It is not silently left out.
- **AC4.3** If a licence is added after classification started, it appears as not yet classified.

### S5. Classify a licence
*As the RA CMC lead, I record a reporting category and my reasoning for a licence on a change, so the classification can be defended later.*

- **AC5.1** The category must belong to the licence's rule set. Recording EU `IB` against a Swissmedic licence is rejected.
- **AC5.2** The reasoning is required, for example the guideline condition met.
- **AC5.3** Where a rule set applies, the filing route is the category's filing route, shown, not re-entered. A filing route cannot be typed in directly.
- **AC5.4** A classification is recorded once per licence. Germany and France under one centralised licence show the same category because they share one classification, and cannot be classified differently.

### S6. Say why a licence has no category
*As the RA CMC lead, when a licence can't be given a category, or the change doesn't touch it, I record that explicitly with a reason. A blank never means "no impact".*

- **AC6.1** A classification is in one of three states:
  - **not yet classified** (the default)
  - **classified** (has a filing route, either from a category or, where the rule set is unknown, recorded directly)
  - **not affected** (the change doesn't touch what this licence registers; a reason is required)
- **AC6.2** Where the rule set is unknown, the user can't pick a category, but can record a filing route with reasoning. A Cambodia licence can be recorded as prior approval with reasoning, but no category can be picked.
- **AC6.3** A classification without a category is marked "no category: rule set unknown" wherever it appears. Reviewers can then tell it apart from a category picked from published rules.
- **AC6.4** "Not affected" is different from a "no filing" category. Singapore's `NO-NOTIFICATION` is a category. "This site isn't registered in Mexico" is "not affected".

### S7. Review the impact as a whole
*As the RA CMC lead presenting to the change board, I see every product and market on the change with its category and filing route. I can show which markets need prior approval and that nothing has been left out.*

- **AC7.1** The view has one row per market each licence covers, showing product, market, regulator, category and filing route.
- **AC7.2** The assessment counts as complete only when no classification is still not yet classified and no affected product is missing a licence. The number of licences still open, and of products without a licence, is shown.
- **AC7.3** The view can be filtered to the market rows whose filing route is prior approval. This includes classifications whose route was recorded without a category (AC6.2).
