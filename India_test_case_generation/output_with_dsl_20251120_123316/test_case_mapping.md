# Test Case Mapping: Employees to Use Cases

**Assessment Year**: 2026-27  
**Total Employees**: 30 (EMP001 - EMP032, excluding EMP022, EMP024)  
**Total Test Cases**: 33 (TC-01 - TC-35, excluding TC-22, TC-25)  
**Output Directory**: output_with_dsl_20251120_123316  
**Generated Date**: November 20, 2025  
**Status**: 30 employees completed  
**Last Updated**: November 20, 2025

## Generation Progress

**Status**: ✅ COMPLETED  
**Employees Generated**: 30 of 30 (100%)  
**Test Cases Covered**: 33 of 33 (100%)

**Regime Distribution**:
- New Regime: 7 employees (EMP001-004, EMP018, EMP021, EMP029)
- Old Regime: 23 employees (EMP005-017, EMP019-020, EMP023, EMP025-028, EMP030-032)
- **Note**: EMP022, EMP024 have been removed
- **Strategy**: Comprehensive coverage of both regimes with focus on Old Regime for maximum deduction/exemption scenarios

### Completed:
- ✅ EMP001 (TC-01): New Regime - Below Exemption Limit - Tax: ₹0
- ✅ EMP002 (TC-02): New Regime - Rebate Threshold Boundary - Tax: ₹93,756
- ✅ EMP003 (TC-03): New Regime - Marginal Relief Zone - Tax: ₹70,356
- ✅ EMP004 (TC-04): New Regime - High Income with Surcharge (10%) - Tax: ₹17.73L
- ✅ EMP005 (TC-05): Old Regime - Maximum Deductions - Tax: ₹1.33L
- ✅ EMP006 (TC-06): Old Regime - Senior Citizen (60-80) - Tax: ₹27,789
- ✅ EMP007 (TC-08): Old Regime - Regime Comparison - Tax: ₹0
- ✅ EMP008 (TC-09): Old Regime - Very High Income with Maximum Surcharge (25%) - Tax: ₹2.11Cr
- ✅ EMP009 (TC-10): Old Regime - HRA Metro Maximum Exemption - Tax: ₹57,574
- ✅ EMP010 (TC-11): Old Regime - HRA Non-Metro Minimal Exemption - Tax: ₹38,667
- ✅ EMP011 (TC-12): Old Regime - Section 80GG (No HRA) - Tax: ₹30,181
- ✅ EMP012 (TC-13): Old Regime - Multiple Allowances Combined - Tax: ₹28,018
- ✅ EMP013 (TC-14): Old Regime - Maximum Deductions Scenario - Tax: ₹4,22,698
- ✅ EMP014 (TC-15): Old Regime - NPS Both Employee & Employer - Tax: ₹1,33,037
- ✅ EMP015 (TC-16): Old Regime - Home Loan Multiple Properties - Tax: ₹4,49,155
- ✅ EMP016 (TC-17): Old Regime - Disability & Dependent Benefits - Tax: ₹35,422
- ✅ EMP017 (TC-18): Old Regime - Investment & Donation Combinations - Tax: ₹65,374
- ✅ EMP018 (TC-19): New Regime - ULIP & Capital Gains - Tax: ₹3,50,896
- ✅ EMP019 (TC-20): Old Regime - Gratuity with Section 89 Relief - Tax: ₹0
- ✅ EMP020 (TC-21): Old Regime - EPF Withdrawal Before 5 Years - Tax: ₹95,867
- ✅ EMP021 (TC-23): New Regime - NRI Employee - Tax: ₹1,30,000
- ❌ EMP022 (TC-22): **REMOVED** - Super Senior Citizen (80+) - Was: Tax ₹0
- ✅ EMP023 (TC-24): Old Regime - Multiple Employers in Same Year - Tax: ₹80,309
- ❌ EMP024 (TC-25): **REMOVED** - Mid-Year Salary Structure Change
- ✅ EMP025 (TC-26): Old Regime - Professional Tax Multiple States - Tax: ₹1,62,717
- ✅ EMP026 (TC-27): Old Regime - TDS Threshold Testing - Rent Payment - Tax: ₹4,20,763
- ✅ EMP027 (TC-28): Old Regime - VPF Contribution (Low Income) - Tax: ₹0
- ✅ EMP028 (TC-29): Old Regime - Additional Income (Rental) - Tax: ₹2,00,740
- ✅ EMP029 (TC-30): New Regime - Mid-Year Tax Regime Change - Tax: ₹1,30,117
- ✅ EMP030 (TC-31, TC-32, TC-33): Old Regime - Monthly Investment Update, Annual Allowance Due Month Detection, LTA Payment and Adjustment - Tax: ₹79,318
- ✅ EMP031 (TC-34): Old Regime - Voluntary Provident Fund Adjustment - Tax: ₹0
- ✅ EMP032 (TC-35): Old Regime - Mid-Year Investment Declaration Change (February) - Tax: ₹0 (with ₹34.3K refund)

## Mapping Overview

This document maps each of the 30 employees to one or more test cases from Use_Cases.md. The goal is to ensure comprehensive coverage of all 38 test cases while generating realistic and compliant test data.

**Note**: Some test case IDs have been adjusted from the original plan to better match the actual implementation.

## Employee to Test Case Mapping

| Employee ID | Test Case ID(s) | Test Case Description | Status | Actual Implementation |
|-------------|-----------------|----------------------|--------|----------------------|
| EMP001 | TC-01 | New Regime - Below Exemption Limit | ✅ DONE | New regime, ₹6.5L gross, ₹5.51L taxable, full rebate 87A, zero tax |
| EMP002 | TC-02 | New Regime - Rebate Threshold Boundary | ✅ DONE | New regime, ₹13.05L gross, ₹12.01L taxable (just above ₹12L rebate), tax ₹93,756 (no rebate), **variable commission ₹70K in December only** |
| EMP003 | TC-03 | New Regime - Marginal Relief Zone | ✅ DONE | New regime, ₹13.5L gross, ₹12.51L taxable, just above ₹12L rebate, tax ₹70,356 |
| EMP004 | TC-04 | New Regime - High Income with Surcharge | ✅ DONE | New regime, ₹70L gross (₹67.54L CTC + ₹2.456L variable commission), ₹69.01L taxable, 10% surcharge (₹50L-₹1Cr tier), **fixed bonus ₹3L/year (₹25K/month)**, **variable commission in Apr/Dec/March (₹80K/₹85.6K/₹80K)**, tax ₹17.73L, ETR 23.64% |
| EMP005 | TC-05 | Old Regime - Maximum Deductions | ✅ DONE | **Adjusted**: Old regime, ₹18L gross, max deductions (80C ₹1.5L, 80D ₹75K, 80CCD(1B) ₹50K, 80CCD(2) ₹36K), effective tax 7.41% |
| EMP006 | TC-06 | Old Regime - Senior Citizen (60-80) | ✅ DONE | **Adjusted**: Old regime, age 62, senior citizen slabs, 80D ₹50K, 80TTB ₹50K, effective tax 2.32% |
| EMP007 | TC-08 | Old vs New - Regime Comparison Case | ✅ DONE | New regime chosen, ₹10L gross (₹9.5L CTC + ₹50K variable performance bonus), **variable performance bonus ₹50K in April only**, ₹0 tax (rebate), old saves ₹28,621, rebate threshold critical |
| EMP008 | TC-09 | Very High Income - Maximum Surcharge | ✅ DONE | **OLD REGIME**, ₹6Cr gross, maximum deductions ₹43.47L, taxable ₹5.46Cr, 25% surcharge (>₹5Cr), tax ₹2.11Cr, ETR 35.10%, old saves ₹16.25L vs new |
| EMP009 | TC-10 | HRA - Metro City Maximum Exemption | ✅ DONE | **OLD REGIME**, Mumbai metro, ₹18L gross, 100% HRA exempt (₹3.6L), high basic 50% (₹9L), high rent ₹60K/month, HRA saves ₹72K tax, ETR 3.20%, take-home 90.66% |
| EMP010 | TC-11 | HRA - Non-Metro with Minimal Exemption | ✅ DONE | **OLD REGIME**, Pune non-metro, ₹12L gross, **MINIMAL 50% HRA exempt (₹60K of ₹1.2L)**, low rent ₹10K/month limits exemption, limiting factor: Rent-10% basic, 40% rule (non-metro), home loan ₹1.5L, ETR 3.22%, contrasts with Metro 100% |
| EMP011 | TC-12 | Section 80GG - No HRA Received | ✅ DONE | **OLD REGIME**, Jaipur non-metro, ₹10L gross, **NO HRA in salary (₹0)**, rent paid ₹12K/month (₹1.44L/year), **Section 80GG ₹60K (max ₹5K/month cap)**, limiting factor: ₹5K/month statutory limit, similar benefit to EMP010 (₹60K), demonstrates rent relief without HRA, ETR 3.02% |
| EMP012 | TC-13 | Multiple Allowances Combined | ✅ DONE | **OLD REGIME**, Bangalore metro, ₹14.2L gross, **9 DIFFERENT ALLOWANCES (₹5.2L total)**, HRA ₹3L (80% exempt ₹2.4L), Conveyance ₹24K (100%), LTA ₹60K (100%), Meal ₹26.4K (100%), CEA ₹24K (10% ₹2.4K), Hostel ₹36K (20% ₹7.2K), Transport ₹19.2K (0%), Books ₹12K (0%), Telephone ₹18K (0%), **total exemptions ₹3.6L (69.3%)**, 2 children, home loan ₹1.8L, ETR 1.97%, take-home 92.78% |
| EMP013 | TC-14 | Maximum Deductions Scenario (Old Regime) | ✅ DONE | **OLD REGIME**, Delhi metro, ₹35L gross, **MAXIMUM DEDUCTIONS ₹9.27L (26.5%)**, 80C ₹1.5L MAX, 80CCD(1B) ₹50K MAX, 80CCD(2) ₹1.4L, 80D ₹75K MAX (family+senior parents), 80G ₹1L donations, 24(b) ₹2L MAX home loan, 80EEA ₹1.5L MAX (first-time buyer), 80TTA ₹10K MAX, HRA ₹4.6L exempt, taxable ₹19.8L, tax ₹4.23L, **tax savings ₹4.26L (50.2%)**, ETR 12.08%, demonstrates optimal tax planning |
| EMP014 | TC-15 | NPS - Both Employee & Employer Contributions | ✅ DONE | **OLD REGIME**, Hyderabad metro, ₹20L gross, **ALL THREE NPS TYPES**, basic ₹10L (50%), **NPS employee ₹1L (80CCD1 within 80C)**, **additional NPS ₹50K (80CCD1B over 80C)**, **employer NPS ₹1L (80CCD2 separate)**, **total NPS ₹2.5L (42.6% of deductions)**, HRA ₹2.6L exempt, taxable ₹10.51L, tax ₹1.33L, tax savings ₹40K (23.3%), ETR 6.65%, demonstrates retirement planning |
| EMP015 | TC-16 | Home Loan - Multiple Properties | ✅ DONE | **OLD REGIME**, Chennai metro, ₹25L gross, **2 PROPERTIES**, Property 1: Self-occupied with home loan interest ₹2L (Section 24(b) max), Property 2: Let-out rental ₹3.6L/year with ₹1.5L loan interest (no limit), **net house property income ₹1L**, HRA ₹1.16L exempt (pays rent elsewhere), GTI ₹26.08L, 80C ₹1.5L, 80D ₹25K, **total interest deductions ₹3.5L**, taxable ₹20.65L, tax ₹4.49L, ETR 17.2%, demonstrates property portfolio taxation |
| EMP016 | TC-17 | Disability & Dependent Benefits | ✅ DONE | **OLD REGIME**, Mumbai metro, ₹18L gross, **DISABILITY BENEFITS**, self 40-80% disability (Section 80U ₹75K), dependent child severe 80%+ disability (Section 80DD ₹1.25L), **transport allowance ₹3.2K/month (double normal ₹19.2K extra)**, **total disability benefits ₹2.19L (28.6% of deductions)**, tax savings ₹43.8K (54.7%), taxable ₹6.08L, tax ₹35.4K, ETR 1.97%, take-home 93.10%, demonstrates government support for disabled persons |
| EMP017 | TC-18 | Investment & Donation Combinations | ✅ DONE | **OLD REGIME**, Bangalore metro, ₹16L gross, **INVESTMENT & DONATION FOCUS**, **80C+CCC+CCD(1) ₹3.34L declared → ₹1.5L allowed (combined limit)**, 80CCD(1B) ₹50K, 80CCD(2) ₹64K, **total investment deductions ₹2.64L**, **80G donations ₹90K (mixed eligibility) → ₹70K deduction (77.8%)**, PM Relief ₹30K (100% no limit), Trust ₹40K→₹20K (50% with limit), NGO ₹20K (100% with limit), **total inv+don ₹3.34L (74.3% of deductions)**, taxable ₹7.52L, tax ₹65.4K, ETR 4.09%, tax savings ₹79.4K, demonstrates diversified tax planning |
| EMP018 | TC-19 | ULIP & Capital Gains | ✅ DONE | **NEW REGIME**, Pune metro, ₹28.08L GTI (₹22L salary + ₹6L ULIP CG + ₹8K interest), **ULIP premium ₹3L/year (>₹2.5L limit)**, total premium ₹9L (3 years), maturity proceeds ₹15L, capital gains ₹6L, **Section 10(10D) NOT applicable**, **LTCG @ 12.5% = ₹75K**, tax on regular income ₹2.62L, total tax ₹3.51L, ETR 12.50%, **Rule IN-CG-2025-ULIP-002**, demonstrates post-Budget 2021 ULIP taxation, high premium ULIPs not exempt |
| EMP019 | TC-20 | Gratuity with Section 89 Relief (15+ years) | ✅ DONE | **OLD REGIME**, Delhi metro, retiring after 18.5 years, salary 3 months ₹3.75L, **gratuity ₹5.35L (100% exempt)**, leave encashment ₹2L (100% exempt), **total retirement benefits ₹7.35L tax-free**, **Section 89 relief for 15+ years service**, Form 10E Annexure IIA, **Rule IN-89-2025-GRATUITY-15PLUS-YRS**, taxable income ₹1.41L (below exemption), tax ₹0, total receipts ₹10.91L, demonstrates tax-efficient retirement |
| EMP020 | TC-21 | EPF Withdrawal Before 5 Years | ✅ DONE | **OLD REGIME**, Bangalore metro, service 3.5 years (<5), **EPF withdrawal ₹1.93L**, employee contribution ₹1.78L taxable, interest ₹15.4K taxable, **added to gross income ₹14.01L**, **Section 89 relief eligible**, Form 10E required, **Rule IN-PF-2025-001**, taxable income ₹9.97L, tax ₹95.9K, ETR 6.84%, demonstrates EPF taxation before 5 years & Section 89 relief process |
| EMP021 | TC-23 | NRI Employee | ✅ DONE | **NEW REGIME**, Mumbai metro, ₹15L gross, **NRI residency**, same tax slabs as residents, standard deduction ₹75K, **Section 87A rebate NOT eligible (Rule IN-SPEC-2025-NRI-001)**, taxable ₹14.25L, base tax ₹125K, rebate ₹0, final tax ₹130K, ETR 8.67%, demonstrates NRI tax treatment - no rebate regardless of income |
| ~~EMP022~~ | ~~TC-22~~ | ~~Super Senior Citizen (80+)~~ | ❌ REMOVED | **REMOVED FROM DATASET** - Was: OLD REGIME, Lucknow non-metro, pensioner, age 82, ₹5L basic exemption, Section 80TTB ₹50K, zero tax |
| EMP023 | TC-24 | Multiple Employers in Same Year | ✅ DONE | **OLD REGIME**, Bangalore metro, **2 employers in FY**, previous employer (Apr-Sep) ₹6L, current employer (Oct-Mar) ₹7.5L, **total income ₹13.5L**, **Form 12B provided**, previous TDS ₹30K, current monthly TDS ₹8.4K, total TDS ₹80.3K, HRA exemption ₹1.62L, 80C ₹1.5L, 80CCD(1B) ₹50K, 80CCD(2) ₹60K, 80D ₹60K, taxable ₹8.24L, tax ₹80.3K, ETR 5.9%, **Rule TDS-PREV-EMP-001**, demonstrates TDS adjustment for multiple employers, Form 12B handling, Form 26AS reconciliation |
| ~~EMP024~~ | ~~TC-25~~ | ~~Mid-Year Salary Structure Change~~ | ❌ REMOVED | **REMOVED FROM DATASET** |
| EMP025 | TC-26 | Professional Tax - Multiple States | ✅ DONE | **OLD REGIME**, Bangalore metro, ₹16.67L gross (₹16L Apr-Nov + ₹18L Dec-Mar pro-rated), **PT paid in Maharashtra (Mumbai) ₹1.6K + Karnataka (Bangalore) ₹800 = ₹2.4K total**, **CTC revision in December** (₹16L → ₹18L, +12.5%), **employee relocation** from Mumbai to Bangalore, **split HRA exemption** (Mumbai ₹53.3K + Bangalore ₹24K = ₹77.3K), taxable ₹11.47L, tax ₹1.63L, ETR 9.76%, demonstrates PT across multiple states with mid-year relocation and CTC change |
| EMP026 | TC-27 | TDS Threshold Testing - Rent Payment | ✅ DONE | **OLD REGIME**, Bangalore metro, ₹30L CTC, **monthly rent ₹60K (EXCEEDS ₹50K threshold)**, **Section 194-I TDS @ 10% = ₹72K/year**, HRA received ₹6L, **HRA 100% exempt (all three options equal at ₹6L)**: Actual HRA ₹6L = Rent-10% basic ₹6L = 50% basic ₹6L, total exemptions ₹7.59L, taxable ₹19.74L, tax ₹4.21L, ETR 14.03%, demonstrates rent TDS compliance when monthly rent >₹50K, landlord PAN required, quarterly TDS returns (Form 26QC), TDS certificate (Form 16C) |
| EMP027 | TC-28 | VPF Contribution (Low Income) | ✅ DONE | **OLD REGIME**, Indore non-metro, ₹6L CTC (low income), owns house (no HRA), **VPF ₹48K (20% of basic)**, mandatory PF ₹28.8K + VPF ₹48K + investments ₹25K = **total 80C ₹1.02L**, Section 80D ₹15K, Section 80TTA ₹5K, taxable ₹3.96L, base tax ₹7.3K, **Section 87A rebate ₹7.3K → ZERO TAX**, demonstrates VPF for retirement corpus building, VPF earns ~8.15% p.a. (tax-free, EEE status), can contribute up to 100% of basic, employer matches only mandatory 12% |
| EMP028 | TC-29 | Additional Income (Rental) | ✅ DONE | **OLD REGIME**, Pune metro, ₹18L salary, **let-out property in Delhi**, rental income ₹3.6L, municipal tax ₹20K, **30% standard deduction ₹1.02L (Section 24)**, **home loan interest ₹2.8L (no limit for let-out)**, **house property LOSS ₹42K**, loss set-off against salary, GTI ₹17.58L (₹18L - ₹42K), HRA exemption ₹1.08L (rent paid ₹1.8L in Pune), taxable ₹12.68L, tax ₹2.01L, ETR 11.42%, demonstrates rental property taxation with loss, tax benefit ~₹8.4K from HP loss |
| EMP029 | TC-30 | Mid-Year Tax Regime Change | ✅ DONE | **NEW REGIME** (final choice), Hyderabad metro, ₹15L gross, **regime change from Old to New in December**, **entire year recalculated under New Regime**, **no exemptions/deductions** (only ₹75K standard deduction), **TDS revision from ₹6K to ₹20.5K/month** from December, taxable ₹14.25L, tax ₹1.30L, ETR 8.67%, demonstrates mid-year regime change mechanics, TDS adjustment, and take-home salary impact (₹14.5K/month reduction) |
| EMP030 | TC-31, TC-32, TC-33 | Monthly Investment Update, Annual Allowance Due Month Detection, LTA Payment and Adjustment | ✅ DONE | **OLD REGIME**, Pune metro, ₹12L gross, **LTA paid in March only** (₹30K annual allowance), regular monthly gross ₹97.5K (excluding LTA), March gross ₹127.5K (including LTA), **monthly investment declaration updates**, **annual allowance tracking**, taxable ₹8.19L, tax ₹79.3K, ETR 6.61%, demonstrates operational test cases for investment update workflow, allowance due month detection, and LTA payment timing |
| EMP031 | TC-34 | Voluntary Provident Fund Adjustment | ✅ DONE | **OLD REGIME**, Kanpur non-metro, ₹4.5L gross, basic ₹15K/month, **VPF ₹12K/month** (within ₹13K statutory cap), total PF+VPF ₹1.656L, **80C limited to ₹1.5L**, excess ₹15.6K earns returns (no tax benefit), taxable ₹2.14L, **zero tax** (below ₹2.5L), demonstrates VPF cap testing and retirement corpus building for low-income employees |
| EMP032 | TC-35 | Mid-Year Investment Declaration Change (February) | ✅ DONE | **OLD REGIME**, Ahmedabad metro, ₹12L gross, **February investment revision**, 80C increased to ₹1.5L (from ₹1.316L), **added 80CCD(1B) ₹50K**, 80D ₹25K (from ₹15K), 24(b) ₹1.5L (from ₹1L), house loss -₹50K (from -₹30K), **original tax ₹41.2K**, **revised tax ₹0** (87A rebate), TDS Apr-Jan ₹3.43K/month (10 months = ₹34.3K), **TDS Feb-Mar ₹0**, **refund ₹34.3K via ITR**, demonstrates mid-year tax optimization and realistic refund scenario |
| EMP009 | TC-09 | Very High Income - Maximum Surcharge | High |
| EMP010 | TC-10 | HRA - Metro City Maximum Exemption | Medium |
| EMP011 | TC-11 | HRA - Non-Metro with Minimal Exemption | Medium |
| EMP012 | TC-12 | Section 80GG - No HRA Received | Medium |
| EMP013 | TC-13 | Multiple Allowances Combined | Medium |
| EMP014 | TC-14 | Maximum Deductions Scenario (Old Regime) | Medium |
| EMP015 | TC-15 | NPS - Both Employee & Employer Contributions | Medium |
| EMP016 | TC-16 | Home Loan - Multiple Properties | Medium |
| EMP017 | TC-17 | Disability & Dependent Benefits | Medium |
| EMP018 | TC-18 | Investment & Donation Combinations | Medium |
| EMP019 | TC-19 | ULIP & Capital Gains | Medium |
| EMP020 | TC-21 | EPF Withdrawal Before 5 Years | Medium |
| EMP021 | TC-23 | NRI Employee | Medium |
| ~~EMP022~~ | ~~TC-22~~ | ~~Super Senior Citizen (80+)~~ | ~~REMOVED~~ |
| EMP023 | TC-24 | Multiple Employers in Same Year | Medium |
| ~~EMP024~~ | ~~TC-25~~ | ~~Mid-Year Salary Structure Change~~ | ~~REMOVED~~ |
| EMP025 | TC-26 | Professional Tax - Multiple States | Medium |
| EMP026 | TC-27 | TDS Threshold Testing - Rent Payment | Low |
| EMP027 | TC-28 | VPF Contribution (Low Income) | Low |
| EMP028 | TC-29 | Additional Income (Rental) | Low |
| EMP029 | TC-30 | Mid-Year Tax Regime Change | Medium |
| EMP030 | TC-31, TC-32, TC-33 | Monthly Investment Update, Annual Allowance Due Month Detection, LTA Payment and Adjustment | Low |

## Additional Test Cases Coverage

The following test cases (TC-34 to TC-38) may require special handling or can be covered as variations in the data of existing employees:

- **TC-34**: Voluntary Provident Fund Adjustment - Can be included in EMP027 or EMP028
- **TC-35**: PF Calculation for International Worker - Can be included in EMP022 (NRI employee)
- **TC-36**: NRI and Residency Status Rebate - Covered by EMP022
- **TC-37**: Retrospective Change in Salary Components - Can be covered in EMP024 or EMP025
- **TC-38**: Grossing Up Components on Client Request - Can be handled as a calculation variation

## Monthly Input Data Requirements

The following employees will have monthly input data:

### Monthly Bonus and Commission Data (April, December, March)
- **At least 5 non-zero values total** across all employees per CSV
- Employees selected: EMP004, EMP005, EMP008, EMP010, EMP013, EMP019, EMP023, EMP024, EMP028

### CTC Revision Data (December)
- **Exactly 3 employees** with CTC revision
- Employees selected: EMP024, EMP025, EMP030

### Tax Regime Revision (December)
- **Exactly 2 employees** with tax regime revision
- Employees selected: EMP029, EMP030

## Test Case Coverage by Category

### Tax Regime Coverage
- **New Regime**: EMP001, EMP002, EMP003, EMP004, EMP005, EMP018, EMP021, EMP022, EMP023, EMP024, EMP028, EMP029
- **Old Regime**: EMP006, EMP007, EMP008, EMP009, EMP010, EMP011, EMP012, EMP013, EMP014, EMP015, EMP016, EMP017, EMP019, EMP020, EMP025, EMP026, EMP027, EMP030

### Income Level Coverage
- **Low Income (₹3-7L)**: EMP001, EMP027
- **Medium Income (₹9-15L)**: EMP002, EMP003, EMP005, EMP006, EMP007, EMP008, EMP010, EMP011, EMP014, EMP015, EMP018, EMP022
- **High Income (₹50L+)**: EMP004, EMP009
- **Very High Income (₹1Cr+)**: EMP009

### Age Category Coverage
- **Normal (< 60)**: EMP001-EMP006, EMP008-EMP030
- **Senior Citizen (60-80)**: EMP007
- **Super Senior Citizen (≥ 80)**: Can be included as variation if needed

### City Type Coverage
- **Metro (Delhi, Mumbai, Chennai, Kolkata)**: EMP006, EMP010, EMP014
- **Non-Metro**: EMP011, EMP026, EMP027, EMP028
- **Tier 1/Tier 2 cities**: Others

## Special Scenarios Coverage

1. **HRA Exemption**: EMP006, EMP010, EMP011, EMP012
2. **Multiple Allowances**: EMP013
3. **Deductions (80C, 80D, 80G)**: EMP006, EMP008, EMP014, EMP018
4. **NPS Contributions**: EMP015
5. **Home Loan**: EMP016, EMP028
6. **Disability Benefits**: EMP017
7. **Investment & Donations**: EMP017
8. **Capital Gains/ULIP**: EMP018
9. **Gratuity/EPF**: EMP019, EMP020
10. **NRI Status**: EMP021
11. **Surcharge applicable**: EMP004, EMP008
12. **Rebate boundary testing**: EMP002, EMP003

## Notes

- All employees will be generated one by one following the iterative workflow (Steps 2-7 for each employee)
- Each employee will have a complete verification markdown file before being appended to master CSVs
- Not all employees require monthly input/output data - only those specified in the requirements
- All data will be compliant with Indian tax laws and mr_dsl.yaml rules
- Assessment Year 2026-27 will be used for all calculations
- Monthly data will be generated for April 2025, December 2025, and March 2026

### Important: Fixed vs Variable Bonus/Commission Handling

**Annual CTC Breakdown (Prepared in April):**
- Represents salary structure known at the start of the financial year (April 2025)
- Should ONLY include fixed/regular components paid every month
- Should NOT include variable bonuses/commissions paid in specific months later
- Variable components are set to 0 in annual input data

**Annual Tax Forecast (Prepared in April):**
- Forward-looking projection including expected annual income
- INCLUDES projected variable bonuses/commissions (even though not yet received)
- Used to calculate monthly TDS = annual_tax / 12

**Two Types of Bonuses/Commissions:**

1. **Fixed/Regular** (e.g., EMP008):
   - Part of regular salary structure, paid every month
   - Included in annual CTC breakdown in April
   - Included in annual input as total annual amount
   - Divided by 12 in monthly payslips
   - NO entries in monthly_bonus_commission CSVs
   - Example: EMP008 - ₹60Cr CTC with ₹50Cr bonus + ₹30Cr commission → ₹4.17Cr + ₹2.5Cr monthly

2. **Variable** (e.g., EMP002, EMP004, EMP007):
   - One-time payments in specific months (performance-based, year-end, quarterly, etc.)
   - NOT included in annual CTC breakdown in April (set to 0)
   - Included in annual tax forecast (projection)
   - Entered in monthly_bonus_commission_{month}.csv for specific month(s)
   - Monthly payslips:
     * Months WITHOUT variable bonus: regular components only, bonus/commission = 0
     * Months WITH variable bonus: regular + variable amount, bonus/commission = actual amount
   - **TDS stays constant** (annual_tax/12) - does NOT change when bonus received
   
**Examples:**

| Employee | Fixed Components | Variable Components | Annual CTC (April) | Monthly CSVs |
|----------|------------------|---------------------|-------------------|--------------|
| EMP002 | Basic, HRA, Special, etc. | ₹70K commission (Dec) | ₹14,30,000 | December: ₹70K |
| EMP004 | Basic, HRA, Special, **₹3L fixed bonus** | ₹2.45L variable commission | ₹67,54,400 | Apr/Dec/March: ₹80K/₹85.6K/₹80K |
| EMP007 | Basic, HRA, Special, etc. | ₹50K performance bonus (Apr) | ₹9,50,000 | April: ₹50K |
| EMP008 | Basic, HRA, Special, **₹5Cr fixed bonus**, **₹3Cr fixed commission** | None | ₹60,00,00,000 | None |

**Monthly Payslip Example (EMP002):**
```
Annual CTC (April): ₹14,30,000 (excluding ₹70K variable commission)
Annual Tax Forecast: Based on ₹15,00,000 (including projected ₹70K commission)
Monthly TDS: ₹7,813 (constant in all months)

April:    gross=₹119,166 (regular), commission=0,      TDS=₹7,813
December: gross=₹189,166 (regular+70K), commission=₹70,000, TDS=₹7,813 (same!)
March:    gross=₹119,166 (regular), commission=0,      TDS=₹7,813
```

**Key Principle**: Annual CTC breakdown (April) reflects known/committed salary components. Variable bonuses are future events, so they're excluded from April CTC but included in the tax forecast projection.

---

## CSV Field Validation Requirements

**CRITICAL**: Always verify field counts before appending data to prevent corruption!

### Required Field Counts

| CSV File | Required Fields | Validation Status |
|----------|----------------|-------------------|
| `annual_employee_input_data_april_2025.csv` | **68** | ✅ Verified |
| `annual_tax_forecast_april_2025.csv` | **50** | ✅ Verified |
| `monthly_payslip_april.csv` | **48** | ✅ Verified |
| `monthly_payslip_december.csv` | **48** | ✅ Verified |
| `monthly_payslip_march.csv` | **48** | ✅ Verified |
| `test_cases_master_summary.csv` | **13** | ✅ Verified |
| `monthly_bonus_commission_april.csv` | **6** | ✅ Verified |
| `monthly_bonus_commission_december.csv` | **6** | ✅ Verified |
| `monthly_bonus_commission_march.csv` | **6** | ✅ Verified |
| `ctc_revision_december.csv` | **10** | ✅ Verified |
| `tax_regime_revision_december.csv` | **7** | ✅ Verified |
| `investment_declaration_revision_february.csv` | **10** | ✅ Verified |

### Validation Checklist (Before Appending)

For EACH employee data row:
1. ✅ Count fields in header
2. ✅ Count fields in employee data row
3. ✅ Verify counts match exactly
4. ✅ Verify no extra/missing fields
5. ✅ Only then append to CSV

### Common Errors to Avoid

❌ **Extra fields in monthly payslips**: Do NOT include:
- `children_education_allowance_monthly`
- `children_hostel_allowance_monthly`
- `books_and_periodical_allowance_monthly`
- `telephone_reimbursement_monthly`

These allowances are included in the gross but NOT as separate columns!

❌ **Missing fields**: Ensure all fields are present, even if empty (use 0, empty string, or `false`)

❌ **Field order mismatch**: Follow exact header order

✅ **Correct approach**: Always compare against existing employee rows (e.g., copy EMP011 structure for EMP012)

### Quick Verification Script

```bash
# Check field counts for a specific employee
grep "^EMP012" annual_employee_input_data.csv | awk -F, '{print NF " fields"}'
head -1 annual_employee_input_data.csv | awk -F, '{print NF " fields (header)"}'
```

If counts don't match, regenerate the row!

---

## Completion Tracking

- ✅ EMP001-EMP005 (5 employees) - COMPLETED
- ✅ EMP006-EMP010 (5 employees) - COMPLETED
- ✅ EMP011-EMP017 (7 employees) - COMPLETED
- ✅ EMP018-EMP021 (4 employees) - COMPLETED
- ❌ EMP022 - REMOVED
- ✅ EMP023 - RE-ADDED
- ❌ EMP024 - REMOVED
- ✅ EMP025-EMP028 (4 employees) - COMPLETED
- ✅ EMP029-EMP032 (4 employees) - COMPLETED

**Total Progress**: 30/30 employees generated (100%, 2 employees removed)

---

## Data Quality Updates

### Latest Update (November 20, 2025)

**EMP023 Re-Added**

**Reason**: EMP023 (Multiple Employers in Same Year, TC-24) was re-generated and added back to the dataset.

**Files Updated**:
- ✅ annual_employee_input_data_april_2025.csv (EMP023 inserted at position 23)
- ✅ annual_tax_forecast_april_2025.csv (EMP023 inserted at position 23)
- ✅ monthly_payslip_april.csv (EMP023 inserted, previous employer data)
- ✅ monthly_payslip_december.csv (EMP023 inserted, current employer data)
- ✅ monthly_payslip_march.csv (EMP023 inserted, current employer data)
- ✅ test_cases_master_summary.csv (TC-24 added)
- ✅ employee_verification_EMP023.md (created)

**Test Case Coverage Restored**:
- TC-24: Multiple Employers in Same Year (₹80,309 tax, ETR 5.9%)

**Employee Details**:
- Name: Priya Sharma
- Age: 32, Bangalore Metro, Old Regime
- Previous Employer (Apr-Sep): ₹6L gross, ₹30K TDS
- Current Employer (Oct-Mar): ₹7.5L gross, ₹50.3K TDS
- Total FY Income: ₹13.5L
- Form 12B: ✅ Provided
- Tax: ₹80,309

---

### EMP015 Re-Added (November 20, 2025)

**Reason**: EMP015 (Home Loan - Multiple Properties, TC-16) was re-generated and added back to the dataset.

**Files Updated**:
- ✅ annual_employee_input_data_april_2025.csv (EMP015 inserted at position 16)
- ✅ annual_tax_forecast_april_2025.csv (EMP015 inserted at position 16)
- ✅ monthly_payslip_april.csv (EMP015 inserted)
- ✅ monthly_payslip_december.csv (EMP015 inserted)
- ✅ monthly_payslip_march.csv (EMP015 inserted)
- ✅ test_cases_master_summary.csv (TC-16 added)
- ✅ employee_verification_EMP015.md (created)

**Test Case Coverage Restored**:
- TC-16: Home Loan - Multiple Properties (₹4,49,155 tax, ETR 17.2%)

**Employee Details**:
- Name: Lakshmi Iyer
- Age: 38, Chennai Metro, Old Regime
- Gross Income: ₹26.08L (Salary ₹25L + House Property ₹1L + Interest ₹8K)
- 2 Properties: Self-occupied (₹2L interest, 24(b)) + Let-out (₹1L net income after deductions)
- HRA Exemption: ₹1.16L (pays rent elsewhere)
- Tax: ₹4,49,155

---

### Previous Removals (November 20, 2025)

**EMP023, EMP024 Removed**

**Reason**: Removed from dataset per user request.

**Files Updated**:
- ✅ annual_employee_input_data_april_2025.csv
- ✅ annual_tax_forecast_april_2025.csv
- ✅ monthly_payslip_april.csv
- ✅ monthly_payslip_december.csv
- ✅ monthly_payslip_march.csv
- ✅ test_cases_master_summary.csv
- ✅ ctc_revision_december.csv (EMP024 entry removed)
- ✅ tax_regime_revision_december.csv
- ✅ employee_verification_EMP023.md (deleted)
- ✅ employee_verification_EMP024.md (deleted)

**Test Cases No Longer Covered**:
- TC-25: Mid-Year Salary Structure Change (EMP024)

---

### EMP022 Removal (November 20, 2025)

**Reason**: EMP022 (Super Senior Citizen, TC-22) was removed from the dataset.

**Files Updated**:
- ✅ All main CSV files
- ✅ employee_verification_EMP022.md (deleted)

**Test Case Impact**: TC-22 (Super Senior Citizen 80+) is no longer covered.

---

### Recent Fixes (November 20, 2025)

**EMP021-EMP024 Data Corrections**: Fixed 41 issues across 4 employees:

1. **EMP021** (10 fixes):
   - Capitalization: `city_type`, `tax_regime`
   - Left shift: `performance_bonus` (72000→0), `employer_pf_contribution` (0→72000)
   - Data types: `property_type`, `disability_status`, `first_time_home_buyer`, `donations_100_percent`, `dependent_severe_disability`

2. **EMP022** (7 fixes):
   - Capitalization: `residency`, `city_type`, `tax_regime`
   - Data types: `property_type`, `first_time_home_buyer`, `disability_status`, `dependent_severe_disability`

3. **EMP023** (10 fixes):
   - Capitalization: `residency`, `city_type`, `tax_regime`
   - Data types: 4 boolean/text fields
   - Component sum: `special_allowance` (₹2.5L→₹5.16L)
   - Left shift: `performance_bonus` (72000→0), `employer_pf_contribution` (0→72000)

4. **EMP024** (14 fixes):
   - Capitalization: `residency`, `city_type`, `tax_regime`
   - Data types: 4 boolean/text fields
   - CTC correction: Changed from blended (₹11.33L) to April CTC (₹10L)
   - Component adjustments: `basic`, `hra`, `special`, `employee_pf`, `employer_pf`
   - Left shift: `special_allowance` (₹3.04L→₹3.76L), `performance_bonus` (72000→0)

**Root Causes Identified**:
- Left shift bugs in salary component fields
- Inconsistent capitalization (e.g., 'IN' vs 'Resident', 'metro' vs 'Metro')
- Data type confusion (numeric '0' in text/boolean fields)
- Blended CTC used instead of April CTC for mid-year change scenario

**All issues resolved and validated** ✅

---

*This document will be updated as employees are generated to track progress and ensure all test cases are covered.*

