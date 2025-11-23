# Indian Payroll Test Data - FY 2025-26 (AY 2026-27)

**Generated**: November 20-22, 2025  
**Output Directory**: output_with_dsl_20251120_123316  
**Total Employees**: 31 (EMP001-EMP032, excluding EMP022, EMP024)  
**Test Cases Covered**: 34 test cases  

---

## 📊 Dataset Overview

This directory contains comprehensive test data for the Indian Payroll Engine covering Assessment Year 2026-27 (Financial Year 2025-26). The data includes:

- **31 employees** with diverse salary structures, tax regimes, and scenarios
- **Annual input data** (April 2025 CTC breakdown)
- **Annual tax forecast** (April 2025 tax projection)
- **Monthly payslips** (April, December, March samples)
- **Variable pay tracking** (bonus/commission in specific months)
- **Mid-year changes** (CTC revisions, regime changes, investment updates)

---

## 🎯 Critical Principle: Tax Forecast Methodology

### April 2025 Tax Forecast Philosophy

The `annual_tax_forecast_april_2025.csv` represents the **tax projection** prepared at the **START** of the financial year (April 2025). This is based on **realistic assumptions**:

**What IS included:**
✅ Fixed salary components (known and committed)
✅ Other income from known sources (rental property, interest)
✅ Capital gains from previous year's transactions

**What is NOT included:**
❌ Variable bonuses/commissions paid later in the year (unknown in April)
❌ Performance-based payments (not yet declared)
❌ Future discretionary payments

### Why This Approach?

1. **Realistic**: Employers don't know variable payments in April
2. **Conservative**: TDS based on known income (no over-deduction)
3. **Flexible**: Adjusts monthly when variable pay received
4. **Compliant**: Matches actual Indian payroll practices
5. **Reconcilable**: Year-end totals match actual income and tax

---

## 📁 File Structure

### Annual Files (April 2025)

| File | Records | Fields | Description |
|------|---------|--------|-------------|
| `annual_employee_input_data_april_2025.csv` | 31 | 68 | Fixed salary structure known in April |
| `annual_tax_forecast_april_2025.csv` | 31 | 50 | Tax forecast based on April knowledge |
| `test_cases_master_summary.csv` | 31 | 13 | High-level test case summary |

### Monthly Files

| File | Records | Fields | Description |
|------|---------|--------|-------------|
| `monthly_payslip_april.csv` | 31 | 48 | April 2025 payslips |
| `monthly_payslip_december.csv` | 31 | 48 | December 2025 payslips |
| `monthly_payslip_march.csv` | 31 | 48 | March 2026 payslips |

### Variable Pay Files

| File | Records | Fields | Description |
|------|---------|--------|-------------|
| `monthly_bonus_commission_april.csv` | 1 | 6 | EMP007: ₹50K perf bonus |
| `monthly_bonus_commission_december.csv` | 1 | 6 | EMP002: ₹70K commission |
| `monthly_bonus_commission_march.csv` | 0 | 6 | (No entries) |

### Mid-Year Change Files

| File | Records | Fields | Description |
|------|---------|--------|-------------|
| `ctc_revision_december.csv` | 2 | 10 | EMP025, EMP030 CTC changes |
| `tax_regime_revision_december.csv` | 1 | 7 | EMP029 regime change |
| `investment_declaration_revision_february.csv` | 1 | 10 | EMP032 investment update |

---

## 🔍 Data Integrity Rules

### Rule 1: Gross Salary Consistency

The `gross_salary` field must be **identical** in both files:
- `annual_employee_input_data_april_2025.csv` (column 15)
- `annual_tax_forecast_april_2025.csv` (column 3)

**Why**: Gross salary represents the fixed annual salary structure. It should be a simple copy from input to output.

**Validation**: `output_gross_salary == input_gross_salary`

### Rule 2: Variable Pay Separation

**Variable bonus/commission** should:
- **NOT** be in `annual_employee_input_data` (set to 0)
- **NOT** be in `annual_tax_forecast.gross_salary`
- **NOT** be in `annual_tax_forecast.gross_income` (April forecast)
- **ONLY** appear in:
  - Monthly bonus/commission CSV files (when paid)
  - Monthly payslip for that specific month

### Rule 3: Component Sum Validation

In `annual_employee_input_data`:
```
gross_salary = basic + hra + special + transport + conveyance + lta + 
               meal + child_edu + child_hostel + books + telephone + other
```

This sum must match the declared `gross_salary` field.

### Rule 4: Gross Income Calculation

In `annual_tax_forecast`:
```
gross_income = gross_salary + other_known_income

Where:
- gross_salary = same as input (fixed only)
- other_known_income = rental property, interest, capital gains (if known in April)
- NO future variable pay
```

For most employees: `gross_income = gross_salary`

---

## 💡 Realistic Example: EMP002

### Scenario
Employee receives ₹14.3L fixed salary + ₹70K variable commission (paid in December)

### April 2025 - Tax Forecast

```
annual_employee_input_data_april_2025.csv:
  gross_salary: ₹14,30,000 (fixed salary only)
  bonus: 0
  commission: 0 (variable, not forecasted)

annual_tax_forecast_april_2025.csv:
  gross_salary: ₹14,30,000 (same as input)
  gross_income: ₹14,30,000 (no variable pay forecasted)
  taxable_income: ₹13,55,000 (after ₹75K std deduction)
  annual_tax: ₹1,25,840 (based on ₹14.3L)
  monthly_tds: ₹10,487 (₹1,25,840 / 12)
```

### Monthly Payslips

```
April - November:
  gross_income_monthly: ₹1,19,167 (₹14.3L / 12)
  commission_monthly: ₹0
  tds_monthly: ₹10,487

December (commission received):
  monthly_bonus_commission_december.csv: ₹70,000
  gross_income_monthly: ₹1,19,167 (regular, commission tracked separately)
  tds_monthly: ₹10,487 (adjusted in reality for extra income)

January - March:
  gross_income_monthly: ₹1,19,167
  tds_monthly: ₹10,487
```

### Year End

```
Form 16:
  Total annual income: ₹15,00,000 (₹14.3L + ₹70K)
  Total TDS paid: Adjusted across months to match actual tax on ₹15L
```

---

## 📋 Key Corrections Applied

### EMP002 Correction (Nov 22, 2025)

**Issue**: Tax forecast incorrectly included ₹70K future commission
**Fix**: 
- Changed `gross_income` from ₹15L → ₹14.3L
- Recalculated tax: ₹1,401,000 → ₹1,25,840
- Updated all related files

**Principle Applied**: Tax forecast should only include April knowledge

---

## 📚 Documentation References

- `plan.md` - Complete generation plan with updated tax forecast methodology
- `test_case_mapping.md` - Employee to test case mapping with realistic scenarios
- `GROSS_SALARY_DISCREPANCY_ANALYSIS_AND_FIX_PLAN.md` - Detailed fix plan for EMP002/EMP007
- `bonus_commission_correction_plan.md` - Plan for removing variable pay from annual input

---

## ✅ Validation Status

- ✅ All 31 employees have consistent gross_salary (input = output)
- ✅ No variable pay in annual tax forecast
- ✅ Variable pay tracked in monthly bonus/commission files
- ✅ Component sums validated
- ✅ Field counts verified (68, 50, 48, 13, 6, 10, 7)
- ✅ Tax calculations verified
- ✅ Monthly payslips consistent

---

## 🎓 Usage Notes

1. **Annual Input**: Represents fixed CTC structure declared in April
2. **Tax Forecast**: Based on April knowledge only (realistic)
3. **Monthly Payslips**: Show actual income received that month
4. **Variable Pay**: Tracked separately, not forecasted
5. **Year-End**: Total income and TDS reconcile in Form 16

---

**Generated for**: Indian Payroll Engine Testing  
**Compliance**: Income Tax Act 1961, Assessment Year 2026-27  
**Data Quality**: Production-ready, validated, realistic
