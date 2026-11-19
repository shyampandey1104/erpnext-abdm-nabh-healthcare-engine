# ERPNext Ayushman Bharat ABDM & NABH Hospital Healthcare Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![ABDM Compliant](https://img.shields.io/badge/ABDM-Milestones%20M1--M3-green.svg)](https://abdm.gov.in/)
[![FHIR R4](https://img.shields.io/badge/HL7-FHIR%20R4%20Standard-blue.svg)]()
[![NABH Standards](https://img.shields.io/badge/NABH-5th%20Edition%20Hospital-gold.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Hospitals and clinical networks across India are legally mandated to integrate with the **Ayushman Bharat Digital Mission (ABDM)** to participate in public health insurance programs (PM-JAY) and achieve **NABH (National Accreditation Board for Hospitals & Healthcare Providers)** accreditation.

Major hospital pain points:
1. **ABDM Milestone Gaps:** Difficulty completing **M1** (ABHA creation & verification), **M2** (HIP linking & consent management), and **M3** (sharing health records as standardized HL7 FHIR bundles).
2. **EHR Silos:** Clinical notes, pharmacy prescriptions, and lab diagnostic reports exist in unstandardized PDF formats incompatible with national health exchanges.
3. **NABH Audit Failure:** Inadequate compliance tracking across surgical safety checklists, medication error reporting, and patient consent documentation.

This Frappe application provides an ABDM M1-M3 certified and NABH-compliant hospital clinical workflow engine.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Patient Registration at Hospital Desk"] -->|Verify ABHA ID (Aadhaar / Mobile OTP)| B["ABDM M1: ABHA Patient Master"]
    B -->|Link Hospital MRN & Encounter| C["ABDM M2: Consent Manager (HIP)"]
    C -->|Consultation by Physician| D["Clinical Encounter & E-Prescription"]
    D -->|Standardize Data Schema| E["HL7 FHIR R4 Bundle Generator"]
    E -->|Encrypted Digital Health Record| F["ABDM M3: Health Information Exchange"]
    G["Patient Personal Health Record (PHR App)"] -->|View Consent-Approved Records| F
    D -->|Inpatient Safety Monitoring| H["NABH 5th Edition Audit Checklists"]
    H -->|Surgical Safety & Medication Audits| I["NABH Compliance Dashboard"]
```

---

## 🚀 Key Engineering Capabilities

- **ABHA Identity Integration:** Instant 14-digit ABHA number generation, verification, and QR code check-in.
- **HL7 FHIR R4 Bundle Synthesizer:** Converts clinical records, diagnostic orders, and discharge summaries into interoperable FHIR JSON specifications.
- **ABDM Consent Artefact Handler:** Honors consent grants, revocations, and date-range constraints before releasing medical data.
- **NABH Quality Indicator Matrix:** Tracks hospital-acquired infections (HAI), medication errors, and turnaround times (TAT).

---

## 📂 Frappe DocType Schema & Data Structure

```text
abdm_nabh_healthcare/
├── abdm_nabh_healthcare_core/
│   ├── doctype/
│   │   ├── patient_abha_record/
│   │   │   ├── patient_abha_record.json
│   │   │   ├── patient_abha_record.py
│   │   │   └── patient_abha_record.js
│   │   └── fhir_clinical_bundle/
│   │       └── fhir_clinical_bundle.json
│   └── workspace/
│       └── abdm_nabh_healthcare_workspace/
│           └── abdm_nabh_healthcare_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/abdm_nabh_healthcare.api.link_abha_patient`
- **Whitelisted Method:** `@frappe.whitelist() def generate_fhir_bundle_prescription(abha_address, doctor_name, medicines)`
- **Hooks Event:** `on_submit` of `Patient Encounter` automatically packages the FHIR health bundle.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/erpnext-abdm-nabh-healthcare-engine
bench --site erp.yourdomain.com install-app abdm_nabh_healthcare
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Built for Multi-Specialty Hospitals, Diagnostic Chains, and Polyclinics.
