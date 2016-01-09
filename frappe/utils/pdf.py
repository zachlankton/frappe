# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals
from subprocess import *

import pdfkit, os, frappe
from frappe.utils import scrub_urls
from frappe import _

def get_pdf(html, options=None):
	p = Popen(["prince",'-', '--baseurl=https://198.27.88.89', '--insecure', '--javascript'], stdin=PIPE, stdout=PIPE)
	p.stdin.write("<html><body><p style=\"page-break-after: always;\"></p></body></html>"+html)
	p.stdin.close()
	pdf = p.stdout.read()

	tk = Popen(['pdftk', '-', 'cat', '2-end', 'output', '-'], stdin=PIPE, stdout=PIPE)
	tk.stdin.write(pdf)
	tk.stdin.close()
	tkpdf = tk.stdout.read()

	return tkpdf

