# Understanding the Social Security Reform Analysis Project

## How This Relates to the Conference Presentation

This document explains the **CRFB Social Security Taxation Reform Project**, which is one example of the broader research presented at the 118th Annual Conference on Taxation (2025).

### The Connection:

**The Conference Presentation** analyzes 4 different approaches to Social Security benefit taxation, focusing on:
- Work incentives and labor supply effects
- Marginal effective tax rates (how much more tax you pay when you earn one more dollar)
- Trust fund projections all the way to 2100
- Age-specific impacts on older workers

**The CRFB Project** (this document) analyzes 8 specific policy options requested by the Committee for a Responsible Federal Budget, focusing on:
- 10-year fiscal impacts (2026-2035)
- Who wins and loses at different income levels
- Total budget effects
- Specific policy proposals being debated in Congress

### What's the Same:

1. **Same researcher:** Ben Ogorek (PolicyEngine)
2. **Same tool:** PolicyEngine microsimulation model
3. **Same general topic:** How should we tax Social Security benefits?
4. **Same methodology:** Use real tax data from millions of Americans to simulate policy changes

### What's Different:

1. **Different policy options:** The presentation explores 4 research-oriented approaches; the CRFB project analyzes 8 specific proposals
2. **Different time horizons:** Presentation looks to 2100; CRFB project focuses on 2026-2035
3. **Different questions:** Presentation asks "How do these affect work incentives?" while CRFB asks "What are the budget and distributional impacts?"

### Some Policies Overlap:

- **Presentation Policy 3** (Universal 85% inclusion) is the same as **CRFB Option 2**
- **Presentation Policy 4** (Taxing employer FICA contributions) relates to **CRFB Options 5 & 6** (Roth-style swaps)

**Think of it this way:** The presentation shows the research method and broader questions we can answer. The CRFB project is one specific application of that method to help policymakers understand real proposals being discussed today.

---

## What is Social Security?

Social Security is a government program that provides monthly payments to people who are:
- **Retired** (usually age 67 or older)
- **Disabled** (cannot work due to a medical condition)
- **Surviving family members** (spouse or children of someone who passed away)

Think of it like an insurance program your parents pay into their whole lives, and when they retire, they get money back as monthly checks.

## The Problem: Taxing Social Security Benefits

Here's where it gets complicated: **the government taxes Social Security checks like regular income.**

### How it works now:

If you're a retiree with some Social Security income and other income (like interest from savings), the government can tax up to **50% or 85%** of your Social Security benefits, depending on how much total income you have.

**Example:** Your parent gets $2,000 in Social Security per month. They also earn $1,000 per month from a pension. The government might require them to pay taxes on part of that $2,000 Social Security check—even though they already paid taxes on it when they were working!

This bothers a lot of people because:
- They already paid taxes while working
- It makes retirement less predictable
- Different people get taxed very differently

## The Question: What Should We Do?

The Committee for a Responsible Federal Budget (CRFB) asked researchers to analyze **8 different policy options** to fix this problem. Each option is a different way to handle Social Security taxation.

## The 8 Policy Options

### Option 1: Get Rid of Taxes on Social Security Completely
- **What it does:** Stop taxing Social Security benefits entirely
- **Who benefits:** Retirees with Social Security income
- **The cost:** The government loses tax revenue (money it needs to pay for roads, schools, etc.)
- **Why consider it:** It's simple and fair to retirees

### Option 2: Tax 85% of Benefits (No Income Limits)
- **What it does:** The government always taxes 85% of Social Security benefits, no matter your total income
- **Current law:** Only people with higher incomes have 85% of benefits taxed; others might have only 50% taxed or no tax
- **This option:** Makes it the same for everyone
- **Why consider it:** Simpler, less confusing

### Option 3: 85% Tax + Keep the Senior Deduction
- **What it does:** Tax 85% of benefits, BUT give seniors an extra tax break (a "deduction")
- **What's a deduction?** It reduces the amount of income you have to pay taxes on—like getting a discount
- **Why consider it:** Helps balance taxing more benefits with helping seniors

### Option 4: Tax Credits Instead of Deductions
- **What it does:** Instead of deducting stuff from income, give seniors a **$500 tax credit** that reduces their taxes owed
- **What's a tax credit?** It's like a coupon that comes off your tax bill directly (better than a deduction)
- **Why consider it:** More straightforward help for seniors

### Option 5: Roth-Style Swap
- **What it does:** Stop taxing Social Security benefits, BUT make the taxes you pay while working heavier
- **Simple version:** Your parents pay more taxes now while working, so they won't be taxed on benefits later
- **Trade-off:** Higher taxes today for simpler retirement
- **Why consider it:** Moves taxes to when people are earning more money

### Option 6: Gradual Roth-Style Swap (2026-2045)
- **What it does:** Same as Option 5, but phase it in slowly over 20 years instead of all at once
- **Why consider it:** Gradual change is sometimes easier for the economy

### Option 7: Let the Senior Deduction Expire
- **What it does:** Keep things mostly the same, but remove a tax break that was added recently (expires in 2028 anyway)
- **Why consider it:** Simple—just stop giving the extra tax break

### Option 8: Tax All Social Security Benefits (100%)
- **What it does:** Treat Social Security like regular income and tax 100% of it
- **Why consider it:** Generates a lot of money for the government

## What This Project Does

This research project **simulates all 8 options** to see what would actually happen if we used each policy. It answers questions like:

- **How much money would each option raise or cost?**
- **Who would win and who would lose?**
- **How would it affect people of different income levels?**
- **What about the federal budget—could we afford it?**

## How Do They Do This?

### Step 1: Build a Detailed Model
The researchers use a computer program called **PolicyEngine** that has information about millions of tax returns. It knows:
- How much different people earn
- What benefits they receive
- What taxes they currently pay
- How their situation would change under each option

### Step 2: Run the Simulation
For each policy option, the computer calculates:
- How much tax each person would pay
- How much money the government would collect
- How different income groups are affected

### Step 3: Analyze the Results
The researchers look at the data and create:
- Charts showing the impact on the budget over 10 years (2026-2035)
- Tables showing who benefits and who pays more
- Comparisons with other research on the same topic

### Step 4: Present Findings
They create two ways to share the results:

**1. A Research Report (Jupyter Book)**
- Professional written analysis
- Charts and tables
- Explains the methodology
- Shows all findings

**2. An Interactive Dashboard (Website)**
- You can select a policy option
- See the 10-year impact
- Play with the numbers yourself

## The Technology (In Simple Terms)

- **Python:** A programming language used to do the calculations
- **PolicyEngine:** A specialized tool that models taxes for millions of Americans
- **Jupyter Notebooks:** Documents that mix explanations and code together
- **React/Dashboard:** A website where you can explore the findings
- **Plotly:** Software that makes interactive charts

## Why Does This Matter?

Social Security affects millions of Americans. Any change to how it's taxed would impact real people's retirements. By analyzing these 8 options carefully, policymakers can:
- Understand the real costs and benefits of each approach
- See who would be helped and who would be hurt
- Make informed decisions about retirement tax policy

## Key Numbers

- **Time frame:** 10 years (2026-2035)
- **Number of policy options:** 8
- **Data source:** Tax data from millions of Americans
- **Number of calculations:** About 70 different scenarios (7 policy options × 10 years)

## Who Did This Work?

This analysis was conducted by researchers using PolicyEngine, in collaboration with the Committee for a Responsible Federal Budget (CRFB), a nonprofit organization that focuses on fiscal policy and the federal budget.

## How This Project Demonstrates the Conference Presentation's Ideas

The conference presentation talks about **how PolicyEngine can analyze Social Security reform**. The CRFB project is a real-world example of that capability in action.

### The Presentation's 4 Policies:

1. **Trust-fund reallocation** - Changing how tax revenues are split between different Social Security funds
2. **Standard-deduction formula** - Simplifying the complex three-tier tax system into a single deduction
3. **Universal 85% inclusion** - Tax the same percentage of everyone's benefits (this is CRFB Option 2!)
4. **Taxing employer FICA contributions** - Make the employer's portion of Social Security taxes count as employee income (this relates to CRFB Options 5 & 6!)

### What the Presentation Shows You Can Calculate:

- **Marginal effective tax rates (METRs):** How much extra tax you pay when you earn one more dollar
- **Work incentive effects:** Will people work more or less under each policy?
- **Labor supply by age:** How does this affect 62-year-olds vs. 70-year-olds?
- **Trust fund solvency:** When will Social Security run out of money under each option?
- **Long-term projections:** What happens by 2100?

### What the CRFB Project Actually Calculates:

- **Revenue effects:** How much money does the government gain or lose? (same capability, applied to different policies)
- **Distributional impacts:** Who wins and who loses? (uses the same simulation)
- **Income decile effects:** What happens to the poorest 10% vs. richest 10%? (same data, different question)
- **10-year budget window:** Standard policy analysis timeframe (shorter than presentation's 2100 horizon, but same tool)

### The Research Pipeline (Works for Both):

```
Real tax data → PolicyEngine → Policy simulation → Results analysis
```

This pipeline is the same whether you're analyzing:
- The 4 policies in the presentation (academic research focus)
- The 8 policies in the CRFB project (applied policy work)
- Any other Social Security reform idea you want to test

### Why This Matters for Understanding the Presentation:

The CRFB project proves that PolicyEngine can:
1. **Handle complex tax policies** (8 different reform options with lots of details)
2. **Process millions of records** (simulating all American taxpayers)
3. **Generate multiple types of analysis** (fiscal impacts, distributional effects, household-level changes)
4. **Produce results quickly** (70 scenarios in reasonable computing time)
5. **Present findings clearly** (interactive dashboard + research report)

When the presentation talks about using microsimulation to analyze Social Security reforms, the CRFB project is concrete proof that this approach works for real policy questions.

---

## Bottom Line

This project takes a complicated tax policy question and answers it with real data and careful analysis. The results help us understand what different policy choices would actually mean for people's retirement income and the federal budget.

**The connection to the conference presentation:** This is one specific example of the research methodology and analytical capabilities being presented. The presentation explains *how* we can analyze Social Security reforms using microsimulation. This CRFB project shows *that* we actually did it, with real policies, producing actionable insights for policymakers.
