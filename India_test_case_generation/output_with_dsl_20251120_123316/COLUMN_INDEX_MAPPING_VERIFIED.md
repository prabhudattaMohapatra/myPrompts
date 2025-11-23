# DEFINITIVE COLUMN INDEX MAPPING

**Source**: `annual_employee_input_data_april_2025.csv`  
**Total Columns**: 61  
**Verified**: November 23, 2025

---

## Complete Mapping (All 61 Columns)

```
[ 0] ID
[ 1] first_name
[ 2] last_name
[ 3] age
[ 4] parent_age
[ 5] number_of_children
[ 6] residency
[ 7] city
[ 8] city_type
[ 9] employment_type
[10] tax_regime
[11] owns_house_in_work_city
[12] date_of_joining
[13] annual_ctc
[14] gross_salary
[15] basic_salary
[16] hra_received
[17] special_allowance
[18] transport_allowance
[19] conveyance_allowance
[20] meal_vouchers
[21] lta_received
[22] children_education_allowance
[23] children_hostel_allowance
[24] books_and_periodical_allowance
[25] telephone_reimbursement
[26] telephone_data_allowance
[27] bonus
[28] commission
[29] performance_bonus
[30] employee_pf_contribution
[31] employer_pf_contribution
[32] nps_employee_contribution
[33] nps_employer_contribution
[34] nps_additional_contribution
[35] section_80c_investments
[36] self_family_premium
[37] parents_premium
[38] professional_tax_paid
[39] income_or_loss_from_house_property
[40] rent_paid
[41] home_loan_interest
[42] property_type
[43] first_time_home_buyer
[44] section_80eea
[45] disability_status
[46] disability_percentage
[47] dependent_disability_expenses
[48] dependent_severe_disability
[49] savings_interest
[50] ulip_premium_annual
[51] ulip_sum_assured
[52] ulip_holding_period
[53] gratuity_received
[54] leave_encashment
[55] service_years
[56] vrs_compensation
[57] voluntary_retirement
[58] prev_gross_salary
[59] prev_pf_contribution
[60] prev_tds
```

---

## Tax Calculation Fields (Most Commonly Used)

| Index | Field Name | Usage |
|-------|-----------|-------|
| **[3]** | age | 80D limits, 80TTA vs 80TTB |
| **[4]** | parent_age | 80D parent limits |
| **[5]** | number_of_children | CEA, CHA exemptions |
| **[8]** | city_type | HRA exemption (Metro vs Non-Metro) |
| **[10]** | tax_regime | OLD vs NEW regime |
| **[14]** | gross_salary | Base for tax calculation |
| **[15]** | basic_salary | HRA, PF, NPS calculations |
| **[16]** | hra_received | HRA exemption |
| **[18]** | transport_allowance | Transport exemption (disabled only) |
| **[19]** | conveyance_allowance | Conveyance exemption (max ₹19,200) |
| **[20]** | meal_vouchers | Meal exemption (max ₹26,400) |
| **[21]** | lta_received | LTA exemption (₹0 in April forecast) |
| **[22]** | children_education_allowance | CEA exemption (₹100/child/month) |
| **[23]** | children_hostel_allowance | CHA exemption (₹300/child/month) |
| **[25]** | telephone_reimbursement | Fully taxable (₹0 exemption) |
| **[32]** | nps_employee_contribution | 80CCD(1) - part of 80C limit |
| **[33]** | nps_employer_contribution | 80CCD(2) - separate from 80C |
| **[34]** | nps_additional_contribution | 80CCD(1B) - additional ₹50K |
| **[35]** | section_80c_investments | 80C deduction (max ₹1.5L) |
| **[36]** | self_family_premium | 80D self/family |
| **[37]** | parents_premium | 80D parents |
| **[38]** | professional_tax_paid | PT deduction (OLD regime only) |
| **[39]** | income_or_loss_from_house_property | House property income |
| **[40]** | rent_paid | HRA exemption calculation |
| **[41]** | home_loan_interest | Section 24(b) |
| **[42]** | property_type | Self-occupied vs Let-out |
| **[43]** | first_time_home_buyer | Section 80EEA eligibility |
| **[44]** | section_80eea | 80EEA deduction |
| **[45]** | disability_status | Section 80U |
| **[46]** | disability_percentage | 80U amount (₹75K or ₹1.25L) |
| **[48]** | dependent_severe_disability | Section 80DD |
| **[49]** | savings_interest | 80TTA (non-senior) or 80TTB (senior) |
| **[50-52]** | ULIP fields | Capital gains taxation |
| **[53]** | gratuity_received | Gratuity exemption |
| **[54]** | leave_encashment | Leave encashment exemption |
| **[58]** | prev_gross_salary | Previous employer (Form 12B) |
| **[59]** | prev_pf_contribution | Previous employer PF |
| **[60]** | prev_tds | Previous employer TDS |

---

## ✅ VERIFIED CORRECT - All indices match actual CSV

This mapping has been verified against the actual CSV file. Use this as the single source of truth.

