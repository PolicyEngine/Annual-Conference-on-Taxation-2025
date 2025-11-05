# Labor Supply Elasticities in PolicyEngine US

## What Are Elasticities?

Labor supply elasticities measure how individuals adjust their work behavior in response to economic incentives:

- **Income elasticity**: Change in labor supply given a 1% change in disposable income
- **Substitution elasticity**: Change in labor supply given a 1% change in the effective marginal wage rate

## The Two Types of Elasticity

### 1. Substitution Elasticity

Measures labor supply response to changes in the after-tax wage rate. When wages increase, work becomes more attractive relative to leisure (the substitution effect).

**Formula**: `elasticity * earnings * relative_wage_change`

**Typical values**: 0.27-0.31 for primary earners (CBO estimates)

**Implementation**: Varies by:
- Primary vs. secondary earner status
- Earnings decile (10 levels for primary earners)
- Age (multiplier for 65+)

### 2. Income Elasticity

Measures labor supply response to changes in total household income. When income increases, individuals can maintain their lifestyle with less work (the income effect).

**Formula**: `elasticity * earnings * relative_income_change`

**Typical values**: -0.04 to -0.05 (negative because income increases reduce work)

**Implementation**:
- Single base parameter for all workers
- Age multiplier for 65+

## How These Effects Interact

Policy changes create opposing forces:

**Example: Tax increase**
1. **Substitution effect**: Lower after-tax wage → work less (wage is less attractive)
2. **Income effect**: Lower disposable income → work more (need to maintain living standards)

The net effect depends on which elasticity dominates. For typical parameter values, substitution effects tend to be larger in magnitude.

## Implementation Architecture

### Core Variable Files

Located in `policyengine_us/variables/gov/simulation/labor_supply_response/`:

1. **Main orchestrator**: `labor_supply_behavioral_response.py`
   - Calculates total earnings-related labor supply change
   - Guards early exit if elasticities are zero (lines 16-17)
   - Returns sum of income and substitution effects

2. **Elasticity calculators**:
   - `income_elasticity.py` - Age-adjusted income elasticity
   - `substitution_elasticity.py` - Position/decile/age-adjusted substitution elasticity
   - `income_elasticity_lsr.py` - Income component of total response
   - `substitution_elasticity_lsr.py` - Substitution component of total response

3. **Supporting calculations**:
   - `relative_wage_change.py` - % change in effective wage rate
   - `relative_income_change.py` - % change in household net income

4. **Income integration**:
   - `employment_income_behavioral_response.py` - Employment income changes
   - `self_employment_income_behavioral_response.py` - Self-employment income changes

### How Behavioral Responses Integrate

The system automatically applies behavioral responses to income calculations through the `adds` pattern:

```python
# employment_income.py
class employment_income(Variable):
    adds = [
        "employment_income_before_lsr",
        "employment_income_behavioral_response",
    ]

# self_employment_income.py
class self_employment_income(Variable):
    adds = [
        "self_employment_income_before_lsr",
        "self_employment_income_behavioral_response",
    ]
```

When elasticities are enabled, all downstream calculations (taxes, benefits, etc.) automatically reflect behavioral responses.

### Guard Clause

From `labor_supply_behavioral_response.py:16-17`:

```python
if p.elasticities.income == 0 and p.elasticities.substitution.all == 0:
    return 0
```

This early exit ensures zero overhead when elasticities are disabled.

## Parameter Structure

### Income Elasticity Parameters

Located in `policyengine_us/parameters/gov/simulation/labor_supply_responses/elasticities/income/`:

- `all.yaml` - Override parameter (default: 0)
- `base.yaml` - Base income elasticity (default: 0)
- `age_threshold.yaml` - Age threshold for multiplier (default: 65)
- `age_multiplier_over_threshold.yaml` - Multiplier for 65+ (default: 2.0)

**Formula**:
- If age < 65: `elasticity = base`
- If age >= 65: `elasticity = base × age_multiplier`

### Substitution Elasticity Parameters

Located in `policyengine_us/parameters/gov/simulation/labor_supply_responses/elasticities/substitution/`:

- `all.yaml` - Override parameter (default: 0)
- `by_position_and_decile.yaml` - 11 values (10 deciles for primary + 1 for secondary)
- `age_threshold.yaml` - Age threshold for multiplier (default: 65)
- `age_multiplier_over_threshold.yaml` - Multiplier for 65+ (default: 2.0)

**Structure of `by_position_and_decile.yaml`**:
```yaml
primary:
  1: 0    # Decile 1 (lowest earners)
  2: 0
  # ... deciles 3-9
  10: 0   # Decile 10 (highest earners)
secondary: 0  # Secondary earners
```

### Bounds Parameters

Located in `policyengine_us/parameters/gov/simulation/labor_supply_responses/bounds/`:

- `income_change.yaml` - Clips relative income changes
- `effective_wage_rate_change.yaml` - Clips relative wage changes

These prevent extreme behavioral responses from unrealistic input changes.

## Why Elasticities Are Disabled by Default

From the parameter README (lines 69-73):

> Default Values
> - All base elasticities default to 0 (no behavioral response)
> - Users must explicitly set base elasticity values to enable behavioral responses

**Design rationale**:

1. **Baseline simplicity**: Policy analysis should start with direct effects only
2. **Parameter uncertainty**: Different studies yield different elasticity estimates; researchers can set their own
3. **Transparency**: Users know when behavioral assumptions are active
4. **Web app usability**: Most users want direct effects; advanced users can enable behavioral modeling

### Historical Context

**December 2024**: CBO elasticities toggle removed (commit `6deafbee50`)
- Previously: Boolean parameter to use CBO-specific elasticity values
- Now: All elasticity values are parameterized; no hardcoded presets
- Reason: Flexibility for different research approaches

## Enabling Elasticities

### Method 1: Using Override Parameters (Simplest)

Edit these two files to set uniform elasticities for all workers:

**Income elasticity** (`elasticities/income/all.yaml`):
```yaml
values:
  2020-01-01: -0.04  # Changed from 0
```

**Substitution elasticity** (`elasticities/substitution/all.yaml`):
```yaml
values:
  2020-01-01: 0.30  # Changed from 0
```

These override all other elasticity parameters if non-zero.

### Method 2: Using Base Parameters with Heterogeneity

For more realistic modeling with age and income heterogeneity:

**Income elasticity** (`elasticities/income/base.yaml`):
```yaml
values:
  2020-01-01: -0.04  # CBO-style value
```

**Substitution elasticity** (`elasticities/substitution/by_position_and_decile.yaml`):
```yaml
primary:
  1: 0.31    # Lowest decile
  2: 0.28
  3: 0.27
  4: 0.27
  5: 0.25
  6: 0.25
  7: 0.22
  8: 0.22
  9: 0.22
  10: 0.22   # Highest decile
secondary: 0.27
```

With default age multipliers (2.0), workers 65+ will have elasticities 2× the base values.

### Recommended Starting Values (CBO-based)

Based on CBO Working Papers 2012-12 and 2012-13:

- **Income elasticity**: -0.04 to -0.05
- **Substitution elasticity**: 0.22 to 0.31 (varies by decile)
- **Age multiplier**: 2.0 (conservative; French 2005 suggests up to 3.0+)

## Example: Tax Policy Analysis

**Scenario**: Income tax rate increases from 20% to 25%

**Without behavioral responses** (elasticities = 0):
- Worker earning $50,000 pays $2,500 more in taxes
- No change in work behavior
- Revenue increase = $2,500

**With behavioral responses** (using CBO values):
- After-tax wage decreases ~6%
- **Substitution effect**: 0.27 × 6% = 1.6% less work
- **Income effect**: -0.04 × (-5%) = 0.2% less work
- **Net effect**: ~1.8% less work, ~0.9% less earnings
- Revenue increase = ~$2,450 (not $2,500)

The behavioral response reduces revenue impact by ~2%.

## Social Security Implications

Labor supply elasticities are particularly important for modeling Social Security reforms:

1. **Benefit cuts**: Reduce lifetime income → income effect encourages more work
2. **Payroll tax increases**: Reduce after-tax wages → substitution effect discourages work
3. **Retirement age increases**: Complex interaction of both effects
4. **Age heterogeneity**: Elderly workers (65+) have higher elasticities → stronger responses

Small elasticity changes can significantly alter revenue and benefit projections over multi-decade horizons.

## Implementation Details

### Negative Earnings Handling

From CLAUDE.md and the implementation:

> **Labor Supply Response & Negative Earnings**: When dealing with income sources that can be negative (especially self-employment), use `max_(earnings, 0)` to prevent sign flips in economic responses. Negative total earnings should result in zero labor supply responses, not negative responses.

This ensures that workers with negative net earnings (e.g., business losses) have zero substitution elasticity rather than perverse incentive effects.

### Primary vs. Secondary Earner Determination

Within each tax unit:
- **Primary earner**: Person with highest total earnings (employment + self-employment)
- **Secondary earners**: All others

Implications:
- Single-person tax units: Always primary
- Multi-person tax units: Only highest earner gets primary elasticity

With default parameters (secondary = 0), only primary earners respond to wage changes.

### Earnings Decile Boundaries

Currently hardcoded (TODO in parameter README to parametrize):

| Decile | Range |
|--------|-------|
| 1 | $0 - $14,000 |
| 2 | $14,000 - $28,000 |
| 3 | $28,000 - $39,000 |
| 4 | $39,000 - $50,000 |
| 5 | $50,000 - $61,000 |
| 6 | $61,000 - $76,000 |
| 7 | $76,000 - $97,000 |
| 8 | $97,000 - $138,000 |
| 9 | $138,000 - $1,726,000 |
| 10 | $1,726,000+ |

### Test Files

Located in `policyengine_us/tests/policy/baseline/gov/simulation/labor_supply_response/`:

- `income_elasticity.yaml` - Tests income elasticity calculation and age multiplier
- `labor_supply_behavioral_response.yaml` - Tests disabled state and edge cases
- `employment_income_behavioral_response.yaml` - Tests income distribution
- `weekly_hours_worked.yaml` - Tests hours worked integration

## Documentation and References

### PolicyEngine Documentation

Comprehensive implementation details:
```
policyengine_us/parameters/gov/simulation/labor_supply_responses/elasticities/README.md
```

Covers:
- Age heterogeneity approach (multiplier vs. separate parameters)
- Parameter structure and formulas
- Usage examples with different multiplier values
- Primary/secondary earner mechanics
- Earnings decile markers

### Academic Literature

**Labor supply elasticity estimates:**
- **French (2005)**: "The Effects of Health, Wealth, and Wages on Labour Supply and Retirement Behaviour", *Review of Economic Studies* 72(2): 395-427
  - Finding: 3.0-3.25× higher elasticities for age 60 vs. age 40
- **CBO Working Paper 2012-12**: "A Review of Recent Research on Labor Supply Elasticities" (McClelland & Mok)
  - Finding: Frisch elasticity range 0.27-0.53, central estimate 0.40
- **CBO Working Paper 2012-13**: "Review of Estimates of the Frisch Elasticity of Labor Supply" (Reichling & Whalen)

### Git History

Key commits:
- `9acf8c23fa` (Dec 2023): Initial implementation of two labor supply elasticities
- `52f4e84488` (2024): Added CBO splits for labor supply and self-employment responses
- `6deafbee50` (Dec 2024): Removed CBO elasticities toggle, fully parameterized system
- `61b8586c61` (2024): Fixed negative self-employment income handling
- `8e95b314b5` (2024): Added 65+ age heterogeneity

## Summary

**Current state:**
- Fully implemented labor supply response system
- Disabled by default (all parameters = 0)
- Guards ensure zero computational overhead when disabled

**To enable:**
- Edit parameter YAML files to non-zero values
- System automatically applies behavioral responses throughout

**Why it matters:**
- Direct effects ≠ total effects
- Behavioral responses can materially change policy conclusions
- Particularly important for multi-decade Social Security projections

**Key design decisions:**
- Parameterized rather than hardcoded (flexibility for different research approaches)
- Age heterogeneity via multipliers (parsimonious, evidence-based)
- Disabled by default (transparency, user control)
