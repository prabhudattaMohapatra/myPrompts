# CTC (Cost to Company) - Composition & Definition

**Date**: November 22, 2025  
**Context**: Indian Payroll - Annual CTC at Start of Financial Year (April)  
**Purpose**: Define what should be included in `annual_ctc` field

---

## 🎯 What is CTC (Cost to Company)?

CTC represents the **total annual cost that the employer will incur** for an employee during the financial year. It's the "offer letter" amount that includes all fixed and variable components that are **committed at the start of the year**.

---

## 📊 CTC Composition - Complete Breakdown

### CTC = Gross Salary + Employer Contributions + Other Benefits

```
CTC (Cost to Company)
│
├── GROSS SALARY (Take-home eligible components)
│   ├── Fixed Components
│   │   ├── Basic Salary
│   │   ├── House Rent Allowance (HRA)
│   │   ├── Special Allowance
│   │   ├── Transport Allowance
│   │   ├── Conveyance Allowance
│   │   ├── Leave Travel Allowance (LTA)
│   │   ├── Meal Vouchers/Allowance
│   │   ├── Children Education Allowance
│   │   ├── Children Hostel Allowance
│   │   ├── Books & Periodicals Allowance
│   │   ├── Telephone/Mobile Allowance
│   │   └── Other Allowances
│   │
│   └── Variable Components (if guaranteed/budgeted in April)
│       ├── Fixed Bonus (annual, declared in April)
│       └── Fixed Incentive (quarterly targets set in April)
│
├── EMPLOYER CONTRIBUTIONS (Non-take-home)
│   ├── Employer PF Contribution (12% of basic, capped at ₹1,800/month)
│   ├── Employer NPS Contribution (if applicable, typically 10% of basic)
│   ├── Employer ESI Contribution (3.25% for salary <₹21K/month)
│   └── Professional Tax (employer's share, if any)
│
└── OTHER BENEFITS (Non-cash)
    ├── Gratuity Provision (annual accrual)
    ├── Medical Insurance Premium (employer-paid)
    ├── Group Life Insurance Premium
    ├── Accidental Insurance Premium
    ├── Food Coupons (beyond meal allowance)
    ├── Wellness Benefits
    └── Other Perquisites
```

---

## 🔍 What Should be INCLUDED in April CTC?

### ✅ ALWAYS Include (Fixed & Committed):

1. **All Fixed Salary Components**
   - Basic, HRA, Special Allowance, etc.
   - Everything in the monthly salary structure × 12

2. **Employer Statutory Contributions**
   - Employer PF (12% of basic, max ₹1,800/month = ₹21,600/year)
   - Employer ESI (if applicable)
   - Professional Tax (if employer-borne)

3. **Annual Guaranteed Bonuses**
   - Fixed performance bonus declared in offer letter
   - Diwali bonus (if guaranteed)
   - Any contractual annual bonus

4. **Employer Benefits (if quantifiable)**
   - Medical insurance premium paid by employer
   - Gratuity accrual (typically 4.81% of basic)
   - Other insurance premiums

---

## ❌ What Should be EXCLUDED from April CTC?

### Variables NOT Known in April:

1. **Performance-Based Variable Pay**
   - Quarterly/annual performance bonuses (uncertain in April)
   - Commission based on actual sales
   - Spot awards/recognition bonuses

2. **Reimbursements**
   - Actual travel reimbursements
   - Medical expense reimbursements (beyond insurance)
   - Internet/phone bill reimbursements (actual expenses)

3. **One-Time Payments**
   - Joining bonus (if already paid)
   - Relocation allowance (one-time)
   - Retention bonus (paid later)

4. **Future Unknowns**
   - Mid-year salary hikes
   - Promotion increments
   - Ad-hoc bonuses decided later

---

## 📐 CTC Calculation Models

### Model 1: Simple CTC (Most Common in Our Dataset)

```
CTC = Gross Salary (all components sum)
```

**When to use:**
- Standard employment with no employer PF in CTC
- Clean, simple structure
- **28 out of 31 employees** in our dataset use this

**Example: EMP001**
```
CTC = ₹650,000
Gross Salary = ₹650,000
Employer PF = ₹0 (not included in CTC)
```

---

### Model 2: CTC Including Employer PF (Traditional)

```
CTC = Gross Salary + Employer PF Contribution
```

**When to use:**
- Traditional payroll modeling
- When showing "total cost" perspective
- More accurate representation of employer's cost

**Example (hypothetical):**
```
Gross Salary = ₹6,00,000
Basic = ₹3,00,000
Employer PF = 12% of ₹3,00,000 = ₹36,000
CTC = ₹6,00,000 + ₹36,000 = ₹6,36,000
```

---

### Model 3: Comprehensive CTC (Full Cost)

```
CTC = Gross Salary + Employer PF + Medical Insurance + Gratuity Provision + Other Benefits
```

**When to use:**
- Complete cost-to-company view
- Executive/senior roles with significant benefits
- Multinational companies

**Example (hypothetical):**
```
Gross Salary = ₹12,00,000
Employer PF = ₹21,600 (capped)
Medical Insurance = ₹15,000
Gratuity Accrual = ₹57,720 (4.81% of basic)
Other Benefits = ₹25,000
CTC = ₹12,00,000 + ₹21,600 + ₹15,000 + ₹57,720 + ₹25,000 = ₹13,19,320
```

---

## 🎯 Recommendation for Our Dataset

### Preferred Approach: **Model 1 (Simple CTC)**

```
annual_ctc = gross_salary (sum of all salary components)
```

**Rationale:**
1. ✅ **Simplicity**: Easier to understand and validate
2. ✅ **Consistency**: 28/31 employees already use this
3. ✅ **Tax Focus**: Our dataset focuses on income tax, not employer cost modeling
4. ✅ **Clean Validation**: `annual_ctc = gross_salary` is easy to verify

**For Special Cases:**
- **Partial Year (EMP019)**: `annual_ctc` = annual rate, `gross_salary` = pro-rated
- **Mid-Year Changes**: Use original April CTC, adjust gross for blended income

---

## 🔧 What About EMP012?

**Current Situation:**
- CTC: ₹1,500,000
- Gross: ₹1,419,600
- Difference: ₹80,400 (5.36%)

**Analysis:**
The ₹80,400 could represent:
1. **Employer PF**: Basic ₹600K × 12% = ₹72K (close!)
2. **Rounding**: CTC set at round ₹15L in offer letter
3. **Gratuity/Insurance**: Small benefit provisions

**Recommendation for EMP012:**

**Option A - Align to Simple Model** (Recommended):
```python
annual_ctc: ₹1,500,000 → ₹1,419,600
# Makes it consistent with 28 other employees
# CTC = Gross (Model 1)
```

**Option B - Document as Model 2**:
```python
annual_ctc: ₹1,500,000 (keep as-is)
# Document: CTC includes ₹80,400 employer costs
# Add note in documentation
```

**Option C - Recalculate if Employer PF**:
If EMP012 should have employer PF:
```python
Basic = ₹600,000
Employer PF = 12% × ₹600,000 = ₹72,000
Expected CTC = ₹1,419,600 + ₹72,000 = ₹1,491,600
Current CTC = ₹1,500,000
Still ₹8,400 difference (could be rounding)
```

---

## 📋 Best Practice Guidelines

### At Start of FY (April):

1. **For Full-Year Employees:**
   ```
   annual_ctc = SUM(all fixed salary components for 12 months)
   gross_salary = annual_ctc
   ```

2. **For Partial-Year Employees:**
   ```
   annual_ctc = Annual rate (what they would earn if full year)
   gross_salary = Pro-rated for actual months worked
   ```

3. **For Mid-Year Joiners:**
   ```
   annual_ctc = Annual rate offered
   gross_salary = Actual earnings from joining month to March
   ```

4. **For Employees with Mid-Year CTC Change:**
   ```
   annual_ctc = April CTC (original)
   gross_salary = Blended gross across all months
   Document revision in ctc_revision_*.csv
   ```

---

## 🎓 Key Principle

### April CTC Should Reflect:

> **"What is KNOWN, FIXED, and COMMITTED at the start of the financial year (April)"**

**Include:**
- ✅ All fixed monthly components × 12
- ✅ Annual guaranteed bonuses (if in offer letter)
- ✅ Employer PF (optional, based on model chosen)

**Exclude:**
- ❌ Variable performance pay (unknown in April)
- ❌ Future bonuses/commissions (not committed)
- ❌ Reimbursements (actual expenses only)
- ❌ Mid-year hikes (not known in April)

---

## 🏆 Final Recommendation

### For Our Indian Tax Test Dataset:

**Use Model 1 (Simple CTC):**
```
annual_ctc = gross_salary
```

**Exceptions:**
- **EMP019**: Keep CTC ≠ Gross (partial year - correct as-is)
- **EMP012**: Align CTC to ₹1,419,600 to match gross (recommended)

**This provides:**
- ✅ Maximum consistency across dataset
- ✅ Easy validation (`annual_ctc == gross_salary` for full-year employees)
- ✅ Clear separation of employer costs (track separately if needed)
- ✅ Focus on employee's taxable income (our primary goal)

---

**Summary**: For April CTC in our dataset, use **Model 1 (Simple CTC)** where `annual_ctc = gross_salary` for all full-year standard employees. This is the cleanest approach for an income tax focused test dataset.

