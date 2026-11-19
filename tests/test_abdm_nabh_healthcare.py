import unittest
from abdm_nabh_healthcare.engine import PatientABHARecord, ABDMHospitalHealthEngine

class TestABDMHospitalHealthEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ABDMHospitalHealthEngine("IN2710001429-MAX-HEALTHCARE")

    def test_abha_linking_and_fhir_prescription(self):
        pat = PatientABHARecord("91-4412-8891-2210", "rajesh.kumar@abdm", "Rajesh Kumar", "M", 1984, "MRN-2026-9041")
        self.engine.link_abha_patient(pat)

        meds = [{"medicine": "Metformin 500mg", "dosage": "Twice daily after meals"}]
        fhir = self.engine.generate_fhir_bundle_prescription("rajesh.kumar@abdm", "Dr. A. K. Sharma", meds)
        self.assertEqual(fhir["abdm_compliance"], "MILESTONE_M3_VERIFIED")
        self.assertEqual(len(fhir["entries"]), 1)

if __name__ == "__main__":
    unittest.main()
