class constant:
    ares_management = "Ares Management"
    others = "others"
    look_up = "lookup"
    look_up_acsg = "lookupAscg"
    not_started = "Not Started"
    running = "Running"
    successful = "Successful"
    failed = "Failed"
    all = "All"
    filename = "filename"
    type = "type"
    uuid = "uuid"
    status = "status"
    data = "data"
    invoice_id = "invoice_id"
    invid = "invid"
    folder_location = "folder_location"
    upload_time = "upload_time"
    processed_time = "processed_time"
    product_name = "Product Name"
    error = "error"
    ok = "ok"


class InvoiceColumns:
    mandatory_acs = "mandatory_acs"
    mandatory_field = "mandatory_field"
    amount_org_sum = "amount_org_sum"
    price_with_manual = "price_with_manual"
    price_with_weighted_average = "price_with_weighted_average"
    price_with_average = "price_with_average"
    cgs_invoice_date = "CGS Invoice Date"
    net_invoice_amount = "Net Invoice Amount"
    product_name = "Product Name"
    chart_of_accounts = "Chart of Accounts"
    legal_entity_missing = "missing_legal_entity"
    legal_entity = "Legal Entity"
    bill_to_entity = "Bill To Entity"
    tax_distribution_manual = "tax_distribution_manual"
    tax_distribution_average = "tax_distribution_average"
    tax_distribution_weighted_average = "tax_distribution_weighted_average"
    line_tax_amount = "Line Tax Amount"
    # price = "Price"
    # control_total = "Control Total"
    currency = "Currency"
    shipping = "Shipping"
    remit_to_code = "Remit To Code"
    requester = "Requester"
    supplier = "Supplier"
    tax_amount = "Tax Amount"
    approval_routing_code = "Approval Routing Code"
    vendor = "Vendor"
    supplier_number = "Supplier Number"
    billability = "Billability"
    account_segment = "account_segment"
    payment_terms = "Payment Terms"
    # header_description = "Header Description"
    # invoice_date = "Invoice Date"
    cgs_due_date = "CGS Due Date"
    invoice_hash = "Invoice #"
    price_total_amount_validation = "price_total_amount_validation"
    line_item_number = "line_item_number"
    line_status = "Line Status"
    id = "id"
    tax_distribution_type = "tax_distribution_type"
    invoice_status = "invoice_status"
    parent_invoice = "parent_invoice"
    amount = "Amount"
    amount_org = "Amount Original"
    tax_and_other_amount = "tax_and_other_amount"
    tax_and_other_amount_original = "tax_and_other_amount_original"
    tax_and_other_amount_manual = "tax_and_other_amount_manual"
    jurisdiction = "Jurisdiction"


class TaxDistributionType:
    average = "Average"
    weighted_average = "Weighted Average"
    manual = "Manually"
    map = {
        average: InvoiceColumns.tax_distribution_average,
        weighted_average: InvoiceColumns.tax_distribution_weighted_average,
        manual: InvoiceColumns.tax_distribution_manual,
    }

    def get_column_name(self, key):
        if key in self.map:
            return self.map[key]
        raise KeyError(f"TaxDistributionType {key} does not exists")


class ApiParams:
    line_item_numbers = "line_item_numbers"
    line_item_number = "line_item_number"
    id = "id"
    invoice_id = "invoice_id"
    key = "key"
    value = "value"


class TimeFormat:
    week_day_month_year_time = "%a, %d %b %Y %H:%M:%S"
    normal = "%d-%b-%H-%M-%S"


class Sftp:
    host = "host"
    username = "username"
    password = "password"
    target_directory = "target_directory"
    post_to_server = "post_to_server"
