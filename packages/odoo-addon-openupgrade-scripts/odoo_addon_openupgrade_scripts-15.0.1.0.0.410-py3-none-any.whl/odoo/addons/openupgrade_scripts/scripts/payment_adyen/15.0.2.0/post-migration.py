from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "payment_adyen", "15.0.2.0/noupdate_changes.xml")
    openupgrade.delete_records_safely_by_xml_id(env, ["payment_adyen.adyen_form"])
