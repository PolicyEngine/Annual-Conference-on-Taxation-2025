
This is where the 85% number comes in

policyengine_us/parameters/gov/irs/social_security/taxability/rate/additional/benefit_cap.yaml




● Read(reforms.py)
  ⎿  Read 50 lines

● The 85% dictionary is doing three things:

  1. Change the fraction (Line 72-73):
  "gov.irs.social_security.taxability.combined_income_ss_fraction": {
      "2026-01-01.2100-12-31": 1.0
  }
  This changes how much of your benefits count toward "combined income." Default is 0.5 (half your benefits). This
   changes it to 1.0 (all your benefits count). Why? So you hit the threshold faster and trigger the 85% taxation
  sooner.

  2. Zero out base thresholds (Lines 76-90):
  "gov.irs.social_security.taxability.threshold.base.main.JOINT": {
      "2026-01-01.2100-12-31": 0
  }
  # ... (same for SINGLE, SEPARATE, SURVIVING_SPOUSE, HEAD_OF_HOUSEHOLD)
  The base threshold is where you'd normally start paying 50% tax. Setting it to 0 means you skip the 50% tier
  entirely.

  3. Zero out adjusted base thresholds (Lines 92-106):
  "gov.irs.social_security.taxability.threshold.adjusted_base.main.JOINT": {
      "2026-01-01.2100-12-31": 0
  }
  # ... (same for all filing statuses)
  The adjusted base threshold is where you'd normally hit the 85% tier. Setting it to 0 means you hit it
  immediately.

  Net Effect:

  With both thresholds = 0 and fraction = 1.0, everyone pays 85% on their benefits from dollar one instead of
  having income-based tiers.


\begin{column}{0.48\textwidth}
\textbf{Why This Matters for SS Reform:}

\vspace{0.2cm}
\begin{itemize}
    \item Near-retirees face \textbf{discrete choice}: work or retire
    \item Tax increases on benefits → larger earnings reductions
    \item Behavioral offsets reduce revenue by more than static analysis suggests
\end{itemize}
\end{column}



● Before the reform, the base threshold was:
  - JOINT: $32,000
  - SINGLE: $25,000
  - SEPARATE: $25,000
  - HEAD_OF_HOUSEHOLD: $25,000
  - SURVIVING_SPOUSE: $25,000

  These thresholds have been frozen at these levels since 2013 (they're not indexed for inflation).

  What this means:
  - If a joint filer had combined income below $32,000, zero of their benefits were taxable
  - Above $32,000, they entered "Tier 1" and started paying 50% tax up to the adjusted base threshold
  - Only above the adjusted base threshold did they hit the 85% rate

  The reform changes it to 0, which means:
  - Even the first dollar of combined income triggers taxation
  - No one gets the benefit of having some income "protected" from taxation
  - The system goes straight from "no taxation" (if combined income = $0) to "85% taxation" (if combined income >
  $0)


