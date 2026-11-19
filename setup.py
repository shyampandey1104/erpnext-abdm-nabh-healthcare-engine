from setuptools import setup, find_packages

setup(
    name="erpnext-abdm-nabh-healthcare-engine",
    version="1.0.0",
    description="ERPNext ABDM & NABH Hospital Healthcare Engine: Ayushman Bharat ABHA ID, FHIR Health Records & NABH Quality Checklists.",
    author="Shyam Kumar Pandey",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
