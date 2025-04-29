# Copyright (c) 2024, lawmes and contributors
# For license information, please see license.txt

# import frappe
#from frappe.model.document import Document

#class Transcation_report(Document):
	#pass




import frappe
from hijri_converter import convert
from datetime import datetime
from frappe.model.document import Document
from frappe import _

class Transcation_report(Document):
    def validate(self):
        if self.gregorian_date:
            try:
                hijri_date, day_name = convert_to_hijri_with_day(self.gregorian_date)
                self.hijri_date = hijri_date
                self.day_name = day_name
            except Exception as e:
                frappe.throw(_("An error occurred while converting the Gregorian date to Hijri: {str(e)}"))

def convert_to_hijri_with_day(gregorian_date):
    try:
        gregorian_date_obj = datetime.strptime(gregorian_date, "%Y-%m-%d")
        hijri_date = convert.Gregorian(
            gregorian_date_obj.year,
            gregorian_date_obj.month,
            gregorian_date_obj.day
        ).to_hijri()
        day_name = get_day_name(gregorian_date_obj)
        return f"{hijri_date.year}-{hijri_date.month:02d}-{hijri_date.day:02d}", day_name
    except ValueError:
        raise ValueError(_("Incorrect Gregorian date format. Please enter the date in the format YYYY-MM-DD."))
    except Exception as e:
        raise Exception(_("An unexpected error occurred during conversion: {str(e)}"))

def get_day_name(date_obj):
    days = [_("Monday"), _("Tuesday"), _("Wednesday"), _("Thursday"), _("Friday"), _("Saturday"), _("Sunday")]
    return days[date_obj.weekday()]