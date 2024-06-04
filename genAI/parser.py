from bs4 import BeautifulSoup

# Read the saved HTML file
with open("page_content.html", "r", encoding="utf-8") as file:
    page_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Create or open a text file to save the extracted content
with open("extracted_content.txt", "w", encoding="utf-8") as output_file:

    # Headings
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    output_file.write("Headings:\n")
    for heading in headings:
        output_file.write(f"{heading.name}: {heading.get_text(strip=True)}\n")
    output_file.write("\n")

    # Paragraphs
    paragraphs = soup.find_all('p')
    output_file.write("Paragraphs:\n")
    for para in paragraphs:
        output_file.write(para.get_text(strip=True) + "\n")
    output_file.write("\n")

    # Links
    links = soup.find_all('a', href=True)
    output_file.write("Links:\n")
    for link in links:
        output_file.write(f"Text: {link.get_text(strip=True)}, URL: {link['href']}\n")
    output_file.write("\n")

    # Tables
    tables = soup.find_all('table')
    output_file.write("Tables:\n")
    for table in tables:
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            cell_text = [cell.get_text(strip=True) for cell in cells]
            output_file.write("\t".join(cell_text) + "\n")
        output_file.write("\n")
    output_file.write("\n")

    # Lists
    output_file.write("Lists:\n")
    lists = soup.find_all(['ul', 'ol'])
    for lst in lists:
        items = lst.find_all('li')
        for item in items:
            output_file.write(item.get_text(strip=True) + "\n")
        output_file.write("\n")
    output_file.write("\n")

    # Forms
    forms = soup.find_all('form')
    output_file.write("Forms:\n")
    for form in forms:
        form_details = {}
        form_details['action'] = form.get('action', 'No action')
        form_details['method'] = form.get('method', 'No method')
        inputs = form.find_all('input')
        form_details['inputs'] = []
        for inp in inputs:
            input_details = {
                'name': inp.get('name', 'No name'),
                'type': inp.get('type', 'No type'),
                'value': inp.get('value', 'No value')
            }
            form_details['inputs'].append(input_details)
        output_file.write(str(form_details) + "\n")
    output_file.write("\n")

    # General extraction of all text
    output_file.write("All Text Content:\n")
    all_text = soup.get_text(separator='\n', strip=True)
    output_file.write(all_text)
