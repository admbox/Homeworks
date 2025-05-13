import re

def clean_html_file(input_filename, output_filename="clean.txt"):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()

        clean_text = re.sub(r'<.*?>', '', content)

        clean_lines = [line.strip() for line in clean_text.splitlines() if line.strip()]

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(clean_lines))

        print(f"\n cleaned text is written to a file: {output_filename}")

    except FileNotFoundError:
        print(f"\n File '{input_filename}' not found")
    except Exception as e:
        print(f"\n error: {e}")

input_file = input("Enter the name of the HTML file to clean up: ").strip()
output_file = input("Enter the file name to save: ").strip()

if not output_file:
    output_file = "clean.txt"

clean_html_file(input_file, output_file)