import subprocess

# Full paths to your Jupyter Notebook and Pandoc executable
notebook_path = r"C:\Skole\Programing\Prosjekt høst\Del 2\Statistikk av Treningsøkt innlevering test.ipynb"
pandoc_path = r"C:\Program Files\Pandoc\pandoc-3.5\pandoc.exe"
output_pdf_path = r"C:\Skole\Programing\Prosjekt høst\Del 2\output.pdf"

# Run Pandoc to convert the notebook to PDF
try:
    result = subprocess.run(
        [pandoc_path, "--from=ipynb", "--to=pdf", notebook_path, "-o", output_pdf_path],
        capture_output=True, text=True, check=True
    )
    print("Conversion successful!")
    print(result.stdout)  # Output of conversion
except subprocess.CalledProcessError as e:
    print(f"Error during conversion: {e}")
    print(f"stderr: {e.stderr}")
