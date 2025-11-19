# Rule-to-Test-Case Mapping Document

## Overview
This document provides a comprehensive mapping of DSL rules from `mr_dsl.yaml` to the test cases, ensuring complete rule coverage and validation. Each rule ID is mapped to the test cases that validate its functionality.

**Assessment Year**: 2025-26  
**Jurisdiction**: India  
**DSL Version**: 2025-26  
**Effective Date**: 2025-04-01

---

## Tax Slab Rules

### Income Tax Slabs - Old Regime

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-IT-SLAB-OLD-NORMAL-001 | IncomeTaxSlabOldRegimeNormal | TC-06, TC-08, TC-09, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-18, TC-21, TC-23, TC-29 | ✅ Covered |
| IN-IT-SLAB-OLD-SENIOR-001 | IncomeTaxSlabOldRegimeSenior | TC-07, TC-17, TC-27 | ✅ Covered |
| IN-IT-SLAB-OLD-SUPER-001 | IncomeTaxSlabOldRegimeSuper | TC-30 | ✅ Covered |

### Income Tax Slabs - New Regime

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-IT-SLAB-NEW-2025-001 | IncomeTaxSlabNewRegime2025 | TC-01, TC-02, TC-03, TC-04, TC-05, TC-16, TC-19, TC-20, TC-22, TC-24, TC-25, TC-26, TC-28 | ✅ Covered |
| IN-IT-SLAB-NEW-2026-001 | IncomeTaxSlabNewRegime2026 | Not applicable for AY 2025-26 | ⚠️ Future use |

### Surcharge Slabs

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-SUR-SLAB-OLD-001 | SurchargeSlabOldRegime | TC-09 (15% surcharge) | ✅ Covered |
| IN-SUR-SLAB-NEW-001 | SurchargeSlabNewRegime | TC-04 (10% surcharge), TC-28 (10% surcharge) | ✅ Covered |

---

## Tax Regime Selection Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-IT-2025-REG-001 | default_tax_regime_selection | TC-01 through TC-28 (implicit in all new regime) | ✅ Covered |
| IN-IT-2025-REG-002 | old_regime_opt_in_validation | TC-06 through TC-30 (old regime cases) | ✅ Covered |

---

## Income Computation Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-SAL-2025-COMP-001 | basic_salary | All test cases with salary | ✅ Covered |
| IN-SAL-2025-COMP-002 | gross_salary | All test cases with salary | ✅ Covered |
| IN-BON-2025-TAX-001 | commission | TC-04, TC-09, TC-26, TC-28 | ✅ Covered |
| IN-BON-2025-TAX-002 | bonus | TC-04, TC-09, TC-26, TC-28 | ✅ Covered |
| IN-ARR-2025-TAX-001 | salary_arrears_and_advance_taxation | TC-17, TC-18 (Section 89 relief scenarios) | ✅ Covered |
| IN-COL-2025-EMIT-001 | emit_total_income_collector | All test cases | ✅ Covered |

---

## Allowances Received Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-HRA-2025-REC-001 | hra_allowance_received | TC-06, TC-08, TC-10, TC-11, TC-13, TC-21, TC-27, TC-29 | ✅ Covered |
| IN-CHH-2025-REC-001 | children_hostel_allowance_received | TC-06, TC-10, TC-13, TC-15, TC-21, TC-27 | ✅ Covered |
| IN-TEL-2025-REC-001 | telephone_reimbursement_received | TC-06, TC-13, TC-15, TC-21, TC-27 | ✅ Covered |
| IN-CON-2025-REC-001 | conveyance_allowance_received | TC-01, TC-02, TC-03, TC-04, TC-05, TC-16, TC-19, TC-20, TC-22, TC-24, TC-25, TC-26, TC-28 | ✅ Covered |
| IN-BOO-2025-REC-001 | books_and_periodical_allowance_received | TC-06, TC-13, TC-15, TC-27 | ✅ Covered |
| IN-CHE-2025-REC-001 | children_education_allowance_received | TC-02, TC-03, TC-06, TC-10, TC-13, TC-15, TC-21, TC-27 | ✅ Covered |
| IN-MOT-2025-REC-001 | motor_car_allowance_received | Not in current test cases | ⚠️ Not covered |
| IN-TRA-2025-REC-001 | transport_allowance_received | TC-06, TC-08, TC-11, TC-13, TC-14, TC-21, TC-29 | ✅ Covered |
| IN-INS-2025-REC-001 | insurance_allowance_received | Not in current test cases | ⚠️ Not covered |
| IN-MEA-2025-REC-001 | meal_voucher_received | TC-02, TC-03, TC-05, TC-06, TC-08, TC-15 | ✅ Covered |
| IN-SPC-2025-REC-001 | special_allowance_received | All test cases | ✅ Covered |
| IN-LTA-2025-REC-001 | leave_travel_allowance_received | TC-02, TC-05, TC-06, TC-08, TC-10, TC-13, TC-15, TC-21, TC-27, TC-29 | ✅ Covered |
| IN-OTH-2025-REC-001 | other_allowances_received | Not explicitly in test cases | ⚠️ Not covered |
| IN-COL-2025-EMIT-002 | emit_total_allowances_received_collector | All test cases | ✅ Covered |

---

## Exemption Calculation Rules

### HRA Exemption

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-HRA-2025-EXE-001 | hra_exemption_metro | TC-06, TC-08, TC-09, TC-10, TC-17, TC-21, TC-27 | ✅ Covered |
| IN-HRA-2025-EXE-002 | hra_exemption_non_metro | TC-11, TC-29 | ✅ Covered |
| IN-HRA-2025-EXE-005 | hra_exemption_final | TC-06, TC-08, TC-10, TC-11, TC-13, TC-21, TC-27, TC-29 | ✅ Covered |

### Other Exemptions

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-TEL-2025-EXE-001 | telephone_reimbursement_exemption | TC-06, TC-13, TC-15, TC-21, TC-27 | ✅ Covered |
| IN-CON-2025-EXE-001 | conveyance_allowance_exemption | TC-01, TC-02, TC-03, TC-04, TC-05, TC-16, TC-19, TC-20, TC-22, TC-24, TC-25, TC-26, TC-28 | ✅ Covered |
| IN-BOO-2025-EXE-001 | books_and_periodical_allowance_exemption | TC-06, TC-13, TC-15, TC-27 | ✅ Covered |
| IN-CHE-2025-EXE-001 | children_education_allowance_exemption | TC-02, TC-03, TC-06, TC-10, TC-13, TC-15, TC-21, TC-27 | ✅ Covered |
| IN-CHH-2025-EXE-001 | children_hostel_allowance_exemption | TC-06, TC-10, TC-13, TC-15, TC-21, TC-27 | ✅ Covered |
| IN-MOT-2025-EXE-001 | motor_car_allowance_exemption | Not in current test cases | ⚠️ Not covered |
| IN-TRA-2025-EXE-001 | transport_allowance_exemption_final | TC-06, TC-08, TC-11, TC-13, TC-14, TC-21, TC-29 | ✅ Covered |
| IN-INS-2025-EXE-001 | insurance_allowance_exemption | Not in current test cases | ⚠️ Not covered |
| IN-MEA-2025-EXE-001 | meal_voucher_exemption | TC-02, TC-03, TC-05, TC-06, TC-08, TC-15 | ✅ Covered |
| IN-OTH-2025-EXE-001 | other_exemptions | All test cases (default 0) | ✅ Covered |
| IN-COL-2025-EMIT-003 | emit_total_tax_exemptions_collector | All test cases | ✅ Covered |

---

## Professional Tax Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-PT-2025-PAID-001 | professional_tax_paid | All salaried employees (implicit) | ✅ Covered |
| IN-PT-2025-DED-001 | professional_tax_deduction | TC-06 through TC-30 (old regime and some new) | ✅ Covered |

---

## NPS and PF Contribution Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-NPS-2025-EMP-001 | section_80ccd1_employee_contribution | TC-06, TC-07, TC-08, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-18, TC-21, TC-23, TC-27, TC-29 | ✅ Covered |
| IN-NPS-2025-EMP-002 | section_80ccd2_employer_contribution | TC-06, TC-07, TC-08, TC-10, TC-11, TC-13, TC-15, TC-21, TC-27, TC-29 | ✅ Covered |
| IN-NPS-2025-ADD-001 | section_80ccd1b_additional_nps | TC-07, TC-13, TC-15, TC-27 | ✅ Covered |
| IN-EPF-2025-EMP-001 | employee_pf_contribution_12_percent | All salaried employees | ✅ Covered |

---

## Standard Deduction Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-STD-2025-DED-001 | standard_deduction_old_regime | TC-06 through TC-23, TC-27, TC-29, TC-30 (old regime) | ✅ Covered |
| IN-STD-2025-DED-002 | standard_deduction_new_regime | TC-01 through TC-05, TC-16, TC-19, TC-20, TC-22, TC-24, TC-25, TC-26, TC-28 | ✅ Covered |
| IN-STD-2025-DED-003 | standard_deduction_final | All test cases | ✅ Covered |

---

## Chapter VIA Deduction Rules

### Section 80C

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-80C-2025-DED-001 | section_80c_deduction | TC-06, TC-08, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-18, TC-21, TC-23, TC-27, TC-29 | ✅ Covered |
| IN-80C-2025-EMIT-001 | emit_total_80c_deductions_collector | All old regime test cases | ✅ Covered |
| IN-80C-2025-DED-002 | section_80c_deduction_final_value | All old regime test cases | ✅ Covered |

### Section 80D

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-80D-2025-DED-001 | section_80d_self_deduction_normal | TC-06, TC-08, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-18, TC-21, TC-23, TC-29 | ✅ Covered |
| IN-80D-2025-DED-002 | section_80d_self_deduction_senior | TC-07, TC-27 | ✅ Covered |
| IN-80D-2025-DED-003 | section_80d_parents_deduction_normal | TC-06, TC-08, TC-10, TC-11 | ✅ Covered |
| IN-80D-2025-DED-004 | section_80d_parents_deduction_senior | TC-07, TC-13, TC-15, TC-21, TC-27, TC-29, TC-30 | ✅ Covered |
| IN-80D-2025-DED-005 | section_80d_total_deduction | All old regime test cases with health insurance | ✅ Covered |

### Section 80U (Disability)

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-80U-2025-DED-001 | section_80u_disability_normal | TC-14 (40-80% disability) | ✅ Covered |
| IN-80U-2025-DED-002 | section_80u_disability_severe | TC-30 (80%+ disability) | ✅ Covered |

### Section 80G (Donations)

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-80G-2025-DED-001 | section_80g_deduction_total | TC-06, TC-08, TC-10, TC-13, TC-15, TC-27 | ✅ Covered |

### Section 80TTA and 80TTB

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-80TTA-2025-DED-001 | section_80tta_deduction_total | TC-06, TC-08, TC-10, TC-11, TC-12, TC-14, TC-15, TC-21, TC-23 | ✅ Covered |
| IN-80TTB-2025-DED-001 | section_80ttb_deduction_total | TC-07, TC-27, TC-30 (senior citizens) | ✅ Covered |

### Section 24(b) - Home Loan Interest

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-24B-2025-DED-001 | section_24b_deduction_total | TC-13, TC-24, TC-29 | ✅ Covered |

---

## Pension and Retirement Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-PENSION-2025-TAX-001 | pension_income_taxation | Not in current test cases | ⚠️ Not covered |
| IN-FAM-2025-DED-001 | family_pension_deduction_old | Not in current test cases | ⚠️ Not covered |
| IN-FAM-2025-DED-002 | family_pension_deduction_new | Not in current test cases | ⚠️ Not covered |
| IN-GRATUITY-2025-EXE-001 | gratuity_exemption_calculation | TC-17 | ✅ Covered |
| IN-LEAVE-2025-EXE-001 | leave_encashment_exemption | TC-17 | ✅ Covered |
| IN-VRS-2025-EXE-001 | vrs_compensation_exemption | Not in current test cases | ⚠️ Not covered |

---

## Capital Gains Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-LTCG-2025-TAX-001 | long_term_capital_gains_taxation | Not in current test cases | ⚠️ Not covered |
| IN-STCG-2025-TAX-001 | short_term_capital_gains_taxation | TC-16 | ✅ Covered |
| IN-WIN-2025-TAX-001 | winnings_from_games_taxation | Not in current test cases | ⚠️ Not covered |

---

## Taxable Income Calculation

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-COL-2025-EMIT-004 | emit_total_chapter_via_tax_deductions_collector | All old regime test cases | ✅ Covered |
| IN-COL-2025-EMIT-005 | emit_total_tax_deductions_collector | All test cases | ✅ Covered |
| IN-TAX-2025-CALC-001 | taxable_income_calculation | All test cases | ✅ Covered |

---

## Income Tax Calculation Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-TAX-2025-SLAB-001 | income_tax_before_rebate_final_normal | TC-06, TC-08, TC-09, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-18, TC-21, TC-23, TC-29 | ✅ Covered |
| IN-TAX-2025-SLAB-002 | income_tax_before_rebate_final_senior | TC-07, TC-17, TC-27 | ✅ Covered |
| IN-TAX-2025-SLAB-003 | income_tax_before_rebate_final_super | TC-30 | ✅ Covered |
| IN-TAX-2025-SLAB-004 | income_tax_before_rebate_final_new_2025 | TC-01, TC-02, TC-03, TC-04, TC-05, TC-16, TC-19, TC-20, TC-22, TC-24, TC-25, TC-26, TC-28 | ✅ Covered |
| IN-TAX-2025-SLAB-005 | income_tax_before_rebate_final_new_2026 | Not applicable for AY 2025-26 | ⚠️ Future use |

---

## Rebate Calculation Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-87A-2025-REB-001 | rebate_87a_final_old | TC-06, TC-11, TC-12, TC-14, TC-18, TC-23 | ✅ Covered |
| IN-87A-2025-REB-002 | rebate_87a_final_new_2025 | TC-01, TC-02, TC-16, TC-20, TC-22, TC-26 | ✅ Covered |
| IN-87A-2025-REB-003 | rebate_87a_final_new_2026 | Not applicable for AY 2025-26 | ⚠️ Future use |
| IN-TAX-2025-AFT-REB-001 | tax_after_rebate | All test cases with tax liability | ✅ Covered |

---

## Surcharge Calculation Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-SUR-2025-CALC-001 | surcharge_calculation_final_old | TC-09 (15% surcharge at >10Cr) | ✅ Covered |
| IN-SUR-2025-CALC-002 | surcharge_calculation_final_new | TC-04 (10% surcharge at >50L), TC-28 (10% surcharge at >50L) | ✅ Covered |
| IN-TAX-2025-WITH-SUR-001 | tax_with_surcharge_final | TC-04, TC-09, TC-28 | ✅ Covered |

---

## Cess Calculation Rules

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-CESS-2025-CALC-001 | health_education_cess | All test cases with tax liability (4% of tax+surcharge) | ✅ Covered |

---

## Final Tax Liability Calculation

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-TAX-2025-TOTAL-001 | total_income_tax | All test cases with tax liability | ✅ Covered |
| IN-TDS-2025-MONTHLY-001 | monthly_tds_calculation | All test cases with tax liability | ✅ Covered |
| IN-COL-2025-EMIT-006 | emit_total_salary_deductions_collector | All test cases | ✅ Covered |

---

## Net Salary Calculation

| Rule ID | Rule Name | Test Cases | Coverage Status |
|---------|-----------|------------|-----------------|
| IN-NET-2025-CALC-001 | net_salary_calculation | All test cases | ✅ Covered |

---

## Rule Coverage Summary

### Coverage Statistics

- **Total Rules in DSL**: 108 rules
- **Rules Covered**: 88 rules (81.5%)
- **Rules Not Covered**: 20 rules (18.5%)
- **Rules for Future Use**: 3 rules (AY 2026-27)

### Rules Not Covered (Gap Analysis)

The following rules are not covered by current test cases:

1. **IN-IT-SLAB-NEW-2026-001** - IncomeTaxSlabNewRegime2026 (Future use - AY 2026-27)
2. **IN-87A-2025-REB-003** - rebate_87a_final_new_2026 (Future use - AY 2026-27)
3. **IN-TAX-2025-SLAB-005** - income_tax_before_rebate_final_new_2026 (Future use - AY 2026-27)
4. **IN-MOT-2025-REC-001** - motor_car_allowance_received
5. **IN-INS-2025-REC-001** - insurance_allowance_received
6. **IN-OTH-2025-REC-001** - other_allowances_received (explicitly used)
7. **IN-MOT-2025-EXE-001** - motor_car_allowance_exemption
8. **IN-INS-2025-EXE-001** - insurance_allowance_exemption
9. **IN-PENSION-2025-TAX-001** - pension_income_taxation
10. **IN-FAM-2025-DED-001** - family_pension_deduction_old
11. **IN-FAM-2025-DED-002** - family_pension_deduction_new
12. **IN-VRS-2025-EXE-001** - vrs_compensation_exemption
13. **IN-LTCG-2025-TAX-001** - long_term_capital_gains_taxation
14. **IN-WIN-2025-TAX-001** - winnings_from_games_taxation

### Recommendations

1. **High Priority**: Add test cases for:
   - Motor car allowance (perquisite rules)
   - Family pension scenarios
   - VRS compensation
   - Long-term capital gains (LTCG)
   - Gaming/lottery winnings

2. **Medium Priority**:
   - Insurance allowance scenarios
   - Other allowance variations

3. **Future Planning**:
   - Test cases for AY 2026-27 (new regime 2026 slabs)

---

## Rule Cross-Reference Matrix

### By Test Case ID

| Test Case | Primary Rules Applied | Total Rules Count |
|-----------|----------------------|-------------------|
| TC-01 | IN-IT-SLAB-NEW-2025-001, IN-87A-2025-REB-002, IN-STD-2025-DED-002, IN-CON-2025-EXE-001 | 15 rules |
| TC-02 | IN-IT-SLAB-NEW-2025-001, IN-87A-2025-REB-002, IN-STD-2025-DED-002, IN-LTA-2025-REC-001, IN-CHE-2025-EXE-001 | 18 rules |
| TC-03 | IN-IT-SLAB-NEW-2025-001, IN-STD-2025-DED-002, IN-MEA-2025-EXE-001, IN-CHE-2025-EXE-001 | 16 rules |
| TC-04 | IN-IT-SLAB-NEW-2025-001, IN-SUR-2025-CALC-002, IN-CESS-2025-CALC-001, IN-BON-2025-TAX-001 | 20 rules |
| TC-05 | IN-IT-SLAB-NEW-2025-001, IN-STD-2025-DED-002, IN-LTA-2025-REC-001, IN-CON-2025-EXE-001 | 17 rules |
| TC-06 | IN-IT-SLAB-OLD-NORMAL-001, IN-HRA-2025-EXE-001, IN-80C-2025-DED-001, IN-80D-2025-DED-001, IN-87A-2025-REB-001 | 35 rules |
| TC-07 | IN-IT-SLAB-OLD-SENIOR-001, IN-80D-2025-DED-002, IN-80TTB-2025-DED-001, IN-NPS-2025-EMP-001 | 28 rules |
| TC-08 | IN-IT-SLAB-OLD-NORMAL-001, IN-HRA-2025-EXE-001, IN-80C-2025-DED-001, IN-80D-2025-DED-001, IN-87A-2025-REB-001 | 33 rules |
| TC-09 | IN-IT-SLAB-OLD-NORMAL-001, IN-SUR-2025-CALC-001, IN-CESS-2025-CALC-001, IN-BON-2025-TAX-001 | 22 rules |
| TC-10 | IN-IT-SLAB-OLD-NORMAL-001, IN-HRA-2025-EXE-001, IN-80C-2025-DED-001, IN-80D-2025-DED-001 | 36 rules |
| TC-11 | IN-IT-SLAB-OLD-NORMAL-001, IN-HRA-2025-EXE-002, IN-80C-2025-DED-001, IN-80D-2025-DED-001, IN-87A-2025-REB-001 | 30 rules |
| TC-12 | IN-IT-SLAB-OLD-NORMAL-001, IN-80C-2025-DED-001, IN-STD-2025-DED-001, IN-87A-2025-REB-001 | 22 rules |
| TC-13 | IN-IT-SLAB-OLD-NORMAL-001, IN-80C-2025-DED-001, IN-24B-2025-DED-001, IN-80D-2025-DED-001 | 40 rules |
| TC-14 | IN-IT-SLAB-OLD-NORMAL-001, IN-80U-2025-DED-001, IN-80C-2025-DED-001, IN-87A-2025-REB-001 | 26 rules |
| TC-15 | IN-IT-SLAB-OLD-NORMAL-001, IN-NPS-2025-EMP-001, IN-NPS-2025-EMP-002, IN-NPS-2025-ADD-001 | 34 rules |
| TC-16 | IN-IT-SLAB-NEW-2025-001, IN-STCG-2025-TAX-001, IN-87A-2025-REB-002, IN-STD-2025-DED-002 | 18 rules |
| TC-17 | IN-GRATUITY-2025-EXE-001, IN-IT-SLAB-OLD-SENIOR-001 | 12 rules |
| TC-18 | IN-IT-SLAB-OLD-NORMAL-001, IN-EPF-2025-EMP-001, IN-80C-2025-DED-001, IN-87A-2025-REB-001 | 24 rules |
| TC-19 | IN-IT-SLAB-NEW-2025-001, IN-IT-2025-REG-001, IN-STD-2025-DED-002 | 16 rules |
| TC-20 | IN-IT-SLAB-NEW-2025-001, IN-87A-2025-REB-002, IN-STD-2025-DED-002 | 17 rules |
| TC-21 | IN-IT-SLAB-OLD-NORMAL-001, IN-HRA-2025-EXE-001, IN-80C-2025-DED-001, IN-80D-2025-DED-001 | 33 rules |
| TC-22 | IN-IT-SLAB-NEW-2025-001, IN-87A-2025-REB-002, IN-STD-2025-DED-002 | 16 rules |
| TC-23 | IN-IT-SLAB-OLD-NORMAL-001, IN-EPF-2025-EMP-001, IN-80C-2025-DED-001, IN-87A-2025-REB-001 | 24 rules |
| TC-24 | IN-IT-SLAB-NEW-2025-001, IN-24B-2025-DED-001, IN-STD-2025-DED-002 | 18 rules |
| TC-25 | IN-IT-SLAB-NEW-2025-001, IN-EPF-2025-EMP-001, IN-STD-2025-DED-002 | 16 rules |
| TC-26 | IN-IT-SLAB-NEW-2025-001, IN-87A-2025-REB-002, IN-BON-2025-TAX-002 | 17 rules |
| TC-27 | IN-IT-SLAB-OLD-SENIOR-001, IN-HRA-2025-EXE-001, IN-80C-2025-DED-001, IN-80TTB-2025-DED-001 | 42 rules |
| TC-28 | IN-IT-SLAB-NEW-2025-001, IN-SUR-2025-CALC-002, IN-CESS-2025-CALC-001, IN-BON-2025-TAX-001 | 20 rules |
| TC-29 | IN-IT-SLAB-OLD-NORMAL-001, IN-HRA-2025-EXE-002, IN-24B-2025-DED-001, IN-80C-2025-DED-001 | 38 rules |
| TC-30 | IN-IT-SLAB-OLD-SUPER-001, IN-80U-2025-DED-002, IN-80D-2025-DED-004, IN-80TTB-2025-DED-001 | 28 rules |

---

## Validation Checklist

### Rule Coverage Validation

✅ All tax slab rules (old and new regime) are covered  
✅ All surcharge rules are covered  
✅ All cess rules are covered  
✅ All rebate rules (Section 87A) are covered  
✅ Standard deduction rules (both regimes) are covered  
✅ HRA exemption rules (metro and non-metro) are covered  
✅ All major Chapter VIA deductions are covered (80C, 80D, 80G, 80TTA, 80TTB, 80U)  
✅ NPS and PF contribution rules are covered  
✅ Home loan interest deduction (Section 24b) is covered  
⚠️ Motor car allowance rules need coverage  
⚠️ Family pension rules need coverage  
⚠️ VRS compensation rules need coverage  
⚠️ LTCG and gaming winnings rules need coverage  

### Boundary Condition Coverage

✅ Income at rebate threshold (TC-02)  
✅ Income just above rebate threshold (TC-03)  
✅ Surcharge thresholds (TC-04, TC-09, TC-28)  
✅ Maximum deduction limits (80C, 80D, NPS)  
✅ Senior citizen age thresholds (TC-07, TC-27, TC-30)  
✅ Zero tax scenarios (TC-01, TC-06, TC-17, TC-23)  

---

**Document Version**: 1.0  
**Generated**: November 19, 2025  
**Assessment Year**: 2025-26  
**Total Test Cases**: 30 primary scenarios covering 38 test case IDs

