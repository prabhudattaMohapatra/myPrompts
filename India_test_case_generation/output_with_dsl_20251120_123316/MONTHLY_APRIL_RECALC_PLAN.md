# Monthly Payslip April 2025 - Complete Recalculation Plan

**Date**: November 24, 2025  
**Scope**: All 31 employees (EMP001-EMP032, excluding EMP022)  
**Source**: `annual_employee_input_data_april_2025.csv`  
**Target**: `monthly_payslip_april.csv`  
**Columns**: 48 fields  
**Status**: READY TO START

---

## 🎯 Objective

Recalculate all monthly payslip fields for April 2025 based on:
1. Annual input data from `annual_employee_input_data_april_2025.csv`
2. Annual tax forecast from `annual_tax_forecast_april_2025.csv`
3. No monthly bonus/commission CSV inputs (April payslip = regular salary only)

**Key Principle**: April 2025 payslip reflects:
- Regular monthly salary components (annual amounts ÷ 12)
- Monthly TDS = Annual Tax ÷ 12
- No variable bonuses/commissions (those appear in specific months only)

---

## 📊 Column-by-Column Calculation Logic

### **Section 1: Basic Information** (Columns 0-3)

#### [0] ID
- **Source**: Direct copy from input file column [0]
- **Validation**: Must match input file exactly

#### [1] month
- **Value**: "April"
- **Fixed**: Same for all employees

#### [2] year
- **Value**: 2025
- **Fixed**: Same for all employees

#### [3] tax_regime
- **Source**: Direct copy from input file column [10]
- **Values**: 'new' or 'old'
- **Validation**: Must be lowercase

---

### **Section 2: Monthly Salary Components** (Columns 4-18)

**CRITICAL PRINCIPLE**: All monthly components = Annual component ÷ 12

#### [4] gross_salary_monthly
- **Calculation**:
  ```python
  gross_salary_monthly = annual_gross_salary / 12
  ```
- **Source**: input[14] (gross_salary) ÷ 12
- **Validation**: Must equal sum of all monthly components (columns 5-18)
- **Rounding**: Round to 2 decimal places

#### [5] basic_salary_monthly
- **Calculation**: `input[15] / 12`
- **Source**: input[15] (basic_salary) ÷ 12

#### [6] hra_received_monthly
- **Calculation**: `input[16] / 12`
- **Source**: input[16] (hra_received) ÷ 12

#### [7] special_allowance_monthly
- **Calculation**: `input[17] / 12`
- **Source**: input[17] (special_allowance) ÷ 12

#### [8] transport_allowance_monthly
- **Calculation**: `input[18] / 12`
- **Source**: input[18] (transport_allowance) ÷ 12

#### [9] conveyance_allowance_monthly
- **Calculation**: `input[19] / 12`
- **Source**: input[19] (conveyance_allowance) ÷ 12

#### [10] meal_vouchers_monthly
- **Calculation**: `input[20] / 12`
- **Source**: input[20] (meal_vouchers) ÷ 12

#### [11] lta_received_monthly
- **Calculation**: `input[21] / 12`
- **Source**: input[21] (lta_received) ÷ 12
- **Note**: LTA accrues monthly but paid annually in lump sum (typically March)
- **Special Case**: Some employees (e.g., EMP030) have LTA paid in March only
  - For these: April LTA = 0 (check monthly input CSV)
  - For regular LTA: April LTA = annual ÷ 12

#### [12] children_education_allowance_monthly
- **Calculation**: `input[22] / 12`
- **Source**: input[22] (children_education_allowance) ÷ 12

#### [13] children_hostel_allowance_monthly
- **Calculation**: `input[23] / 12`
- **Source**: input[23] (children_hostel_allowance) ÷ 12

#### [14] books_and_periodical_allowance_monthly
- **Calculation**: `input[24] / 12`
- **Source**: input[24] (books_and_periodical_allowance) ÷ 12

#### [15] telephone_reimbursement_monthly
- **Calculation**: `input[25] / 12`
- **Source**: input[25] (telephone_reimbursement) ÷ 12

#### [16] insurance_allowance_monthly
- **Calculation**: (if field exists in input)
- **Source**: Insurance allowance field ÷ 12
- **Note**: Verify column index for insurance allowance

#### [17] bonus_monthly
- **Calculation**: 
  ```python
  # For April (no monthly bonus CSV)
  if employee has FIXED bonus in annual input:
      bonus_monthly = input[27] / 12  # Fixed bonus
  else:
      bonus_monthly = 0  # Variable bonus (not in April)
  ```
- **Source**: input[27] (bonus) ÷ 12 (only if fixed)
- **Examples**:
  - EMP008: ₹50Cr fixed bonus → ₹4.17Cr monthly
  - EMP002: Variable bonus → ₹0 in April

#### [18] commission_monthly
- **Calculation**:
  ```python
  # For April (no monthly commission CSV)
  if employee has FIXED commission in annual input:
      commission_monthly = input[28] / 12  # Fixed commission
  else:
      commission_monthly = 0  # Variable commission (not in April)
  ```
- **Source**: input[28] (commission) ÷ 12 (only if fixed)

---

### **Section 3: Monthly Exemptions** (Columns 19-31)

**CRITICAL**: Monthly exemptions = Annual exemptions ÷ 12

**Source**: All exemptions from `annual_tax_forecast_april_2025.csv` ÷ 12

#### [19] hra_exemption_monthly
- **Calculation**: `forecast[5] / 12`
- **Source**: forecast[5] (hra_exemption) ÷ 12

#### [20] conveyance_allowance_exemption_monthly
- **Calculation**: `forecast[6] / 12`
- **Source**: forecast[6] (conveyance_allowance_exemption) ÷ 12

#### [21] lta_exemption_monthly
- **Calculation**: `forecast[7] / 12`
- **Source**: forecast[7] (lta_exemption) ÷ 12
- **Note**: Will be ₹0 (April forecast has LTA exemption = ₹0)

#### [22] meal_voucher_exemption_monthly
- **Calculation**: `forecast[8] / 12`
- **Source**: forecast[8] (meal_voucher_exemption) ÷ 12

#### [23] children_education_allowance_exemption_monthly
- **Calculation**: `forecast[9] / 12`
- **Source**: forecast[9] (children_education_allowance_exemption) ÷ 12

#### [24] children_hostel_allowance_exemption_monthly
- **Calculation**: `forecast[10] / 12`
- **Source**: forecast[10] (children_hostel_allowance_exemption) ÷ 12

#### [25] transport_allowance_exemption_monthly
- **Calculation**: `forecast[11] / 12`
- **Source**: forecast[11] (transport_allowance_exemption) ÷ 12

#### [26] insurance_allowance_exemption_monthly
- **Calculation**: `forecast[12] / 12`
- **Source**: forecast[12] (insurance_allowance_exemption) ÷ 12
- **Note**: Will be ₹0 (insurance fully taxable)

#### [27] books_and_periodical_exemption_monthly
- **Calculation**: `forecast[13] / 12`
- **Source**: forecast[13] (books_and_periodical_exemption) ÷ 12

#### [28] telephone_reimbursement_exemption_monthly
- **Calculation**: `forecast[14] / 12`
- **Source**: forecast[14] (telephone_reimbursement_exemption) ÷ 12
- **Note**: Will be ₹0 (telephone fully taxable)

#### [29] motor_car_allowance_exemption_monthly
- **Calculation**: `forecast[15] / 12`
- **Source**: forecast[15] (motor_car_allowance_exemption) ÷ 12
- **Note**: Will be ₹0 (motor car fully taxable)

#### [30] gratuity_exemption_monthly
- **Calculation**: `forecast[16] / 12`
- **Source**: forecast[16] (gratuity_exemption) ÷ 12

#### [31] total_tax_exemptions_monthly
- **Calculation**: Sum of all monthly exemptions (columns 19-30)
- **Validation**: Must equal `forecast[19] / 12`

---

### **Section 4: Monthly Deductions** (Columns 32-40)

**CRITICAL**: Monthly deductions = Annual deductions ÷ 12

**Source**: All deductions from `annual_tax_forecast_april_2025.csv` ÷ 12

#### [32] standard_deduction_monthly
- **Calculation**: `forecast[20] / 12`
- **Source**: forecast[20] (standard_deduction) ÷ 12
- **Values**: ₹4,167 (OLD) or ₹6,250 (NEW)

#### [33] section_80c_deduction_monthly
- **Calculation**: `forecast[21] / 12`
- **Source**: forecast[21] (section_80c_deduction) ÷ 12

#### [34] section_80d_deduction_monthly
- **Calculation**: `forecast[25] / 12`
- **Source**: forecast[25] (section_80d_deduction) ÷ 12

#### [35] section_80g_deduction_monthly
- **Calculation**: `forecast[28] / 12`
- **Source**: forecast[28] (section_80g_deduction) ÷ 12

#### [36] section_24b_deduction_monthly
- **Calculation**: `forecast[29] / 12`
- **Source**: forecast[29] (section_24b_deduction) ÷ 12

#### [37] section_80tta_deduction_monthly
- **Calculation**: `forecast[32] / 12`
- **Source**: forecast[32] (section_80tta_deduction) ÷ 12

#### [38] section_80ttb_deduction_monthly
- **Calculation**: `forecast[33] / 12`
- **Source**: forecast[33] (section_80ttb_deduction) ÷ 12

#### [39] professional_tax_deduction_monthly
- **Calculation**: `forecast[34] / 12`
- **Source**: forecast[34] (professional_tax_deduction) ÷ 12
- **Typical Value**: ₹200/month (₹2,400/year ÷ 12)

#### [40] total_deductions_monthly
- **Calculation**: Sum of all monthly deductions (columns 32-39)
- **Validation**: Must equal `forecast[35] / 12`
- **Alternative**: `forecast[35] / 12` (simpler)

---

### **Section 5: Monthly Tax Calculation** (Columns 41-47)

#### [41] taxable_income_monthly
- **Calculation**:
  ```python
  taxable_income_monthly = (gross_salary_monthly - 
                           total_tax_exemptions_monthly - 
                           total_deductions_monthly)
  ```
- **Validation**: Should approximately equal `forecast[36] / 12`
- **Note**: May have small rounding differences

#### [42] tds_monthly
- **Calculation**:
  ```python
  tds_monthly = forecast[46] / 12  # Total annual tax ÷ 12
  ```
- **Source**: forecast[46] (total_tax_liability) ÷ 12
- **Rounding**: Round to nearest rupee (no decimals)
- **CRITICAL**: TDS is constant throughout the year (based on annual forecast)

#### [43] employee_pf_contribution_monthly
- **Calculation**: `input[30] / 12`
- **Source**: input[30] (employee_pf_contribution) ÷ 12
- **Note**: Deducted from salary

#### [44] nps_employee_contribution_monthly
- **Calculation**: `input[32] / 12`
- **Source**: input[32] (nps_employee_contribution) ÷ 12
- **Note**: Deducted from salary

#### [45] nps_additional_contribution_monthly
- **Calculation**: `input[34] / 12`
- **Source**: input[34] (nps_additional_contribution) ÷ 12
- **Note**: Deducted from salary

#### [46] professional_tax_paid_monthly
- **Calculation**: `input[38] / 12`
- **Source**: input[38] (professional_tax_paid) ÷ 12
- **Typical Value**: ₹200/month

#### [47] net_salary_monthly
- **Calculation**:
  ```python
  net_salary_monthly = (gross_salary_monthly - 
                       tds_monthly - 
                       employee_pf_contribution_monthly - 
                       nps_employee_contribution_monthly - 
                       nps_additional_contribution_monthly - 
                       professional_tax_paid_monthly)
  ```
- **Validation**: Should approximately equal `forecast[48] / 12`
- **Note**: This is the take-home pay

---

## 🔍 Validation Checklist (Per Employee)

### Component Sum Validation:
- [ ] gross_salary_monthly = sum of columns 5-18
- [ ] total_tax_exemptions_monthly = sum of columns 19-30
- [ ] total_deductions_monthly = sum of columns 32-39
- [ ] All monthly values = annual values ÷ 12 (±rounding)

### Annual Consistency Validation:
- [ ] gross_salary_monthly × 12 ≈ input gross_salary
- [ ] tds_monthly × 12 = forecast total_tax_liability
- [ ] net_salary_monthly × 12 ≈ forecast net_salary

### Logical Validation:
- [ ] net_salary_monthly > 0
- [ ] tds_monthly >= 0
- [ ] All exemptions <= corresponding allowances
- [ ] No negative values (except for specific cases)

### NEW Regime Specific Validation:
- [ ] All Chapter VI-A deduction_monthly = ₹0
- [ ] Most exemption_monthly = ₹0 (except standard)
- [ ] standard_deduction_monthly = ₹6,250 (₹75K ÷ 12)

### OLD Regime Specific Validation:
- [ ] standard_deduction_monthly = ₹4,167 (₹50K ÷ 12)
- [ ] Exemptions and deductions properly calculated

---

## 📋 Special Cases to Handle

### 1. LTA Payment Timing
- **Issue**: Some employees (e.g., EMP030) have LTA paid only in March
- **April Handling**:
  - If LTA is paid in specific month only: `lta_received_monthly = 0`
  - If LTA accrues monthly: `lta_received_monthly = annual / 12`
- **Check**: Look for entries in `monthly_payslip_march.csv` for LTA

### 2. Fixed vs Variable Bonus/Commission
- **Fixed** (e.g., EMP008):
  - Included in annual input as total amount
  - Divide by 12 for each month
  - `bonus_monthly = input[27] / 12`
  
- **Variable** (e.g., EMP002, EMP004, EMP007):
  - Set to ₹0 in annual input
  - `bonus_monthly = 0` in April
  - Appears only in specific months (check monthly CSVs)

### 3. Mid-Year Changes (Not Applicable to April)
- Mid-year salary changes, regime changes, investment updates do NOT affect April
- April payslip uses original April annual input data only

### 4. Previous Employer Income (EMP023)
- **Issue**: Employee has previous employer income in same FY
- **April Handling**: April payslip shows CURRENT employer only
- **Annual tax** includes previous employer income
- **Monthly TDS** is higher to account for total annual liability

---

## 🎯 Processing Order

Process employees in this order:

1. **Simple cases first** (EMP001-EMP010): Standard salary, no special scenarios
2. **Complex allowances** (EMP011-EMP018): Multiple allowances, exemptions
3. **Special scenarios** (EMP019-EMP032): Gratuity, NRI, multiple employers, etc.

---

## ✅ Implementation Approach

### Step-by-Step Process:

1. **Read Input Files**:
   - `annual_employee_input_data_april_2025.csv`
   - `annual_tax_forecast_april_2025.csv`

2. **For Each Employee**:
   - Extract annual values from input
   - Extract annual exemptions/deductions from forecast
   - Calculate monthly values (÷ 12)
   - Validate calculations
   - Create monthly payslip row (48 fields)

3. **Write Output**:
   - Update `monthly_payslip_april.csv`
   - Preserve existing data structure

4. **Validation**:
   - Verify 48 fields per row
   - Verify calculations
   - Check annual consistency

---

## 📊 Expected Outcomes

### Before Recalculation:
- Unknown: Current state of monthly payslip data
- Potential issues: Misalignment with annual data

### After Recalculation:
- All 31 employees with correct April payslips
- Perfect consistency with annual data
- All calculations validated
- All 48 fields correctly populated

---

## ⚠️ Critical Reminders

1. **Division by 12**: All annual amounts must be divided by 12
2. **Rounding**: Use consistent rounding (2 decimals for amounts, 0 for TDS)
3. **Field Count**: Always 48 fields (never more, never less)
4. **TDS Constant**: TDS same every month (annual tax ÷ 12)
5. **No Variable Pay**: April has no variable bonuses/commissions (unless fixed)
6. **Source Truth**: Annual input + Annual forecast are source of truth
7. **LTA Exemption**: Always ₹0 in April (cannot predict travel)

---

## 📈 Success Criteria

1. ✅ All 31 employees processed
2. ✅ All 48 columns filled correctly
3. ✅ All monthly values = annual ÷ 12
4. ✅ Perfect annual consistency (monthly × 12 = annual)
5. ✅ All validations pass
6. ✅ No data corruption
7. ✅ Field count = 48 for all rows

---

**Status**: READY TO START  
**Next Step**: Begin with EMP001 and process systematically  
**Estimated Time**: 2-3 hours for all 31 employees

