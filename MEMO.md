# 🧭 MEMO: where a change must be classified
 
> [!TIP]
> A user classifies each **licence** a change touches. The licence's **markets** and the product's **type** decide which **rule set** applies, and the rule set offers the **categories** to pick from.
 
**Colour key:** 🟨 existing · 🟦 reference data (seeded) · 🟩 customer data (written by users)
 
---
 
## 🗺️ The model
 
```mermaid
flowchart LR
  CH[Change]:::existing -- "touches 1..n" --> PR[Product]:::existing
  PR -- "has 1" --> PT[ProductType]:::ref
  LI[Licence]:::txn -- "for 1" --> PR
  LI -- "granted by 1" --> RG[Regulator]:::ref
  LI -- "covers 1..n" --> MK[Market]:::ref
  RG -- "acts for 1..n" --> MK
  RS[RuleSet]:::ref -- "applies in 1..n" --> MK
  RS -- "applies to 1..n" --> PT
  RC[ReportingCategory]:::ref -- "belongs to 1" --> RS
  CL[Classification]:::txn -- "on 1" --> CH
  CL -- "for 1" --> LI
  CL -. "0..1" .-> RC
  classDef existing fill:#FFF4CC,stroke:#C9A400,color:#333
  classDef ref fill:#DCEBFF,stroke:#3B7DD8,color:#333
  classDef txn fill:#DDF5E3,stroke:#2E9E55,color:#333
```
 
## 🧱 Core concepts
 
| | Concept | What it is | Why it exists |
|---|---|---|---|
| 🟦 | **Market** | A country a licence can cover (ISO code) | Users see results per country |
| 🟦 | **Regulator** | Body that grants licences, acting for 1+ markets | The EC covers all EU/EEA; BfArM only Germany |
| 🟦 | **ProductType** | Synthetic or biological | Brazil has a separate rule set for each |
| 🟦 | **RuleSet** | A published scheme of categories for market × product type pairs | Where the categories come from |
| 🟦 | **ReportingCategory** | One category in one rule set, plus its **FilingRoute** | What the user picks; route makes markets comparable |
| 🟩 | **Licence** | A product's authorisation from one regulator, covering 1+ markets | One EU centralised licence = one row, many markets |
| 🟩 | **Classification** | One change × one licence: category, route only, or "not affected", with reasoning | The thing the user records |
 
## 🎯 Key decisions
 
- **Rule set ≠ regulator.** The UK, Switzerland, Saudi Arabia and South Africa reuse EU labels (`IA`, `IB`, `II`) but are separate rule sets. Codes are prefixed (`EU_IB`, `UK_IB`) so they never collide.
- **ASEAN is not a rule set.** Nobody files with ACCSQ-PPWG. Each member gets its own national rule set only where a primary source confirms one (E4). I relied on **E4 over E2**, e.g. for Cambodia.
- **Classify the licence, not the market.** One centralised EU licence gets one answer, shown in every market it covers.
- **Not stored, computed:** a licence's rule set (from its markets + product type) and "not yet classified" (an affected licence with no classification row).
---
 
## ⚠️ Deliberately not modelled
 
> [!WARNING]
> **Markets and product types with no confirmed rule set:** every product in Brunei, Cambodia, Lao PDR, Myanmar, Thailand and Timor-Leste; biologics in Argentina (Disp. 4351/2026, categories not in the evidence) and in Singapore, Malaysia, the Philippines, Indonesia and Vietnam (the AVG excludes biologics).
> **v1:** "rule set unknown" (AC2.5); the user records a filing route without a category, plus reasoning.
> **Model it when:** the domain team confirms the categories from a primary source. Each is a new rule set row, not a schema change.
 
> [!WARNING]
> **Rule set editions** (e.g. EU 2024/1701 replacing the old regulation)
> **v1:** only the current edition is held and updated in place. Reasoning is kept on each classification.
> **Model it when:** auditors need to see which edition a past classification was made under.
 
> [!WARNING]
> **EU procedure routes** (MRP / DCP / national)
> **v1:** each national licence is its own row under its national regulator. Same rule set either way.
> **Model it when:** filing planning comes into scope (coordination differs by route).
 
> [!WARNING]
> **One change that triggers several categories on one licence** (EU grouping)
> **v1:** record the most restrictive category; note the rest in reasoning.
> **Model it when:** grouping or worksharing decisions come into scope.

> [!WARNING]
> **Mexico's biologic subcategories** (administrativa / técnica / cesión de derechos, on top of menor / moderada / mayor)
> **v1:** biologics get the three MCRS tiers; the user names the subcategory in reasoning. All are prior approval, so the route is unaffected.
> **Model it when:** the domain team lists them from a primary source.
 
---
 
## ❓ Open questions
 
> [!IMPORTANT]
> | Question | Who decides |
> |---|---|
> | Are two product types enough, or do vaccines, ATMPs or herbals need their own rule sets? | Domain team |
> | Must every classification record the rule set edition it used? | Product + QA / compliance |
> | E3 lists a US no-filing category (`PQS-NOFILE`); E2 says the US has no such tier. Seeded following E3. Is it real? | Domain team (US regulatory specialist) |
> | Brazil's `BIO-MENOR` is recorded in the product change history like `SYN-HMP`, yet E3 tags it notify at implementation. Does it need an individual filing, or is it do and document? Seeded following E3. | Domain team (Brazil regulatory lead) |
> | Which edition of HSA's registration guidance do Singapore's categories come from? | Domain team (ASEAN regulatory lead) |
> | Do the ASEAN national schemes cover biologics? Not seeded, so biologics there show "rule set unknown". | Domain team (ASEAN regulatory lead) |
> | Which categories apply in each unconfirmed ASEAN country? Does Brunei's MaV/MiV procedure count as the AVG? | Domain team (ASEAN regulatory lead) |
> | Thailand cites the AVG "alongside other frameworks". Which one wins on a conflict? | Domain team |
> | Is Vietnam’s minor notification “notify at implementation” or “notify then wait”? | Domain team |
