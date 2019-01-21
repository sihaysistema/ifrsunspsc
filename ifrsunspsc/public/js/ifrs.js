console.log('Hola desde IFRS');
frappe.ui.form.on("Cost Center", {
    refresh: function (frm, cdt, cdn) {
        console.log('Hola mundo adentro de cost center');
        frm.add_custom_button(__('Crear'), function () {
            frappe.call({
                method: "ifrsunspsc.api.addlvl1",
                args: {
                    center: frm.doc.cost_center_name
                },
                callback: function () {
                    //frm.reload_doc();
                }
            });
        }).addClass("btn-primary");
    }
});