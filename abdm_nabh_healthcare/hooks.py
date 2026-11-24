# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "abdm_nabh_healthcare"
app_title = "Erpnext Abdm Nabh Healthcare Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Abdm Nabh Healthcare Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/abdm_nabh_healthcare/css/abdm_nabh_healthcare.bundle.css"
app_include_js = "/assets/abdm_nabh_healthcare/js/abdm_nabh_healthcare.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Abdm Nabh Healthcare Engine Entry": {
        "validate": "abdm_nabh_healthcare.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "abdm_nabh_healthcare.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "abdm_nabh_healthcare.tasks.hourly_sync"
    ],
    "daily": [
        "abdm_nabh_healthcare.tasks.daily_reconciliation"
    ],
    "weekly": [
        "abdm_nabh_healthcare.tasks.weekly_digest"
    ]
}
