import os
c = get_config()

c.LatexExporter.template_path = ['.', os.path.expanduser('nb_pdf_template/nb_pdf_template/templates')]
c.LatexExporter.template_file = 'classic.tplx'