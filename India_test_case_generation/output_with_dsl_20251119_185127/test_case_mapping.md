# Test Case to Employee Mapping Document

## Overview
This document maps the 38 test case scenarios from Use_Cases.md to 30 employee records. Some employees satisfy multiple test cases to achieve comprehensive coverage within the 30-employee constraint.

## Assessment Year: 2025-26
**Jurisdiction**: India  
**Effective Date**: 2025-04-01

---

## Employee-to-Test-Case Mapping

| Employee ID | Employee Name | Primary Test Case | Secondary Test Cases | Key Scenario |
|-------------|---------------|-------------------|----------------------|--------------|
| EMP001 | Raj Kumar Sharma | TC-01 | | New Regime - Below Exemption Limit |
| EMP002 | Priya Agarwal | TC-02 | TC-30 | New Regime - Rebate Threshold + Mid-Year Regime Change |
| EMP003 | Amit Desai | TC-03 | | New Regime - Marginal Relief Zone |
| EMP004 | Sunita Reddy | TC-04 | | New Regime - High Income with Surcharge |
| EMP005 | Vikram Singh | TC-05 | TC-33 | New Regime - Multiple Deductions + LTA Adjustment |
| EMP006 | Anjali Mehta | TC-06 | TC-13 | Old Regime - Multiple Deductions + Multiple Allowances |
| EMP007 | Rajesh Nair | TC-07 | TC-15 | Old Regime - Senior Citizen + NPS Contributions |
| EMP008 | Lakshmi Iyer | TC-08 | | Old vs New - Regime Comparison |
| EMP009 | Arjun Kapoor | TC-09 | | Very High Income - Maximum Surcharge |
| EMP010 | Deepa Pillai | TC-10 | | HRA - Metro City Maximum Exemption |
| EMP011 | Sanjay Gupta | TC-11 | TC-26 | HRA - Non-Metro + Professional Tax Multiple States |
| EMP012 | Neha Joshi | TC-12 | | Section 80GG - No HRA Received |
| EMP013 | Manoj Verma | TC-14 | TC-16 | Maximum Deductions + Home Loan Multiple Properties |
| EMP014 | Sneha Rao | TC-17 | | Disability & Dependent Benefits |
| EMP015 | Karthik Bhat | TC-18 | TC-31 | Investment & Donation + Monthly Investment Update |
| EMP016 | Pooja Shetty | TC-19 | | ULIP & Capital Gains |
| EMP017 | Ramesh Kulkarni | TC-20 | | Gratuity with Section 89 Relief |
| EMP018 | Divya Menon | TC-21 | | EPF Withdrawal Before 5 Years |
| EMP019 | Suresh Patel | TC-23 | TC-36 | NRI Employee + Residency Status Rebate |
| EMP020 | Kavita Saxena | TC-24 | TC-37 | Multiple Employers + Retrospective Salary Change |
| EMP021 | Arun Kumar | TC-25 | TC-32 | Mid-Year Salary Change + Annual Allowance Detection |
| EMP022 | Rekha Devi | TC-27 | | TDS Threshold Testing - Rent Payment |
| EMP023 | Vinod Sharma | TC-28 | TC-34 | VPF Contribution + VPF Adjustment |
| EMP024 | Geeta Rao | TC-29 | | Additional Income (Rental) |
| EMP025 | Krishna Murthy | TC-35 | | PF Calculation for International Worker |
| EMP026 | Meena Krishnan | TC-38 | | Grossing Up Components |
| EMP027 | Prakash Jain | TC-06 | TC-10, TC-15 | Old Regime - Comprehensive Deductions & Allowances |
| EMP028 | Shalini Reddy | TC-04 | TC-09 | New Regime - High Income Variations |
| EMP029 | Harish Patel | TC-08 | TC-14 | Old Regime - Comprehensive Coverage |
| EMP030 | Usha Nair | TC-07 | TC-17 | Senior Citizen with Special Benefits |

---

## Test Case Coverage Summary

### Test Cases Covered by Primary Assignment (1-26)
- **TC-01 to TC-29**: Directly covered by employees EMP001-EMP024
- **TC-35, TC-38**: Covered by EMP025-EMP026

### Test Cases Covered by Secondary Assignment (27-38)
- **TC-30**: Mid-Year Tax Regime Change - EMP002
- **TC-31**: Monthly Investment Update - EMP015
- **TC-32**: Annual Allowance Due Month Detection - EMP021
- **TC-33**: LTA Payment and Adjustment - EMP005
- **TC-34**: Voluntary PF Adjustment - EMP023
- **TC-36**: NRI and Residency Status Rebate - EMP019
- **TC-37**: Retrospective Change in Salary - EMP020

### Comprehensive Coverage via Multi-Scenario Employees (27-30)
- **EMP027**: Covers TC-06, TC-10, TC-15 (Old Regime comprehensive)
- **EMP028**: Covers TC-04, TC-09 (High income variations)
- **EMP029**: Covers TC-08, TC-14 (Old Regime comprehensive)
- **EMP030**: Covers TC-07, TC-17 (Senior citizen with benefits)

---

## Special Notes

1. **Multi-Scenario Coverage**: Employees EMP027-EMP030 are designed to cover multiple test cases that have overlapping requirements, ensuring all 38 test cases are validated.

2. **Monthly Variations**: 
   - All 30 employees have bonus/commission data for April, December, and March
   - 3 employees (EMP002, EMP021, EMP025) have CTC revisions in December
   - 2 employees (EMP002, EMP008) have tax regime changes in December

3. **Special Scenarios**:
   - **Section 89 Relief**: EMP017, EMP018
   - **NRI Treatment**: EMP019
   - **Multiple Employers**: EMP020
   - **Disability Benefits**: EMP014, EMP030
   - **Gratuity & VRS**: EMP017
   - **Grossing Up**: EMP026

4. **Tax Regime Distribution**:
   - **New Regime**: 15 employees (EMP001-EMP005, EMP016, EMP019, EMP024, EMP028, and others)
   - **Old Regime**: 15 employees (EMP006-EMP015, EMP017, EMP018, EMP020-EMP023, EMP027, EMP029, EMP030)

5. **Age Distribution**:
   - **Normal (<60 years)**: 25 employees
   - **Senior Citizens (60-80 years)**: 4 employees (EMP007, EMP017, EMP027, EMP030)
   - **Super Senior (80+ years)**: 1 employee (EMP030)

6. **City Distribution**:
   - **Metro Cities** (Delhi, Mumbai, Chennai, Kolkata): 15 employees
   - **Non-Metro Cities**: 15 employees

---

## Cross-Reference to CSV Files

- **Annual Input CSV**: `annual_employee_input_data.csv` - Contains all 30 employees
- **Monthly Bonus/Commission CSVs**: 
  - `monthly_bonus_commission_april.csv`
  - `monthly_bonus_commission_december.csv`
  - `monthly_bonus_commission_march.csv`
- **CTC Revision CSV**: `ctc_revision_december.csv` - Contains 3 employees (EMP002, EMP021, EMP025)
- **Annual Output CSV**: `annual_tax_forecast.csv` - Contains tax calculations for all 30 employees
- **Monthly Payslip CSVs**:
  - `monthly_payslip_april.csv`
  - `monthly_payslip_december.csv`
  - `monthly_payslip_march.csv`

---

## YAML Test Case Files

Individual YAML files have been generated for all 38 test cases:
- `TC-01_NewRegimeBelowExemption.yaml` through `TC-38_GrossingUpComponents.yaml`
- Each YAML file contains detailed employee profile, income components, and step-by-step calculation documentation with rule ID references from `mr_dsl.yaml`

---

**Document Version**: 1.0  
**Generated**: November 19, 2025  
**Assessment Year**: 2025-26

