# Memo

*Draft: edge cases and open questions are collected here as the stories are written. Core concepts and the model diagram come after step 5.*

## Edge cases deliberately not modelled

| Edge case | How v1 copes | What would trigger modelling it |
|---|---|---|
| **Two licences for one product in one market**, for example separate licences for different strengths. AC1.3 allows at most one. | Record each separately licensed presentation as its own product, so each product still has one licence per market. | Customers' registration data shows several licences per product per market is common, or splitting products distorts which products a change touches. |
| **Mutual-recognition and decentralised licences:** several national licences, one variation. AC5.4 keeps one classification per licence, so nothing keeps Germany's and France's national licences aligned. | Each national licence is classified separately. All share the EU rule set, so the same category is available to each, but the user keeps them consistent by hand. | Classifications in one mutual-recognition or decentralised family are found to disagree, or customers hold many such licences. Fix: link the licences in a procedure. |
| **A second national regulator by product type.** Germany licenses vaccines and blood products through the Paul-Ehrlich-Institut, not BfArM. | A German national licence for such a product is recorded against BfArM. | A customer holds German national licences for biologics. Fix: one more regulator row. |
| **Saudi Arabia's GCC centralised route.** A product can also be authorised through the GCC-DR route (E2). | Only the SFDA licence is recorded. | A customer uses the GCC route for Saudi licences. |
| **Classification that depends on what changed.** South Africa requires prior approval for name and scheduling changes even at IB. | The user picks the category that applies and says why in the reasoning. | Such rules turn out to be common enough that users get them wrong. |
| **Filing body differs from licensing body.** China's record-filings (`REC`) go to the provincial MPA, and EU centralised variations go to EMA, not the Commission. | The licence's regulator is the licensing body; where filings go is out of scope. | Filing planning comes into scope. |
| **No rule-set history.** Each rule set holds only its current edition (AC3.4), so a past classification can't show which edition it was made under. | The reasoning cites the guideline condition and edition. | An audit or inspection needs proof of the edition that applied, or a fast-changing market (Viet Nam: three circulars in seven years) moves while assessments are in flight. |
| **No regional sign-off.** The journey has regional RA confirming each classification, but v1 records no approval. | Reviewers read the reasoning (AC5.2). | A need to record who approved each market's classification. |
| **Only two product types.** China separates chemical drugs, biologics and TCM. | Product type is a seeded list with two rows; China has one rule set for both. | A TCM product (or another type with its own rules) is brought in. It's a new row, not a schema change. |

## Open questions

| Question | Who should answer |
|---|---|
| **Rule set not established by the evidence:** what scheme applies in Brunei, Cambodia, Lao PDR, Myanmar, Thailand and Timor-Leste? E2 says most of them use the ASEAN guideline, but E4's primary sources don't establish it. Thailand cites the AVG "alongside other frameworks". | The regulatory team's primary-source review |
| **Rule set exists but isn't seeded:** US biologics (21 CFR 601.12), Argentine biologics (Disp. 4351/2026), and Mexico's extra biologics categories (administrativa / técnica / cesión de derechos). | Whoever maintains the reference data |
| **UK and South African `IA`:** the UK's can be filed individually within 12 months or grouped; South Africa's is called "Do and Tell" but has a quality annual notification. Neither sits cleanly in one filing route. Both are seeded as do and document, following E3. | The regulatory team (UK and South Africa specialists) |
| **Extensions:** E3 tags the UK and Swiss `EXT` as prior approval but the EU and South African `EXT` as registration. All are seeded as new application. | The regulatory team |
| **US `PQS-NOFILE`:** E3 lists a US no-filing category; E2 says the US has no such tier. Not seeded: a change kept inside the quality system is recorded as not affected. | The regulatory team (US specialist) |
| **ASEAN biologics:** do the Singapore, Malaysia, Philippines, Indonesia and Viet Nam schemes cover biologics? The AVG excludes them, and E2 says Malaysia handles them separately. Seeded as synthetic only, so biologics there show "rule set unknown". | The regulatory team's primary-source review |
| **Indonesia and Viet Nam filing routes:** E4 confirms only that the schemes are national; the routes come from E2. Viet Nam's notification (~20 working days) may be notify then wait rather than notify at implementation. | The regulatory team (ASEAN specialist) |
| **The journey:** the roles and order of work are general industry practice, not observed. | RA users (CMC leads and RA operations) at a customer |
