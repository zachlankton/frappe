# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals
from subprocess import *

import pdfkit, os, frappe
from frappe.utils import scrub_urls
from frappe import _

def get_pdf(html, options=None):
	p = Popen(["prince",'-', '--baseurl=https://198.27.88.89', '--insecure', '--javascript'], stdin=PIPE, stdout=PIPE)
	p.stdin.write(html)
	p.stdin.close()
	pdf = p.stdout.read()


	return pdf.replace(bytearray("/Rect [572.0000 752.0000 597.0000 777.0000]", "utf8"), bytearray("", "utf8"))



