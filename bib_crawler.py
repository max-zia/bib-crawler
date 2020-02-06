"""
Iterates through paragraphs (i.e., individual references) in a reference
list or bibliography, deleting two kinds of references:
	
	1. Those containing no brackets. Note that, in all footnote referencing 
	styles, the nth reference to an article that has already been cited will
	be an abbreviated version of the original. These abbreviated versions should
	not contain any brackets, and - of course - they shouldn't be included in
	the reference list.

	2. Duplicates. Any references that entirely duplicate an original reference
	should be removed.   
"""

from docx import Document

doc = Document('bibliography.docx')

def delete_paragraph(paragraph):
	"""
	Function for deleting an entire paragraph.
	"""
	p = paragraph._element
	p.getparent().remove(p)
	p._p = p._element = None

# Array for holding each paragraph/reference
p_holder = []

for p in doc.paragraphs:
	# Delete paragraphs with no brackets (i.e., any abbreviated references)
	if "(" not in p.text:
		delete_paragraph(p)
	# Check if this paragraph is a duplicate
	elif p.text in p_holder:
		delete_paragraph(p)
	else:
		# Add the reference to the paragraph/reference holder array
		p_holder.append(p.text)


doc.save('bibliography_new.docx')