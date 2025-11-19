| Test Case ID | Persona / Scenario Description | Key Data Points |
| --- | --- | --- |
| **TC-01** | New Regime - Below Exemption Limit | Tax Regime: New; Taxable Income: ~₹3-7L; Multiple allowances |
| **TC-02** | New Regime - Rebate Threshold Boundary | Tax Regime: New; Taxable Income: ~₹12L; Rebate eligibility |
| **TC-03** | New Regime - Marginal Relief Zone | Tax Regime: New; Taxable Income: just above rebate threshold (~₹12L) |
| **TC-04** | New Regime - High Income with Surcharge | Tax Regime: New; Taxable Income: >₹50L; Multiple slab applicability; Surcharge & cess; Multiple allowances |
| **TC-05** | New Regime - Multiple Deduction and Exemption | Tax Regime: New; Taxable Income: ~₹15L;Conveyance Allowance Exemption and other deductions/exemptions |
| **TC-06** | Old Regime - Multiple Deductions | Tax Regime: Old; Taxable Income: ~₹9L; Section 80C/80D/HRA/80CCD,80G; Metro city |
| TC-07 | Old Regime - Senior Citizen (60-80) | Tax Regime: Old; Taxable Income: ~₹14L; Senior citizen deductions (80D, 80TTB) |
| **TC-08** | Old vs New - Regime Comparison Case | Tax Regime: Old; Taxable Income: ~₹10L; Multiple allowances; Multiple Applicable Deductions and Exemptions |
| **TC-09** | Very High Income - Maximum Surcharge | Tax Regime: Old; Taxable Income: >₹1Cr; High surcharge slab |
| TC-10 | HRA - Metro City Maximum Exemption | Tax Regime: Old; City: Metro; Basic Salary: High; HRA & Rent: High; HRA exemption calculation; Other deductions and exemptions applicable |
| TC-11 | HRA - Non-Metro with Minimal Exemption | Tax Regime: Old; City: Non-metro; Basic Salary: Moderate; HRA & Rent: Low; Minimal HRA exemption; Other deductions and exemptions applicable |
| TC-12 | Section 80GG - No HRA Received | Tax Regime: Old; HRA: Not received; Rent paid: Moderate; No house ownership; Section 80GG deduction; Other deductions and exemptions applicable |
| TC-13 | Multiple Allowances Combined | Tax Regime: Old; Multiple allowances (LTA, conveyance, meal, CEA, tribal, uniform); Exemption calculations; Other deductions and exemptions applicable |
| TC-14 | Maximum Deductions Scenario (Old Regime) | Tax Regime: Old; Taxable Income: ~₹15L; Multiple deductions (80C, 80CCD, 80D, home loan, 80EE, 80G, HRA) |
| TC-15 | NPS - Both Employee & Employer Contributions | Tax Regime: Old; Taxable Income: ~₹12L; NPS contributions (employee, employer and additional); |
| TC-16 | Home Loan - Multiple Properties | Tax Regime: Old; Multiple properties (self-occupied & let-out); Home loan interest; First-time buyer; Section 24(b) |
| TC-17 | Disability & Dependent Benefits | Tax Regime: Old; Disability (self & dependent); Section 80U, 80DD; Transport allowance |
| TC-18 | Investment & Donation Combinations | Tax Regime: Old; 80C/80CCC/80CCD investments; Donations under 80G (mixed eligibility); Combined deduction limits |
| TC-19 | ULIP & Capital Gains | Tax Regime: New; ULIP premium: High; Maturity proceeds; Short holding period; Capital gains applicability |
| TC-20 | Gratuity with Section 89 Relief (15+ years) | Tax Regime: Old; Service: >15 years; Gratuity received; Section 89(1) relief (spread over 3 years) |
| TC-21 | EPF Withdrawal Before 5 Years | Tax Regime: Old; Service: <5 years; EPF withdrawal; Employee contribution & interest; Section 89 relief; Form 10E |
| TC-23 | NRI Employee | Tax Regime: New; Residency: NRI; Taxable Income: ~₹11L; No Section 87A rebate |
| TC-24 | Multiple Employers in Same Year | Tax Regime: New/Old; Multiple employers in FY; Salary split; TDS from both; Form 26AS reconciliation |
| TC-25 | Mid-Year Salary Structure Change | Tax Regime: New/Old; Salary structure changes mid-year; Pro-rated salary components; Revised TDS |
| TC-26 | Professional Tax - Multiple States | Tax Regime: New/Old; Employment in multiple states; Professional tax in each; Annual PT cap |
| TC-27 | TDS Threshold Testing - Rent Payment | Tax Regime: New/Old; Employee pays high rent; Section 194I TDS;  |
| TC-28 | VPF Contribution (Low Income) | Tax Regime: Old; Taxable Income: ~₹4L; VPF contribution details (part of 80C). |
| TC-29 | Additional Income (Rental) | Tax Regime: New; Salaried with additional income from a let-out property; Home loan interest paid on that property. |
| TC-30 | Mid-Year Tax Regime Change | Request to change the tax regime in the middle of the financial year; System should handle regime switch and pro-rate calculations accordingly |
| TC-31 | Monthly Investment Update (Old Regime) | Additional changes before 10th of the month (updated tax declarations); Professional uploads this with LSPs; GP does not collect it yet; Payroll must consider latest declarations before finalizing payroll each month |
| TC-32 | Annual Allowance Due Month Detection & Reminder | Annual allowances (paid as per client’s policies); System should detect due month from CTC uploaded during onboarding; Reminder functionality for LSPs; Can be a good postdated use case |
| TC-33 | LTA Payment and Adjustment | Change in LTA when salary changes within the year; LTA part of CTC, paid only in March; Monthly accrual but paid in March; Requests to add/remove LTA and adjust CTC structure |
| TC-34 | Voluntary Provident Fund Adjustment | Voluntarily PF (rare but possible); VPF cannot go higher than 13K; Adjustment of Voluntary Provident Fund (VPF); Monthly Basic Salary: INR 15000 |
| TC-35 | PF Calculation for International Worker | International worker; PF calculated as 12% * (Gross-HRA); Adjustment of PF for International Worker |
| TC-36 | NRI and Residency Status Rebate | NRI employee or change in residency status; rebate-related cases |
| TC-37 | Retrospective Change in Salary Components | Retrospective change in salary components within the financial year; system must recalculate all affected payroll/tax items |
| TC-38 | Grossing Up Components on Client Request | Struggling with a LSP scenario on amount gross up (give bonus and commission so that tax is charged to client); Feature request from all countries; Example: client may decide they want to give 10K net amount, so total amount will be larger; System calculates gross accordingly |