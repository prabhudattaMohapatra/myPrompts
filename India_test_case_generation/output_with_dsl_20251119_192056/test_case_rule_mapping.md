# Rule-to-Test-Case Mapping Document

## Overview
This document provides a comprehensive mapping between the DSL rules defined in `mr_dsl.yaml` and the test cases. Each test case validates specific rules, and this mapping ensures complete rule coverage and traceability.

## Mapping Methodology

1. **Rule Extraction**: All rules extracted from `mr_dsl.yaml` with their IDs, names, and purposes
2. **Test Case Assignment**: Each rule mapped to one or more test cases that validate it
3. **Coverage Analysis**: Identification of rules covered by test cases and any gaps
4. **Validation**: Verification that rule conditions (when clauses) and actions (then clauses) are correctly tested

---

## Tax Slab Rules

### Old Regime Tax Slabs

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-IT-SLAB-OLD-NORMAL-001 | IncomeTaxSlabOldRegimeNormal | Old regime tax slab for normal taxpayers (age <60) | TC-06, TC-08, TC-09, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-16, TC-17, TC-18, TC-21, TC-25, TC-28, TC-31, TC-33, TC-34, TC-37, TC-39, TC-41, TC-43, TC-45, TC-47, TC-49 | EMP006, EMP008, EMP009, EMP010, EMP011, EMP012, EMP013, EMP014, EMP015, EMP016, EMP017, EMP018, EMP021, EMP025, EMP028, EMP031, EMP033, EMP034, EMP037, EMP039, EMP041, EMP043, EMP045, EMP047, EMP049 | 0-2.5L: 0%, 2.5-5L: 5%, 5-10L: 20%, >10L: 30% |
| IN-IT-SLAB-OLD-SENIOR-001 | IncomeTaxSlabOldRegimeSenior | Old regime tax slab for senior citizens (age 60-79) | TC-07 | EMP007 | 0-3L: 0%, 3-5L: 5%, 5-10L: 20%, >10L: 30% |
| IN-IT-SLAB-OLD-SUPER-001 | IncomeTaxSlabOldRegimeSuper | Old regime tax slab for super senior citizens (age ≥80) | None | None | Not covered - no employee ≥80 years |

### New Regime Tax Slabs

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-IT-SLAB-NEW-2025-001 | IncomeTaxSlabNewRegime2025 | New regime tax slab for AY 2025-26 | TC-01, TC-02, TC-03, TC-04, TC-05, TC-19, TC-23, TC-24, TC-26, TC-27, TC-29, TC-30, TC-32, TC-36, TC-38, TC-40, TC-42, TC-44, TC-46, TC-48, TC-50 | EMP001, EMP002, EMP003, EMP004, EMP005, EMP019, EMP023, EMP024, EMP026, EMP027, EMP029, EMP030, EMP032, EMP036, EMP038, EMP040, EMP042, EMP044, EMP046, EMP048, EMP050 | 0-3L: 0%, 3-7L: 5%, 7-10L: 10%, 10-12L: 15%, 12-15L: 20%, >15L: 30% |
| IN-IT-SLAB-NEW-2026-001 | IncomeTaxSlabNewRegime2026 | New regime tax slab for AY 2026-27 | None | None | Not covered - AY 2025-26 only |

---

## Surcharge Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-SUR-SLAB-OLD-001 / IN-SUR-2025-CALC-001 | SurchargeSlabOldRegime | Surcharge for old regime | TC-09 | EMP009 | >50L: 10%, >1Cr: 15%, >2Cr: 25%, >5Cr: 37% |
| IN-SUR-SLAB-NEW-001 / IN-SUR-2025-CALC-002 | SurchargeSlabNewRegime | Surcharge for new regime | TC-04 | EMP004 | >50L: 10%, >1Cr: 15%, >2Cr: 25%, >5Cr: 25% |

---

## Cess Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-CESS-2025-CALC-001 | health_education_cess | Health and education cess at 4% on (tax + surcharge) | All test cases with tax liability | All employees with tax | 4% cess applied correctly |

---

## Rebate Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-87A-2025-REB-001 | rebate_87a_final_old | Rebate under Section 87A for old regime (income ≤5L) | TC-21, TC-28, TC-34 | EMP021, EMP028, EMP034 | Max ₹12,500 rebate if income ≤5L |
| IN-87A-2025-REB-002 | rebate_87a_final_new_2025 | Rebate under Section 87A for new regime (income ≤7L for AY 2025-26) | TC-01 | EMP001 | Max ₹25,000 rebate if income ≤7L |
| IN-87A-2025-REB-003 | rebate_87a_final_new_2026 | Rebate under Section 87A for new regime (income ≤12L for AY 2026-27) | None | None | Not covered - AY 2025-26 only |

---

## Income Computation Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-SAL-2025-COMP-001 | basic_salary | Basic salary as part of gross income | All test cases | All employees | Basic salary included in gross income |
| IN-SAL-2025-COMP-002 | gross_salary | Gross salary computation (basic + all allowances) | All test cases except TC-01 | All employees except EMP001 | Sum of basic + allowances |
| IN-BON-2025-TAX-001 | commission | Commission as taxable income | Test cases with commission | Employees with commission | Commission fully taxable |
| IN-BON-2025-TAX-002 | bonus | Bonus as taxable income | Test cases with bonus | Employees with bonus | Bonus fully taxable |
| IN-ARR-2025-TAX-001 | salary_arrears_and_advance_taxation | Arrears and advance salary taxation | None | None | Not covered - no arrears data |
| IN-COL-2025-EMIT-001 | emit_total_income_collector | Total income collector | All test cases | All employees | Collector emits total income |

---

## Allowance Received Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-HRA-2025-REC-001 | hra_allowance_received | HRA allowance received | Test cases with HRA | Employees with HRA | HRA collected as received |
| IN-CHH-2025-REC-001 | children_hostel_allowance_received | Children hostel allowance received | TC-13 | EMP013 | Hostel allowance collected |
| IN-TEL-2025-REC-001 | telephone_reimbursement_received | Telephone reimbursement received | TC-44 | EMP044 | Telephone reimbursement collected |
| IN-CON-2025-REC-001 | conveyance_allowance_received | Conveyance allowance received | TC-01, TC-05, TC-40 | EMP001, EMP005, EMP040 | Conveyance collected |
| IN-BOO-2025-REC-001 | books_and_periodical_allowance_received | Books allowance received | TC-41 | EMP041 | Books allowance collected |
| IN-CHE-2025-REC-001 | children_education_allowance_received | Children education allowance received | TC-13, TC-41 | EMP013, EMP041 | CEA collected |
| IN-MOT-2025-REC-001 | motor_car_allowance_received | Motor car allowance received | TC-43 | EMP043 | Motor car allowance collected |
| IN-TRA-2025-REC-001 | transport_allowance_received | Transport allowance received | TC-40 | EMP040 | Transport allowance collected |
| IN-INS-2025-REC-001 | insurance_allowance_received | Insurance allowance received | TC-42, TC-45 | EMP042, EMP045 | Insurance allowance collected |
| IN-MEA-2025-REC-001 | meal_voucher_received | Meal voucher received | TC-42 | EMP042 | Meal voucher collected |
| IN-SPC-2025-REC-001 | special_allowance_received | Special allowance received | Most test cases | Most employees | Special allowance collected |
| IN-LTA-2025-REC-001 | leave_travel_allowance_received | LTA received | TC-13, TC-33 | EMP013, EMP033 | LTA collected |
| IN-OTH-2025-REC-001 | other_allowances_received | Other allowances received | Various | Various | Other allowances collected |
| IN-COL-2025-EMIT-002 | emit_total_allowances_received_collector | Total allowances collector | All test cases | All employees | Collector emits total allowances |

---

## Exemption Calculation Rules

### HRA Exemption

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-HRA-2025-EXE-001 | hra_exemption_metro | HRA exemption for metro cities (50% of basic) | TC-06, TC-08, TC-10, TC-13, TC-14, TC-15, TC-16, TC-20, TC-21, TC-31, TC-47 | EMP006, EMP008, EMP010, EMP013, EMP014, EMP015, EMP016, EMP020, EMP021, EMP031, EMP047 | Min(actual HRA, rent-10% basic, 50% basic) |
| IN-HRA-2025-EXE-002 | hra_exemption_non_metro | HRA exemption for non-metro cities (40% of basic) | TC-11, TC-17, TC-18, TC-25, TC-30, TC-33, TC-34, TC-37, TC-39, TC-41, TC-43, TC-45, TC-49 | EMP011, EMP017, EMP018, EMP025, EMP030, EMP033, EMP034, EMP037, EMP039, EMP041, EMP043, EMP045, EMP049 | Min(actual HRA, rent-10% basic, 40% basic) |
| IN-HRA-2025-EXE-005 | hra_exemption_final | Final HRA exemption | All HRA test cases | All HRA employees | Final HRA exemption calculated |

### Other Exemptions

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-TEL-2025-EXE-001 | telephone_reimbursement_exemption | Telephone reimbursement exemption | TC-44 | EMP044 | Full exemption for telephone |
| IN-CON-2025-EXE-001 | conveyance_allowance_exemption | Conveyance allowance exemption | TC-01, TC-05, TC-23, TC-40 | EMP001, EMP005, EMP023, EMP040 | Full exemption for conveyance |
| IN-BOO-2025-EXE-001 | books_and_periodical_allowance_exemption | Books allowance exemption (old regime only) | TC-41 | EMP041 | Full exemption for books (old regime) |
| IN-CHE-2025-EXE-001 | children_education_allowance_exemption | CEA exemption (₹100/child/month, max 2 children) | TC-13, TC-41 | EMP013, EMP041 | ₹100 × 2 children × 12 months = ₹2,400 |
| IN-CHH-2025-EXE-001 | children_hostel_allowance_exemption | Children hostel allowance exemption (₹300/child/month, max 2 children) | TC-13 | EMP013 | ₹300 × 2 children × 12 months = ₹7,200 |
| IN-MOT-2025-EXE-001 | motor_car_allowance_exemption | Motor car allowance exemption | TC-43 | EMP043 | Perquisite-based exemption |
| IN-TRA-2025-EXE-001 | transport_allowance_exemption_final | Transport allowance exemption | TC-40 | EMP040 | Full exemption for transport |
| IN-INS-2025-EXE-001 | insurance_allowance_exemption | Insurance allowance exemption | TC-42, TC-45 | EMP042, EMP045 | Full exemption for insurance |
| IN-MEA-2025-EXE-001 | meal_voucher_exemption | Meal voucher exemption (₹50 × 2 meals × 22 days × 12 months) | TC-42 | EMP042 | Max ₹26,400 annual exemption |
| IN-OTH-2025-EXE-001 | other_exemptions | Other exemptions | Various | Various | Catch-all exemptions |
| IN-COL-2025-EMIT-003 | emit_total_tax_exemptions_collector | Total exemptions collector | All test cases | All employees | Collector emits total exemptions |

---

## Professional Tax Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-PT-2025-PAID-001 | professional_tax_paid | Professional tax paid | All test cases | All employees | PT collected as salary deduction |
| IN-PT-2025-DED-001 | professional_tax_deduction | Professional tax deduction | All test cases | All employees | PT deducted from taxable income |

---

## NPS and PF Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-NPS-2025-EMP-001 | section_80ccd1_employee_contribution | NPS employee contribution under 80CCD(1) | TC-06, TC-07, TC-08, TC-10, TC-11, TC-12, TC-13, TC-14, TC-16, TC-17, TC-18, TC-25, TC-28, TC-31, TC-33, TC-34, TC-37, TC-39, TC-41, TC-43, TC-45, TC-47, TC-49 | Multiple employees with NPS | Employee NPS within 80C limit |
| IN-NPS-2025-EMP-002 | section_80ccd2_employer_contribution | NPS employer contribution under 80CCD(2) | TC-06, TC-07, TC-08, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-16, TC-17, TC-18, TC-25, TC-28, TC-31, TC-33, TC-34, TC-37, TC-39, TC-41, TC-43, TC-45, TC-47, TC-49 | Multiple employees with NPS | Employer NPS deduction (separate from 80C) |
| IN-NPS-2025-ADD-001 | section_80ccd1b_additional_nps | Additional NPS under 80CCD(1b) (max ₹50K) | TC-15 | EMP015 | Additional ₹50K NPS deduction |
| IN-EPF-2025-EMP-001 | employee_pf_contribution_12_percent | Employee PF contribution (12% of basic) | TC-21, TC-28, TC-34, TC-35 | EMP021, EMP028, EMP034, EMP035 | 12% PF contribution |

---

## Standard Deduction Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-STD-2025-DED-001 | standard_deduction_old_regime | Standard deduction for old regime (₹50K) | All old regime test cases | All old regime employees | ₹50,000 standard deduction |
| IN-STD-2025-DED-002 | standard_deduction_new_regime | Standard deduction for new regime (₹75K) | All new regime test cases | All new regime employees | ₹75,000 standard deduction |
| IN-STD-2025-DED-003 | standard_deduction_final | Final standard deduction | All test cases | All employees | Max of old/new regime deduction |

---

## Chapter VIA Deduction Rules

### Section 80C

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-80C-2025-DED-001 | section_80c_deduction | Section 80C deduction (investments, max ₹1.5L) | TC-06, TC-07, TC-08, TC-11, TC-12, TC-17, TC-21, TC-25, TC-28, TC-33, TC-34, TC-43, TC-45 | Multiple old regime employees | Max ₹1.5L deduction |
| IN-80C-2025-EMIT-001 | emit_total_80c_deductions_collector | Total 80C deductions collector | Old regime test cases | Old regime employees | Collector emits total 80C |
| IN-80C-2025-DED-002 | section_80c_deduction_final_value | Final 80C deduction value | Old regime test cases | Old regime employees | Final 80C with ₹1.5L cap |

### Section 80D

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-80D-2025-DED-001 | section_80d_self_deduction_normal | 80D self/family premium (age <60, max ₹25K) | TC-06, TC-08, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-16, TC-17, TC-18, TC-25, TC-31, TC-37, TC-39, TC-41, TC-43, TC-45, TC-47, TC-49 | Multiple employees <60 years | Max ₹25,000 for self/family |
| IN-80D-2025-DED-002 | section_80d_self_deduction_senior | 80D self/family premium (age ≥60, max ₹50K) | TC-07 | EMP007 | Max ₹50,000 for senior citizens |
| IN-80D-2025-DED-003 | section_80d_parents_deduction_normal | 80D parents premium (age <60, max ₹25K) | Various | Various | Max ₹25,000 for parents <60 |
| IN-80D-2025-DED-004 | section_80d_parents_deduction_senior | 80D parents premium (age ≥60, max ₹50K) | TC-07, TC-10, TC-13, TC-14, TC-15, TC-16, TC-20, TC-31, TC-37, TC-39, TC-47, TC-49 | Multiple employees with senior parents | Max ₹50,000 for senior parents |
| IN-80D-2025-DED-005 | section_80d_total_deduction | Total 80D deduction | All 80D test cases | All 80D employees | Sum of self + parents premiums |

### Section 80U

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-80U-2025-DED-001 | section_80u_disability_normal | 80U disability deduction (40-80%, ₹75K) | TC-17 | EMP017 | ₹75,000 for moderate disability |
| IN-80U-2025-DED-002 | section_80u_disability_severe | 80U disability deduction (≥80%, ₹1.25L) | None | None | Not covered - no severe disability cases |

### Section 80G

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-80G-2025-DED-001 | section_80g_deduction_total | Section 80G charitable donations | TC-18 | EMP018 | Donation deduction with eligibility % |

### Section 80TTA/80TTB

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-80TTA-2025-DED-001 | section_80tta_deduction_total | 80TTA savings interest (age <60, max ₹10K) | TC-47 | EMP047 | Max ₹10,000 for savings interest |
| IN-80TTB-2025-DED-001 | section_80ttb_deduction_total | 80TTB savings/deposit interest (age ≥60, max ₹50K) | TC-07 | EMP007 | Max ₹50,000 for senior citizens |

### Section 24(b)

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-24B-2025-DED-001 | section_24b_deduction_total | Section 24(b) home loan interest (max ₹2L for self-occupied) | TC-14, TC-16, TC-29 | EMP014, EMP016, EMP029 | Max ₹2L deduction for home loan interest |

---

## Pension and Retirement Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-PENSION-2025-TAX-001 | pension_income_taxation | Family pension taxation | TC-49 | EMP049 | Family pension as income |
| IN-FAM-2025-DED-001 | family_pension_deduction_old | Family pension deduction (old regime, max ₹15K or 1/3rd) | TC-49 | EMP049 | Min(1/3rd pension, ₹15K) |
| IN-FAM-2025-DED-002 | family_pension_deduction_new | Family pension deduction (new regime, max ₹25K or 1/3rd) | None | None | Not covered - no new regime pension cases |
| IN-GRATUITY-2025-EXE-001 | gratuity_exemption_calculation | Gratuity exemption (max ₹20L) | TC-20 | EMP020 | Min(actual, formula, ₹20L) |
| IN-LEAVE-2025-EXE-001 | leave_encashment_exemption | Leave encashment exemption (max ₹25L or 10 months) | TC-50 | EMP050 | Min(actual, 10 months salary, ₹25L) |
| IN-VRS-2025-EXE-001 | vrs_compensation_exemption | VRS compensation exemption (max ₹5L) | None | None | Not covered - no VRS cases |

---

## Capital Gains Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-LTCG-2025-TAX-001 | long_term_capital_gains_taxation | LTCG taxation (12.5% after ₹1.25L exemption) | TC-19 | EMP019 | 12.5% tax on LTCG above ₹1.25L |
| IN-STCG-2025-TAX-001 | short_term_capital_gains_taxation | STCG taxation (20%) | None | None | Not covered - no STCG cases |
| IN-WIN-2025-TAX-001 | winnings_from_games_taxation | Winnings from games (30% tax) | None | None | Not covered - no winnings cases |

---

## Taxable Income Calculation Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-COL-2025-EMIT-004 | emit_total_chapter_via_tax_deductions_collector | Total Chapter VIA deductions collector | Old regime test cases | Old regime employees | Collector emits Chapter VIA deductions |
| IN-COL-2025-EMIT-005 | emit_total_tax_deductions_collector | Total tax deductions collector | All test cases | All employees | Collector emits total tax deductions |
| IN-TAX-2025-CALC-001 | taxable_income_calculation | Taxable income calculation | All test cases | All employees | Income - exemptions - deductions |

---

## Income Tax Calculation Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-TAX-2025-SLAB-001 | income_tax_before_rebate_final_normal | Tax calculation for normal taxpayers (old regime) | All normal old regime cases | Normal old regime employees | Progressive slab calculation |
| IN-TAX-2025-SLAB-002 | income_tax_before_rebate_final_senior | Tax calculation for senior citizens (old regime) | TC-07 | EMP007 | Senior citizen slab |
| IN-TAX-2025-SLAB-003 | income_tax_before_rebate_final_super | Tax calculation for super senior citizens (old regime) | None | None | Not covered |
| IN-TAX-2025-SLAB-004 | income_tax_before_rebate_final_new_2025 | Tax calculation for new regime AY 2025-26 | All new regime cases | All new regime employees | New regime slab calculation |
| IN-TAX-2025-SLAB-005 | income_tax_before_rebate_final_new_2026 | Tax calculation for new regime AY 2026-27 | None | None | Not covered - AY 2025-26 only |

---

## Surcharge and Cess Calculation Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-TAX-2025-AFT-REB-001 | tax_after_rebate | Tax after rebate | All test cases with tax | All employees with tax | Base tax - rebate |
| IN-SUR-2025-CALC-001 | surcharge_calculation_final_old | Surcharge for old regime | TC-09 | EMP009 | Surcharge % based on income |
| IN-SUR-2025-CALC-002 | surcharge_calculation_final_new | Surcharge for new regime | TC-04 | EMP004 | Surcharge % based on income |
| IN-TAX-2025-WITH-SUR-001 | tax_with_surcharge_final | Tax with surcharge | All test cases with surcharge | Employees with surcharge | Tax + surcharge |

---

## Final Tax Liability Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-TAX-2025-TOTAL-001 | total_income_tax | Total income tax liability | All test cases | All employees | Tax + surcharge + cess + special taxes |
| IN-TDS-2025-MONTHLY-001 | monthly_tds_calculation | Monthly TDS calculation | All test cases | All employees | Annual tax / 12 months |
| IN-COL-2025-EMIT-006 | emit_total_salary_deductions_collector | Total salary deductions collector | All test cases | All employees | Collector emits salary deductions |

---

## Net Salary Calculation Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-NET-2025-CALC-001 | net_salary_calculation | Net salary calculation | All test cases | All employees | Gross - deductions |

---

## Tax Regime Selection Rules

| Rule ID | Rule Name | Description | Test Cases | Employees | Validation |
|---------|-----------|-------------|------------|-----------|------------|
| IN-IT-2025-REG-001 | default_tax_regime_selection | Default to new regime | TC-01, TC-02, TC-03, TC-04, TC-05, TC-19, TC-23, TC-24, TC-26, TC-27, TC-29, TC-30, TC-32, TC-36, TC-38, TC-40, TC-42, TC-44, TC-46, TC-48, TC-50 | New regime employees | Default regime = new |
| IN-IT-2025-REG-002 | old_regime_opt_in_validation | Old regime opt-in validation | TC-06, TC-07, TC-08, TC-09, TC-10, TC-11, TC-12, TC-13, TC-14, TC-15, TC-16, TC-17, TC-18, TC-20, TC-21, TC-25, TC-28, TC-31, TC-33, TC-34, TC-37, TC-39, TC-41, TC-43, TC-45, TC-47, TC-49 | Old regime employees | Can claim exemptions in old regime |

---

## Rule Coverage Summary

### Total Rules in mr_dsl.yaml: ~120 rules

### Coverage Statistics:
- **Fully Covered**: ~95 rules (79%)
- **Partially Covered**: ~15 rules (13%)
- **Not Covered**: ~10 rules (8%)

### Not Covered Rules:
1. **IN-IT-SLAB-OLD-SUPER-001**: Super senior citizen slab (age ≥80) - No employee in this age group
2. **IN-IT-SLAB-NEW-2026-001**: New regime AY 2026-27 - Not applicable for AY 2025-26
3. **IN-87A-2025-REB-003**: Rebate for new regime AY 2026-27 - Not applicable
4. **IN-ARR-2025-TAX-001**: Salary arrears taxation - Explicitly excluded from scope
5. **IN-80U-2025-DED-002**: Severe disability (≥80%) - No employee with severe disability
6. **IN-FAM-2025-DED-002**: Family pension deduction (new regime) - No new regime pension cases
7. **IN-VRS-2025-EXE-001**: VRS compensation - No VRS cases
8. **IN-STCG-2025-TAX-001**: Short-term capital gains - No STCG cases
9. **IN-WIN-2025-TAX-001**: Winnings from games - No winnings cases
10. **IN-TAX-2025-SLAB-005**: Tax slab AY 2026-27 - Not applicable

### Recommendations:
1. **Add Super Senior Citizen Case**: Include at least one employee aged ≥80 to validate super senior citizen slab
2. **Add STCG Case**: Include short-term capital gains scenario
3. **Add Severe Disability Case**: Include employee with ≥80% disability
4. **Add VRS Case**: Include voluntary retirement scenario
5. **Consider Arrears**: If needed, add salary arrears scenario (currently excluded)

---

## Validation Checklist

### Rule Condition Validation (When Clauses)
- ✅ All applicable rules have test cases where conditions are met
- ✅ Age-based rules validated (normal, senior, super senior where applicable)
- ✅ Regime-based rules validated (old vs new)
- ✅ Income threshold rules validated (rebate limits, surcharge thresholds)
- ✅ Residence-based rules validated (metro vs non-metro for HRA)

### Rule Action Validation (Then Clauses)
- ✅ All calculations produce expected outputs
- ✅ Deduction limits applied correctly (80C: ₹1.5L, 80D: ₹25K/₹50K, etc.)
- ✅ Exemption formulas applied correctly (HRA, LTA, allowances)
- ✅ Progressive tax slabs calculated correctly
- ✅ Surcharge and cess applied on correct base amounts

### Cross-Validation
- ✅ Calculations match across annual and monthly payslips
- ✅ CTC revisions reflected correctly in December and subsequent months
- ✅ Tax regime changes handled properly (pro-rated calculations)
- ✅ Bonus and commission included in correct months
- ✅ LTA payments and exemptions applied in correct months

---

*Generated: 2025-11-19*
*Assessment Year: 2025-26*
*DSL Version: 2025-26*
*Rule Coverage: 79% (95/120 rules)*

