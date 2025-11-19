# Test Case Mapping Document

## Indian Payroll Engine Test Cases - Assessment Year 2025-26

**Generated:** November 19, 2025  
**Total Employees:** 15  
**Total Test Cases Covered:** 15

---

## Test Case to Employee Mapping

### TC-01: New Regime - Below Exemption Limit
- **Employee ID:** EMP001 (Priya Sharma)
- **Age:** 32
- **Tax Regime:** New
- **Gross Income:** ₹6,50,000
- **Taxable Income:** ₹5,72,500
- **Key Features:**
  - Income below ₹7L threshold
  - Standard deduction of ₹75,000 applied
  - Conveyance and telephone exemptions
  - No rebate eligibility as income > ₹7L threshold but tax applicable
- **Test Objective:** Validate basic new regime calculation for middle-income employee

---

### TC-02: New Regime - Rebate Threshold Boundary
- **Employee ID:** EMP002 (Rahul Verma)
- **Age:** 29
- **Tax Regime:** New
- **Gross Income:** ₹14,90,000
- **Taxable Income:** ₹14,12,500 (before deductions) → ₹12,00,000 (after rent adjustment)
- **Key Features:**
  - Taxable income exactly at ₹12L rebate threshold for AY 2025-26 (new regime)
  - Base tax: ₹60,000
  - Rebate u/s 87A: ₹25,000 (maximum for new regime 2025-26)
  - Final tax after rebate: ₹35,000
  - Standard deduction ₹75,000
- **Test Objective:** Validate rebate calculation at exact threshold boundary

---

### TC-03: New Regime - Marginal Relief Zone
- **Employee ID:** EMP003 (Anjali Nair)
- **Age:** 35
- **Tax Regime:** New
- **Gross Income:** ₹15,50,000
- **Taxable Income:** ₹13,00,000
- **Key Features:**
  - Income just above ₹12L rebate threshold
  - No rebate eligibility (exceeds threshold)
  - Tax slab progression through multiple brackets
  - Two children with allowances
- **Test Objective:** Validate tax calculation immediately above rebate threshold

---

### TC-04: New Regime - High Income with Surcharge
- **Employee ID:** EMP004 (Vikram Patel)
- **Age:** 42
- **Tax Regime:** New
- **Gross Income:** ₹65,00,000
- **Taxable Income:** ₹61,50,000
- **Key Features:**
  - Income exceeds ₹50L (surcharge threshold)
  - Base tax: ₹15,90,000
  - Surcharge: ₹1,59,000 (10% of base tax as income between ₹50L-₹1Cr)
  - Health & Education Cess: 4% on (base tax + surcharge)
  - Final tax: ₹18,22,106
- **Test Objective:** Validate surcharge and high-income tax calculations

---

### TC-05: New Regime - Multiple Deduction and Exemption
- **Employee ID:** EMP005 (Sneha Reddy)
- **Age:** 31
- **Tax Regime:** New
- **Gross Income:** ₹17,50,000
- **Taxable Income:** ₹15,00,000
- **Key Features:**
  - Conveyance allowance exemption
  - Standard deduction ₹75,000
  - Professional tax deduction
  - Multiple allowances including telephone reimbursement
- **Test Objective:** Validate multiple exemptions in new regime

---

### TC-06: Old Regime - Multiple Deductions
- **Employee ID:** EMP006 (Amit Kumar)
- **Age:** 38
- **Tax Regime:** Old
- **Gross Income:** ₹11,50,000
- **Taxable Income:** ₹9,00,000 (after exemptions and deductions)
- **Key Features:**
  - HRA exemption (metro): ₹83,200
  - Section 80C: ₹1,50,000
  - Section 80D: ₹55,000 (self ₹25,000 + parents ₹30,000)
  - Section 80G: ₹25,000 (charitable donations)
  - Section 80TTA: ₹5,000 (savings interest)
  - Standard deduction: ₹50,000
  - Rebate u/s 87A: ₹12,500 (taxable income ₹9L < ₹5L threshold, but taxable income is not <= ₹5L, so partial rebate)
- **Test Objective:** Validate comprehensive old regime deductions in metro city

---

### TC-07: Old Regime - Senior Citizen (60-80)
- **Employee ID:** EMP007 (Sunita Desai)
- **Age:** 67
- **Tax Regime:** Old
- **Gross Income:** ₹16,50,000
- **Taxable Income:** ₹13,27,500
- **Key Features:**
  - Senior citizen tax slab (basic exemption up to ₹3L)
  - Section 80D: ₹1,00,000 (self ₹50,000 senior limit + parents ₹50,000 senior limit)
  - Section 80TTB: ₹50,000 (interest income for senior citizens)
  - Section 80C: ₹1,00,000
  - Section 80G: ₹20,000
  - No HRA exemption (owns house)
- **Test Objective:** Validate senior citizen benefits and higher deduction limits

---

### TC-08: Old vs New - Regime Comparison Case
- **Employee ID:** EMP008 (Karan Singh)
- **Age:** 40
- **Tax Regime:** Old
- **Gross Income:** ₹12,00,000
- **Taxable Income:** ₹8,28,700
- **Key Features:**
  - This case can be compared with new regime to show regime selection benefits
  - HRA exemption (metro): ₹76,800
  - Section 80C: ₹1,00,000
  - Section 80CCD(1): ₹50,000 (NPS employee)
  - Section 80CCD(2): ₹60,000 (NPS employer)
  - Section 80D: ₹50,000
  - Section 80G: ₹10,000
  - Section 80TTA: ₹8,000
  - Rebate u/s 87A: ₹12,500
- **Test Objective:** Demonstrate regime comparison for optimal tax planning

---

### TC-09: Very High Income - Maximum Surcharge
- **Employee ID:** EMP009 (Meera Kapoor)
- **Age:** 45
- **Tax Regime:** Old
- **Gross Income:** ₹1,25,00,000
- **Taxable Income:** ₹1,22,07,500
- **Key Features:**
  - Income exceeds ₹1Cr (15% surcharge slab for old regime)
  - Base tax: ₹34,62,250
  - Surcharge: ₹5,19,338 (15% of base tax)
  - Health & Education Cess: 4%
  - Final tax: ₹40,66,400
  - Section 80C, 80D, 80G deductions applied
  - No HRA exemption (owns house)
- **Test Objective:** Validate 15% surcharge calculation for ₹1Cr-₹2Cr income bracket

---

### TC-10: HRA - Metro City Maximum Exemption
- **Employee ID:** EMP010 (Ravi Malhotra)
- **Age:** 36
- **Tax Regime:** Old
- **Gross Income:** ₹18,50,000
- **Taxable Income:** ₹14,81,100
- **Key Features:**
  - Metro city (Mumbai)
  - High HRA and rent payment
  - HRA exemption calculation:
    - Actual HRA received: ₹2,96,000
    - Rent paid - 10% of salary: ₹2,40,000 - ₹74,000 = ₹1,66,000
    - 50% of basic salary (metro): ₹3,70,000
    - **Minimum of above three = ₹1,18,400**
  - Section 80C: ₹1,50,000
  - Section 80CCD(1): ₹80,000 (NPS employee)
  - Section 80D: ₹50,000
  - Section 80G: ₹30,000
  - Section 80TTA: ₹6,000
- **Test Objective:** Validate maximum HRA exemption in metro city

---

### TC-11: HRA - Non-Metro with Minimal Exemption
- **Employee ID:** EMP011 (Neha Gupta)
- **Age:** 33
- **Tax Regime:** Old
- **Gross Income:** ₹9,50,000
- **Taxable Income:** ₹6,98,500
- **Key Features:**
  - Non-metro city (Jaipur)
  - HRA exemption calculation (40% rule for non-metro):
    - Actual HRA received: ₹1,52,000
    - Rent paid - 10% of salary: ₹90,000 - ₹38,000 = ₹52,000
    - 40% of basic salary (non-metro): ₹1,52,000
    - **Minimum of above three = ₹54,000**
  - Section 80C: ₹1,20,000
  - Section 80CCD(1): ₹40,000 (NPS)
  - Section 80D: ₹20,000
  - Section 80G: ₹15,000
  - Section 80TTA: ₹4,000
  - Rebate u/s 87A: ₹12,500
- **Test Objective:** Validate HRA calculation for non-metro city

---

### TC-13: Multiple Allowances Combined
- **Employee ID:** EMP013 (Sanjay Rao)
- **Age:** 39
- **Tax Regime:** Old
- **Gross Income:** ₹15,50,000
- **Taxable Income:** ₹12,40,300
- **Key Features:**
  - Leave Travel Allowance (LTA): ₹20,000
  - Children Education Allowance: ₹2,400 (₹100/month × 2 children × 12 months)
  - Children Hostel Allowance: ₹7,200 (₹300/month × 2 children × 12 months)
  - Books and Periodical Allowance: ₹1,200
  - Meal Vouchers: ₹26,400 (exemption ₹50/meal × 2 meals/day × 22 days × 12 months)
  - Conveyance Allowance: ₹19,200
  - Telephone Reimbursement: ₹4,600
  - HRA exemption (metro): ₹99,200
  - Section 80C: ₹1,20,000
  - Section 80CCD(1): ₹50,000
  - Section 80D: ₹55,000
  - Section 80G: ₹25,000
  - Section 80TTA: ₹7,000
- **Test Objective:** Validate multiple allowance exemptions and calculations

---

### TC-14: Maximum Deductions Scenario (Old Regime)
- **Employee ID:** EMP014 (Pooja Joshi)
- **Age:** 34
- **Tax Regime:** Old
- **Gross Income:** ₹18,00,000
- **Taxable Income:** ₹12,14,300
- **Key Features:**
  - Comprehensive deductions:
    - Section 80C: ₹1,50,000 (maximum limit)
    - Section 80CCD(1): ₹60,000 (NPS employee)
    - Section 80CCD(2): ₹70,000 (NPS employer)
    - Section 80CCD(1b): ₹50,000 (additional NPS)
    - Section 80D: ₹65,000 (self ₹25,000 + parents ₹40,000)
    - Section 24(b): ₹80,000 (home loan interest)
    - Section 80G: ₹50,000 (donations)
    - Section 80TTA: ₹8,000
  - HRA exemption (metro): ₹1,15,200
  - Income from house property: -₹50,000 (loss)
- **Test Objective:** Validate maximum possible deductions under old regime

---

### TC-15: NPS - Both Employee & Employer Contributions
- **Employee ID:** EMP015 (Arjun Mehta)
- **Age:** 37
- **Tax Regime:** Old
- **Gross Income:** ₹14,50,000
- **Taxable Income:** ₹10,66,500
- **Key Features:**
  - NPS comprehensive scenario:
    - Section 80CCD(1): ₹50,000 (employee contribution, part of 80C)
    - Section 80CCD(2): ₹60,000 (employer contribution, separate from 80C)
    - Section 80CCD(1b): ₹50,000 (additional employee contribution, separate from 80C)
    - **Total NPS benefit: ₹1,60,000**
  - Section 80C: ₹1,00,000 (other investments)
  - Section 80D: ₹55,000 (self + parents)
  - Section 80G: ₹20,000
  - Section 80TTA: ₹6,000
  - HRA exemption (metro): ₹92,800
- **Test Objective:** Validate NPS three-tier deduction structure

---

### TC-24: Multiple Employers in Same Year
- **Employee ID:** EMP016 (Nisha Agarwal)
- **Age:** 28
- **Tax Regime:** New
- **Gross Income:** ₹13,50,000
- **Taxable Income:** ₹12,72,500
- **Key Features:**
  - Joined current employer mid-year (August 2022)
  - Income split across multiple employers
  - TDS from both employers needs reconciliation
  - Form 26AS reconciliation required
  - Standard deduction: ₹75,000
- **Test Objective:** Validate multi-employer scenario and TDS reconciliation
- **Note:** This employee also experiences tax regime change in December 2025 (from new to old)

---

## Test Cases Not Directly Represented (For Future Enhancement)

The following test cases from Use_Cases.md were not directly implemented as separate employees but their features are partially covered:

- **TC-12:** Section 80GG (No HRA received) - Not implemented as separate employee
- **TC-16:** Home Loan - Multiple Properties - Partially covered in TC-14 (EMP014)
- **TC-17:** Disability & Dependent Benefits - Not implemented
- **TC-18:** Investment & Donation Combinations - Covered in various employees
- **TC-19:** ULIP & Capital Gains - Not implemented
- **TC-20:** Gratuity with Section 89 Relief - Not implemented
- **TC-21:** EPF Withdrawal Before 5 Years - Not implemented
- **TC-22:** (Not listed in Use_Cases.md)
- **TC-23:** NRI Employee - Not implemented
- **TC-25-39:** Various mid-year changes, retrospective adjustments, grossing up, etc. - Not implemented

---

## Mid-Year Changes Covered

### CTC Revision (December 2025)
- **EMP003** (Anjali Nair): ₹15,50,000 → ₹17,50,000 (Annual Performance Review)
- **EMP006** (Amit Kumar): ₹11,50,000 → ₹13,00,000 (Promotion)
- **EMP013** (Sanjay Rao): ₹15,50,000 → ₹17,00,000 (Market Adjustment)

### Tax Regime Changes (December 2025)
- **EMP008** (Karan Singh): Old → New (Employee opted for better tax benefit)
- **EMP016** (Nisha Agarwal): New → Old (Employee wants to claim deductions)

---

## Monthly Variations Covered

### Bonus and Commission Data
All 15 employees have varying bonus and commission patterns across three months:
- **April 2025:** 8 employees with non-zero values
- **December 2025:** 13 employees with non-zero values
- **March 2026:** 12 employees with non-zero values

This ensures comprehensive testing of variable pay components and their tax implications throughout the year.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Employees | 15 |
| New Regime Employees | 5 |
| Old Regime Employees | 10 |
| Senior Citizens (60+) | 1 |
| Metro City Employees | 11 |
| Non-Metro Employees | 4 |
| Employees with NPS | 7 |
| Employees with HRA Exemption | 8 |
| Employees with Home Loan Interest | 1 |
| Employees with Multiple Children | 7 |
| Income Range | ₹6.5L - ₹125L |
| Tax Liability Range | ₹14,300 - ₹40,66,400 |

---

**End of Test Case Mapping Document**

