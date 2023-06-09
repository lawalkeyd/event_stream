// Copyright (c) 2023, Kayode Lawal and contributors
// For license information, please see license.txt


frappe.ui.form.on("Event Producers", {
	refresh: function (frm) {
		frm.set_query("ref_doctype", "producer_doctypes", function () {
			return {
				filters: {
					issingle: 0,
					istable: 0,
				},
			};
		});

		frm.add_custom_button(__('Pull Changes'), () => {
			frappe.call({
				method: 'event_stream.event_stream.doctype.event_producers.event_producers.pull_from_node',
				args: {
					'event_producer': frm.doc.producer_url,
				},
				freeze: true,
				freeze_message: __('...Pulling Event Producer Changes')
			})
		});

		frm.set_indicator_formatter("status", function (doc) {
			let indicator = "orange";
			if (doc.status == "Approved") {
				indicator = "green";
			} else if (doc.status == "Rejected") {
				indicator = "red";
			}
			return indicator;
		});
	},
});
