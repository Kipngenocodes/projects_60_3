from googletrans import Translator

def translate_file(input_file, output_file, dest_language='ja'):
    translator = Translator()

    try:
        # Read the contents of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Translate the text to the desired language
        translation = translator.translate(text, dest=dest_language)

        # Write the translated text to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translation.text)

        print(f'Translation completed! Translated text saved in "{output_file}".')

    except Exception as e:
        print(f'An error occurred: {e}')

# Define input and output files
input_filename = 'tr.txt'
output_filename = 'translated_tr.txt'

# Call the function to translate
translate_file(input_filename, output_filename)
