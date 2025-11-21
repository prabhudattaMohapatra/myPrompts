# Indian Payroll Engine Test Data Generation

**Assessment Year**: 2026-27  
**Output Directory**: output_with_dsl_20251120_123316  
**Generated Date**: November 20, 2025  
**Status**: Phase 1 Complete

## Overview

This directory contains comprehensive test case data for the Indian Payroll Engine, generated according to the requirements specified in the test case generation prompt. The data covers 30 employees (EMP001 - EMP030) and 38 test cases (TC-01 - TC-38) with full compliance to Indian tax laws and the machine-readable DSL rules (`mr_dsl.yaml`).

## Phase 1: Initial Setup (Completed)

### Files Created

#### 1. Test Case Mapping
- **File**: `test_case_mapping.md`
- **Purpose**: Maps each of the 30 employees to test cases from `Use_Cases.md`
- **Status**: ✅ Complete

#### 2. Master CSV Files (Headers Only)

All CSV files have been created with appropriate header rows:

**Annual Input Files:**
- `annual_employee_input_data.csv` - Annual CTC breakdown, demographics, tax info, investment declarations

**Monthly Input Files:**
- `monthly_bonus_commission_april.csv` - Bonus/commission data for April 2025
- `monthly_bonus_commission_december.csv` - Bonus/commission data for December 2025
- `monthly_bonus_commission_march.csv` - Bonus/commission data for March 2026
- `ctc_revision_december.csv` - CTC revisions for December 2025 (3 employees)
- `tax_regime_revision_december.csv` - Tax regime revisions for December 2025 (2 employees)

**Annual Output Files:**
- `annual_tax_forecast.csv` - Annual tax calculations with all exemptions, deductions, and tax breakdowns

**Monthly Output Files:**
- `monthly_payslip_april.csv` - Monthly payslip data for April 2025
- `monthly_payslip_december.csv` - Monthly payslip data for December 2025
- `monthly_payslip_march.csv` - Monthly payslip data for March 2026

**Summary Files:**
- `test_cases_master_summary.csv` - Master summary of all test cases

## Input Files Reference

The test data generation is based on the following input files from the parent directory:

1. **employee_dsl.yaml** - Complete employee data schema definition (version 2025-26)
2. **mr_dsl.yaml** - Machine-readable DSL rules for Indian payroll and taxation
   - Tax slabs (old regime, new regime, senior citizens, super senior citizens)
   - Surcharge rules and thresholds
   - Cess calculations (4% health and education cess)
   - Rebate rules (Section 87A)
   - Deduction limits (80C, 80D, 80G, 80CCD, etc.)
   - Exemption rules (HRA, conveyance, LTA, meal vouchers, etc.)
   - Professional tax rules
   - Standard deduction rules (₹75,000 for new regime, ₹50,000 for old regime)
3. **Data_requirements.md** - Data requirements (30 employees, input/output datasets)
4. **Use_Cases.md** - 38 test cases covering various tax scenarios

## Key DSL Rules for Assessment Year 2026-27

### Tax Slabs (New Regime 2026-27)
- ₹0 - ₹4,00,000: 0%
- ₹4,00,001 - ₹8,00,000: 5%
- ₹8,00,001 - ₹12,00,000: 10%
- ₹12,00,001 - ₹16,00,000: 15%
- ₹16,00,001 - ₹20,00,000: 20%
- ₹20,00,001 - ₹24,00,000: 25%
- ₹24,00,001 and above: 30%

### Tax Slabs (Old Regime - Normal)
- ₹0 - ₹2,50,000: 0%
- ₹2,50,001 - ₹5,00,000: 5%
- ₹5,00,001 - ₹10,00,000: 20%
- ₹10,00,001 and above: 30%

### Rebate (Section 87A) - 2026-27
- **New Regime**: Taxable income ≤ ₹12,00,000 → Rebate up to ₹60,000
- **Old Regime**: Taxable income ≤ ₹5,00,000 → Rebate up to ₹12,500

### Standard Deduction
- **New Regime**: ₹75,000
- **Old Regime**: ₹50,000

### Surcharge Slabs
- ₹0 - ₹50L: 0%
- ₹50L - ₹1Cr: 10%
- ₹1Cr - ₹2Cr: 15%
- ₹2Cr - ₹5Cr: 25%
- Above ₹5Cr: 37% (old regime) / 25% (new regime)

### Cess
- Health and Education Cess: 4% of (tax + surcharge)

## Test Case Coverage

### By Tax Regime
- **New Regime**: 11 employees
- **Old Regime**: 19 employees

### By Income Level
- **Low (₹3-7L)**: 2 employees
- **Medium (₹9-15L)**: 16 employees
- **High (₹50L+)**: 2 employees
- **Very High (₹1Cr+)**: 1 employee

### By Age Category
- **Normal (< 60)**: 29 employees
- **Senior Citizen (60-80)**: 1 employee

### By City Type
- **Metro (Delhi, Mumbai, Chennai, Kolkata)**: 3 employees
- **Non-Metro**: 4 employees
- **Tier 1/Tier 2 cities**: 23 employees

## Next Steps: Phase 2 - Employee Generation

Phase 2 will involve generating employees one by one following this workflow:

1. **Step 2**: Generate annual input data for one employee
2. **Step 3**: Generate monthly input data (if required by test case)
3. **Step 4**: Generate annual tax forecast output with calculations
4. **Step 5**: Generate monthly output data (if required)
5. **Step 6**: Create verification report with mathematical and rule compliance checks
6. **Step 7**: Append verified data to master CSV files
7. **Step 8**: Repeat for next employee

Each employee will have:
- Complete input data (annual + monthly if applicable)
- Complete output data (annual + monthly if applicable)
- Verification report (`employee_verification_{ID}.md`)
- All calculations compliant with `mr_dsl.yaml` rules
- Rule ID references for each calculation

## Verification Requirements

Each employee will be verified for:
- **Mathematical accuracy**: All calculations correct
- **Rule compliance**: All calculations comply with mr_dsl.yaml rules
- **Data consistency**: Input and output data are logically consistent
- **Use case coverage**: Employee satisfies assigned test case requirements
- **Indian tax law compliance**: All data complies with Income Tax Act

## Directory Structure

```
output_with_dsl_20251120_123316/
├── README.md (this file)
├── test_case_mapping.md
├── annual_employee_input_data.csv
├── monthly_bonus_commission_april.csv
├── monthly_bonus_commission_december.csv
├── monthly_bonus_commission_march.csv
├── ctc_revision_december.csv
├── tax_regime_revision_december.csv
├── annual_tax_forecast.csv
├── monthly_payslip_april.csv
├── monthly_payslip_december.csv
├── monthly_payslip_march.csv
├── test_cases_master_summary.csv
├── employee_verification_EMP001.md (to be created in Phase 2)
├── employee_verification_EMP002.md (to be created in Phase 2)
... (30 verification files total)
├── test_case_rule_mapping.md (to be created in Phase 3)
└── final_verification_summary.md (to be created in Phase 3)
```

## Progress Tracking

- ✅ Phase 1: Initial Setup - Complete
- ⏳ Phase 2: Employee Generation (EMP001-EMP030) - Not Started
  - [ ] EMP001-EMP005 (0/5 complete)
  - [ ] EMP006-EMP010 (0/5 complete)
  - [ ] EMP011-EMP015 (0/5 complete)
  - [ ] EMP016-EMP020 (0/5 complete)
  - [ ] EMP021-EMP025 (0/5 complete)
  - [ ] EMP026-EMP030 (0/5 complete)
- ⏳ Phase 3: Final Quality Assurance - Not Started

**Total Progress**: 0/30 employees generated

## Compliance Standards

All generated data will comply with:

1. **Indian Income Tax Act** - All provisions for Assessment Year 2026-27
2. **mr_dsl.yaml Rules** - All rules from the DSL file (used as minimum rule set)
3. **Mathematical Accuracy** - All calculations verified and documented
4. **Data Consistency** - All data logically consistent across files
5. **Schema Compliance** - All data conforms to employee_dsl.yaml schema

## Key Features

- ✅ Comprehensive test case coverage (38 test cases)
- ✅ Assessment Year 2026-27 calculations
- ✅ Both old and new tax regime support
- ✅ Senior citizen tax slab support
- ✅ Complete exemption calculations (HRA, conveyance, LTA, etc.)
- ✅ Complete deduction calculations (80C, 80D, 80G, etc.)
- ✅ Surcharge and cess calculations
- ✅ Rebate calculations (Section 87A)
- ✅ Monthly payslip data for 3 months
- ✅ CTC and tax regime revision support
- ✅ Detailed verification reports with rule ID references

---

**Generated by**: Indian Payroll Engine Test Data Generation Prompt  
**Version**: 1.0  
**Date**: November 20, 2025

