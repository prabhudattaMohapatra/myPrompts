# Master Column Index Reference - CORRECT INDICES

**File**: `annual_employee_input_data_april_2025.csv`  
**Total Columns**: 61  
**Date**: November 23, 2025

---

## Copy-Paste Python Code (VERIFIED CORRECT)

```python
def safe_float(val):
    try:
        return float(val) if val else 0
    except:
        return 0

def safe_int(val):
    try:
        return int(val) if val else 0
    except:
        return 0

# Extract ALL fields with CORRECT indices
age = safe_int(emp_input[3])
parent_age = safe_int(emp_input[4])
num_children = safe_int(emp_input[5])
city_type = emp_input[8].lower()
tax_regime = emp_input[10].lower()

# Salary & Allowances
gross_salary = safe_float(emp_input[14])
basic_salary = safe_float(emp_input[15])
hra_received = safe_float(emp_input[16])
transport_allowance = safe_float(emp_input[18])
conveyance_allowance = safe_float(emp_input[19])
meal_vouchers = safe_float(emp_input[20])
lta_received = safe_float(emp_input[21])
cea = safe_float(emp_input[22])
cha = safe_float(emp_input[23])
telephone_reimbursement = safe_float(emp_input[25])

# NPS Contributions (CORRECTED!)
nps_employee = safe_float(emp_input[32])
nps_employer = safe_float(emp_input[33])
nps_additional = safe_float(emp_input[34])

# Investments & Deductions
section_80c_investments = safe_float(emp_input[35])
self_family_premium = safe_float(emp_input[36])
parents_premium = safe_float(emp_input[37])
professional_tax_paid = safe_float(emp_input[38])

# Property
income_or_loss_from_house_property = safe_float(emp_input[39])
rent_paid = safe_float(emp_input[40])
home_loan_interest = safe_float(emp_input[41])
property_type = emp_input[42]
first_time_home_buyer = emp_input[43]
section_80eea = safe_float(emp_input[44])

# Disability
disability_status = emp_input[45]
disability_percentage = safe_int(emp_input[46])
dependent_disability_expenses = safe_float(emp_input[47])
dependent_severe_disability = emp_input[48]

# Other
savings_interest = safe_float(emp_input[49])
```

---

## Quick Reference Table

| Index | Field Name | Type | Notes |
|-------|-----------|------|-------|
| [3] | age | int | |
| [4] | parent_age | int | |
| [5] | number_of_children | int | |
| [8] | city_type | str | 'Metro' or 'Non-Metro' |
| [10] | tax_regime | str | 'new' or 'old' |
| [14] | gross_salary | float | |
| [15] | basic_salary | float | |
| [16] | hra_received | float | |
| [18] | transport_allowance | float | |
| [19] | conveyance_allowance | float | |
| [20] | meal_vouchers | float | ✅ CORRECTED |
| [21] | lta_received | float | ✅ CORRECTED |
| [22] | children_education_allowance | float | |
| [23] | children_hostel_allowance | float | |
| [25] | telephone_reimbursement | float | |
| **[32]** | **nps_employee_contribution** | float | ✅ CORRECTED (was [27]) |
| **[33]** | **nps_employer_contribution** | float | ✅ CORRECTED (was [28]) |
| **[34]** | **nps_additional_contribution** | float | ✅ CORRECTED (was [29]) |
| [35] | section_80c_investments | float | ✅ CORRECTED (was [34]) |
| [36] | self_family_premium | float | |
| [37] | parents_premium | float | |
| [38] | professional_tax_paid | float | |
| [39] | income_or_loss_from_house_property | float | |
| [40] | rent_paid | float | ✅ CORRECTED (was [44]) |
| [41] | home_loan_interest | float | |
| [42] | property_type | str | 'Self-occupied', 'Let-out', or '' |
| [43] | first_time_home_buyer | str | 'true' or 'false' |
| [44] | section_80eea | float | |
| [45] | disability_status | str | 'none', 'normal', 'severe' |
| [46] | disability_percentage | int | |
| [47] | dependent_disability_expenses | float | |
| [48] | dependent_severe_disability | str | 'true', 'false', '0' |
| [49] | savings_interest | float | |

---

## Key Corrections Made

1. **NPS Contributions**: Indices 32, 33, 34 (not 27, 28, 29)
2. **Section 80C**: Index 35 (not 34)
3. **Rent Paid**: Index 40 (not 44)
4. **Meal Vouchers**: Index 20 (not 21)
5. **LTA Received**: Index 21 (not 20)

---

## Usage in Recalculation

Always use this as the single source of truth for column indices when extracting data from `annual_employee_input_data_april_2025.csv`.

