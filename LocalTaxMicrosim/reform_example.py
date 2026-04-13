# Slide 1 ----------------------------------------------
from policyengine_us import Microsimulation
from policyengine_core.reforms import Reform

# Create the reform using Reform.from_dict
double_standard_deduction = Reform.from_dict({
    "gov.irs.deductions.standard.amount.SINGLE": {
        "2025-01-01.2100-12-31": 31_500
    },
    "gov.irs.deductions.standard.amount.JOINT": {
        "2025-01-01.2100-12-31": 63_000
    },
    "gov.irs.deductions.standard.amount.HEAD_OF_HOUSEHOLD": {
        "2025-01-01.2100-12-31": 47_250
    },
    "gov.irs.deductions.standard.amount.SEPARATE": {
        "2025-01-01.2100-12-31": 31_500
    },
    "gov.irs.deductions.standard.amount.SURVIVING_SPOUSE": {
        "2025-01-01.2100-12-31": 63_000
    },
}, country_id="us")

baseline = Microsimulation(dataset="hf://policyengine/test/NC.h5")
reform = Microsimulation(
    dataset="hf://policyengine/test/NC.h5",
    reform=double_standard_deduction,
)

# Slide 2 ------------------
print("Baseline income tax:", baseline.calculate("income_tax", 2025).sum() / 1E9 )
# Baseline income tax: 30.244186651078152
print("Reform income tax:", reform.calculate("income_tax", 2025).sum() / 1E9)
# Reform income tax: 20.983373598848175

df = reform.calculate_dataframe(["household_id", "household_weight", "congressional_district_geoid", "income_tax"])
df.loc[df.income_tax > 0].sample(3)

#      household_id  household_weight  congressional_district_geoid    income_tax
#3124       2080524         46.448639                          3703   3903.695557
#2567       2071429        209.020447                          3702  16684.183594
#7655       2121120        211.719910                          3707  15872.220703

