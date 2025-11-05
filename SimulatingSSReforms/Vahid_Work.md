# Vahid's Work: Age Heterogeneity in Labor Supply Responses

## Overview

**PR #6681**: "Add the 65+ age heterogeneity to US LSRs"
**Author**: Vahid Ahmadi
**Status**: Merged on October 28, 2025
**Repository**: PolicyEngine/policyengine-us

## Summary

This PR introduces age-based heterogeneity to PolicyEngine's labor supply response (LSR) parameters, recognizing that older workers (65+) respond differently to economic incentives than younger workers. The implementation uses a **multiplier approach** rather than a full age breakdown, making it both empirically grounded and parsimonious.

## Problem Addressed

Prior to this PR, PolicyEngine's labor supply elasticities treated all workers the same regardless of age. However, extensive economic literature shows that:

1. **Older workers are more responsive** to wage changes, especially on the extensive margin (whether to work at all)
2. **Retirement-age individuals (62-70)** have particularly high own-wage elasticities
3. The **intensive margin** (how many hours to work) response is much smaller for older workers

This created inaccuracies when modeling policies affecting older workers, such as Social Security reforms, retirement benefit changes, or tax policy targeting retirees.

## Implementation Approach: Multiplier vs Full Breakdown

Vahid chose a **multiplier approach** over creating separate elasticity values for each age group. This decision was based on:

### Why Multiplier Approach?

1. **Evidence-based**: Literature shows older workers (62–70) have higher elasticities, but no studies provide age-by-income-decile or age-by-earner breakdowns

2. **Parsimony**: A single multiplier parameter avoids an unnecessary 44-parameter expansion (22 elasticity values × 2 age groups)

3. **Transparency**: The interpretation is straightforward: "65+ workers are X times more responsive"

4. **Flexibility**: Users can easily tune the multiplier (e.g., 1.5–3.0 range) or set it to 1.0 for no age effect

### How the Multiplier Works

The multiplier is applied as follows:

- **Base elasticity**: Elasticity value for workers under 65 (by position and decile for substitution elasticity)
- **Age multiplier**: Scalar applied when age ≥ 65
- **Final elasticity**: `base_elasticity × age_multiplier` for individuals 65+

Default multiplier value: **2.0×** (meaning 65+ workers are twice as responsive as younger workers)

## Technical Changes

### Parameter Structure Changes

**Before PR #6681**:
```yaml
substitution:
  by_position_and_decile:
    primary:
      1: 0.0  # Decile 1
      2: 0.0  # Decile 2
      # ... etc
    secondary: 0.0

income: 0.0  # Single value for all
```

**After PR #6681**:
```yaml
substitution:
  all: 0.0  # Global override
  by_position_and_decile:
    age_threshold: 65
    age_multiplier_over_threshold: 2.0
    under_65:
      primary:
        1: 0.0  # Decile 1
        # ... etc
      secondary: 0.0
    65_and_over:
      # Uses: base × multiplier

income:
  all: 0.0  # Global override
  age_threshold: 65
  age_multiplier_over_threshold: 2.0
  by_age:
    under_65: 0.0
    65_and_over: 0.0  # Uses: base × multiplier
```

### Code Implementation

The implementation modified two key variable files:

1. **`substitution_elasticity.py`**: Now checks age and applies multiplier
   - Determines age from `person("age", period.this_year)`
   - Applies multiplier when `age >= 65`
   - Maintains existing position (primary/secondary) and decile logic

2. **`income_elasticity.py`**: Adds age-based differentiation
   - Previously just returned a single parameter value
   - Now checks age and applies appropriate elasticity with multiplier

### Files Changed

- **Parameter files** (11 files): Restructured to support age heterogeneity
- **Variable files** (2 files): Updated calculation logic
- **Test files** (4 files): Comprehensive tests for age-based behavior
- **Documentation** (1 README): 206-line documentation explaining the approach

## Empirical Basis

### Substitution Elasticity Research

| Study | Age Group | Elasticity | Implied 65+/<65 Multiplier |
|-------|-----------|------------|----------------------------|
| CBO (2012) | 25–64 | 0.27–0.53 (central 0.40) | — (baseline) |
| French (2005) | 40 → 60 | 0.2–0.4 → 1.0–1.3 | ≈ 3.0–3.25× |
| Blau & Shvydko (2011) | 62–69 | 0.5–0.8 (extensive) | ≈ 2–3× |
| Coile & Gruber (2007) | 62–64 | 0.4–0.7 | ≈ 2× |
| Gustman & Steinmeier (2009) | 65–69 | 0.45–0.8 | ≈ 2–2.5× |

**Recommended range**: 1.5–3.0× (default: 2.0×)

### Income Elasticity Research

| Study | Age Group | Elasticity | Implied 65+/<65 Multiplier |
|-------|-----------|------------|----------------------------|
| CBO (2012) | 25–64 | −0.02 to −0.05 (central −0.04) | — (baseline) |
| French (2005) | 60+ | −0.06 to −0.08 | ≈ 1.5–2× |
| Gustman & Steinmeier (2009) | 65+ | −0.07 to −0.10 | ≈ 2× |
| Rogerson & Wallenius (2009) | Model calibration | — | ≈ 1.3–1.5× |

**Recommended range**: 1.3–2.0× (default: 2.0×)

## Default Values

All elasticities default to **0** (no behavioral response). Users must explicitly set values to enable behavioral responses.

The **default multiplier is 2.0×**, based on the central tendency of the empirical literature.

## Testing Strategy

The PR includes comprehensive tests:

1. **Unit tests**: Test age threshold logic (age 64 vs 65)
2. **Integration tests**: Test couples with different ages and earnings
3. **Edge cases**: Zero elasticities, single individuals, same-age couples

Example test case:
```yaml
- name: Couple with different ages (under 65 and 65+)
  input:
    person1: {age: 67, employment_income: 60_000}
    person2: {age: 55, employment_income: 40_000}
    age_multiplier_over_threshold: 2.0
  output:
    substitution_elasticity: [0.40, 0]  # 67yo gets 2.0× multiplier
    income_elasticity: [-0.08, -0.05]
```

## Impact on PolicyEngine

This enhancement improves PolicyEngine's ability to model:

1. **Social Security reforms**: Better captures behavioral responses to benefit changes
2. **Retirement policy**: More accurate modeling of retirement timing decisions
3. **Tax policy for retirees**: Better estimates of labor supply responses to tax changes
4. **Medicare/Medicaid**: More realistic modeling of work decisions around eligibility ages

The multiplier approach makes it easy for researchers to:
- Run **sensitivity analyses** by varying the multiplier (e.g., 1.5× to 3.0×)
- **Disable age effects** by setting multiplier to 1.0
- Use **empirically calibrated values** by setting multiplier to 2.0 (default)

## Key References

1. **CBO (2012-12)**: [A Review of Recent Research on Labor Supply Elasticities](https://www.cbo.gov/publication/43675)
2. **CBO (2012-13)**: [Review of Estimates of the Frisch Elasticity of Labor Supply](https://www.cbo.gov/publication/43676)
3. **French (2005)**: "The Effects of Health, Wealth, and Wages on Labour Supply and Retirement Behaviour." *Review of Economic Studies* 72(2): 395–427
4. **Blau & Shvydko (2011)**: "Labor Market Rigidities and the Employment Behavior of Older Workers." *ILR Review* 64(3): 464–484
5. **Coile & Gruber (2007)**: "Future Social Security Entitlements and the Retirement Decision." *Review of Economics and Statistics* 89(2): 234–246

## Conclusion

Vahid's work represents a significant methodological improvement to PolicyEngine's behavioral microsimulation capabilities. By grounding the implementation in empirical literature while maintaining parsimony through the multiplier approach, this enhancement enables more accurate modeling of policies affecting older workers without unnecessarily complicating the parameter space.

The choice of a 2.0× multiplier as the default is well-justified by the convergence of estimates across multiple empirical studies, while the flexibility to adjust this multiplier enables sensitivity analysis and alternative calibrations.
