from . import __version__ as app_version

app_name = "event_stream"
app_title = "Event Stream"
app_publisher = "Kayode Lawal"
app_description = "Simplified Event Streaming"
app_email = "lawalkeyd@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/event_stream/css/event_stream.css"
# app_include_js = "/assets/event_stream/js/event_stream.js"

# include js, css files in header of web template
# web_include_css = "/assets/event_stream/css/event_stream.css"
# web_include_js = "/assets/event_stream/js/event_stream.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "event_stream/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "event_stream.utils.jinja_methods",
#	"filters": "event_stream.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "event_stream.install.before_install"
# after_install = "event_stream.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "event_stream.uninstall.before_uninstall"
# after_uninstall = "event_stream.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "event_stream.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"event_stream.tasks.all"
#	],
#	"daily": [
#		"event_stream.tasks.daily"
#	],
#	"hourly": [
#		"event_stream.tasks.hourly"
#	],
#	"weekly": [
#		"event_stream.tasks.weekly"
#	],
#	"monthly": [
#		"event_stream.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "event_stream.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "event_stream.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "event_stream.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


doc_events = {
    "*": {
        "after_insert": "event_stream.event_stream.doctype.event_update_logs.event_update_logs.notify_consumers",
        "on_update": "event_stream.event_stream.doctype.event_update_logs.event_update_logs.notify_consumers",
        "on_cancel": "event_stream.event_stream.doctype.event_update_logs.event_update_logs.notify_consumers",
        "on_trash": "event_stream.event_stream.doctype.event_update_logs.event_update_logs.notify_consumers"
    }
}

# Request Events
# ----------------
# before_request = ["event_stream.utils.before_request"]
# after_request = ["event_stream.utils.after_request"]

# Job Events
# ----------
# before_job = ["event_stream.utils.before_job"]
# after_job = ["event_stream.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"event_stream.auth.validate"
# ]
