# Trump News Article Typology

## Motivation & Context
To achieve the goal of using data science to better understand how Donald Trump is covered in the media, we have developed the following typology. We are especially concerned with coverage in North America. This typology is specifically designed to address two main questions:

1. Whether the coverage is positive or negative.
2. What topics the coverage focuses on.

With the vast volume of media coverage spanning legal proceedings, political actions, personal behavior, and family or corporate entities, consistent categorization allows researchers, journalists, and analysts to:  

- **Maintain clarity** on article focus.  
- **Enable quantitative analyses** of coverage trends.  
- **Differentiate between personal, political, legal, and public dimensions** of Trump-related news.  

By defining clear categories, we reduce ambiguity and ensure that analyses of media coverage are both replicable and meaningful.


## Overview of Types
This typology divides Trump-related news into six mutually exclusive types. Each type represents a distinct focus, though real-world articles can occasionally straddle categories.  

| Type | Primary Focus | Distinction |
|------|---------------|------------|
| 1 | Legal challenges & criminal proceedings | Judicial processes, trials, verdicts |
| 2 | Political entity relations | Responses or interactions from political actors |
| 3 | Trump’s personal actions | Private behavior, celebrity persona, business activity |
| 4 | Policies & political actions under Trump | Official governmental actions, executive orders, campaigns |
| 5 | Public reactions | Responses from the general public, NGOs, celebrities, civil society |
| 6 | Trump-adjacent individuals & entities | Family members, relatives, Trump-related organizations |


## Typology Details

### **TYPE 1 — Legal Challenges & Criminal Proceedings**
**Definition:**  
Articles primarily covering legal processes involving Trump, including charges, trials, hearings, verdicts, motions, evidence, and judicial outcomes. Public or political reactions may appear, but the legal process is central.

**Positive Examples (Inclusion):**  
- *“Trump’s guilty verdict shocks political world.”* → Focused on verdict itself.  
- *“Jury deliberations enter day three in hush-money case.”* → Procedural focus.  
- *“Judge sets new trial date in classified documents case.”* → Core legal development.

**Negative Examples (Exclusion):**  
- *“GOP rallies around Trump after trial.”* → Political reaction, Type 2.  
- *“How CNN and Fox portrayed the trial differently.”* → Media framing, Type 5.

**Edge Cases:**  
- Articles mixing legal recap + political implications → include only if ≥60% is legal.  
- Legal context serving as backdrop for political fallout → classify as Type 2.  

**Rule:** Include when legal processes are the primary subject; exclude when focus is political, public, or media reactions.


### **TYPE 2 — Political Entity Relations**
**Definition:**  
Articles about how political actors (parties, elected officials, candidates, foreign governments, diplomats, voters) respond to or interact with Trump. Covers endorsements, conflicts, statements, alliances, condemnations, and strategic positioning.

**Positive Examples:**  
- *“GOP unites behind Trump within hours of verdict.”*  
- *“Democrats condemn Trump’s legal maneuvers.”*  
- *“European leaders react to Trump’s tariffs.”*  
- *“Some Republicans distance themselves from Trump.”*  
- *“Affordability or Trump? What matters more to these voters.”*

**Negative Examples:**  
- *“Public opinion splits across demographics.”* → Type 5  
- *“Trump signs a bill into law.”* → Type 4

**Edge Cases:**  
- Articles quoting both domestic and international leaders → Type 2 if political reactions dominate.  
- Political reactions present only as background → classify under primary domain (legal, policy, personal).  

**Rule:** Include when focus is on political entities’ responses; exclude articles centered on policies (Type 4) or public reactions (Type 5).


### **TYPE 3 — Trump’s Personal Actions**
**Definition:**  
Articles covering Trump’s private, non-governmental actions, behaviors, remarks, lifestyle choices, business dealings, or interpersonal conflicts. Includes public reactions to these personal actions.

**Positive Examples:**  
- *“Trump attends private gala at Mar-a-Lago.”*  
- *“Trump insults celebrity; social media erupts.”*  
- *“Trump’s real estate deal raises public criticism.”*  
- *“Rally speech sparks backlash when Trump mocks entertainer.”*

**Negative Examples:**  
- *“Trump issues executive order restricting asylum.”* → Type 4  
- *“Republicans react to Trump’s diplomatic visit.”* → Type 2

**Edge Cases:**  
- Rally speeches: Policy content → Type 4; Personal rhetoric → Type 3  
- Articles on personal actions causing political consequences → classify by main focus.

**Rule:** Include when core subject is personal behavior or public reactions to it; exclude official political authority or policy content.


### **TYPE 4 — Policies & Political Actions Under Trump**
**Definition:**  
Articles about Trump’s governmental or official political actions: policies, executive orders, regulations, diplomacy, or campaign governance. Includes public or political reactions to these actions.

**Positive Examples:**  
- *“Trump signs new bill into law; advocacy groups respond.”*  
- *“Executive order on immigration sparks nationwide protests.”*  
- *“Administration rolls back environmental rules, drawing criticism from scientists.”*  
- *“Foreign leaders react to Trump’s trade tariffs.”*

**Negative Examples:**  
- *“Trump mocks rival at rally.”* → Type 3  
- *“GOP unites behind Trump.”* → Type 2  
- *“Trial motion filed in New York case.”* → Type 1

**Edge Cases:**  
- Proposed actions count if treated as formal political moves.  
- Articles heavy on reactions → Type 4 if reactions pertain to policy/action.

**Rule:** Include when central focus is official political/government action or reactions to it.


### **TYPE 5 — Public Reactions**
**Definition:**  
Articles about how non-political actors—general public, celebrities, NGOs, universities, corporations, activists, religious groups—respond to, perceive, or are affected by Trump.  

**Positive Examples:**  
- *“Kim Kardashian criticizes Trump’s criminal justice policies.”*  
- *“NFL players respond to Trump’s remarks.”*  
- *“Universities issue statements on Trump’s education rules.”*  
- *“Citizens protest new executive order.”*

**Negative Examples:**  
- *“GOP leaders defend Trump.”* → Type 2  
- *“Judge delays hearing.”* → Type 1

**Edge Cases:**  
- Articles mixing political and public reactions → classify by which group dominates.  
- NGOs and corporations count as public, not political actors.  
- Public reactions to legal outcomes → classify as Type 2.

**Rule:** Include when primary subject is reactions by non-politicians or non-government entities.


### **TYPE 6 — Trump-Adjacent Individuals & Entities**
**Definition:**  
Articles primarily focused on family members, relatives, or organizations closely associated with Trump, rather than Trump himself.  

**Positive Examples:**  
- *“Ivanka Trump distances herself from politics.”*  
- *“Donald Trump Jr. launches new media venture.”*  
- *“Eric Trump testifies in New York civil fraud trial.”*  
- *“Melania Trump’s public disappearance sparks speculation.”*  
- *“Trump Organization faces new financial penalties.”*  
- *“Mary Trump releases book criticizing her family.”*

**Negative Examples:**  
- *“Donald Trump and Ivanka Trump subpoenaed…”* → Trump is central → Type 1  
- *“Republicans criticize Trump after rally remarks”* → Type 2 or 3

**Edge Cases:**  
- Articles covering both Trump and a family member → classify by dominant actor.  
- Legal stories about family members → Type 6 unless case concerns Trump directly.  
- Corporate entities → Type 6 unless focus is Trump personally.

**Rule:** Use Type 6 when primary subject is family, relative, or Trump-affiliated organization.


## Comprehensiveness
This typology is designed to comprehensively cover all major aspects of Trump-related news, ensuring every article can be assigned a primary type without overlap or ambiguity. Key points:  

1. **Mutual Exclusivity:**  
   Each type is defined so that no article should fit into more than one type as the primary focus. Edge-case guidance ensures consistent coding for articles with mixed content.

2. **Complete Scope of Coverage:**  
   - **Legal dimension:** Type 1 captures all formal judicial processes involving Trump.  
   - **Political dimension:** Type 2 covers reactions and interactions by political entities.  
   - **Personal dimension:** Type 3 focuses on Trump’s private actions, lifestyle, and non-official behavior.  
   - **Policy/governmental actions:** Type 4 captures executive orders, legislation, regulations, and official political maneuvers.  
   - **Public reactions:** Type 5 addresses non-political actors, NGOs, corporations, and general societal responses.  
   - **Trump-adjacent entities:** Type 6 accounts for family, relatives, and organizations closely linked to Trump, distinct from Trump himself.

3. **Boundary Clarity:**  
   - Each type includes explicit positive and negative examples and rules for edge cases.  
   - Articles straddling multiple domains are classified by **primary subject**, reducing ambiguity in quantitative analyses.  
   - Legal, political, personal, public, and family/corporate categories together encompass all possible reporting angles, minimizing unclassified articles.

4. **Replicability:**  
   Clear definitions, inclusion/exclusion rules, and edge-case guidance ensure that multiple coders can consistently categorize articles with high inter-coder reliability.  

By combining clear definitions with illustrative examples, this typology provides a robust framework for systematically coding all Trump-related news content.

