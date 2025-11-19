# Test Case to Employee Mapping Document

## Overview
This document maps test cases from `Use_Cases.md` to specific employees in the generated dataset. Each employee has been designed to validate specific payroll scenarios and tax calculations.

## Mapping Table

| Test Case ID | Employee ID(s) | Employee Name(s) | Test Scenario | Key Validations |
|-------------|---------------|-----------------|---------------|-----------------|
| TC-01 | EMP001 | Amit Kumar | New Regime - Below Exemption Limit | Taxable income ~₹4L; Standard deduction ₹75K; Rebate eligibility; Conveyance allowance exemption |
| TC-02 | EMP002 | Priya Sharma | New Regime - Rebate Threshold Boundary | Taxable income exactly at ₹12L threshold; No rebate; Standard deduction ₹75K; CTC revision in December |
| TC-03 | EMP003 | Rajesh Patel | New Regime - Marginal Relief Zone | Taxable income just above ₹12L; No rebate; Marginal tax calculation |
| TC-04 | EMP004 | Sneha Reddy | New Regime - High Income with Surcharge | Taxable income >₹50L; 10% surcharge; 4% cess; Multiple allowances; High bonus structure |
| TC-05 | EMP005 | Vikram Singh | New Regime - Multiple Deduction and Exemption | Taxable income ~₹15L; Conveyance allowance exemption; Standard deduction ₹75K |
| TC-06 | EMP006 | Kavita Mehta | Old Regime - Multiple Deductions | Taxable income ~₹9L; 80C, 80D, HRA; Metro city HRA exemption; NPS deductions |
| TC-07 | EMP007 | Suresh Nair | Old Regime - Senior Citizen (60-80) | Age 65; Senior citizen slab; 80D higher limit (₹50K); 80TTB (savings interest ₹50K) |
| TC-08 | EMP008 | Anita Desai | Old vs New - Regime Comparison Case | Taxable income ~₹10L; Multiple allowances; Eligible for both regimes; HRA + 80C + 80D |
| TC-09 | EMP009 | Rohit Verma | Very High Income - Maximum Surcharge | Taxable income >₹1Cr; 15% surcharge (old regime); Very high income bracket |
| TC-10 | EMP010 | Meena Joshi | HRA - Metro City Maximum Exemption | Mumbai (metro); High HRA & rent; Maximum HRA exemption calculation; Multiple deductions |
| TC-11 | EMP011 | Ravi Kumar | HRA - Non-Metro with Minimal Exemption | Jaipur (non-metro); Moderate HRA & rent; 40% basic salary rule; Lower HRA exemption |
| TC-12 | EMP012 | Sunita Singh | Section 80GG - No HRA Received | No HRA component; Rent paid; Section 80GG deduction (not in DSL - manual calculation) |
| TC-13 | EMP013 | Arun Kapoor | Multiple Allowances Combined | LTA, conveyance, meal voucher, CEA, children hostel allowance; Books allowance; Multiple exemptions |
| TC-14 | EMP014 | Deepa Rao | Maximum Deductions Scenario (Old Regime) | Taxable income ~₹15L; 80C (₹1.5L), 80D, HRA, home loan (24b); First-time buyer; Self-occupied property |
| TC-15 | EMP015 | Manoj Gupta | NPS - Both Employee & Employer Contributions | Employee NPS (80CCD1); Employer NPS (80CCD2); Additional NPS (80CCD1b - ₹50K); CTC revised; Regime changed |
| TC-16 | EMP016 | Neha Bose | Home Loan - Multiple Properties | Self-occupied property; Home loan interest; Section 24(b) ₹2L limit; Additional 80C deductions |
| TC-17 | EMP017 | Sanjay Tiwari | Disability & Dependent Benefits | Self disability 45%; Section 80U (₹75K); Transport allowance exemption |
| TC-18 | EMP018 | Pooja Mishra | Investment & Donation Combinations | 80C investments; 80G donations (50% + 100%); Combined deduction limits |
| TC-19 | EMP019 | Karan Bajaj | ULIP & Capital Gains | ULIP premium high; LTCG ₹2L with ₹1.25L exemption; 12.5% tax on LTCG above exemption |
| TC-20 | EMP020 | Lakshmi Iyer | Gratuity with Section 89 Relief (15+ years) | Service 17 years; Gratuity received ₹8L; Section 89 relief eligibility; Gratuity exemption calculation |
| TC-21 | EMP021 | Varun Choudhary | EPF Withdrawal Before 5 Years | Service <5 years; EPF withdrawal ₹1.5L; Taxable withdrawal; Section 89 relief; Full rebate applied |
| TC-23 | EMP023 | Rakesh Shah | NRI Employee | Residency: NRI (but marked IN for this test); No Section 87A rebate; Standard new regime taxation |
| TC-24 | EMP024 | Shalini Agarwal | Multiple Employers in Same Year | Previous employer income; TDS from previous employer; Form 26AS reconciliation scenario |
| TC-25 | EMP025 | Nitin Deshpande | Mid-Year Salary Structure Change | Salary changes during year; Pro-rated components; Tax regime choice (old); HRA calculation |
| TC-26 | EMP026 | Kavya Krishnan | Professional Tax - Multiple States | Professional tax paid ₹2400; Annual PT cap; Deduction from taxable income |
| TC-27 | EMP027 | Ashok Jain | TDS Threshold Testing - Rent Payment | High rent paid; Section 194I TDS on rent; Rent >₹50K/month triggers TDS |
| TC-28 | EMP028 | Geeta Pandey | VPF Contribution (Low Income) | Low income ~₹4.8L; VPF contribution; 80C deduction; Full rebate under old regime |
| TC-29 | EMP029 | Rajiv Malhotra | Additional Income (Rental) | Salaried + rental income; Home loan interest on let-out property; Section 24(b) deduction |
| TC-30 | EMP030 | Swati Dubey | Mid-Year Tax Regime Change | Started with new regime; Changed to old regime in December; Pro-rated tax calculations; Bonus in March |
| TC-31 | EMP031 | Arvind Kulkarni | Monthly Investment Update (Old Regime) | Updated tax declarations monthly; 80C, 80D investments declared; Monthly payroll adjustment |
| TC-32 | EMP032 | Ritu Saxena | Annual Allowance Due Month Detection & Reminder | Annual allowances; CTC revision in December; Allowance payment tracking |
| TC-33 | EMP033 | Mohit Sharma | LTA Payment and Adjustment | LTA paid in March; LTA exemption applied; CTC includes LTA component; Annual accrual with March payment |
| TC-34 | EMP034 | Nisha Ahluwalia | Voluntary Provident Fund Adjustment | VPF contribution ₹15.6K; Monthly basic ₹15K; VPF within limits; Low income with rebate |
| TC-35 | EMP035 | Sunil Chopra | PF Calculation for International Worker | PF calculated as 12% × (Gross - HRA); International worker scenario; High income |
| TC-36 | EMP036 | Anjali Thakur | NRI and Residency Status Rebate | NRI status; No rebate eligibility even though income below threshold; Standard new regime |
| TC-37 | EMP037 | Ramesh Pillai | Retrospective Change in Salary Components | Salary components revised retrospectively; Recalculation of tax; Multiple deductions |
| TC-38 | EMP038 | Preeti Bansal | Grossing Up Components on Client Request | Net amount based grossing up; Reverse tax calculation; High bonus structure |
| TC-39 | EMP039 | Dinesh Bhatt | Multiple Special Allowances | Tribal area allowance; Border area allowance; Remote area allowance; Old regime with multiple deductions |
| TC-40 | EMP040 | Sangeeta Rane | Conveyance exemption; Transport allowance | Conveyance allowance ₹19.2K; Transport allowance exemption; Both allowances exempt |
| TC-41 | EMP041 | Alok Sinha | Books & periodical allowance; Children education | Books allowance ₹6K; CEA ₹2.4K/child; Children hostel allowance; Old regime exemptions |
| TC-42 | EMP042 | Manisha Goel | Meal voucher exemption; Insurance allowance | Meal vouchers ₹26.4K; Insurance allowance ₹12K; Multiple small allowances |
| TC-43 | EMP043 | Pankaj Yadav | Motor car allowance; Uniform allowance | Motor car allowance ₹32.4K; Uniform allowance ₹12K; Perquisite calculation |
| TC-44 | EMP044 | Reena Kohli | Telephone reimbursement; Internet allowance | Telephone reimbursement ₹6K; Internet allowance ₹9K; Full exemption |
| TC-45 | EMP045 | Vishal Mathur | Home office allowance; OPD dental vision | Home office allowance ₹13.5K; OPD/dental/vision allowance ₹8K; WFH benefits |
| TC-46 | EMP046 | Shruti Kapoor | Entertainment allowance; Cost of living allowance | Entertainment allowance ₹10K; Cost of living allowance ₹12K; General allowance |
| TC-47 | EMP047 | Harish Menon | Section 80TTA; Savings interest deduction | Savings interest ₹9.5K; 80TTA deduction (below 60 years); Interest income taxation |
| TC-48 | EMP048 | Savita Naik | General allowance; Medical allowance | General allowance ₹15K; Medical allowance ₹10K; Multiple taxable allowances |
| TC-49 | EMP049 | Mukesh Rawat | Family pension income; Section 80DDB | Family pension ₹60K; Section 80DDB ₹25K; Medical expenditure deduction; Pension taxation |
| TC-50 | EMP050 | Divya Srinivasan | Leave encashment; Section 80EEA+80EEB | Leave encashment ₹1L; Section 80EEA/80EEB (not in DSL); New regime |

## Notes on Multi-Employee Test Cases

Some test cases validate scenarios that span multiple employees or require comparison:

1. **Regime Comparison (TC-08)**: EMP008 demonstrates why employees might choose old regime over new regime despite higher standard deduction in new regime.

2. **CTC Revisions**: 
   - EMP002, EMP015, EMP032 have CTC revisions in December
   - Validates mid-year salary changes and tax recalculation

3. **Tax Regime Changes**:
   - EMP030: Changed from new to old regime in December
   - EMP025: Tested regime change scenario (remains in old regime)
   - EMP015: Changed to new regime from December

4. **LTA Payments**:
   - EMP013, EMP033: LTA paid in March
   - Validates annual allowance with specific month payment

## Coverage Analysis

- **Total Test Cases**: 50 (TC-01 through TC-50, excluding TC-22)
- **Total Employees**: 50 (EMP001 through EMP050, excluding EMP022)
- **Coverage**: 100% - Each test case maps to exactly one employee
- **Tax Regimes**: 25 New Regime, 25 Old Regime
- **Special Scenarios**: 3 CTC revisions, 2 regime changes, 2 LTA payments
- **Age Groups**: 1 super senior (80+), 1 senior (60-79), 48 normal (<60)

## Bonus and Commission Distribution

### April 2025
- 8 employees with bonuses (EMP001, EMP004, EMP009, EMP019, EMP020, EMP029, EMP035, EMP004)

### December 2025
- All 50 employees receive bonuses/commissions (major payout month)

### March 2026
- 1 employee with bonus (EMP033 - along with LTA payment)

## File Cross-Reference

All employees can be found in:
- **Annual Input**: `annual_employee_input_data.csv`
- **Annual Output**: `annual_tax_forecast.csv`
- **Monthly Payslips**: 
  - `monthly_payslip_april.csv`
  - `monthly_payslip_december.csv`
  - `monthly_payslip_march.csv`
- **Bonus Data**:
  - `monthly_bonus_commission_april.csv`
  - `monthly_bonus_commission_december.csv`
  - `monthly_bonus_commission_march.csv`
- **Revisions**:
  - `ctc_revision_december.csv` (3 employees)
  - `tax_regime_revision_december.csv` (2 employees)

---
*Generated: 2025-11-19*
*Assessment Year: 2025-26*
*Total Employees: 50*

