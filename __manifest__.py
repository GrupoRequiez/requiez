{
    "name": "Requiez Instance",
    "author": "Vauxoo, Humanytek",
    "summary": """
    All the necessary modules to auto install our service instance
    """,
    "website": "https://requiez.com",
    "license": "LGPL-3",
    "category": "requiez",
    "version": "1.0.1",
    "depends": [
        "account_asset",
        "account_budget",
        "account_online_sync",
        "account_followup",
        "base_import_module",
        "board",
        "calendar",
        "contacts",
        "crm",
        "delivery",
        "fleet",
        "google_account",
        "google_calendar",
        "google_drive",
        "helpdesk",
        "hr",
        "hr_appraisal",
        "hr_holidays",
        "hr_holidays_gantt",
        "hr_recruitment",
        "link_tracker",
        "l10n_mx_check_printing",
        "l10n_mx_edi_landing",
        "l10n_mx_reports",
        "maintenance",
        "mass_mailing",
        "mass_mailing_themes",
        "mrp",
        "mrp_ii",
        "mrp_maintenance",
        "mrp_plm",
        "mrp_mps",
        "pad",
        "pad_project",
        "product_compromise",
        "product_supply",
        "project",
        "project_forecast",
        "purchase",
        "quality",
        "quality_mrp",
        "rating",
        "sale",
        "sale_crm",
        "sale_commission",
        "sale_brand",
        "sale_order_observation",
        "sale_stock",
        "stock",
        "stock_picking_batch",
        "survey",
        "utm",
        "web_studio",
        "website",
        "website_enterprise",
        "website_links",
        "website_mail",
        "website_mass_mailing",
    ],
    "data": [
        "data/chart_template.xml",
        # Security
        # "security/ir.model.access.csv",
        "security/responsible_confirm_order_security.xml",
        "security/invoice_prioritize_security.xml",
        "security/archive_product_security.xml",
        "security/account_control_security.xml",
        "security/invoice_cancel_security.xml",
        # Data
        "data/res_company_data.xml",
        "data/report_data.xml",
        "data/mail_template_data.xml",
        # Views
        "view/res_partner_view.xml",
        "view/product_view.xml",
        "view/res_partner_view.xml",
        "view/product_view.xml",
        "view/purchase_view.xml",
        "view/sale_view.xml",
        "view/account_invoice_view.xml",
        "view/stock_picking_views.xml",
        "view/template.xml",
        "view/mrp_production_views.xml",
        "wizard/upload_forecast_view.xml",
        # Reports
        "report/requiez_reports_definition.xml",
        "report/mrp_report_template.xml",
        'report/sale_report_template.xml',
        "report/product_label_picking_template.xml",
        "report/shipping_label_template.xml",
        "report/shipping_order_template.xml",
        "report/product_label_mrp_template.xml",
        "report/report_invoice.xml",
        "report/purchase_order_templates.xml",
        "report/purchase_quotation_templates.xml",
    ],
    "demo": [
    ],
    "test": [
    ],
    "qweb": [
        "static/src/xml/qweb_teplates.xml",
    ],
    "pre_init_hook": "pre_init_hook",
    "auto_install": False,
    "application": True,
    "installable": True,
}
